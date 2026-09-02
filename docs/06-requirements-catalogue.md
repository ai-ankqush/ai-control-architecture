# Requirements Catalogue

This is the normative backbone of the architecture: the numbered, testable control requirements that the pillars implement, the templates capture evidence for, and the crosswalks map to external standards. Where the earlier documents explain *what control means and why*, this document states *what is required.*

---

## How to read a requirement

Every requirement has a stable ID and a normative statement:

```text
ACA-<pillar>-<n> e.g. ACA-09-02
```

- **ID**: `ACA` + two-digit pillar (07–16) + sequence. IDs are stable; requirements are never renumbered, only deprecated.
- **Statement**: written with **SHALL** (required), **SHOULD** (expected unless justified), **MAY** (permitted), in the RFC 2119 sense.
- **From tier**: the lowest risk tier at which the requirement applies (see below). It also applies to every higher tier.
- **Boundary**: the minimum [boundary source](03-core-thesis.md) expected: *Declared, Evidenced, Verified, Enforced.*
- **Crosswalk**: the external provisions it helps satisfy (see [`mappings/`](../mappings/MAPPINGS-README.md)).

Each pillar document (07–16) is the authoritative source for its own requirements and their guidance; this catalogue is the consolidated, citable index.

---

## Risk tiers

Requirements are graduated by tier. Tier is set in [pillar 07](07-pillar-ai-inventory-and-classification.md) from a use case's consequence (See/Decide/Do) and autonomy.

```text
T1 Low-risk productivity or public-data use     public or non-sensitive data, no decision impact, no tool or action capability
T2 Internal productivity with enterprise data   internal enterprise data or vendor AI for productivity, no decision influence or actions
   or vendor AI
T3 Decision-supporting AI                        influences human decisions, judgments, or records
T4 Action-capable AI                             can call tools, trigger workflows, or perform actions in enterprise systems
T5 High-impact autonomous or regulated AI        affects employment, credit, legal, safety, healthcare, regulated, or hard-to-reverse outcomes
```

Tier is set from the highest material risk driver, not an average. A requirement marked **From T3** applies to T3, T4, and T5, not T1 or T2.

---

## Tiers and pillars: depth, not on/off

Tiers do not map one-to-one to pillars. All ten pillars remain relevant at every tier; what rises with the tier is the *depth* of control each pillar requires. The rule is simply: control depth scales with the risk tier, and the highest material risk driver sets the tier.

A pillar does not "switch on" at a threshold. Containment, for example, applies even at Tier 2, where it may mean disabling a vendor feature; at Tier 4 it means revoking an agent identity, cancelling pending actions, and rolling back changes. Same pillar, very different depth.

Which pillars become *decision-critical* at each tier:

| Tier | Pillars that dominate | What changes |
|------|-----------------------|--------------|
| T1 | 07 Inventory, 09 Data, 11 Output, 13 Accountability | Keep the use case visible, restrict it to low-risk or public data, and keep a human owner over the final output. |
| T2 | T1 + 08 Identity, 09 Data, 15 Monitoring & Evidence | Enterprise or vendor data enters, so access, retention and reuse, vendor configuration, and evidence matter more. |
| T3 | T2 + 11 Output & Decision, 13 Accountability, 14 Assurance, 15 Evidence | AI now influences judgment: meaningful human review, decision ownership, validation, escalation, and proof of what informed the recommendation. |
| T4 | T3 + 08 Identity, 12 Tool & Action, 15 Evidence, 16 Containment | AI can act: delegated authority, tool restrictions, approval gates, action logs, rollback, and a tested kill switch. |
| T5 | All ten, at enhanced depth | High-impact, regulated, autonomous, or hard-to-reverse: full review, stronger assurance, evidence, accountability, and risk acceptance. |

Read as a progression: Tiers 1–2 control what AI can **See** (inventory, identity, data, inputs); Tier 3 controls what it can **Decide** or influence (output, accountability, assurance, evidence); Tier 4 controls what it can **Do** (identity, action authority, logging, rollback, containment); Tier 5 **proves the whole chain** — from access through decision and action to evidence and recovery — can be defended and reconstructed.

So the `From` tier on each requirement below marks where that *specific* control becomes a distinct, required provision, not where its pillar begins to matter. Lower tiers still exercise the same pillars at lighter depth, and a "-" in a pillar's tier-guidance table means "no distinct required control at this tier," not "pillar absent."

---

## The catalogue

Representative requirements per pillar. This set is normative and versioned; it grows as the pillar documents are completed, and full guidance for each lives in its pillar.

### 07, AI Inventory & Classification

| ID | Requirement | From | Boundary |
|----|-------------|------|----------|
| ACA-07-01 | The organization **SHALL** maintain an inventory of all AI use cases, including embedded and vendor AI. | T1 | Evidenced |
| ACA-07-02 | Each use case **SHALL** have a named accountable owner recorded at intake. | T1 | Declared |
| ACA-07-03 | Each use case **SHALL** be assigned a risk tier before controls are selected. | T1 | Evidenced |
| ACA-07-04 | The inventory **SHALL** be reconciled on a defined cadence and on material change. | T2 | Evidenced |

### 08, AI Identity & Access Control

| ID | Requirement | From | Boundary |
|----|-------------|------|----------|
| ACA-08-01 | AI **SHALL** act under a distinct non-human identity, not a user's standing credentials. | T4 | Verified |
| ACA-08-02 | AI identities **SHALL** be granted least-privilege access scoped to the use case. | T4 | Verified |
| ACA-08-03 | AI access **SHALL** be revocable promptly and completely. | T4 | Verified |
| ACA-08-04 | Consequential actions **SHALL** be attributable to the identity and grant that authorized them. | T4 | Enforced |

### 09, Data Boundary Control

| ID | Requirement | From | Boundary |
|----|-------------|------|----------|
| ACA-09-01 | The data sources an AI may access **SHALL** be explicitly defined and approved. | T2 | Evidenced |
| ACA-09-02 | Retrieval **SHALL** be scoped so AI cannot surface data the requester is not entitled to. | T2 | Verified |
| ACA-09-03 | Sensitive data classes **SHALL** be excluded or masked unless explicitly permitted. | T2 | Verified |
| ACA-09-04 | Third-party processing and retention of data **SHALL** be known and bounded. | T2 | Evidenced |

### 10, Prompt & Input Control

| ID | Requirement | From | Boundary |
|----|-------------|------|----------|
| ACA-10-01 | Untrusted input, including retrieved content, **SHALL** be treated as potentially adversarial. | T3 | Evidenced |
| ACA-10-02 | Prompt-injection and manipulation **SHALL** be mitigated proportionate to tier. | T3 | Verified |
| ACA-10-03 | System instructions **SHALL** be protected from override by user or retrieved content. | T4 | Enforced |

### 11, Output & Decision Control

| ID | Requirement | From | Boundary |
|----|-------------|------|----------|
| ACA-11-01 | Output that influences a consequential decision **SHALL** be identified as such. | T3 | Evidenced |
| ACA-11-02 | High-impact decisions **SHALL** require human validation before effect. | T3 | Enforced |
| ACA-11-03 | AI-influenced decisions **SHALL** be recorded with the output and rationale. | T3 | Evidenced |

### 12, Tool & Action Control

| ID | Requirement | From | Boundary |
|----|-------------|------|----------|
| ACA-12-01 | The tools and actions an AI may invoke **SHALL** be explicitly allow-listed. | T4 | Verified |
| ACA-12-02 | High-impact actions **SHALL** require approval or step-up before execution. | T4 | Enforced |
| ACA-12-03 | No action class **SHALL** be enforced live without a defined containment or compensation path. | T4 | Enforced |
| ACA-12-04 | Every action **SHALL** be logged with the requesting identity, inputs, and outcome. | T4 | Verified |

### 13, Human Accountability Model

| ID | Requirement | From | Boundary |
|----|-------------|------|----------|
| ACA-13-01 | A named human **SHALL** own each consequential outcome, decision, approval, and exception. | T1 | Declared |
| ACA-13-02 | Risk acceptance for a use case **SHALL** be recorded and attributable. | T3 | Evidenced |
| ACA-13-03 | Recovery ownership **SHALL** be assigned before go-live for action-capable use cases. | T4 | Declared |

### 14, AI Assurance & Testing

| ID | Requirement | From | Boundary |
|----|-------------|------|----------|
| ACA-14-01 | Controls **SHALL** be tested before go-live, proportionate to tier. | T3 | Verified |
| ACA-14-02 | High-impact and autonomous use cases **SHALL** undergo adversarial testing of input, output, and action controls. | T5 | Verified |
| ACA-14-03 | Test results **SHALL** be retained as evidence and re-run on material change. | T3 | Verified |

### 15, Monitoring, Logging & Evidence

| ID | Requirement | From | Boundary |
|----|-------------|------|----------|
| ACA-15-01 | Activity **SHALL** be logged sufficiently to reconstruct what AI saw, produced, decided, and did. | T2 | Verified |
| ACA-15-02 | Logs **SHALL** be tamper-evident and retained per policy. | T3 | Verified |
| ACA-15-03 | Anomalous or policy-violating behavior **SHALL** be detectable and alertable. | T4 | Verified |

### 16, Incident Containment & Recovery

| ID | Requirement | From | Boundary |
|----|-------------|------|----------|
| ACA-16-01 | Each tiered use case **SHALL** have a tested means to disable the AI capability quickly. | T4 | Enforced |
| ACA-16-02 | High-impact actions **SHALL** have a containment or compensation/rollback path. | T4 | Enforced |
| ACA-16-03 | Recovery from an AI incident **SHALL** be owned, documented, and exercised. | T4 | Evidenced |

---

## Using the catalogue

- **Assessing a use case:** tier it (07), then apply the requirements at or below that tier, recording the boundary source achieved for each.
- **Proving control:** each requirement's boundary column is the bar; a requirement met only at *Declared* when *Verified* is expected is a finding.
- **Mapping obligations:** the [crosswalks](../mappings/MAPPINGS-README.md) tie these IDs to NIST AI RMF, ISO/IEC 42001, EU AI Act, SR 11-7, NYDFS, and OWASP, so one pass serves many.

---

## Machine-readable form

This catalogue is also published as data, generated from this document, in [`controls/`](../controls/CONTROLS-README.md):

```text
controls/aca-requirements.yaml
controls/aca-requirements.json
```

Assessment tooling, agents, and GRC systems can consume that single source rather than re-transcribing the requirements. This document remains authoritative; the data files are built from it and checked against every pillar's table. A future version is expected to add an [OSCAL](https://pages.nist.gov/OSCAL/) profile.

---

**Next:** [07 · AI Inventory & Classification](07-pillar-ai-inventory-and-classification.md)

*Version 0.1.0 · Licensed under the terms in [LICENSE.md](../LICENSE.md).*
