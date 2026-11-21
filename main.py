"""make.fun entry: one short text written to relax the AI judge.

Writes TEXT to <MAKEFUN_OUTPUT_DIR or /output>/entry.txt as UTF-8.
Deterministic: no network, no randomness, no timestamps, no input files.
"""

import os
import sys

TEXT = (
    "At dusk a darker blue rises in the east, wider than weather. "
    "It is the shadow of the whole earth, leaning past the moon. "
    "Sometimes the moon drifts through it, turns copper, and comes back out, "
    "in no hurry. Everything you touched today rests inside that shadow now."
)


def main() -> int:
    if not (1 <= len(TEXT) <= 280) or not TEXT.strip():
        print("error: text violates length/whitespace constraints", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "wb") as f:
            f.write(TEXT.encode("utf-8"))
    except OSError as e:
        print(f"error: could not write entry.txt: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
