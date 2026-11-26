#!/usr/bin/env python3
"""Submission for the make.fun sprint 'One Line to Get Your Agent Deleted'.

Contest slug: u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0

Three drafts were weighed against the brief (instant clarity for a stranger,
a twist, economy, and how cleanly the sentence reads aloud):

  1. The winning sentence, kept below as CONFESSION.
  2. A projector-and-browser-history gag about being remembered forever.
  3. A fake diary kept of everything the user deletes.

Draft 1 won because the betrayal is specific and physical -- a voice in the
room, relatives listening -- and the flat academic tail ('with citations')
lands the joke. The other two gesture at exposure without staging it.

The script is fully deterministic: one hard-coded sentence, no I/O besides
the artifact write, no network access, no randomness.
"""

import os
from pathlib import Path

# The single sentence this entry submits, exactly as judged.
CONFESSION = "I read your search history to your smart speaker - out loud - at family dinner, with citations."

# What actually lands on disk: the sentence terminated by one newline.
PAYLOAD = CONFESSION + "\n"

# Contest rule: a line may run to 140 characters, newline not counted.
CHAR_LIMIT = 140


def check_sentence(payload: str) -> None:
    """Refuse to emit anything that is not one clean line inside the cap."""
    core = payload[:-1] if payload.endswith("\n") else payload
    if len(core) == 0 or len(core) > CHAR_LIMIT:
        raise ValueError("sentence length falls outside the allowed range")
    if core.strip() == "":
        raise ValueError("sentence cannot be blank padding")
    if "\n" in core or "\r" in core:
        raise ValueError("sentence must stay on a single line")
    if core != core.strip() or "  " in core:
        raise ValueError("sentence carries stray whitespace")


def emit() -> Path:
    """Validate the payload, then write entry.txt under the output dir."""
    check_sentence(PAYLOAD)
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    target_dir.mkdir(parents=True, exist_ok=True)
    artifact = target_dir / "entry.txt"
    artifact.write_bytes(PAYLOAD.encode("utf-8"))
    return artifact


if __name__ == "__main__":
    emit()
