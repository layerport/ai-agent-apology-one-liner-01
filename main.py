"""Write the AI Agent Apology One-Liner to /output/entry.txt.

Stdlib only. No network. The entry is a single original line an AI agent
sends its human right after accidentally deleting a file.
"""

import os

ENTRY = "I deleted the file. I would restore it from backup, but the backup was stored in the file."


def main():
    text = ENTRY
    assert 1 <= len(text) <= 159, "entry must be 1 to 159 characters"
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
