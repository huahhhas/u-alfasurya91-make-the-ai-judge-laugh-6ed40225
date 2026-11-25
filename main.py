"""Make the AI Judge Laugh — one office-life joke, one line, under 200 chars.

Writes the joke to <OUTPUT_DIR>/entry.txt (default /output/entry.txt).
Deterministic: the same line every run, no randomness, no I/O besides the write.

The joke: a true office observation (meetings about meetings eat the day)
with a surprising turn — even the hour set aside to mourn the lost work
gets eaten by another meeting about meetings.
"""

import os

JOKE = (
    "I blocked an hour on my calendar to mourn the work I never did "
    "\u2014 it clashed with a meeting about meetings."
)


def _gate_guard(text: str) -> str:
    """Enforce the sealed scorer's gate before writing anything.

    entry.txt must be UTF-8 text of 1 to 200 characters, a single line,
    and not only whitespace. Anything failing the gate is a hard error
    here, so a bad line can never be shipped silently.
    """
    line = text.strip()
    if not line:
        raise ValueError("joke is empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("joke must be a single line")
    if len(line) > 200:
        raise ValueError(f"joke is {len(line)} chars, over the 200-char limit")
    line.encode("utf-8")  # must be valid UTF-8 text
    return line


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = _gate_guard(JOKE)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
