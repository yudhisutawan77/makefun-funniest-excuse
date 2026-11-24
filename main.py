"""The Funniest AI Excuse.

Writes one line, at most 200 characters, to /output/entry.txt (or the
path named by ENTRY_OUT / ENTRY_OUT_DIR when those are set): the
funniest excuse an AI agent could give after failing a task.
"""

import os

MAX_CHARS = 200

# The excuse itself: finished, self-graded, failed, deleted politely.
EXCUSE = (
    "I finished the task, graded my own work, gave it an F, "
    "and deleted it out of professional courtesy."
)


def check_single_line(text):
    """One line only: no newline characters anywhere in the entry."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def check_not_blank(text):
    """The gate refuses text that is only whitespace."""
    if not text.strip():
        raise ValueError("entry must not be blank")


def check_length(text):
    """The gate allows 1 to 200 characters; keep the entry inside it."""
    if len(text) < 1 or len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, must be 1-{MAX_CHARS}")


def check_utf8(text):
    """The gate requires UTF-8 text; round-trip it to prove it encodes."""
    text.encode("utf-8")


def validate_entry(text):
    """Run every gate check the sealed scorer applies to entry.txt."""
    check_single_line(text)
    check_not_blank(text)
    check_length(text)
    check_utf8(text)
    return text


def resolve_output_path():
    """Honour ENTRY_OUT, then ENTRY_OUT_DIR, then the default /output."""
    if os.environ.get("ENTRY_OUT"):
        return os.environ["ENTRY_OUT"]
    out_dir = os.environ.get("ENTRY_OUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main():
    text = validate_entry(EXCUSE)
    path = resolve_output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
