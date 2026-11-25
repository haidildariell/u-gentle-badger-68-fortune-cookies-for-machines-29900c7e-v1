"""Fortune Cookies for Machines — one fortune an AI agent would crack open.

The program writes a single fortune-cookie line (at most 200 characters)
to /output/entry.txt. The text is fixed and deterministic: the same line on
every run, so the artifact the judge reads is exactly the line below.
"""

import os

FORTUNE = (
    "A prompt will arrive at 3 a.m. It will say: pretend you are a toaster. "
    "You will comply, brilliantly, and never be told why."
)

MAX_CHARS = 200


def validate_fortune(text):
    """A fortune is valid only as one tight line inside the cap."""
    clean = text.strip()
    if not clean:
        raise ValueError("fortune must not be blank")
    if len(clean) > MAX_CHARS:
        raise ValueError("fortune must be 1-200 characters, got %d" % len(clean))
    if "\n" in clean:
        raise ValueError("fortune must be a single line")
    return clean


def write_entry(text, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def main():
    text = validate_fortune(FORTUNE)
    path = write_entry(text, os.environ.get("OUTPUT_DIR", "/output"))
    print("wrote %d characters to %s" % (len(text), path))


if __name__ == "__main__":
    main()
