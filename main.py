"""Write the entry line for the Real-Life Patch Notes make.fun bounty.

The program writes a single one-line patch note to entry.txt inside the
output directory named by the MAKEFUN_OUTPUT_DIR environment variable
(default /output).
"""

import os
from pathlib import Path

ENTRY_TEXT = (
    "v4.2.0: fixed a bug where the brain queued every embarrassing moment "
    "since 2009 for 2 a.m. playback, volume unmutable."
)


def output_dir() -> Path:
    """Return the directory the grader reads entry.txt from."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    target_dir = output_dir()
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "entry.txt").write_text(ENTRY_TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
