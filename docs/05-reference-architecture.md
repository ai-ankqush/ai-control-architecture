# Reference Architecture

The [thesis](03-core-thesis.md) says AI's authority must be made bounded, provable, and reversible. This document shows *how the ten pillars compose* to do that, where each control attaches across the life of an AI use case, and how they fit an existing enterprise estate.

---

## The organizing model

The ten pillars divide into two groups with different jobs:

- **Seven pillars bound what the AI is and can do**: across the three surfaces of authority (See, Decide, Do), plus the identity it acts under, the risk tier it sits in, and the human who owns it.
- **Three pillars make that boundedness real**: Assurance proves the controls hold, Monitoring makes behavior observable and reconstructable, and Containment makes it stoppable and reversible.

Accountability spans everything: a named human owns the use case and its outcomes end to end.

```text
 ┌───────────────────────────────────────────────┐
 │ 07 INVENTORY & CLASSIFICATION (see it, tier it)
 └───────────────────────────────────────────────┘
 SEE DECIDE DO
 ┌────────────┐ ┌──────────────┐ ┌──────────────────┐
 │08 Identity │ │11 Output & │ │12 Tool & Action │
 │ & Access │ │ Decision │ │ Control │
 │09 Data │──────▶ │ Control │──────▶ │ │
 │ Boundary │ │ │ │ │
 │10 Input │ │ │ │ │
 │ Control │ │ │ │ │
 └────────────┘ └──────────────┘ └──────────────────┘
 │ │ │
 └──────────── 13 HUMAN ACCOUNTABILITY ────────┘
 │
 ┌──────────────────────────┴──────────────────────────┐
 │ 14 ASSURANCE 15 MONITORING & 16 CONTAINMENT & │
 │ & TESTING EVIDENCE RECOVERY │
 │ (prove it) (observe it) (stop / undo it) │
 └─────────────────────────────────────────────────────┘
```

---

## The control lifecycle of a use case

Controls attach at specific points as an AI use case moves from idea to running system. The pillars map onto that flow:

```text
INTAKE ─▶ CLASSIFY ─▶ ACCESS ─▶ INPUT ─▶ INFERENCE ─▶ OUTPUT ─▶ ACTION ─▶ RUN
 │ │ │ │ │ │ │ │
 07 07 08,09 10 (model) 11 12 14,15,16
inventory risk identity input output tool assure,
& owner tier & data & decision & act monitor,
 boundary control control control contain
```

- **Intake & Classify (07):** the use case is registered, owned, and risk-tiered before controls are chosen. Nothing is governed that isn't first *seen*.
- **Access (08, 09):** the AI is given a bounded identity and an explicit data boundary, what it may retrieve and expose.
- **Input (10):** prompts and untrusted input are controlled for injection and manipulation.
- **Output & Decision (11):** output is validated and prevented from silently becoming a decision without accountability.
- **Action (12):** tools, actions, and workflows are bounded, the point at which AI becomes an actor.
- **Accountability (13):** a named human owns the outcomes throughout.
- **Assure / Monitor / Contain (14, 15, 16):** controls are tested, behavior is logged and reconstructable, and the capability can be stopped and recovered.

---

## Control points, where controls attach

Every pillar resolves to one or more **control points**: a place in the running system where a boundary is declared, evidenced, verified, or enforced.

```text
Control point Pillar Boundary strength it can reach
────────────────────────────────────────────────────────────
AI inventory record 07 Declared → Evidenced
Identity / auth 08 Verified → Enforced
Data retrieval scope 09 Verified → Enforced
Input handling 10 Evidenced → Enforced
Output validation 11 Evidenced → Enforced
Action / tool broker 12 Verified → Enforced
Accountability record 13 Declared → Evidenced
Assurance test 14 Verified
Log / evidence store 15 Verified
Kill switch / recovery 16 Enforced
```

A use case's real control strength is the **weakest boundary on a surface that matters**, an enforced action broker means little if the data boundary is only declared. The [boundary-source ladder](03-core-thesis.md) is applied per control point, not once for the whole use case.

---

## Risk tier is the modulator

The reference architecture is not "apply all controls everywhere." Tiering (pillar 07) sets how far each control point must go. A lower-tier, read-only copilot may need its data boundary only *evidenced*; a higher-tier, action-capable agent needs identity, data, action, monitoring, and containment all *verified or enforced*, with human approval gates on high-impact actions. Tier first; then apply the boundary strength the tier requires.

---

## Fitting a brownfield estate

The architecture does not introduce a parallel stack; each pillar plugs into systems the enterprise already runs:

```text
Pillar Plugs into
──────────────────────────────────────────────────────────
08 Identity & Access IdP / IAM, secrets, service identity
09 Data Boundary DLP, data classification, RAG scoping
10 Input Control gateway / prompt firewall, WAF
11 Output & Decision review workflow, approval systems
12 Tool & Action API gateway, action broker, MCP proxy
13 Accountability GRC, ownership records
14 Assurance test frameworks, red-team tooling
15 Monitoring & Evidence SIEM, logging, audit store
16 Containment & Recovery incident response, feature flags, backups
```

This is the point of vendor-neutrality: the architecture defines *what boundary must hold at each control point*, and the enterprise satisfies it with the tools it already owns.

---

## From architecture to requirements

Each pillar (07–16) specifies the controls for its surface. The [Requirements Catalogue](06-requirements-catalogue.md) turns those into numbered, testable requirements with tier applicability and standards crosswalks; the [templates](../templates/TEMPLATES-README.md) capture the evidence per use case; the [mappings](../mappings/MAPPINGS-README.md) tie each requirement to the frameworks the enterprise is held to.

---

**Next:** [06 · Requirements Catalogue](06-requirements-catalogue.md)

*Version 0.1.0 · Licensed under the terms in [LICENSE.md](../LICENSE.md).*
