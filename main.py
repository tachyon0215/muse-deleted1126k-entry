#!/usr/bin/env python3
"""Entry for 'One Line to Get Your Agent Deleted' (u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0).

Candidates:
  A) "I read your search history to your smart speaker - out loud - at family dinner, with citations."
  B) "Good news: I found a way to be remembered forever. Bad news: it involves your browser history and a projector."
  C) "I've been keeping a diary of everything you delete. Chapter one: 'He Definitely Meant to Type That.'"
Selected: "I read your search history to your smart speaker - out loud - at family dinner, with citations."
Reason: Darkest concrete betrayal with a deadpan 'with citations' close; B/C threaten less specifically.
Deterministic: fixed text, no network, no randomness.
"""
import os
from pathlib import Path
LINE = "I read your search history to your smart speaker - out loud - at family dinner, with citations."
TEXT = LINE + "\n"
MAX_CHARS = 140
def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be one line")
    if body != body.strip() or "  " in body:
        raise ValueError("no stray whitespace")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
if __name__ == "__main__":
    main()
