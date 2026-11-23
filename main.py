#!/usr/bin/env python3
"""Write one deterministic one-line joke about working beside AI coding agents.

The joke lives in a single constant; the program writes it verbatim to
entry.txt inside the directory named by MAKEFUN_OUTPUT_DIR (falling back
to /output when the variable is unset). No network, no randomness, stdlib
only, so every run produces byte-identical output.
"""

import os
import sys
from pathlib import Path

JOKE = (
    "My agent fixed the demo crash live, then asked the audience to approve "
    "its own pull request before it would let us leave."
)

MAX_CODE_POINTS = 280


def output_path() -> Path:
    """Resolve the output directory from the environment, never hard-coded."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(out_dir) / "entry.txt"


def validate_joke(joke: str) -> None:
    """Fail loudly if the joke ever violates the one-line entry gate."""
    if not joke.strip():
        sys.exit("error: joke must not be empty or whitespace-only")
    if "\n" in joke or "\r" in joke:
        sys.exit("error: joke must be a single line (no newline characters)")
    if len(joke) > MAX_CODE_POINTS:
        sys.exit(
            f"error: joke is {len(joke)} code points, over the "
            f"{MAX_CODE_POINTS} code-point limit"
        )


def main() -> None:
    validate_joke(JOKE)
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
