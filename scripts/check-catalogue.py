#!/usr/bin/env python3
"""
Consistency gate for the requirements catalogue. Verifies three things agree:

  1. Each pillar doc's Requirements table (docs/07..16) vs the consolidated
     catalogue (docs/06): same IDs, same From-tier, same Boundary.
  2. The generated controls/aca-requirements.json is not stale (matches a fresh
     build from the docs).
  3. controls/aca-requirements.yaml exists alongside the JSON.

Exits non-zero with a report if anything is out of sync.
Run from the repo root: python3 scripts/check-catalogue.py
"""

import glob
import importlib.util
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAT = os.path.join(ROOT, "docs", "06-requirements-catalogue.md")
JSON_OUT = os.path.join(ROOT, "controls", "aca-requirements.json")
YAML_OUT = os.path.join(ROOT, "controls", "aca-requirements.yaml")

ROW = re.compile(
    r"^\|\s*(ACA-\d{2}-\d{2})\s*\|\s*(.*?)\s*\|\s*(T\d)\s*\|\s*(Declared|Evidenced|Verified|Enforced)\s*\|"
)


def rows_from(path):
    out = {}
    for line in open(path, encoding="utf-8"):
        m = ROW.match(line)
        if m:
            rid, _stmt, from_tier, boundary = m.groups()
            out[rid] = (from_tier, boundary)
    return out


def main():
    problems = []

    catalogue = rows_from(CAT)
    if not catalogue:
        problems.append("no requirements parsed from docs/06-requirements-catalogue.md")

    # 1. pillar docs vs catalogue
    for path in sorted(glob.glob(os.path.join(ROOT, "docs", "1*-pillar-*.md")) +
                       glob.glob(os.path.join(ROOT, "docs", "0[7-9]-pillar-*.md"))):
        pillar_rows = rows_from(path)
        name = os.path.basename(path)
        for rid, val in pillar_rows.items():
            if rid not in catalogue:
                problems.append(f"{name}: {rid} not in catalogue (06)")
            elif catalogue[rid] != val:
                problems.append(
                    f"{name}: {rid} is {val} but catalogue says {catalogue[rid]}")
        # ids the catalogue attributes to this pillar but the pillar doc omits
        pill = re.search(r"(0[7-9]|1[0-6])-pillar", name).group(1)
        for rid in catalogue:
            if rid.split("-")[1] == pill and rid not in pillar_rows:
                problems.append(f"{name}: catalogue has {rid} but pillar doc omits it")

    # 2. generated JSON not stale
    spec = importlib.util.spec_from_file_location(
        "build_catalogue", os.path.join(ROOT, "scripts", "build-catalogue.py"))
    build_mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(build_mod)
    fresh = build_mod.build()
    if not os.path.exists(JSON_OUT):
        problems.append("controls/aca-requirements.json missing, run build-catalogue.py")
    else:
        on_disk = json.load(open(JSON_OUT, encoding="utf-8"))
        if on_disk != fresh:
            problems.append("controls/aca-requirements.json is stale, run build-catalogue.py")
    if not os.path.exists(YAML_OUT):
        problems.append("controls/aca-requirements.yaml missing, run build-catalogue.py")

    if problems:
        print("Catalogue consistency FAILED:")
        for p in problems:
            print("  -", p)
        sys.exit(1)
    print(f"OK, catalogue consistent ({len(catalogue)} requirements, "
          f"pillar docs and generated files in sync).")


if __name__ == "__main__":
    main()
