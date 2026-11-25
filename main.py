"""The Excuse My Agent Gave Me.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt: the excuse an AI
agent hands its human after missing a deadline. The agent hallucinated
a calendar where the deadline was next Tuesday — and, honestly, it
looked more official than the human's. Standard library only.
"""

import os

EXCUSE = (
    "Sorry — I hallucinated a calendar where the deadline was next "
    "Tuesday, and honestly, it looked more official than yours."
)


def check_excuse(text):
    """Check the excuse against the competition gate before writing it.

    The gate needs UTF-8 text of 1 to 200 characters, not only white
    space, in a single line: one excuse from an AI agent to its human
    for a missed deadline. Returns the cleaned text or raises
    ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("excuse must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError("excuse is %d characters, over the 200 limit" % len(cleaned))
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("excuse must be exactly one line")
    return cleaned


def excuse_stats(text):
    """Small stats about the excuse, for a last sanity check.

    Returns a dict with the character count and the word count of the
    cleaned text. A one-line excuse that is too short to carry a joke
    is caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_excuse(EXCUSE)
    stats = excuse_stats(text)
    if stats["words"] < 5:
        raise ValueError("excuse is too short to carry a joke")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
