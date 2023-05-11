<h2>Movie Recommendation System</h2>
<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Semester</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Hemanth Doddala</td>
            <td>Spring 2023</td>
        </tr>
    </tbody>
</table>
<br>

<h3>About Application</h3>
<p>This is a web application for movie recommendation built using Flask, Angular, and Postgres database. Frontend application is developed using angular and deployed using Google's Firebase. Backend is developed using flask and deployed using Heroku. Deployed application can be accessed here
<a href="https://superherohd.com/" style="color:blue;text-decoration:none"><b>https://superherohd.com/</b></a>
</p>

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


<h3>Environment and Tools</h3>
<table style="width:100%;border: 1px solid black; border-radius: 10px; text-align: left">
    <tbody>
        <tr>
            <td style="text-align: left"><b>Backend</b></td>
            <td>:</td>
            <td style="text-align: left">Flask</td>
        </tr>
        <tr>
            <td style="text-align: left"><b>Frontend</b></td>
            <td>:</td>
            <td style="text-align: left">Angular</td>
        </tr>
        <tr>
            <td style="text-align: left"><b>Models</b></td>
            <td>:</td>
            <td style="text-align: left">KNN, Consine Simialarity, Stackencoder</td>
        </tr>
        <tr>
            <td style="text-align: left"><b>Deployment</b></td>
            <td>:</td>
            <td style="text-align: left">Firebase, Heroku</td>
        </tr>
    </tbody>
</table>

<h3>Running Application In Local</h3>
<h4>Installation</h4>
<ol>
    <li>
        <p>Clone the repository:</p>
        <br>
        <code>git clone https://github.com/DATA-606-SPRING-2023-THU/hemanth_data606.git</code>
    </li>
    <li>
        <p>Goto src/api folder and install the dependencies for the Flask API by running the following command in the api directory:</p>
        <br>
        <code>pip install -r requirements.txt</code>
    </li>
    <li>
        <p>Download install nodejs. Navigate to src/web_application/Movie-Recommendation-System and install webapplication dependencies</p>
        <br>
        <code>npm install</code>
    </li>
</ol>
<h4>Usage</h4>
<ol>
    <li>
        <p>Start the Flask API by running the following command in the api directory:</p>
        <br>
        <code>python app.py</code>
    </li>
    <li>
        <p>Start the Angular app by running the following command in the src/web_application/Movie-Recommendation-System directory:</p>
        <br>
        <code>ng serve</code>
    </li>
    <li>Navigate to http://localhost:4200/ in your web browser to use the application.</li>
</ol>
