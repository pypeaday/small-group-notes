from python:3.8-slim
run apt update -y && apt install tree

copy . .
run python3 make_index.py

cmd ["python3", "-m", "http.server", "80"]
