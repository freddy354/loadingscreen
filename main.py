"""Loading Screen Gold: A Tip in 200 Characters.

Writes a single loading-screen tip for stressed developers and
AI coding agents to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).

Gate: entry.txt is UTF-8, exactly one line of 1-200 characters,
with no trailing newline.
"""

import os

TIP = (
    "Your agent just rewrote the same function for the third time. "
    "It is not learning. Neither are you. Take a walk."
)

MAX_LEN = 200
assert 1 <= len(TIP) <= MAX_LEN, "tip must be 1-200 characters"


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(TIP)


if __name__ == "__main__":
    main()
