from python:3.8-slim

copy ./app /app

cmd ["python3", "-m", "http.server", "--directory", "/app/posts", "80"]
