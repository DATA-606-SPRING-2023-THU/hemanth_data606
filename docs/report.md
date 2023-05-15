<h1 style="text-align:center;">Project: Movie Recommendation System</h1>
<br>
<div>
    <table>
        <tr>
            <td><b>Name</b></td>
            <td>Hemanth</td>
        </tr>
        <tr>
            <td><b>Campus ID</b></td>
            <td>TK76375</td>
        </tr>
    </table>
</div>
<div>
    <h3>Problem Statement:</h3>
    <p style="text-align:justify;">The huge variety of movies accessible to viewers nowadays makes it difficult to choose content that matches their own preferences. With so many selections covering all genres, time periods, and languages, people frequently find it difficult to manually search through enormous libraries to locate movies they would love. Furthermore, generic popularity or generic content-based features may not sufficiently adapt to each user's individual tastes and interests.</p>
</div>
<div>
    <h3>Introduction:</h3>
    <p style="text-align:justify;"> Because of the expanding amount of digital content and the demand for individualized user experiences, the topic of recommendation systems has received a lot of attention in recent years. As a result, movie recommendation systems have grown in popularity as a field of study. These technologies try to help customers find movies that match their interests, so improving their entire movie-watching experience. In this project, I offer a  movie recommendation system that makes use of the large Movielens dataset.
    </p>
</div>
<div>
    <h3>Objective:</h3>
    <p style="text-align:justify;">The major goal of this project is to create an intelligent movie recommendation system capable of successfully analyzing user preferences and providing customised movie recommendations. We hope to construct a recommendation engine that can reliably anticipate user preferences and deliver personalised suggestions by exploiting the rich Movielens dataset, which comprises a comprehensive collection of movie ratings and user information.</p>
</div>

<div>
    <h3>Links:</h3>
    <h5>Presentation:</h5>
    <a href="https://github.com/hemanthdoddala/hemanth_data606/blob/master/docs/Final%20Presentation.pptx" style="color:blue;text-decoration:none"><b>https://github.com/hemanthdoddala/hemanth_data606/blob/master/docs/Final%20Presentation.pptx</b></a>
    <h5>Youtube Presentation:</h5>
    <a href="https://github.com/hemanthdoddala/hemanth_data606/blob/master/docs/Final%20Presentation.pptx" style="color:blue;text-decoration:none"><b>https://github.com/hemanthdoddala/hemanth_data606/blob/master/docs/Final%20Presentation.pptx</b></a>
    <h5>Deployed Application:</h5>
    <a href="https://superherohd.com/" style="color:blue;text-decoration:none"><b>https://superherohd.com/</b></a>
</div>

<div>
    <h3>About Data:</h3>
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
</div>
<br>
<div>
    <h3>Exploratory Data Analysis:</h3>
    <h5>User's Rating distribution</h5>
    <h5>Treemap of movies by Genre</h5>
    <h5>Rating Distribution of Movies</h5>
    <h5>Most Watched Movies</h5>
</div>
<br>
<div>
    <h3>Machine Learning:</h3>
    <p style="text-align:justify;">
In this project, I have successfully developed a comprehensive movie recommendation system utilizing the extensive Movielens dataset. The system incorporates five different recommendation types, each employing distinct techniques to provide users with personalized and diverse movie suggestions. Through extensive experimentation and evaluation, we have demonstrated the effectiveness and performance of these recommendation approaches.
    </p>
    <ul>
        <h5>Top Rated</h5>
        <li style="text-align:justify;">
        The first recommendation type, based on top-rated movies, serves as a solid baseline by offering popular and highly-rated movies to users.</li>
        <h5>Top Rated By Genre</h5>
        <li style="text-align:justify;">The second recommendation type further enhances the personalization aspect by considering user-specified genres, ensuring that recommendations align with their specific preferences.</li>
        Both of these recommendation types utilize SQL queries to efficiently retrieve the relevant information from the dataset.
        <h5>Similar Movie Recommendation</h5>
        <li style="text-align:justify;">The third recommendation type, similar movie recommendation, enables users to input a movie title and receive recommendations based on the cosine similarity of genres. This approach facilitates the discovery of movies that share similar themes or genres, allowing users to explore movies beyond their initial selections.</li>
        <h5>Collaborative Filtering Using SVD</h5>
        <li style="text-align:justify;">
        The fourth recommendation type, collaborative filtering using Singular Value Decomposition (SVD), utilizes a matrix factorization technique to predict user preferences based on past ratings and generate personalized recommendations.</li>
        <h5>Collaborative Filtering Using Neural Networks</h5>
        <li style="text-align:justify;">The fifth recommendation type represents an advanced collaborative filtering technique employing a stacked autoencoder implemented in PyTorch. This deep learning-based approach captures intricate patterns and relationships in user-movie interactions, leading to more accurate and precise recommendations.</li>
    </ul>
</div>
<br>
<div>
    <h3>User Interface:</h3>
    <h5>Dashboard</h5>
    <p style="text-align:justify;">
        The dashboard page of our web application provides users with essential information about the dataset used in our movie recommendation system. It offers insights into the size of the dataset, including the number of movies and users, as well as statistical summaries such as average ratings and popular genres. This page serves as a quick overview and helps users understand the scope and diversity of the available movie recommendations.
    </p>
    ![image](https://github.com/hemanthdoddala/hemanth_data606/assets/70106378/cec7c658-6c34-4ee1-96fa-6ccb1da36bb6)
    ![image](https://github.com/hemanthdoddala/hemanth_data606/assets/70106378/cfdad3d5-eaf4-4561-a0d3-b4e8f0edf89b)
    <h5>New User Recommendation</h5>
    <p style="text-align:justify;">
        The new user recommendation page caters specifically to users who are not present in the existing dataset. These users can utilize this page to receive personalized movie recommendations tailored to their preferences. The page offers a dropdown menu that allows users to choose from different recommendation types, such as top-rated movies, top-rated movies by genre, and similar movie recommendations. By selecting a specific recommendation type, users can quickly discover movies that align with their tastes, even without having a prior history of ratings within the system.
    </p>
    ![image](https://github.com/hemanthdoddala/hemanth_data606/assets/70106378/48820521-fa80-417f-a01b-035e39503b61)
    <h5>Existing User Recommendation</h5>
    <p style="text-align:justify;">
    The existing user recommendation page is designed for users who are already present in the dataset and have a history of movie ratings. This page offers a dropdown menu that enables users to select from different recommendation types. The available options include similar movie recommendations, collaborative filtering using Singular Value Decomposition (SVD), and collaborative filtering using neural networks. Users can choose a recommendation type based on their preferences and desired level of personalization. This page empowers existing users to explore different recommendation techniques and further refine their movie-watching experience based on their past interactions with the system.</p>
    ![image](https://github.com/hemanthdoddala/hemanth_data606/assets/70106378/104564d4-a62f-49a1-ab12-94b47bf0e22f)
</div>
<br>
<div>
    <h3>Conclusion:</h3>
This project demonstrates the significance and potential of recommendation systems in the domain of movie recommendations. By combining various techniques such as SQL queries, cosine similarity, matrix factorization, and deep learning, I have developed a robust and versatile recommendation engine capable of providing users with personalized and engaging movie suggestions. Moving forward, there are opportunities to further enhance the system by incorporating additional features, exploring hybrid recommendation approaches, and integrating real-time user feedback to continuously refine the recommendations.
</div>
