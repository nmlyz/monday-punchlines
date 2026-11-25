#!/usr/bin/env python3
"""Write one Monday-morning punchline to /output/entry.txt.

Standard library only. Deterministic: the same bytes on every run.
"""

import os
import sys

JOKE = (
    "I tried to ghost Monday this morning. "
    "It texted back from my calendar, my inbox, "
    "and my boss's mouth."
)


def main():
    if not 1 <= len(JOKE) <= 200 or not JOKE.strip():
        raise SystemExit("entry must be 1-200 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    path = os.path.join("/output", "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
