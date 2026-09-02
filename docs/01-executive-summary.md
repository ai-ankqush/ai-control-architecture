# Executive Summary

> AI Control Architecture, a vendor-neutral model for governing, securing, assuring, and containing enterprise AI.

---

## The one-sentence thesis

The next major AI failure in the enterprise will probably not come from a model becoming evil.

It will come from organizations giving **probabilistic systems deterministic authority**, access to data, influence over decisions, and the ability to take actions, **without a control architecture.**

---

## The situation

AI is being adopted faster than enterprise control can absorb it. Copilots are enabled, AI features appear inside SaaS platforms, RAG systems are wired into corporate knowledge, internal LLM applications are built, and agents are beginning to call tools, trigger workflows, update records, and act across systems.

Most of this is happening before organizations can answer the basic control questions:

```text
What AI exists?
What can it see?
What can it decide?
What can it do?
Who is accountable?
What evidence exists?
How is failure contained?
```

An AI policy does not answer these. A policy can say "use AI responsibly." It cannot, by itself, define what data an AI may retrieve, what identity it uses, what decisions it may influence, what tools it may call, what approvals are required, what evidence is retained, and how it is stopped when it fails.

That gap, between policy language and operating control, is what this architecture closes.

---

## What AI Control Architecture is

AI Control Architecture is the discipline of defining how AI is **inventoried, owned, risk-tiered, access-controlled, data-bounded, input-controlled, output-validated, action-limited, human-accountable, tested, monitored, evidenced, contained, and recovered.**

It does not replace AI governance, security, privacy, legal, compliance, risk, audit, data governance, or enterprise architecture. It **connects** them, and turns them into controls that can be applied, tested, and evidenced against real systems.

It is deliberately **vendor-neutral** and **brownfield-compatible**: it assumes you already have identity systems, data platforms, SaaS, security tooling, GRC processes, and vendor contracts, and it works across whatever AI you run, copilots, internal LLM apps, RAG assistants, embedded vendor features, agent frameworks, model APIs, developer tools, or workflow automation.

---

## The six control questions

The architecture is organized around six practical questions. Everything else in this architecture exists to help an enterprise answer them for a given AI use case:

```text
1. What AI exists? → inventory, ownership, classification
2. What can it see? → data boundaries, retrieval scope, access
3. What can it decide? → output validation, decision influence
4. What can it do? → tools, actions, workflows, agents
5. Who is accountable? → human ownership of outcomes
6. How is failure evidenced → monitoring, logging, containment,
 and contained? recovery
```

---

## The ten control pillars

The questions resolve into ten control pillars, each with its own document, requirements, and template:

| # | Pillar | What it controls |
|---|--------|------------------|
| [07](07-pillar-ai-inventory-and-classification.md) | AI Inventory & Classification | See the AI; own it; tier its risk |
| [08](08-pillar-ai-identity-and-access-control.md) | Identity & Access Control | Give AI a bounded identity, not a human's |
| [09](09-pillar-data-boundary-control.md) | Data Boundary Control | Constrain what AI can retrieve and expose |
| [10](10-pillar-input-control.md) | Input Control | Manage injection, manipulation, and untrusted input |
| [11](11-pillar-output-and-decision-control.md) | Output & Decision Control | Stop output silently becoming a decision |
| [12](12-pillar-tool-and-action-control.md) | Tool & Action Control | Bound what AI can *do*, the actor problem |
| [13](13-pillar-human-accountability.md) | Human Accountability | Assign a human owner to every consequential outcome |
| [14](14-pillar-assurance-and-testing.md) | Assurance & Testing | Prove the controls actually hold |
| [15](15-pillar-monitoring-and-evidence.md) | Monitoring & Evidence | Observe, log, and reconstruct what AI did |
| [16](16-pillar-containment-and-recovery.md) | Containment & Recovery | Stop it, contain it, and recover when it fails |

Controls are graduated by **risk tier**, so a low-impact copilot and an action-capable agent do not carry the same burden. The first seven pillars bound what an AI *is and can do*; the last three make that boundedness **provable, observable, and reversible.**

---

## How it aligns to existing frameworks

AI Control Architecture is not a rival to the recognized frameworks, it is the **common control language beneath them.** Every control carries a conceptual crosswalk to the standards enterprises are already held to, so one assessment can serve many obligations:

NIST AI RMF · ISO/IEC 42001 · EU AI Act · SR 11-7 · NYDFS Part 500 · OWASP LLM & Agentic Top 10 · US state AI laws.

The crosswalks live in [`mappings/`](../mappings/MAPPINGS-README.md). They are conceptual, not legal opinions.

---

## What is in this repository

- **The architecture**: this executive summary, the [introduction](02-introduction.md), the [core thesis](03-core-thesis.md), the [architecture principles](04-architecture-principles.md), the [reference architecture](05-reference-architecture.md), and the [requirements catalogue](06-requirements-catalogue.md).
- **The pillars**: documents 07–13 above.
- **Operating the model**: implementation checklists, maturity model, control patterns, failure scenarios, adoption playbook, governance/operating model, metrics, assurance & audit, and a triage-to-minimum-controls guide ([docs 14–22](DOCS-README.md)).
- **Templates**: reusable intake, risk-tiering, control-assessment, evidence, assurance, incident, and per-pillar templates ([`templates/`](../templates/TEMPLATES-README.md)).
- **Mappings**: the standards crosswalks ([`mappings/`](../mappings/MAPPINGS-README.md)).
- **Examples**: worked use cases ([`examples/`](../examples/EXAMPLES-README.md)).
- A **[quickstart](../QUICKSTART.md)** that walks a single AI use case end to end.

---

## Who it is for

Security architects, AI governance and risk teams, privacy and compliance functions, internal audit, enterprise architects, and the engineers actually building and deploying AI, anyone who has to answer "is this AI under control?" and prove it.

---

## What it is, and is not

It **is** a practical reference model, a set of reusable requirements, templates, examples, and a way to turn AI risk into operating control.

It is **not** an ethics statement, a model benchmark, a legal opinion, a product comparison, or a claim that AI should not be adopted. It exists to help organizations adopt AI *faster* without losing control.

---

## The outcome it enables

An organization operating this architecture can say, for any AI it runs:

```text
We know it exists and who owns it.
We know its risk tier.
We know what data it can reach.
We know what decisions it can influence.
We know what tools and actions it can use.
We know which controls apply and whether they hold.
We have the evidence.
We know how to test it, stop it, and recover.
```

That is the purpose of AI Control Architecture: to let enterprises move fast on AI while keeping, and proving, control.

---

**Next:** [02 · Introduction](02-introduction.md) · [03, Core Thesis](03-core-thesis.md) · [Quickstart](../QUICKSTART.md)

*Version 0.1.0 · Licensed under the terms in [LICENSE.md](../LICENSE.md).*
