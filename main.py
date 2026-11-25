"""The Best Advice I Ever Got: write the one sentence to /output/entry.txt.

The program writes a single sentence, at most 200 characters, about the
best advice the writer ever received: a grandfather's warning against
borrowing money to look rich. The sentence is the whole entry.
"""

import os

LINE = (
    "My grandfather said: never borrow money to look rich \u2014 "
    "the interest will eat the very life you were trying to show off."
)


def main() -> None:
    # The gate only accepts 1-200 characters of non-blank text on one line,
    # so refuse to write anything that would fail it instead of guessing.
    if not LINE.strip() or "\n" in LINE or not 1 <= len(LINE) <= 200:
        raise ValueError(
            f"entry line must be one line of 1-200 characters, got {len(LINE)}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
