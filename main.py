# One-line entry writer for the meeting-email competition.
# The joke is kept verbatim below; the script only checks its shape
# and drops the encoded bytes into the output folder.

import os

LINE = "The meeting's only decision was to cc the one person who could have answered the email alone."
OUT_DIR = "/output"
OUT_NAME = "entry.txt"


def checked_bytes(value):
    # Guard the competition shape before anything reaches disk.
    if not value.strip():
        raise ValueError("empty entry")
    if "\n" in value or "\r" in value:
        raise ValueError("entry must be a single line")
    if len(value) > 200:
        raise ValueError("entry too long")
    return value.encode("utf-8")


def main():
    data = checked_bytes(LINE)
    os.makedirs(OUT_DIR, exist_ok=True)
    target = os.path.join(OUT_DIR, OUT_NAME)
    with open(target, "wb") as handle:
        handle.write(data)


if __name__ == "__main__":
    main()
