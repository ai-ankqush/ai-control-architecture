# Pillar 16: Incident Containment & Recovery

**Control question:** *When it fails, can we stop it and recover?*
**Surface:** makes See, Decide, and Do reversible.

---

## Purpose

Controls will fail, bypassed, misconfigured, or simply wrong. This pillar assumes it. It requires that every tiered use case can be **stopped quickly**, that high-impact actions have a **containment or compensation path**, and that recovery from an AI incident is **owned, documented, and exercised.** It is the pillar that makes AI authority *reversible*, and it is the precondition the architecture places on live enforcement: never enforce what you cannot undo.

---

## Why it matters

An AI that can act at machine speed can also fail at machine speed, thousands of wrong actions before a human notices. The question that decides whether that is an incident or a catastrophe is: *how fast can we stop it, and how much can we undo?* Most organizations discover they have no answer only during the incident, no kill switch that works, no rollback for the actions taken, no one who owns making it right. This pillar exists so that answer is known and tested *before* go-live, not improvised during a crisis. It is also what makes it safe to grant enforcement authority at all: the [Core Thesis](03-core-thesis.md) demands that authority be reversible, and this is where reversibility is built.

---

## Control objectives

- Provide a **tested means to disable** the AI capability quickly, for each tiered use case.
- Ensure high-impact actions have a **containment or compensation/rollback path.**
- Make incident **recovery owned, documented, and exercised.**

---

## Requirements

From the [Requirements Catalogue](06-requirements-catalogue.md):

| ID | Requirement | From | Boundary |
|----|-------------|------|----------|
| ACA-16-01 | Each tiered use case has a tested means to disable the AI capability quickly. | T4 | Enforced |
| ACA-16-02 | High-impact actions have a containment or compensation/rollback path. | T4 | Enforced |
| ACA-16-03 | Recovery from an AI incident is owned, documented, and exercised. | T4 | Evidenced |

---

## Reversibility classes

Classify what can be undone, because it dictates what may be enforced ([pillar 12](12-pillar-tool-and-action-control.md)):

```text
Reversible the action can be cleanly undone → safest to enforce
Compensatable the effect can be offset by a counter-action → enforce with a path
Irreversible the effect cannot be undone or offset → gate hard; human authority
```

The hard rule: **no action class is enforced live without a reversibility answer.** Irreversible actions demand the strongest gates (human approval, step-up) and the smallest scope.

---

## Key controls

- **Kill switch**: a tested, fast, complete way to disable a use case or revoke its authority (ties to [identity revocation, pillar 08](08-pillar-ai-identity-and-access-control.md)): feature flags, credential revocation, action-broker off-switch. Tested, not theoretical.
- **Containment**: the ability to halt in place: stop further actions, freeze the agent, quarantine outputs, without waiting for full shutdown.
- **Compensation / rollback**: for actions that ran, a defined way to undo or offset them, and a recovery ledger of what was done so it can be reversed.
- **Reversibility-graduated autonomy**: grant more autonomy where actions are reversible; require more human authority where they are not.
- **Recovery ownership & exercises**: a named owner for "make it right," a documented recovery procedure, and periodic exercise so it works when needed.

The incident how-to lives in the operating docs ([failure scenarios and incident guidance](DOCS-README.md)); this pillar defines the containment and recovery that are *required*.

---

## Tier guidance

| | T1 | T2 | T3 | T4 | T5 |
|---|----|----|----|----|----|
| Tested kill switch | - | - | - | Required | Required (tested) |
| Containment / compensation path | - | - | - | Required | Required (before enforcement) |
| Recovery owner & procedure | - | - | - | Required | Required (exercised) |
| Reversibility classification | - | - | Recommended | Required | Required |

---

## Evidence

The [AI Incident Containment & Recovery template](../templates/ai-incident-containment-recovery-template.md) and [AI Incident Record template](../templates/ai-incident-record-template.md) capture the kill switch, the containment and compensation paths, the reversibility classification, and the recovery ownership and exercises. This pillar is the precondition for *Enforced* boundaries elsewhere: enforcement is only granted where containment exists behind it.

---

## Standards crosswalk

Maps to NIST AI RMF **Manage** (incident response and recovery), ISO/IEC 42001 (incident management, corrective action), EU AI Act (corrective actions, ability to intervene and stop, Arts. 14, 20), NYDFS Part 500 (incident response), and SR 11-7 (contingency and remediation). See [`mappings/`](../mappings/MAPPINGS-README.md).

---

## Failure modes

- A kill switch that was never tested and does not actually stop the AI.
- Live enforcement on an irreversible action with no compensation path.
- Actions taken that cannot be undone or even enumerated after the fact.
- No named owner of recovery, everyone assumes someone else has it.

---

**Next:** the operating section, [implementation, maturity, playbook, governance, metrics, assurance, and triage](DOCS-README.md).

*Version 0.1.0 · Licensed under the terms in [LICENSE.md](../LICENSE.md).*
