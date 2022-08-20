from python:3.8-slim
run apt update -y && apt install tree

# copy ./notes ./notes
# copy ./make_index.py ./make_index.py
# copy ./rename.py ./rename.py

# run python3 make_index.py

copy . .

cmd ["python3", "-m", "http.server", "80", "-d", "markout"]
