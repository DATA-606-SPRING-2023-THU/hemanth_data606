import os
import psycopg2
from flask_cors import CORS
from flask import Flask, jsonify
from flask import request
import pickle
import pandas as pd
import torch
import torch.nn as nn
import numpy as np

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.debug = True
db_url = os.getenv("DATABASE_URL")
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://hemanth:hemanth123@my-db.c8684qazpg5m.us-east-1.rds.amazonaws.com:5432/movie_recommendation_db'
conn = psycopg2.connect(
    host="my-db.c8684qazpg5m.us-east-1.rds.amazonaws.com",
    database="movie_recommendation_db",
    user="hemanth",
    password="hemanth123",
    port=5432
)

# Fetch the ratings and movies data using SQL queries
ratings_query = "SELECT userid, movieid, rating FROM ratings"
movies_query = "SELECT movieid, title FROM movies"
ratings = pd.read_sql(ratings_query, conn)
movies = pd.read_sql(movies_query, conn)

data = pd.merge(ratings, movies, on="movieid")

data = data.pivot_table(index='userid', columns='title', values='rating')
data = data.fillna(0)
data_tensor = torch.FloatTensor(data.values)

input_size = data_tensor.shape[1]
hidden_size_1 = 512
hidden_size_2 = 256
output_size = input_size
# Define model class
class StackedAutoencoder(nn.Module):
    def __init__(self):
        super(StackedAutoencoder, self).__init__()
        # Encoder layers
        self.linear_1 = nn.Linear(input_size, hidden_size_1)
        self.linear_2 = nn.Linear(hidden_size_1, hidden_size_2)
        # Decoder layers
        self.linear_3 = nn.Linear(hidden_size_2, hidden_size_1)
        self.linear_4 = nn.Linear(hidden_size_1, output_size)
        # Activation function
        self.relu = nn.ReLU()
    
    def forward(self, x):
        # Encode input
        x = self.linear_1(x)
        x = self.relu(x)
        x = self.linear_2(x)
        x = self.relu(x)
        # Decode input
        x = self.linear_3(x)
        x = self.relu(x)
        x = self.linear_4(x)
        return x

with open('model.pkl', 'rb') as f:
    colab_model = pickle.load(f)

# Create model instance
model = StackedAutoencoder()
model.load_state_dict(torch.load('model.pth'))

# create a function to get the movie id from the movie title
def get_id_from_title(movie_title):
    with conn.cursor() as cur:
        query = "SELECT movieid FROM movies WHERE title = %s"
        params = (movie_title,)
        # execute a SQL query to get the movie id from the database
        cur.execute(query, params)
        # fetch and return the result
        return cur.fetchone()[0]
    

def get_title_from_id(movie_id):
    with conn.cursor() as cur:
        # execute a SQL query to get the movie id from the database
        cur.execute("SELECT title FROM movies WHERE movieid="+str(movie_id))
        # fetch and return the result
        return cur.fetchone()


def get_similar_movies(movie_title, n=10):
    # get the movie id from the title using the get_id_from_title function
    movie_id = get_id_from_title(movie_title)
    with conn.cursor() as cur:
        # execute a SQL query to get the similarity scores for all movies with respect to the given movie from the database
        cur.execute("SELECT cs.sim_scores FROM cosine_sim cs WHERE movie_id="+str(movie_id))
        # fetch and convert the result into a list of tuples
        sim_scores = cur.fetchone()
        cur.execute("SELECT movie_id from cosine_sim")
        movie_ids = [x[0] for x in cur.fetchall()]
        sim_scores = list(zip(movie_ids, sim_scores[0]))
        # sort the movies by similarity scores in descending order
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        # get the ids of the top n similar movies
        sim_movie_ids = [i[0] for i in sim_scores[1:n + 1]]
        # get the titles of the top n similar movies using the get_title_from_id function
#         sim_movie_titles = [get_title_from_id(i) for i in sim_movie_ids]
        cur.execute("""SELECT json_build_object( 'title', m.title, 'posterpath', l.posterpath ) as movie FROM movies m 
        left join links l on l.movieid = m.movieid where m.movieid in ("""+','.join((map(str, sim_movie_ids)))+")")
        recommendations = cur.fetchall()
        # return the list of similar movie titles
        return [x[0] for x in recommendations]

def getMovieDataFromMovieName(movies):
    with conn.cursor() as cursor:
        cursor.execute("SELECT m.movieid, m.title, l.posterpath FROM movies m left join links l on l.movieid = m.movieid WHERE title IN %s", (tuple(movies),))
        data = cursor.fetchall()
    return data

@app.route("/")
def hello_world():
    return jsonify("A Movie Recommendation System")


@app.get("/getUsers")
def getUsers():
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("select distinct userid from ratings order by userid")
            data = cursor.fetchall()
    return {"users": [x[0] for x in data]}


@app.route("/getTopRatedMovies")
def getTopRatedMovies():
    nrecommendations = request.args.get('recommendations')
    query = """
        SELECT JSON_BUILD_OBJECT
        (
        'movieid', m.movieid,
        'title', m.title,
        'rating', avg(r.rating),
        'posterpath', l.posterpath
        ) FROM movies m 
        LEFT JOIN ratings r ON r.movieid = m.movieid
        LEFT JOIN LINKS l ON l.movieid = m.movieid 
        WHERE r.rating IS NOT NULL
        GROUP BY m.movieid, l.posterpath
        ORDER BY AVG(r.rating) DESC
        LIMIT """
    query = query + str(nrecommendations)
    with conn.cursor() as cursor:
        cursor.execute(query)
        data = cursor.fetchall()
    return [x[0] for x in data]


@app.route("/getMostWatchedMovies")
def getTopRecommendationsByGenres():
    query = """
            select json_build_object(
            'title', m.title,
            'posterpath', l.posterpath,
            'rating_count', count(*)
            ) as movie
            from ratings r
            left join movies m on m.movieid = r.movieid
            left join links l on l.movieid = m.movieid 
            group by r.movieid, m.movieid, l.posterpath
            order by count(*) desc limit 100;"""
    with conn.cursor() as cursor:
        cursor.execute(query)
        data = cursor.fetchall()
    return [x[0] for x in data]


@app.route("/getMoviesInfo")
def getMovieInfo():
    with conn.cursor() as cursor:
        cursor.execute(
            "select json_agg(json_build_object('movie_id', mv.movieid, 'title', mv.title,'poster', l.posterpath))  from movies mv left join links l on l.movieid = mv.movieid;")
        data = cursor.fetchall()
    return {"moviesinfo": data[0][0]}

@app.route("/getGenre")
def getGenre():
    with conn.cursor() as cursor:
        cursor.execute("select distinct unnest(genre) as genre from movies where not '(no genres listed)' = any(genre);")
        data = cursor.fetchall()
    return [x[0] for x in data]


@app.route("/getRatingDistribution")
def getRatingDistribution():
    with conn.cursor() as cursor:
        cursor.execute("""
        SELECT COUNT(*) AS frequency FROM ratings GROUP BY rating ORDER BY rating;
        """)
        data = cursor.fetchall()
    return [x[0] for x in data]


@app.route("/getTreeGenreMap")
def getRatingVsReleaseScatterPlot():
    with conn.cursor() as cursor:
        cursor.execute("""
        SELECT
        JSONB_AGG(TO_JSONB(t)) AS movies_by_genre
        FROM (
        SELECT
        g AS x,
        COUNT(movieid) AS y
        FROM movies
        CROSS JOIN LATERAL UNNEST(genre) AS g
        GROUP BY g
        ) t;
        """)
        data = cursor.fetchall()
    return data[0][0]


@app.route("/getMoviePieChart")
def getCountMovieRatingRange():
    with conn.cursor() as cursor:
        cursor.execute("""
        SELECT rating_range, COUNT(*) FROM 
        (SELECT m.movieid, CASE when rating BETWEEN 0 and 1 then '0-1' 
        WHEN rating BETWEEN 1 AND 2 THEN '1-2' WHEN rating BETWEEN 2 and 3 THEN '2-3' 
        WHEN rating BETWEEN 3 and 4 THEN '3-4' WHEN rating BETWEEN 4 and 5 THEN '4-5'
        ELSE 'other' END AS rating_range FROM movies m 
        LEFT JOIN ratings r ON r.movieid = m.movieid ) t GROUP BY rating_range;
        """)
        data = cursor.fetchall()
    return data


@app.route('/getSimilarMovies')
def recommendSimilarMovies():
    # get the movie title from the user input
    movie_title = request.args.get('moviename')
    # get the number of recommendations from the user input or use default value of 10
    n = int(request.args.get('recommendations') or 20)
    # get the list of similar movie titles using the get_similar_movies function
    similar_movies = get_similar_movies(movie_title, n)
    # render the recommend.html template with the movie title and similar movies as arguments
    return similar_movies

@app.route('/getTopRatedMoviesByGenre')
def getTopRatedMoviesByGenre():
    genre = request.args.get('genre') 
    nrecommendations = request.args.get('recommendations')
    query = """SELECT row_to_json (t) FROM ( 
            SELECT m.movieid, m.title, avg(r.rating), l.posterpath FROM movies m 
            LEFT JOIN ratings r ON r.movieid = m.movieid 
            LEFT JOIN links l ON l.movieid = m.movieid WHERE %s = ANY (m.genre)  
            and r.rating is not null GROUP BY m.movieid, l.posterpath ORDER BY avg(r.rating) DESC LIMIT %s 
            ) t"""
    params = (genre, nrecommendations)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        data = cursor.fetchall()
    return [x[0] for x in data]

@app.route('/getPopularityOfMovie')
def getPopularityOfMovie():
    moviename = request.args.get('moviename')
    query = """
    SELECT m.title, EXTRACT(YEAR FROM r.ratingtime) AS year, COUNT(r.rating) AS ratings_count
    FROM movies m
    JOIN ratings r ON m.movieid = r.movieid
    WHERE m.title = %s
    GROUP BY m.title, year
    ORDER BY year;
    """
    params = (moviename,)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        data = cursor.fetchall()
    return {"years":[x[1] for x in data], "popularity":[x[2] for x in data]}

@app.route('/getMoviesByCollabFiltering')
def getMoviesByCollabFiltering():
    userid = request.args.get('userid')
    nrecommendations = request.args.get('recommendations')
    query="""
        SELECT m.movieid, m.title, l.posterpath
        FROM movies m
        LEFT JOIN ratings r ON m.movieid = r.movieid AND r.userid = %s
        LEFT JOIN links l on l.movieid = m.movieid
        WHERE r.rating IS NULL;
    """
    params = (userid,)
    recommendations = []
    with  conn.cursor() as cursor:
        cursor.execute(query, params)
        unwatchedmovies = cursor.fetchall()
    for movie in unwatchedmovies:
        rating = colab_model.predict(userid, movie[0]).est
        recommendations.append({'movieid':movie[0], 'title':movie[1], 'posterpath':movie[2], 'rating':rating})
    sortedmovies = sorted(recommendations, key=lambda movie:movie['rating'], reverse=True)
    return jsonify(sortedmovies[0:int(nrecommendations)])



@app.route('/getRecommendationsFromNn')
def getRecommendationFromNn():
    user_id = int(request.args.get('userid'))-1
    nrecommendations = int(request.args.get('recommendations'))
    # Get the user ratings vector
    user_ratings = data_tensor[user_id]
    # Forward pass through the model
    output = model(user_ratings)
    # Get the predicted ratings
    pred_ratings = output.detach().numpy()
    # Get the movie titles
    movie_titles = data.columns
    # Sort the movies by predicted ratings in descending order
    sorted_indices = np.argsort(pred_ratings)[::-1]
    sorted_movies = movie_titles[sorted_indices]
    sorted_ratings = pred_ratings[sorted_indices]
    # Return the top k movies and ratings
    # return jsonify(sorted_movies[:nrecommendations].tolist())
    recommendations = getMovieDataFromMovieName(sorted_movies[:nrecommendations].tolist())
    return [{"movieid":x[0], "title":x[1], "posterpath":x[2]} for x in recommendations]

@app.route('/getMoviesWatchedByUser')
def getMoviesWatchedByUser():
    userid = int(request.args.get('userid'))
    query = """
                SELECT m.title, m.movieid, l.posterpath FROM ratings r
                LEFT JOIN movies m ON m.movieid = r.movieid
                LEFT JOIN links l ON l.movieid = r.movieid 
                WHERE r.userid = %s ORDER BY r.rating DESC
            """
    params = (userid,)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        data = cursor.fetchall()
    return [{"title":x[0], "movieid":x[1], "posterpath":x[2]} for x in data]