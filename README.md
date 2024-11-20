# IDS706 Week 12 Movie Service API

This repository contains a Flask-based web application that provides a movie service API. It allows users to fetch, search, and classify movies by title or genre and integrates with a language model for sentiment-based genre classification.

![flask_app](static/images/flaskApp.JPG)

[Dockerhub Image](https://hub.docker.com/repository/docker/alejandroparedeslatorre/flask-app/general) 

---

## Features

- **Home Page**: Render static pages, including a home page and predefined route pages.
- **Fetch Movies**: Retrieve a list of movies from a database.
- **Search Movies**: Search movies by title or genre.
- **Genre Classification**: Classify input text into a movie genre using an external language model API.
- **Error Logging**: Comprehensive logging for debugging and monitoring.

---

## Installation Using Docker

### Prerequisites

- Docker installed on your system.
- API key for the Gemini Language Model.

### Steps

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Create a `.env` file in the root directory and add the required environment variables:

   ```env
   LLM_API_KEY=your_api_key_here
   ```

3. Build the Docker image:

   ```bash
   docker build -t movie-service-api .
   ```

4. Run the Docker container:

   ```bash
   docker run -d -p 5000:5000 --env-file .env movie-service-api
   ```

5. Access the application in your browser at:

   ```
   http://localhost:5000
   ```

---

## Endpoints

### 1. **Static Pages**
#### `GET /`
- Renders the home page.

#### `GET /<page>`
- Renders a predefined static page (`search_page` or `bygenre_page`).

---

### 2. **Movies**
#### `GET /movies`
- Fetches a list of movies from the database.
- **Response**: JSON array of movie details.

#### `GET /movie/<int:movie_id>`
- Fetches details of a specific movie by ID.
- **Response**: JSON object of movie details or error message.

---

### 3. **Search**
#### `GET /search`
- Searches for movies by title.
- **Query Params**: `title`
- **Response**: JSON array of movies matching the title.

#### `GET /bygenre`
- Searches for movies by genre.
- **Query Params**: `genre`
- **Response**: JSON array of movies matching the genre.

---

### 4. **Genre Classification**
#### `POST /classify`
- Classifies the input text into a movie genre using the Gemini API.
- **Request Body**: 
    ```json
    {
        "text": "Your input text here"
    }
    ```
- **Response**: JSON array of movies matching the classified genre.

---

## Logging

Logs are stored in `app.log` and displayed in the console. Adjust the logging level in the `logging.basicConfig()` configuration.

---

## Error Handling

The application handles:
- Database connection errors
- API request errors
- Invalid or missing input errors

---

## License

This project is licensed under the MIT License.

--- 

### Notes:
- This version replaces the manual setup steps with Docker-based instructions for simplicity and consistency across environments.
- Ensure Docker is running on your system before proceeding.