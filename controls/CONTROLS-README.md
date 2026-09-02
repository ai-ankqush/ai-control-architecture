# Machine-Readable Catalogue

The AI Control Architecture requirements, as data. The prose in [`docs/`](../docs/DOCS-README.md) is for humans; these files are for tools, agents, and GRC systems that need to *query* the requirements rather than read them.

```text
aca-requirements.yaml   the catalogue in YAML
aca-requirements.json   the same catalogue in JSON
```

Both are **generated** from [`docs/06-requirements-catalogue.md`](../docs/06-requirements-catalogue.md) by [`scripts/build-catalogue.py`](../scripts/build-catalogue.py). The documents are the source of truth. Do not edit these files by hand; edit the docs and rebuild.

---

## Regenerating and checking

```bash
python3 scripts/build-catalogue.py    # rebuild controls/ from the docs
python3 scripts/check-catalogue.py    # verify docs, catalogue, and generated files agree
```

The check confirms that every pillar document's requirements table matches the consolidated catalogue (same IDs, tiers, boundary sources) and that the generated files are not stale. Run it before publishing a release.

---

## Schema

Top level:

| Field | Meaning |
|-------|---------|
| `schema` | schema identifier and version (`aca-requirements/v0.1`) |
| `version` | catalogue version, tracks `VERSION.md` |
| `license` | `CC-BY-4.0`, the license of the catalogue content |
| `homepage` | canonical home of the architecture |
| `source_of_truth` | the document these files are generated from |
| `tiers` | the five risk tiers (T1 low-risk/public-data, T2 internal productivity with enterprise data or vendor AI, T3 decision-supporting, T4 action-capable, T5 high-impact autonomous or regulated) |
| `boundary_sources` | the boundary-source ladder (Declared, Evidenced, Verified, Enforced) |
| `pillars` | the ten control pillars and their metadata |
| `requirements` | the flat list of normative requirements |

Each `pillars` entry:

| Field | Meaning |
|-------|---------|
| `id` | two-digit pillar number (`07`..`16`) |
| `name` | pillar name |
| `surface` | which of See / Decide / Do it governs |
| `question` | the control question the pillar answers |
| `nist_functions` | NIST AI RMF functions it aligns with (Govern, Map, Measure, Manage) |
| `frameworks` | external frameworks it crosswalks to (pillar-level in this version) |

Each `requirements` entry:

| Field | Meaning |
|-------|---------|
| `id` | stable requirement identifier, `ACA-<pillar>-<n>` |
| `pillar` | the pillar it belongs to |
| `statement` | the normative requirement text |
| `normative_keyword` | `SHALL`, `SHOULD`, or `MAY` (RFC 2119 sense) |
| `from_tier` | the lowest tier at which it applies |
| `applies_to_tiers` | every tier it applies to (from `from_tier` upward) |
| `boundary` | the minimum boundary source expected |

---

## Notes on this version

Framework crosswalks are **pillar-level** here. Provision-level detail (specific articles, functions, and controls) lives in [`mappings/`](../mappings/MAPPINGS-README.md). A future version is expected to publish the catalogue in [OSCAL](https://pages.nist.gov/OSCAL/) so it can be ingested directly by compliance tooling, and to power an MCP server that lets an agent query the requirements at assessment time.

---

*Version 0.1.0 · Licensed under [CC BY 4.0](../LICENSE.md) · Stewarded by Neo Control · neocontrol.ai*
