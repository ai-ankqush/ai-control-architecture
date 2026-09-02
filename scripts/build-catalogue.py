#!/usr/bin/env python3
"""
Build the machine-readable AI Control Architecture requirements catalogue.

Source of truth: docs/06-requirements-catalogue.md (the requirement rows) plus the
curated pillar metadata below. Emits:

    controls/aca-requirements.yaml
    controls/aca-requirements.json

Run from the repository root:  python3 scripts/build-catalogue.py
Dependency-free (standard library only).
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "docs", "06-requirements-catalogue.md")
OUT_DIR = os.path.join(ROOT, "controls")

VERSION = open(os.path.join(ROOT, "VERSION.md")).read().strip()

# Curated pillar metadata. Framework tags are pillar-level in v0.1; provision-level
# detail lives in mappings/. Keep in sync with the pillar docs (07..16).
PILLARS = {
    "07": {"name": "AI Inventory & Classification",
           "surface": "See (precondition for all three)",
           "question": "What AI exists?",
           "nist_functions": ["Map"],
           "frameworks": ["NIST-AI-RMF", "ISO-42001", "EU-AI-ACT", "SR-11-7"]},
    "08": {"name": "AI Identity & Access Control",
           "surface": "See (and the foundation of Do)",
           "question": "Under what identity and access does the AI act?",
           "nist_functions": ["Manage"],
           "frameworks": ["NIST-AI-RMF", "ISO-42001", "EU-AI-ACT", "NYDFS-500", "OWASP-LLM"]},
    "09": {"name": "Data Boundary Control",
           "surface": "See",
           "question": "What can it see?",
           "nist_functions": ["Map", "Manage"],
           "frameworks": ["NIST-AI-RMF", "ISO-42001", "EU-AI-ACT", "NYDFS-500", "GDPR", "OWASP-LLM"]},
    "10": {"name": "Prompt & Input Control",
           "surface": "See (the input path into inference)",
           "question": "What is shaping the AI's behavior?",
           "nist_functions": ["Measure", "Manage"],
           "frameworks": ["NIST-AI-RMF", "ISO-42001", "EU-AI-ACT", "OWASP-LLM", "OWASP-AGENTIC"]},
    "11": {"name": "Output & Decision Control",
           "surface": "Decide",
           "question": "What can it decide?",
           "nist_functions": ["Measure", "Manage"],
           "frameworks": ["NIST-AI-RMF", "ISO-42001", "EU-AI-ACT", "SR-11-7"]},
    "12": {"name": "Tool & Action Control",
           "surface": "Do",
           "question": "What can it do?",
           "nist_functions": ["Manage"],
           "frameworks": ["NIST-AI-RMF", "ISO-42001", "EU-AI-ACT", "OWASP-LLM", "OWASP-AGENTIC"]},
    "13": {"name": "Human Accountability Model",
           "surface": "Spans See, Decide, Do",
           "question": "Who is accountable?",
           "nist_functions": ["Govern"],
           "frameworks": ["NIST-AI-RMF", "ISO-42001", "EU-AI-ACT", "SR-11-7"]},
    "14": {"name": "AI Assurance & Testing",
           "surface": "Proves the boundedness of See, Decide, Do",
           "question": "Do the controls hold?",
           "nist_functions": ["Measure"],
           "frameworks": ["NIST-AI-RMF", "ISO-42001", "EU-AI-ACT", "SR-11-7"]},
    "15": {"name": "Monitoring, Logging & Evidence",
           "surface": "Observes See, Decide, Do",
           "question": "Can we reconstruct what it did?",
           "nist_functions": ["Measure", "Manage"],
           "frameworks": ["NIST-AI-RMF", "ISO-42001", "EU-AI-ACT", "NYDFS-500", "SR-11-7"]},
    "16": {"name": "Incident Containment & Recovery",
           "surface": "Makes See, Decide, Do reversible",
           "question": "Can we stop and recover?",
           "nist_functions": ["Manage"],
           "frameworks": ["NIST-AI-RMF", "ISO-42001", "EU-AI-ACT", "NYDFS-500", "SR-11-7"]},
}

TIERS = {
    "T1": {"name": "Low-risk productivity or public-data use", "applies_to": "public or non-sensitive data, no decision impact, no tool or action capability"},
    "T2": {"name": "Internal productivity with enterprise data or vendor AI", "applies_to": "uses internal enterprise data or vendor AI for productivity, without influencing decisions or taking actions"},
    "T3": {"name": "Decision-supporting AI", "applies_to": "influences human decisions, judgments, or records (classify, rank, score, summarize, recommend)"},
    "T4": {"name": "Action-capable AI", "applies_to": "can call tools, trigger workflows, or prepare, request, or perform actions in enterprise systems"},
    "T5": {"name": "High-impact autonomous or regulated AI", "applies_to": "affects employment, credit, legal, safety, healthcare, regulated, privileged, or difficult-to-reverse outcomes"},
}
TIER_ORDER = ["T1", "T2", "T3", "T4", "T5"]
BOUNDARY_SOURCES = ["Declared", "Evidenced", "Verified", "Enforced"]

ROW = re.compile(
    r"^\|\s*(ACA-\d{2}-\d{2})\s*\|\s*(.*?)\s*\|\s*(T\d)\s*\|\s*(Declared|Evidenced|Verified|Enforced)\s*\|"
)
KEYWORD = re.compile(r"\b(SHALL|SHOULD|MAY)\b")


def parse_requirements():
    reqs = []
    for line in open(SRC, encoding="utf-8"):
        m = ROW.match(line)
        if not m:
            continue
        rid, statement, from_tier, boundary = m.groups()
        statement = statement.replace("**", "").strip()
        kw = KEYWORD.search(statement)
        pillar = rid.split("-")[1]
        if pillar not in PILLARS:
            sys.exit(f"ERROR: {rid} references unknown pillar {pillar}")
        reqs.append({
            "id": rid,
            "pillar": pillar,
            "statement": statement,
            "normative_keyword": kw.group(1) if kw else None,
            "from_tier": from_tier,
            "applies_to_tiers": TIER_ORDER[TIER_ORDER.index(from_tier):],
            "boundary": boundary,
        })
    reqs.sort(key=lambda r: r["id"])
    return reqs


def build():
    reqs = parse_requirements()
    catalogue = {
        "schema": "aca-requirements/v0.1",
        "title": "AI Control Architecture, Requirements Catalogue",
        "version": VERSION,
        "license": "CC-BY-4.0",
        "homepage": "https://aicontrolarchitecture.org",
        "source_of_truth": "docs/06-requirements-catalogue.md",
        "generated_by": "scripts/build-catalogue.py",
        "notes": "Framework tags are pillar-level in this version; provision-level mappings live in mappings/.",
        "tiers": TIERS,
        "boundary_sources": BOUNDARY_SOURCES,
        "pillars": [dict(id=k, **v) for k, v in sorted(PILLARS.items())],
        "requirements": reqs,
    }
    return catalogue


# --- minimal, dependency-free YAML emitter for this known structure ---

def y(v):
    """Serialize a scalar as a YAML-safe (JSON-compatible) token."""
    if v is None:
        return "null"
    if isinstance(v, (list, tuple)):
        return "[" + ", ".join(y(x) for x in v) + "]"
    return json.dumps(v, ensure_ascii=False)


def emit_yaml(cat):
    out = []
    out.append("# AI Control Architecture, machine-readable requirements catalogue")
    out.append("# Generated by scripts/build-catalogue.py. Do not edit by hand.")
    out.append("# Source of truth: docs/06-requirements-catalogue.md")
    for key in ["schema", "title", "version", "license", "homepage",
                "source_of_truth", "generated_by", "notes"]:
        out.append(f"{key}: {y(cat[key])}")

    out.append("tiers:")
    for t in TIER_ORDER:
        info = cat["tiers"][t]
        out.append(f"  {t}:")
        out.append(f"    name: {y(info['name'])}")
        out.append(f"    applies_to: {y(info['applies_to'])}")

    out.append(f"boundary_sources: {y(cat['boundary_sources'])}")

    out.append("pillars:")
    for p in cat["pillars"]:
        out.append(f"  - id: {y(p['id'])}")
        out.append(f"    name: {y(p['name'])}")
        out.append(f"    surface: {y(p['surface'])}")
        out.append(f"    question: {y(p['question'])}")
        out.append(f"    nist_functions: {y(p['nist_functions'])}")
        out.append(f"    frameworks: {y(p['frameworks'])}")

    out.append("requirements:")
    for r in cat["requirements"]:
        out.append(f"  - id: {y(r['id'])}")
        out.append(f"    pillar: {y(r['pillar'])}")
        out.append(f"    statement: {y(r['statement'])}")
        out.append(f"    normative_keyword: {y(r['normative_keyword'])}")
        out.append(f"    from_tier: {y(r['from_tier'])}")
        out.append(f"    applies_to_tiers: {y(r['applies_to_tiers'])}")
        out.append(f"    boundary: {y(r['boundary'])}")
    return "\n".join(out) + "\n"


def main():
    cat = build()
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "aca-requirements.json"), "w", encoding="utf-8") as f:
        json.dump(cat, f, indent=2, ensure_ascii=False)
        f.write("\n")
    with open(os.path.join(OUT_DIR, "aca-requirements.yaml"), "w", encoding="utf-8") as f:
        f.write(emit_yaml(cat))
    print(f"OK, wrote {len(cat['requirements'])} requirements across "
          f"{len(cat['pillars'])} pillars to controls/aca-requirements.{{yaml,json}}")


if __name__ == "__main__":
    main()
