"""Rename tiddler exports"""

from pathlib import Path
import os


def get_new_name(filepath: Path) -> Path:

    try:
        digi, title = filepath.name.split("_")
    except ValueError:  # not a numbered post
        return filepath
    new_digi = "{0}".format(digi.zfill(2))

    new_filename = Path(filepath.parent, f"{new_digi}:{title}")
    return new_filename


def main(directory: str):

    for _file in Path(directory).glob("*.html"):
        new_filename = get_new_name(_file)
        os.rename(str(_file), str(new_filename))
        # print(f"renaming {_file} to {new_filename}")


if __name__ == "__main__":
    main("./posts")
