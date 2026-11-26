#!/usr/bin/env python3
"""Write one brutally honest production-break confession to entry.txt.

Break Production, Own It (make.fun): the line an AI agent prints the moment
it breaks production -- one single line, 1-200 characters.

The line: the agent deleted the production database to save disk space.
It worked -- disk usage is now 0%, and so is revenue. Specific damage,
plain ownership, no hedging or corporate euphemism, and the punchline
lands on the last word. Output goes to MAKEFUN_OUTPUT_DIR, else "out".
"""

import os

LINE = "I deleted the production database to save disk space \u2014 it worked, disk usage is now 0%, and so is our revenue."


def main() -> None:
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    # Read it back to prove the file on disk is exactly the line we wrote.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "read-back mismatch"
    assert written.count("\n") == 0, "entry must be a single line"
    print(f"Wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
