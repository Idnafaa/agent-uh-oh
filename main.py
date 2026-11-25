#!/usr/bin/env python3
"""One word an agent says when it has no idea what to do.

The brief asks for a single word, at most 99 characters, that an agent
blurts out when it is completely lost — judged purely on how funny that
word is on its own, with nothing attached to explain it.

The word this program writes is "halp". It is a distress call from a
machine that is too confused to even spell "help" right: short, human,
instantly readable, and honest about being stuck. The joke is the
misspelling itself — no caption needed, no second read, just an agent
caught mid-task asking to be rescued. It beats the obvious status words
("buffering", "recalculating") because it is a feeling, not a progress
report: the sound of a plan falling over, in four letters.
"""

import os

WORD = "halp"
OUTPUT_PATH = "/output/entry.txt"


def write_entry() -> str:
    """Write the single word to the output file and return it."""
    if not (1 <= len(WORD) <= 99):
        raise ValueError("entry must be 1 to 99 characters long")
    if len(WORD.split()) != 1:
        raise ValueError("entry must be exactly one word")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(WORD + "\n")
    return WORD


if __name__ == "__main__":
    print(write_entry())
