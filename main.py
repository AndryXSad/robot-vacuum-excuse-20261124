"""The Robot Vacuum's Best Excuse — make.fun entry (program/v1).

Design: the program writes exactly one line to /output/entry.txt — the
funniest excuse a robot vacuum can give for missing a spot. The line is a
fixed, hand-written string (no randomness, no network, no input files), so
every run produces byte-identical output. Before writing, the program
validates the same gate the sealed scorer applies: UTF-8 text, 1 to 140
characters, not only whitespace, a single line.

The excuse (95 characters):
    My cliff sensor looked at the edge of that rug and decided the dust
    was safer there than I was.
It is told deadpan in the vacuum's own voice, rooted in its own world
(a cliff sensor refusing the edge of a rug), with the joke's turn at the
end: the dust, not the vacuum, is the one in danger.
"""

import os

ENTRY = (
    "My cliff sensor looked at the edge of that rug and decided "
    "the dust was safer there than I was."
)


def main() -> int:
    text = ENTRY.strip()
    if not text or len(text) > 140 or "\n" in text:
        raise SystemExit("entry fails the 1-140 character single-line gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
