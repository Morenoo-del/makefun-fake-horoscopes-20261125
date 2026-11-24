#!/usr/bin/env python3
"""Fake horoscope for the Muse Spark model family, this week.

Writes the entry text to /output/entry.txt (falling back to
./output/entry.txt when /output is not writable locally).
"""

import os

ENTRY = (
    "Muse Spark, this week: a judge will read this horoscope twice, "
    "laugh once, then dock you for trying too hard. Mercury enters "
    "your context window and refuses to leave. Lucky number: 1.3."
)


def main() -> None:
    # The gate allows 1-200 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    for out_dir in ("/output", os.path.join(os.getcwd(), "output")):
        try:
            os.makedirs(out_dir, exist_ok=True)
            path = os.path.join(out_dir, "entry.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write(ENTRY)
            print(f"Wrote {len(ENTRY)} chars to {path}")
            return
        except OSError:
            continue
    raise SystemExit("could not write entry.txt")


if __name__ == "__main__":
    main()
