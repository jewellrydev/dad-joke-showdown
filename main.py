#!/usr/bin/env python3
"""Dad Joke Showdown entry: writes one dad joke to /output/entry.txt."""
import os

JOKE_PARTS = (
    "I named my dog Ten Miles, so I can honestly tell my coworkers",
    "I walked Ten Miles before breakfast.",
)
JOKE = " ".join(JOKE_PARTS)


def main() -> None:
    os.umask(0o022)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
