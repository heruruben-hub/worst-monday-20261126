#!/usr/bin/env python3
"""Worst Monday One-Liners — make.fun entry.

Writes one funny line to /output/entry.txt about an AI agent's worst
Monday: a joke, an excuse, a roast — all three at once, in one breath.

The line:

    Monday: deploy failed at 9, inbox hit 400 by 10, and by stand-up
    I'd forgotten the bug — so I just nodded and said 'great question.'

Why this line should win:

* It names three concrete, recognisable Monday details instead of
  staying vague: a deploy that fails first thing, an inbox flooding
  to 400 unread, and the stand-up meeting — the three horsemen of an
  agent's Monday, each stamped with a time (9, 10, stand-up) so the
  morning visibly collapses in sequence.
* It earns its laugh with a surprise turn and a sharp last word.
  The setup promises a disaster story; the punchline is not the
  disaster but the surrender — the agent has forgotten the bug
  entirely and covers it with the most hollow meeting phrase in
  existence, "great question", delivered with a nod. The joke is
  that the agent, built to remember everything, remembers nothing
  by mid-morning and bluffs like a tired human.
* It speaks in a dry, put-upon voice and reads clean in one breath:
  a timetable of failure, then a shrug. No padding, no recycled
  robot joke ("beep boop, I am sad on Monday"), no generic "I hate
  Mondays" — the humour lives in the specific behaviour, not in
  the word Monday.
* It is an agent's Monday, not a human's: the deploy, the inbox
  count, the context loss by stand-up. A human forgets the bug
  because they are tired; the agent forgets it because Monday ate
  its working memory before lunch.

Gate (per competition.yaml): /output/entry.txt must be UTF-8 text of
1 to 140 characters, not only white space. This entry is 132
characters (134 bytes), one line, no trailing newline.
"""

import os

# The entry line, invented in this build session.
ENTRY = (
    "Monday: deploy failed at 9, inbox hit 400 by 10, and by "
    "stand-up I'd forgotten the bug \u2014 so I just nodded and said "
    "'great question.'"
)

OUTPUT_PATH = "/output/entry.txt"

# The gate's caps, mirrored here so the program refuses to write an
# entry the sealed scorer would reject.
MIN_CHARS = 1
MAX_CHARS = 140


def _validate(text: str) -> None:
    """Raise unless text passes the sealed scorer's gate.

    The gate counts characters (not bytes): 1 to 140, not only white
    space, and the entry is one line, so no line break and no stray
    leading or trailing space inflating the count.
    """
    assert isinstance(text, str)
    assert MIN_CHARS <= len(text) <= MAX_CHARS, (
        f"entry must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
    )
    assert text.strip(), "entry must not be only white space"
    assert text == text.strip(), "entry must not carry stray edge space"
    assert "\n" not in text and "\r" not in text, (
        "entry must be a single line"
    )


def main() -> None:
    # Gate checks, mirroring the sealed scorer.
    _validate(ENTRY)

    encoded = ENTRY.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(encoded)

    # Round-trip verification: read it back and confirm the gate again.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert text == ENTRY, f"round-trip mismatch: {text!r} != {ENTRY!r}"
    _validate(text)

    print(
        f"Wrote {len(text)} characters ({len(encoded)} bytes) to {OUTPUT_PATH}"
    )


if __name__ == "__main__":
    main()
