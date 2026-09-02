# Pillar 13: Human Accountability Model

**Control question:** *Who is accountable?*
**Surface:** spans all three, See, Decide, Do.

---

## Purpose

This pillar ensures that a **named human owns every consequential outcome** of an AI use case. AI can inform, draft, recommend, and act, but it cannot be accountable. It cannot accept risk, answer to a regulator, or be held responsible when something goes wrong. This pillar assigns and records the humans who can: the owner of the use case, the approver of consequential decisions, the acceptor of risk, and the owner of recovery.

---

## Why it matters

Accountability is the control that cannot be automated, and the one most easily lost. As AI produces more of the work, the human role thins to a signature, and then to nothing, as the output flows straight through. When a failure happens, the organization discovers there is no one who owned the decision, no one who accepted the risk, no one responsible for recovery. "The AI did it" is not an answer a board, a regulator, or a court accepts. This pillar exists to make sure that answer never has to be given, that for anything consequential, a person chose, and can say why.

---

## Control objectives

- Assign a **named accountable human** to each consequential outcome, decision, approval, and exception.
- **Record** risk acceptance for a use case, attributably.
- Assign **recovery ownership** before an action-capable use case goes live.

---

## Requirements

From the [Requirements Catalogue](06-requirements-catalogue.md):

| ID | Requirement | From | Boundary |
|----|-------------|------|----------|
| ACA-13-01 | A named human owns each consequential outcome, decision, approval, and exception. | T1 | Declared |
| ACA-13-02 | Risk acceptance for a use case is recorded and attributable. | T3 | Evidenced |
| ACA-13-03 | Recovery ownership is assigned before go-live for action-capable use cases. | T4 | Declared |

---

## Key controls

- **Use-case ownership**: every AI use case has a single accountable owner from intake ([pillar 07](07-pillar-ai-inventory-and-classification.md)), through changes, to retirement.
- **Decision accountability**: the human who confirms or corrects a consequential AI-influenced decision is the accountable party for it ([pillar 11](11-pillar-output-and-decision-control.md)); that act is recorded.
- **Risk acceptance**: where a use case runs with a known, accepted residual risk (or an exception to a control), a named human of appropriate authority records that acceptance.
- **Exception ownership**: deviations from required controls are owned, time-bound, and reviewed, not permanent silent gaps.
- **Recovery ownership**: before an action-capable use case goes live, someone owns "if this fails, I make it right" ([pillar 16](16-pillar-containment-and-recovery.md)).
- **Judgement, not delegation**: the architecture's stance ([Core Thesis](03-core-thesis.md)): you can use AI to inform a judgement, but you cannot outsource the judgement itself.

---

## Tier guidance

| | T1 | T2 | T3 | T4 | T5 |
|---|----|----|----|----|----|
| Named use-case owner | Required | Required | Required | Required | Required |
| Decision accountability recorded | - | - | Required | Required | Required |
| Risk acceptance recorded | - | Recommended | Required | Required | Required |
| Recovery owner assigned | - | - | - | Required (before go-live) | Required (before go-live) |

---

## Evidence

The [AI Human Accountability template](../templates/ai-human-accountability-template.md) and [AI Exception Record template](../templates/ai-exception-record-template.md) capture the owners, the risk acceptances, and the exceptions. Boundary source is *Declared* when owners are named, and *Evidenced* when risk acceptances and exceptions are recorded with authority and date.

---

## Standards crosswalk

Maps to NIST AI RMF **Govern**, ISO/IEC 42001 (roles, responsibilities, and human oversight), EU AI Act (human oversight and provider/deployer obligations), and SR 11-7 (model risk ownership and governance). See [`mappings/`](../mappings/MAPPINGS-README.md).

---

## Failure modes

- A consequential decision with no accountable human, "the AI decided."
- Residual risk running with no one who accepted it.
- A control exception that quietly became permanent, owned by no one.
- A live high-impact use case with no assigned recovery owner.

---

**Next:** [14 · AI Assurance & Testing](14-pillar-assurance-and-testing.md)

*Version 0.1.0 · Licensed under the terms in [LICENSE.md](../LICENSE.md).*
