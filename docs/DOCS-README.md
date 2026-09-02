# AI Control Architecture

An open-source, vendor-agnostic model for governing, securing, assuring, and containing enterprise AI.

> **The thesis, in one line:** the next major AI failure in the enterprise will not come from a model becoming evil, it will come from giving a **probabilistic system deterministic authority** over data, decisions, or actions **without a control architecture.** This is how you build that architecture.

The architecture is organized around six control questions:

```text
1. What AI exists?
2. What can it see?
3. What can it decide?
4. What can it do?
5. Who is accountable?
6. How is failure evidenced and contained?
```

These resolve into **ten control pillars** and a supporting operating model.

---

## How the documentation is structured

```text
01–06 Foundation what control means and why
07–16 Pillars the ten control domains, in depth
17–25 Operating how to implement, assess, run, and audit it
26 Glossary shared definitions
```

### Foundation (01–06)

| # | Document |
|---|----------|
| 01 | [Executive Summary](01-executive-summary.md) |
| 02 | [Introduction](02-introduction.md) |
| 03 | [Core Thesis](03-core-thesis.md) |
| 04 | [Architecture Principles](04-architecture-principles.md) |
| 05 | [Reference Architecture](05-reference-architecture.md) |
| 06 | [Requirements Catalogue](06-requirements-catalogue.md) |

### The ten pillars (07–16)

| # | Pillar | Question |
|---|--------|----------|
| 07 | [AI Inventory & Classification](07-pillar-ai-inventory-and-classification.md) | What AI exists? |
| 08 | [AI Identity & Access Control](08-pillar-ai-identity-and-access-control.md) | Under what identity / access? |
| 09 | [Data Boundary Control](09-pillar-data-boundary-control.md) | What can it see? |
| 10 | [Prompt & Input Control](10-pillar-input-control.md) | What shapes it? |
| 11 | [Output & Decision Control](11-pillar-output-and-decision-control.md) | What can it decide? |
| 12 | [Tool & Action Control](12-pillar-tool-and-action-control.md) | What can it do? |
| 13 | [Human Accountability Model](13-pillar-human-accountability.md) | Who is accountable? |
| 14 | [AI Assurance & Testing](14-pillar-assurance-and-testing.md) | Do the controls hold? |
| 15 | [Monitoring, Logging & Evidence](15-pillar-monitoring-and-evidence.md) | Can we reconstruct it? |
| 16 | [Incident Containment & Recovery](16-pillar-containment-and-recovery.md) | Can we stop and recover? |

### Operating (17–25)

| # | Document |
|---|----------|
| 17 | [Implementation Checklists](17-implementation-checklists.md) |
| 18 | [Control Maturity Model](18-control-maturity-model.md) |
| 19 | [Common AI Control Patterns](19-common-ai-control-patterns.md) |
| 20 | [Common Failure Scenarios](20-common-failure-scenarios.md) |
| 21 | [Adoption Playbook](21-adoption-playbook.md) |
| 22 | [Governance & Operating Model](22-governance-and-operating-model.md) |
| 23 | [Metrics & Reporting](23-metrics-and-reporting.md) |
| 24 | [Assurance & Audit Guide](24-assurance-and-audit-guide.md) |
| 25 | [Triage & Minimum Controls](25-triage-and-minimum-controls.md) |

### Reference

| # | Document |
|---|----------|
| 26 | [Glossary](26-glossary.md) |

---

## Supporting assets (repository root)

- [`templates/`](../templates/TEMPLATES-README.md), reusable intake, risk-tiering, per-pillar control, assurance, evidence, and incident templates.
- [`mappings/`](../mappings/MAPPINGS-README.md), standards crosswalks (NIST AI RMF, ISO/IEC 42001, EU AI Act, SR 11-7, NYDFS Part 500, OWASP LLM & Agentic, US state AI laws).
- [`examples/`](../examples/EXAMPLES-README.md), worked use-case examples.
- [`../QUICKSTART.md`](../QUICKSTART.md), a single AI use case walked from intake to evidence.

---

## Where to start

**New to the architecture** → read the foundation in order:
`01 → 02 → 03 → 04 → 05`, then skim `06`.

**Implementing controls** → start with the [Quickstart](../QUICKSTART.md), then `17` (checklists), `21` (adoption playbook), `22` (governance).

**Assessing maturity** → `18` (maturity model) + `23` (metrics) + the maturity-assessment template.

**Understanding a control domain** → the relevant pillar (07–16).

**Understanding how AI fails** → `20` (failure scenarios).

**Testing or auditing** → `24` (assurance & audit) + the assurance and evidence templates.

**Just need the minimum** → `25` (triage & minimum controls).

---

## Contributing, license, and the name

The AI Control Architecture is open and openly licensed under [CC BY 4.0](../LICENSE.md): use and adapt it freely, including commercially, with attribution. The name and any conformance marks are reserved, see [Trademark & Conformance](../TRADEMARK.md). To propose changes, see [Contributing](../CONTRIBUTING.md).

---

*Version 0.1.0 · Architecture licensed under [CC BY 4.0](../LICENSE.md) · Stewarded by Neo Control · neocontrol.ai*
