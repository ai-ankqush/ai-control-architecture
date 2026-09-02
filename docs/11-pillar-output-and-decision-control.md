# Pillar 11: Output & Decision Control

**Control question:** *What can the AI decide?*
**Surface:** Decide.

---

## Purpose

This pillar governs the point where AI **output becomes influence over a decision**. It ensures that when an AI's answer shapes a customer, employee, financial, legal, compliance, or operational outcome, that influence is visible, validated where it matters, and recorded with an accountable owner, rather than a suggestion silently hardening into a decision no one consciously made.

---

## Why it matters

The most insidious AI risk is not a wrong answer; it is a **wrong answer that quietly becomes a decision.** An AI drafts a recommendation, a human skims and forwards it, and downstream systems treat it as settled, a loan is priced, a candidate is screened out, a ticket is closed, an alert is dismissed. No one decided to delegate the decision to the AI; it happened by default because the output was fluent and the review was nominal. Automation bias makes it worse: confident, well-formatted output gets less scrutiny, not more. This pillar exists to stop *output* from becoming *decision* without someone accountable choosing to let it.

---

## Control objectives

- **Identify** AI output that influences a consequential decision, as such.
- Require **human validation** of high-impact decisions before they take effect.
- **Record** AI-influenced decisions with the output, rationale, and the accountable human.

---

## Requirements

From the [Requirements Catalogue](06-requirements-catalogue.md):

| ID | Requirement | From | Boundary |
|----|-------------|------|----------|
| ACA-11-01 | Output that influences a consequential decision is identified as such. | T3 | Evidenced |
| ACA-11-02 | High-impact decisions require human validation before effect. | T3 | Enforced |
| ACA-11-03 | AI-influenced decisions are recorded with the output and rationale. | T3 | Evidenced |

---

## Key controls

- **Decision classification**: identify which outputs feed consequential decisions (people, money, rights, safety, security) versus low-stakes assistance; only the former carry the heavy controls.
- **Human-in-the-loop, made real**: for high-impact decisions, require a validation step that is genuine, not a rubber stamp: give the reviewer the AI's rationale, its confidence, its sources, and what it does *not* know, so the human can actually check rather than defer.
- **Confirm-or-correct gates**: the accountable human confirms or corrects the AI's recommendation, and that act is the decision of record, a direct expression of the [judgement principle](03-core-thesis.md): AI proposes; a human decides.
- **Decision record**: capture the output, the human action, the rationale, and the owner, so an AI-influenced decision can be reconstructed and defended.
- **Output validation**: where output feeds automated steps, validate structure, grounding, and policy compliance before it propagates.

---

## Tier guidance

| | T1 | T2 | T3 | T4 | T5 |
|---|----|----|----|----|----|
| Decision influence identified | - | - | Required | Required | Required |
| Human validation of high-impact | - | - | Required (enforced) | Required (enforced) | Required (enforced) |
| Decision record kept | - | - | Required | Required | Required |
| Output grounding/validation | - | Recommended | Required | Required | Required |

---

## Evidence

The [AI Output & Decision Control template](../templates/ai-output-and-decision-control-template.md) captures which decisions the use case influences, the validation gates, and the decision-record design. Boundary source reaches *Enforced* when a control point actually prevents a high-impact decision from taking effect without the required human validation.

---

## Standards crosswalk

Maps to NIST AI RMF **Measure/Manage**, ISO/IEC 42001 (human oversight), EU AI Act (human oversight, Art. 14; and its rules on automated decisions), SR 11-7 (model outputs used in decisions), and sectoral fairness/adverse-action rules. See [`mappings/`](../mappings/MAPPINGS-README.md).

---

## Failure modes

- An AI recommendation that becomes a decision with no accountable human.
- A "human in the loop" who rubber-stamps because they're given no basis to check.
- Automated propagation of unvalidated output into consequential systems.
- No record of why an AI-influenced decision was made, when it is later challenged.

---

**Next:** [12 · Tool & Action Control](12-pillar-tool-and-action-control.md)

*Version 0.1.0 · Licensed under the terms in [LICENSE.md](../LICENSE.md).*
