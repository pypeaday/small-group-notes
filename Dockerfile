from python:3.8-slim

copy ./app /app

cmd ["python3",  "server.py"]
