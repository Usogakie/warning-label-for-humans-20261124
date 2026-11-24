"""Warning label for humans: write one funny single-line safety warning
label to ${MAKEFUN_OUTPUT_DIR:-/output}/entry.txt."""

import os

LABEL = (
    "WARNING: Human. Contents: one (1) ego, zero (0) sense of direction, "
    "and a firm belief that 'just five more minutes' means an hour."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
