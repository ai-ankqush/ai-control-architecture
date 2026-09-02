# ACA Schemas

Machine-readable contracts of the AI Control Architecture. Part of the specification; CC BY 4.0.

| File | What it is |
|------|------------|
| `aca-evidence.schema.json` | JSON Schema (draft-07) for the **ACA Evidence Object** — the portable representation of proof. Connectors, test tools, monitoring products and auditors exchange evidence in this shape without a translation layer. |
| `aca-conformance-profiles.json` | Minimum evidence expectations **per risk tier**, so "enough proof" is objective. The required boundary-source strength graduates with the tier (Declared → Evidenced → Verified → Enforced). |

The control catalogue itself is in [`../controls/aca-requirements.json`](../controls/aca-requirements.json).

Evidence portability is the interoperability layer: standardising *what* controls exist (the catalogue) and *how proof is represented* (this schema) is what lets control evidence travel across tools, auditors and time.
