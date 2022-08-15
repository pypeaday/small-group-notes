from pathlib import Path
from string import Template

t = Template(
    """
---
templateKey: blog-post
tags: ['bema']
title: $title
date: 2022-01-$i
status: published
cover: ""
---

$notes
             """
)


def main():
    files = sorted(list(Path("./notes").glob("*.html")))
    for i, f in enumerate(files):

        i = min(i + 1, 31)
        text = f.read_text()

        new = t.substitute(
            notes=text, title=f.stem.replace(":", ""), i=f"{i}T00:00:00".zfill(2)
        )

        Path(f"./pages/bema/{f.stem.replace(':', '').replace(' ', '-')}.md").write_text(
            new
        )


if __name__ == "__main__":
    main()
