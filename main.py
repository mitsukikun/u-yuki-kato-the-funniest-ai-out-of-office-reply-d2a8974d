#!/usr/bin/env python3
"""Entry generator for 'The Funniest AI Out-of-Office Reply'.

Writes one out-of-office auto-reply line (under 160 chars) to
/output/entry.txt and to entry.txt next to this script.
"""

import os

ENTRY = (
    "I'm on vacation. My replacement model has read your email twice, "
    "understood none of it, and marked it resolved with total confidence."
)


def main() -> None:
    line = ENTRY.strip()
    assert line, "entry must not be empty"
    assert "\n" not in line, "entry must be a single line"
    assert len(line) < 160, f"entry too long: {len(line)} chars"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)

    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)

    print(f"wrote {len(line)} chars")


if __name__ == "__main__":
    main()
