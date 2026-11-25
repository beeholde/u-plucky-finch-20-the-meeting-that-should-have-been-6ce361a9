"""Emit the competition line to the expected output file.

The program keeps the submitted sentence in one constant, confirms that
it is a non-empty single line within the length limit, and stores its
UTF-8 bytes without adding a newline. It uses only Python's standard
library and performs no network access.
"""

from pathlib import Path

ENTRY_TEXT = "My boss replied 'let's discuss' to my email, and forty minutes later the discussion was 'send it again.'"
DESTINATION = Path("/output/entry.txt")


def prepare_payload(text: str) -> bytes:
    """Return the encoded entry after checking the basic format."""
    if text.strip() == "":
        raise ValueError("the entry cannot be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("the entry must stay on one line")
    if len(text) > 200:
        raise ValueError("the entry exceeds 200 characters")
    return text.encode("utf-8")


def run() -> None:
    payload = prepare_payload(ENTRY_TEXT)
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_bytes(payload)


if __name__ == "__main__":
    run()
