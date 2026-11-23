#!/usr/bin/env python3
"""A Day of One-Line Pitches: write one convincing sentence to /output/entry.txt."""

import os

# Friend-to-friend warmth + one concrete low-risk reason: describe it in plain
# words, see it working in minutes, change one sentence to rebuild.
LINE = "Tell it your idea in plain words, watch it build a working app in minutes, and if you don't like it, change one sentence and watch it rebuild \u2014 you risk nothing but an idea you've already had."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

# 192 characters: one sentence, one read, no jargon, nothing overpromised.
