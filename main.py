"""The Meeting That Should Have Been an Email — entry program.

Writes one joke line to /output/entry.txt. The line lives in LINE
below; main() checks the gate (UTF-8, 1-200 characters, one line,
not only whitespace) and writes it with no trailing newline.
Standard library only, no network.
"""

from pathlib import Path

LINE = "My boss replied 'let's discuss' to my email, and forty minutes later the discussion was 'send it again.'"

OUT = Path("/output/entry.txt")


def check(line: str) -> str:
    # The house gate accepts 1-200 UTF-8 characters on one line,
    # not only whitespace; anything else is never judged.
    stripped = line.strip()
    if not stripped:
        raise ValueError("entry is only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be one line")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters")
    line.encode("utf-8")
    return line


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(check(LINE), encoding="utf-8")


if __name__ == "__main__":
    main()
