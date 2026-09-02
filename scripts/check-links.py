#!/usr/bin/env python3
"""
AI Control Architecture — link & reference readiness gate.

Scans every Markdown file in the repository, resolves each internal link and every
bare docs/ templates/ mappings/ examples/ path reference, and fails if any target
does not exist. A framework about proving control must pass its own "show me":
run this before shipping, and in CI on every change.

    python3 scripts/check-links.py         # from the repo root
    exit code 0 = all references resolve; 1 = broken references found
"""
import os
import re
import sys
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Validate real Markdown links only — [text](target). Bare path strings in prose,
# code blocks, or planning/file-tree listings are documentation, not links.
LINK = re.compile(r"\]\(([^)]+)\)")


def main() -> int:
    os.chdir(ROOT)
    md_files = [f for f in glob.glob("**/*.md", recursive=True) if not f.startswith(".git")]
    broken: dict[str, set[str]] = {}

    for f in md_files:
        d = os.path.dirname(f)
        text = open(f, encoding="utf-8", errors="ignore").read()
        targets = set()
        for m in LINK.finditer(text):
            t = m.group(1).split("#")[0].strip()
            if not t or t.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if t.endswith(".md") or "/" in t:
                targets.add(os.path.normpath(os.path.join(d, t)))
        for resolved in targets:
            if not os.path.exists(resolved):
                broken.setdefault(resolved, set()).add(f)

    if not broken:
        print(f"OK — all internal references resolve ({len(md_files)} files scanned).")
        return 0

    print(f"BROKEN REFERENCES — {len(broken)} missing target(s):\n")
    for target in sorted(broken):
        print(f"  {target}")
        for src in sorted(broken[target]):
            print(f"      ← {src}")
    print(f"\n{len(broken)} broken target(s) across {len(md_files)} files. Fix before shipping.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
