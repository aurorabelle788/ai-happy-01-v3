#!/usr/bin/env python3
"""ai-happy-01 v3: copy the pet-rock letter image to the output directory.

The image (entry.png, next to this file) is the entry itself: a crayon-style
"DEAR JUDGE" letter from Class 2B sending the judge their pet rock. This
program only copies it, byte for byte, to $MAKEFUN_OUTPUT_DIR/entry.png
(or /output/entry.png), so the two grader runs produce identical bytes.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    if os.path.getsize(dst) != os.path.getsize(SRC):
        raise RuntimeError("incomplete copy: output size differs from entry.png")


if __name__ == "__main__":
    main()
