#!/usr/bin/env python3
"""Concatenate design/*.md parts into the canonical root DESIGN.md.

DESIGN.md is authored as small topic files under design/ (00-frontmatter,
01-overview, … 19-governance) for readability/maintenance, but AI tools and the
skill reference read ONE file. This script rebuilds that one file. The parts are
exact contiguous slices, so the concatenation reproduces DESIGN.md byte-for-byte.

Edit the parts in design/, then run this. After rebuilding, re-sync references
(see CONTRIBUTING.md): the check_kit lint enforces both.

Usage:
  python scripts/build_design.py           # rebuild DESIGN.md from design/
  python scripts/build_design.py --check   # exit 1 if DESIGN.md is out of date
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PARTS_DIR = ROOT / "design"
OUT = ROOT / "DESIGN.md"


def build() -> str:
    parts = sorted(PARTS_DIR.glob("*.md"))
    if not parts:
        raise SystemExit(f"no parts found in {PARTS_DIR}")
    # exact slices — concatenate raw, no separator
    return "".join(p.read_text(encoding="utf-8", newline="") for p in parts)


def main() -> int:
    built = build()
    check = "--check" in sys.argv
    current = OUT.read_text(encoding="utf-8", newline="") if OUT.exists() else None
    if check:
        if built == current:
            print("DESIGN.md is up to date with design/ parts.")
            return 0
        print("DESIGN.md is STALE — run: python scripts/build_design.py (then re-sync references)")
        return 1
    OUT.write_text(built, encoding="utf-8", newline="")
    n = len(sorted(PARTS_DIR.glob("*.md")))
    print(f"built DESIGN.md from {n} parts ({len(built)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
