# Introduction

This document orients you to the AI Control Architecture: the problem it addresses, what it is and is not, who it is for, and how to read the rest of it. If you want the one-page version, read the [Executive Summary](01-executive-summary.md) first. If you want the argument in full, read the [Core Thesis](03-core-thesis.md) next.

---

## The shift that creates the problem

For most of its history, enterprise AI generated text. You asked; it answered. The risk was bounded because the output was inert, a draft, a summary, a suggestion a human then acted on.

That is no longer the shape of enterprise AI. AI now:

```text
reads enterprise documents, email, chat, tickets, code, and records
retrieves context from corporate knowledge (RAG)
influences customer, employee, financial, and operational decisions
calls APIs, triggers workflows, updates systems, and sends communications
runs as agents that chain these together with limited human oversight
```

The moment an AI can *see* real data, *influence* a real decision, or *take* a real action, it stops being a feature and becomes an **actor inside the enterprise.** Actors need identity, authority limits, boundaries, logging, approval gates, kill switches, and someone accountable for what they do.

Most organizations enabled the feature before they built the controls for the actor. That is the gap.

---

## Why existing controls do not simply cover it

Enterprises already have identity management, data governance, security tooling, and GRC. AI does not fit cleanly into any of them:

- **Identity** was built for humans and service accounts, not for a probabilistic system acting on a user's behalf with the user's access.
- **Data governance** assumes access is granted to *records*; AI accesses data through *retrieval* and *inference*, which can cross boundaries no ACL was written to stop.
- **Application security** assumes deterministic logic; AI behavior is probabilistic and prompt-shaped, so the same input can produce different actions.
- **Change and approval processes** assume a human initiates each action; an agent can initiate thousands.

AI Control Architecture does not replace these disciplines. It **connects** them, extending identity, data, security, and accountability controls to cover a new kind of actor.

---

## Why policy is necessary but not sufficient

An AI policy sets intent: *use AI responsibly, protect data, keep a human in the loop.* Intent matters. But a policy cannot, by itself, define **what data this AI may retrieve, what identity it uses, what decisions it may influence, what tools it may call, what approvals are required, what evidence is retained, and how it is stopped when it fails.**

Those are control questions, and they have to be answered per AI use case, in the real systems, with evidence. Turning policy intent into applied, testable, evidenced control is the entire purpose of this architecture. (For the fuller motivation, see [WHY_THIS_EXISTS](../WHY_THIS_EXISTS.md).)

---

## What this architecture is

AI Control Architecture is a **vendor-neutral, brownfield-compatible reference model** for governing, securing, assuring, and containing enterprise AI. It is organized around six control questions and ten control pillars, and it ships with requirements, templates, standards crosswalks, and worked examples so it can be applied rather than merely read.

It is built to work regardless of where the AI comes from, a copilot, an internal LLM application, a RAG assistant, a SaaS feature, an embedded vendor capability, an agent framework, a model API, a developer tool, or a workflow automation.

---

## Scope

**In scope:** how enterprises inventory AI, tier its risk, control its identity and data access, manage its inputs and outputs, bound its tools and actions, assign human accountability, and assure, monitor, and contain it, across the full lifecycle of an AI use case.

**Out of scope:** model training and alignment research, AI ethics positions, legal opinions, product or vendor comparisons, and safety of frontier model development. This architecture governs how AI is *adopted and operated* inside an organization, not how models are built.

---

## Who it is for

| Reader | Why |
|--------|-----|
| Security architects & engineers | Design and implement the controls |
| AI governance & risk teams | Structure assessments and risk tiering |
| Privacy & compliance | Map controls to obligations |
| Internal audit & assurance | Test controls and gather evidence |
| Enterprise architects | Fit AI control into existing estates |
| Builders deploying AI | Answer "is this under control?" and prove it |

---

## How the architecture is structured

```text
01–06 Foundation , what control means and why (this section)
07–16 Pillars , the ten control domains, in depth
17–25 Operating , how to implement, assess, run, and audit it
26 Glossary , shared definitions
```

- **Foundation (01–06):** [Executive Summary](01-executive-summary.md), this Introduction, [Core Thesis](03-core-thesis.md), [Architecture Principles](04-architecture-principles.md), [Reference Architecture](05-reference-architecture.md), and the [Requirements Catalogue](06-requirements-catalogue.md).
- **Pillars (07–16):** from [AI Inventory & Classification](07-pillar-ai-inventory-and-classification.md) through [Incident Containment & Recovery](16-pillar-containment-and-recovery.md).
- **Operating (17–25) and the full index:** see [DOCS-README](DOCS-README.md).
- **Supporting assets:** [`templates/`](../templates/TEMPLATES-README.md), [`mappings/`](../mappings/MAPPINGS-README.md) (standards crosswalks), and [`examples/`](../examples/EXAMPLES-README.md).

---

## A few terms used throughout

Defined fully in the [Glossary](26-glossary.md); introduced here so the rest reads cleanly:

- **AI use case**: a specific deployment of AI in a business context (this copilot, that agent), and the unit the architecture assesses and controls.
- **Control**: an applied, testable measure that constrains what an AI can see, decide, or do, not a policy statement.
- **Risk tier**: the level of scrutiny a use case attracts, based on its impact and autonomy; controls are graduated by tier.
- **See / Decide / Do**: the three ways an AI touches the enterprise: what it can access, what it can influence, and what it can act on.
- **Boundary source**: how strongly a control is backed: *declared → evidenced → verified → enforced.* A control that is only declared is visibly weaker than one that is enforced.

---

## How to use it

If you are new, continue through the foundation (03 → 05). If you are implementing, jump to the [Quickstart](../QUICKSTART.md), which walks a single AI use case from intake to evidence, and to the operating docs. If you are assessing or auditing, start from the pillars relevant to your use case and the assurance and evidence templates.

---

**Next:** [03 · Core Thesis](03-core-thesis.md)

*Version 0.1.0 · Licensed under the terms in [LICENSE.md](../LICENSE.md).*
