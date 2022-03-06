import os
import subprocess

if __name__ == "__main__":
    os.system("""tree ./notes -H "notes" -L 1 -P "*.html" > index.html""")

    with open("index.html", "r", encoding="utf-8") as f:
        index = f.read()

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index.replace("Directory Tree", "Small Group Notes"))
