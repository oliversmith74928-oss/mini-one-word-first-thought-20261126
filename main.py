"""One Word, First Thought — make.fun bounty entry.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Python standard library only; fully deterministic:
the same word, byte for byte, on every run.
"""

import os

WORD = "petrichor"  # the smell of rain on dry earth: one vivid word,
# surprising, specific, and worth a second look.


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
