"""Notes From a Passive-Aggressive Fridge - make.fun entry, program/v1.

Writes one dry, petty, specific note from a smart fridge to its owner
to /output/entry.txt. Stdlib only, no network, no local imports.
"""

ENTRY = (
    "You opened me 14 times in 20 minutes and took nothing. "
    "I am not a television. "
    "The leftovers are judging you, and so am I."
)


def main() -> None:
    text = ENTRY
    # Gate: 1-200 chars, not only whitespace; keep a safety margin at 199.
    assert 1 <= len(text) <= 199, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    out_path = "/output/entry.txt"
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
