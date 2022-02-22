from python:3.8-slim

copy ./posts ./posts

cmd ["python3",  "server.py"]
