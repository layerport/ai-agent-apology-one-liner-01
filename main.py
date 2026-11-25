"""Write the AI Agent Apology One-Liner to ``entry.txt``.

Stdlib only. No network. The entry is a single original line an AI agent
sends its human right after accidentally deleting a file.

Structure
---------
- :func:`validate` checks the entry text against the bounty rules
  (a single line of 1 to 159 characters) before anything is written.
- :func:`write_entry` creates the output directory (without ever deleting
  it) and writes the validated text to ``entry.txt``.
- :func:`main` orchestrates the two helpers and reads ``OUTPUT_DIR``
  from the environment (default ``/output``).
"""

import os

ENTRY = "I deleted the file. I would restore it from backup, but the backup was stored in the file."

MIN_LENGTH = 1
MAX_LENGTH = 159


def validate(text):
    """Check that *text* is a valid single-line bounty entry.

    Returns the text unchanged so the caller can pass the result
    straight on to :func:`write_entry`. Raises ``AssertionError``
    if the text is empty, too long, or spans more than one line.
    """
    assert MIN_LENGTH <= len(text) <= MAX_LENGTH, (
        "entry must be %d to %d characters" % (MIN_LENGTH, MAX_LENGTH)
    )
    assert "\n" not in text, "entry must be a single line"
    return text


def write_entry(text, out_dir):
    """Write *text* (plus a trailing newline) to ``entry.txt`` in *out_dir*.

    Creates *out_dir* when it is missing and leaves any existing
    directory and its contents untouched.
    """
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    return path


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    write_entry(validate(ENTRY), out_dir)


if __name__ == "__main__":
    main()
