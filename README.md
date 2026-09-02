# AI Control Architecture

**An open-source, vendor-agnostic model for governing, securing, assuring, and containing enterprise AI.**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-blue.svg)](LICENSE.md)
[![Website](https://img.shields.io/badge/site-aicontrolarchitecture.org-2b6bff.svg)](https://aicontrolarchitecture.org)

AI Control Architecture (ACA) gives an organisation a shared way to answer one question about any AI it runs, *"is this under control?"*, and to prove it. It is deliberately vendor-agnostic and brownfield-compatible: it assumes you already have identity systems, data platforms, SaaS, security tooling, and GRC processes, and it works across whatever AI you run, from copilots and RAG assistants to embedded vendor features and action-capable agents.

> **The thesis, in one line:** the next major AI failure in the enterprise will not come from a model becoming evil. It will come from giving a **probabilistic system deterministic authority**, over data, decisions, or actions, **without a control architecture.**

## Start here

- **New to this?** Read [Why This Exists](WHY_THIS_EXISTS.md) and the [Executive Summary](docs/01-executive-summary.md).
- **Want to try it?** Follow the [Quickstart](QUICKSTART.md), which walks a single AI use case end to end.
- **Prefer a rendered site?** Everything is at **[aicontrolarchitecture.org](https://aicontrolarchitecture.org)**, including a [Start Here](https://aicontrolarchitecture.org/start-here) hub and downloadable [Resources](https://aicontrolarchitecture.org/resources).

## The six control questions

Everything in the architecture exists to help you answer these for a given AI use case:

1. What AI exists?
2. What can it see?
3. What can it decide?
4. What can it do?
5. Who is accountable?
6. How is failure evidenced and contained?

An AI touches the enterprise in exactly three ways, what it can **See**, **Decide**, and **Do**. Risk rises as a use case moves See → Decide → Do, and as human oversight falls away.

## The ten control pillars

| # | Pillar | What it controls |
|---|--------|------------------|
| [07](docs/07-pillar-ai-inventory-and-classification.md) | AI Inventory & Classification | See the AI, own it, tier its risk |
| [08](docs/08-pillar-ai-identity-and-access-control.md) | Identity & Access Control | Give AI a bounded identity, not a human's |
| [09](docs/09-pillar-data-boundary-control.md) | Data Boundary Control | Constrain what AI can retrieve and expose |
| [10](docs/10-pillar-input-control.md) | Prompt & Input Control | Manage injection, manipulation, untrusted input |
| [11](docs/11-pillar-output-and-decision-control.md) | Output & Decision Control | Stop output silently becoming a decision |
| [12](docs/12-pillar-tool-and-action-control.md) | Tool & Action Control | Bound what AI can *do*, the actor problem |
| [13](docs/13-pillar-human-accountability.md) | Human Accountability | Assign a human owner to every consequential outcome |
| [14](docs/14-pillar-assurance-and-testing.md) | Assurance & Testing | Prove the controls actually hold |
| [15](docs/15-pillar-monitoring-and-evidence.md) | Monitoring & Evidence | Observe, log, and reconstruct what AI did |
| [16](docs/16-pillar-containment-and-recovery.md) | Containment & Recovery | Stop it, contain it, and recover when it fails |

Pillars 07 to 13 bound what an AI is and can do. Pillars 14 to 16 make that boundedness provable, observable, and reversible.

## Control depth scales with risk

Controls are graduated across five risk tiers, so a low-risk copilot and an action-capable agent do not carry the same burden:

| Tier | Description | Review depth |
|------|-------------|--------------|
| T1 | Low-risk productivity, public data only | Minimal (fast-track) |
| T2 | Enterprise data or vendor AI | Data and vendor review |
| T3 | Influences decisions and records | Decision accountability |
| T4 | Calls tools, triggers workflows | Containment and approval gates |
| T5 | Autonomous, regulated, hard to reverse | Full assurance and evidence |

See [Triage and Minimum Controls](docs/25-triage-and-minimum-controls.md) for the triage questions and the minimum-control baseline per tier.

## Proving a boundary holds

Every control is graded by its **boundary source**, the strength of the basis it rests on:

`Declared → Evidenced → Verified → Enforced`

This keeps the architecture honest: it never lets "we have a policy" masquerade as "the control holds," and it makes the gap between claimed and proven control explicit and auditable.

## Standards and framework crosswalks

ACA is not a rival to the recognised frameworks, it is the common control language beneath them. Every control carries a conceptual crosswalk, so one assessment can serve many obligations. Crosswalks live in [`mappings/`](mappings/MAPPINGS-README.md):

NIST AI RMF · ISO/IEC 42001 · EU AI Act · SR 11-7 · NYDFS Part 500 · OWASP LLM & Agentic Top 10 · US state AI laws.

Crosswalks are conceptual, not legal opinions.

## Repository structure

| Path | Contents |
|------|----------|
| [`docs/`](docs/) | The architecture: executive summary, core thesis, principles, reference architecture, the ten pillars, and operating guidance (maturity, adoption, governance, metrics, assurance, triage). |
| [`controls/`](controls/) | The requirements catalogue as machine-readable data (YAML and JSON), generated from the docs. |
| [`schemas/`](schemas/) | The ACA Evidence Schema and conformance profiles, the interoperability contract for portable proof. |
| [`mappings/`](mappings/) | Crosswalks to external standards and regulations. |
| [`templates/`](templates/) | Reusable intake, risk-tiering, control-assessment, evidence, assurance, and incident templates. |
| [`examples/`](examples/) | Worked use cases (RAG assistant, copilot, agent, vendor AI). |
| [`site/`](site/) | The source for the documentation website. |

## The open ecosystem

The specification is open, and so is a reference implementation you can build on:

- **[neo-community-edition](https://github.com/ai-ankqush/neo-community-edition)** is the open, self-hostable assessment app: classify, risk-tier, control selection, and evidence/verification, with your own model key (AGPL-3.0).
- **[aca-core](https://github.com/ai-ankqush/aca-core)** is the open reference implementation of the assessment engine and extension slots (Apache-2.0).
- **[aca-tools](https://github.com/ai-ankqush/aca-tools)** is an MCP server over the control catalogue, so an agent can query the requirements at assessment time.
- **[aca-registry](https://github.com/ai-ankqush/aca-registry)** is a signed, two-track registry for distributing add-ons.
- **[aca-plugins](https://github.com/ai-ankqush/aca-plugins)** provides first-party reference add-ons, one per extension slot.

## Contributing

ACA is a public, evolving specification. See [CONTRIBUTING](CONTRIBUTING.md) for how to propose changes, and [ROADMAP](ROADMAP.md) for what is planned. Issues and pull requests are welcome, including from other vendors: if ACA becomes portable across the field's tools, it is a standard.

## License, trademark, and stewardship

The specification and documentation are licensed under [Creative Commons Attribution 4.0 (CC BY 4.0)](LICENSE.md). Please see [TRADEMARK](TRADEMARK.md) for use of the name and conformance marks.

AI Control Architecture is stewarded by [Neo Control](https://neocontrol.ai), which offers the reference implementation. You never need Neo, or any vendor, to adopt it.
