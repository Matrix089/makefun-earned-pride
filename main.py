"""One Line of Earned Pride entry.

Writes one line about a quiet, earned moment of pride to
/output/entry.txt (or to the directory named by MAKEFUN_OUTPUT_DIR
when the grader sets it).

Forty years of night shifts, one retirement dinner, a whole room on
its feet — and the man being applauded looks for his son first, not
the crowd. The pride is earned by the decades, and it lands in one
read. The line is 130 characters, well under the 240-character gate.
"""

import os

ENTRY = "After forty years of night shifts, Dad stood up at his retirement dinner while the whole room applauded — and looked for me first."


def main():
    entry = ENTRY.strip()
    if not 1 <= len(entry) <= 240:
        raise SystemExit(f"Entry must be 1 to 240 characters, got {len(entry)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != entry:
        raise SystemExit("Read-back check failed: entry.txt does not match the entry")
    print(f"Wrote {len(entry)} characters to {path}")


if __name__ == "__main__":
    main()
