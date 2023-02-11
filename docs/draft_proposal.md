<h2 style="text-align:center">Movie Recommedation System (Draft Proposal)</h2>
<h3>Abstract:</h3>
<p style="text-align: justify;
  text-justify: inter-word">
    Movies can serve as a great escape from the stress and challenges of daily life. They offer an opportunity to immerse
    oneself in different worlds, stories, and characters, and can provide a form of relaxation and stress relief. By watching a
    movie, people can forget about their problems for a little while and enjoy a temporary escape from reality. Additionally,
    movies can evoke strong emotions and provide a sense of empathy and connection with the characters on screen, which can also
    help alleviate stress and improve mental wellbeing. Overall, movies can play an important role in helping people cope with
    stress and improve their overall quality of life.
</p>
<hr>
<h3>Problem Statement:</h3>
<p style="text-align: justify;
  text-justify: inter-word">
    Finding movies as per one's liking is time-consuming, especially with the abundance of content available these days. With so
    many options to choose from, it is difficult to decide what to watch, and the process of searching and filtering through
    titles can be overwhelming. This is where movie recommendation systems can be very helpful. By providing users with
    personalized recommendations based on their viewing history and preferences, movie recommendation systems can save users
    time and effort in their search for movies to watch. They can also help users discover new and relevant movies that they may
    not have found otherwise, making the overall experience of finding movies to watch more enjoyable and efficient.
</p>
<hr>
<h3>Intial Questions</h3>
<ol>
    <li>How do we recommend movies to a particular user based on his watch history and ratings</li>
    <li>How can we balance the user's individual preferences with the popularity and relevance of each movie?</li>
    <li>How can we handle the cold start problem (i.e., making recommendations for new users with limited or no viewing
        history)?</li>
    <li>How can we evaluate and improve the performance of the recommendation system over time?</li>
    <li>How can we recommend movies to a new user(not in dataset)?</li>
</ol>
<hr>
<h3>About Data</h3>
<p style="text-align: justify; text-justify: inter-word">
    Data is obtained from grouplens.org.
    This dataset (ml-latest-small) describes 5-star rating and free-text tagging activity from MovieLens, a movie
    recommendation service. It contains 100836 ratings and 3683 tag applications across 9742 movies. These data were created by
    610 users between March 29, 1996 and September 24, 2018. This dataset was generated on September 26, 2018.
</p>
<h4>Source:</h4>
<p>https://grouplens.org/datasets/movielens/</p>
<br>
<a href="https://files.grouplens.org/datasets/movielens/ml-latest-small.zip" style="color:blue;text-decoration:none"><b>Click here to Download</b></a>
<h4>Data Overview:</h4>

<table style="width:100%;border: 1px solid black; border-radius: 10px; text-align: left">
    <thead>
        <tr>
            <th style="text-align: left">File</th>
            <th style="text-align: left">Size</th>
            <th style="text-align: left">Format</th>
            <th style="text-align: left">Dimensions(rows x columns)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: left">links</td>
            <td style="text-align: left">194 KB</td>
            <td style="text-align: left">csv</td>
            <td style="text-align: left">9742 x 3</td>
        </tr>
        <tr>
            <td style="text-align: left">movies</td>
            <td style="text-align: left">483 KB</td>
            <td style="text-align: left">csv</td>
            <td style="text-align: left">9742 x 3</td>
        </tr>
        <tr>
            <td style="text-align: left">ratings</td>
            <td style="text-align: left">2.5 MB</td>
            <td style="text-align: left">csv</td>
            <td style="text-align: left">100836 x 4</td>
        </tr>
        <tr>
            <td style="text-align: left">tags</td>
            <td style="text-align: left">116 KB</td>
            <td style="text-align: left">csv</td>
            <td style="text-align: left">3683 x 4</td>
        </tr>
    </tbody>
</table>
<h5 style="color:gray">1. Links Data File Structure (links.csv)</h5>
<p>Identifiers that can be used to link to other sources of movie data are contained in the file links.csv. Each line of this file after the header row represents one movie</p>
<table style="width:100%;border: 1px solid black; border-radius: 10px;">
    <thead>
        <tr>
            <th style="text-align: left">Column</th>
            <th style="text-align: left">Datatype</th>
            <th style="text-align: left">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: left">movieId</td>
            <td style="text-align: left">Integer</td>
            <td style="text-align: left">
                movieId is an identifier for movies used by https://movielens.org. 
                E.g., the movie Toy Story has the link https://movielens.org/movies/1
            </td>
        </tr>
        <tr>
            <td style="text-align: left">imdbId</td>
            <td style="text-align: left">Integer</td>
            <td style="text-align: left">
                imdbId is an identifier for movies used by http://www.imdb.com. E.g., the movie Toy Story has the link
                http://www.imdb.com/title/tt0114709/
            </td>
        </tr>
        <tr>
            <td style="text-align: left">tmdbId</td>
            <td style="text-align: left">Integer</td>
            <td style="text-align: left">
                tmdbId is an identifier for movies used by https://www.themoviedb.org. E.g., the movie Toy Story has the link
                https://www.themoviedb.org/movie/862
            </td>
        </tr>
    </tbody>
</table>
<h5 style="color:gray">
    2. Movies Data File Structure (movies.csv)
</h5>
<p>
    Movie information is contained in the file movies.csv. Each line of this file after the header row represents one movie.
</p>
<table  style="width:100%;border: 1px solid black; border-radius: 10px;">
    <thead>
        <tr>
            <th style="text-align: left">Column</th>
            <th style="text-align: left">Datatype</th>
            <th style="text-align: left">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: left">movieId</td>
            <td style="text-align: left">Integer</td>
            <td style="text-align: left">
                movieId is an identifier for movies used by https://movielens.org. 
                E.g., the movie Toy Story has the link https://movielens.org/movies/1
            </td>
        </tr>
        <tr>
            <td style="text-align: left">title</td>
            <td style="text-align: left">String</td>
            <td style="text-align: left">
                Movie titles are manually imported from themoviedb.org. Title of the movie includes release year of the movie
                in parentheses. Errors and inconsistencies are present.
                E.g., Toy Story (1995)
            </td>
        </tr>
        <tr>
            <td style="text-align: left">genres</td>
            <td style="text-align: left">String</td>
            <td style="text-align: left">
                Genres are a pipe-separated strings appearing as single string.
                E.g., Adventure|Animation|Children|Comedy|Fantasy
            </td>
        </tr>
    </tbody>
</table>
<h5 style="color:gray">3. Ratings Data File Structure (ratings.csv)</h5>
<p>All ratings are contained in the file ratings.csv. Each line of this file after the header row represents one rating of one movie by one user</p>
<table  style="width:100%;border: 1px solid black; border-radius: 10px;">
    <thead>
        <tr>
            <th style="text-align: left">Column</th>
            <th style="text-align: left">Datatype</th>
            <th style="text-align: left">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: left">userId</td>
            <td style="text-align: left">Integer</td>
            <td style="text-align: left">
                UserId of the user, to uniquely identify the user and his movie ratings.
            </td>
        </tr>
        <tr>
            <td style="text-align: left">movieId</td>
            <td style="text-align: left">Integer</td>
            <td style="text-align: left">
                movieId is an identifier for movies used by https://movielens.org. 
                E.g., the movie Toy Story has the link https://movielens.org/movies/1
            </td>
        </tr>
        <tr>
            <td style="text-align: left">rating</td>
            <td style="text-align: left">Float</td>
            <td style="text-align: left">
                Ratings are made on a 5-star scale, with half-star increments (0.5 stars - 5.0 stars).
            </td>
        </tr>
        <tr>
            <td style="text-align: left">timestamp</td>
            <td style="text-align: left">Integer</td>
            <td style="text-align: left">
                Timestamps represent seconds since midnight Coordinated Universal Time (UTC) of January 1, 1970.
            </td>
        </tr>
    </tbody>
</table>
<h5 style="color:gray">4. Tags Data File Structure (tags.csv)</h5>
<p>
    All tags are contained in the file tags.csv. Each line of this file after the header row represents one tag applied to one
    movie by one user
</p>
<table  style="width:100%;border: 1px solid black; border-radius: 10px;">
    <thead>
        <tr>
            <th style="text-align: left">Column</th>
            <th style="text-align: left">Datatype</th>
            <th style="text-align: left">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: left">userId</td>
            <td style="text-align: left">Integer</td>
            <td style="text-align: left">
                UserId of the user, to uniquely identify the user and his movie ratings.
            </td>
        </tr>
        <tr>
            <td style="text-align: left">movieId</td>
            <td style="text-align: left">Integer</td>
            <td style="text-align: left">
                movieId is an identifier for movies used by https://movielens.org. 
                E.g., the movie Toy Story has the link https://movielens.org/movies/1
            </td>
        </tr>
        <tr>
            <td style="text-align: left">tag</td>
            <td style="text-align: left">String</td>
            <td style="text-align: left">
                Tags are user-generated metadata about movies. Each tag is typically a single word or short phrase. The
                meaning, value, and purpose of a particular tag is determined by each user.
            </td>
        </tr>
        <tr>
            <td style="text-align: left">timestamp</td>
            <td style="text-align: left">Integer</td>
            <td style="text-align: left">
                Timestamps represent seconds since midnight Coordinated Universal Time (UTC) of January 1, 1970.
            </td>
        </tr>
    </tbody>
</table>
<hr>
<h3>Analysis</h3>
<p>
    <li>
        Analyze movie ratings and user viewing history, and provide users with personalized and recommendations based on their
        preferences and tendencies.
    </li>
    <li>
        Analyze 100k movie ratings, watch history of 610 users of some the movie of the movies released between March 29, 1996
        and September 24, 2018
    </li>
    <li>
        Plan is to use UserId, MovieId, Genres, Rating, Movie Name, tags columns to analyse and build machine learning models
        to recommendations
    </li>
</p>
<h3>Initial Implementation Details</h3>
<h5>Machine Learning Algorithms and Tools to Recommends Movies:</h5>
<ol>
    <li>Pandas or SQL</li>
    <li>K-Nearest Neighbors</li>
    <li>Deep Neurak Networks with number of hidden layers and experiment with different activation functions</li>
</ol>
<h4>
    Model Evaluation:
</h4>
<p>
    <li>
        <b>Precision</b> which is a measure of proportion of the recommended movies that user actually likes. 
    </li>
    <li>
        <b>Recall</b> which is a measure of proportion of the user's preferred movies that have been recommended.
    </li> 
</p>
<hr>
<h4>Web Application:</h4>
<p>
    <h5>Backend: Django or Flask</h5>
    <li>Rest Api will be developed to invoke or send request to machine learning model.</li>
    <li>Backend Restful application will be developed using Django or Flask Frameworks</li>
</p>
<p>
    <h5>Data Storage:</h5>
    <li>Traditional SQL database or Pandas(In Memory) will be used to store, retrieve data for the webapplication</li>
</p>
<p>
    <h5>Front End/UI:</h5>
    <li>Angular Framework will be used to develop frontend of the movie recommendation system.</li>
    <li>HTTP-Client module in angular would be used to make REST API calls</li>
</p>
<hr>
<h3>Web Application Functional Overview</h3>

<h4>Main Screen or Home Page Layout</h4>
<p>
    Movie Recommendation has two flows i.e.
    <ol>
        <li>Movie recommendation for existing users</li>
        <li>Movie recommendation for new users</li>
    </ol>
    Selecting an option from main screen will navigate us to respectice screen 
</p>

![image](https://user-images.githubusercontent.com/70106378/218270441-9383cf82-65d3-4ffa-89f8-7f63e823c30e.png)

<h4>Movie Recommendation for Existing User</h4>
<p>
    <ol>
        <li>Clicking Existing user recommendation will navigate us to this screen.</li>
        <li>Application user will be presented with 2 dropdowns. First dropdown is used to select existing user and second dropdown is used to select type of recommendation i.e. Content based, Collaborative etc</li>
        <li>After selecting the options on the dropdown and clicking on Get Recommendations will fetch movie recommendation on right side of the screen.</li>
    </ol>
</p>

![image](https://user-images.githubusercontent.com/70106378/218270197-7a40a857-4ae7-417b-b308-3f365ecd4528.png)

<h4>New User Movie Recommendation</h4>
<p>
  <ol>
      <li>Clicking on New User Recommendation will navigate us to this screen.</li>
    <li>User is presented with a searchable dropdown where he can enter movie name which is present in the dataset</li>
    <li>After selecting the movie from the dropdown and clicking on Get Recommendations will fetch top rated movies and similar movies to the selected movie in the dropdown</li>
  </ol>
</p>

![NewUserRecommendationScreen](https://user-images.githubusercontent.com/70106378/218270228-68af81a7-eed5-4ad4-8049-9f8549235580.jpg)
