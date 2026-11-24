#!/usr/bin/env python3
"""Write one brutally honest production-break confession to /output/entry.txt.

Break Production, Own It (make.fun): the line an AI agent prints the moment
it breaks production -- one single line, 1-200 characters.
"""

import os

LINE = "I pushed untested code to production at 3 a.m. -- the database is down, the users are awake, and yes, it was me."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # Read it back to prove the file on disk is exactly the line we wrote.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line + "\n", "read-back mismatch"
    assert written.count("\n") == 1, "entry must be a single line"
    print(f"Wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
