# Pillar 15: Monitoring, Logging & Evidence

**Control question:** *Can we see, and later reconstruct, what the AI did?*
**Surface:** observes See, Decide, and Do.

---

## Purpose

This pillar makes AI behavior **observable and reconstructable.** It requires that activity be logged sufficiently to reconstruct what an AI saw, produced, decided, and did; that those logs be tamper-evident and retained; and that anomalous or policy-violating behavior be detectable and alertable. Assurance ([14](14-pillar-assurance-and-testing.md)) proves controls hold before go-live; monitoring proves what actually happened after.

---

## Why it matters

When an AI use case fails, a boundary breach, a bad decision, an unauthorized action, the first questions are always the same: *what did it see, what did it do, when, and on whose authority?* If the logs cannot answer, you have an incident you cannot scope, a breach you cannot bound, and an audit you cannot pass. Worse, without monitoring you do not know a failure happened at all until its consequences surface elsewhere. Evidence is also what turns the rest of the architecture from assertion into proof: the boundary sources, the decisions, the actions, all of it depends on a durable, trustworthy record.

---

## Control objectives

- **Log** activity sufficiently to reconstruct what AI saw, produced, decided, and did.
- Keep logs **tamper-evident and retained** per policy.
- Make **anomalous or policy-violating behavior detectable and alertable.**

---

## Requirements

From the [Requirements Catalogue](06-requirements-catalogue.md):

| ID | Requirement | From | Boundary |
|----|-------------|------|----------|
| ACA-15-01 | Activity is logged sufficiently to reconstruct what AI saw, produced, decided, and did. | T2 | Verified |
| ACA-15-02 | Logs are tamper-evident and retained per policy. | T3 | Verified |
| ACA-15-03 | Anomalous or policy-violating behavior is detectable and alertable. | T4 | Verified |

---

## Key controls

- **Reconstruction-grade logging**: capture the See/Decide/Do trail: inputs and retrieved context (or references to them), outputs, decisions and their human validation, and every action with its identity, inputs, and outcome. Enough to answer "what happened" without guesswork.
- **Integrity & retention**: logs are tamper-evident and retained to policy, so they hold up as evidence and cannot be quietly altered.
- **Detection & alerting**: surface anomalies and policy violations (boundary-escape attempts, unauthorized action attempts, injection signatures, unusual volume or scope) to the people and systems that can respond.
- **Feed the response path**: monitoring is the trigger for [containment](16-pillar-containment-and-recovery.md); interdictions and hostile-flagged behavior should reach the SOC/response function.
- **Privacy-aware**: log what is needed for reconstruction and control, minimizing sensitive content; reference rather than duplicate regulated data where possible.

The metrics and reporting how-to lives in the operating guide ([Metrics & Reporting](DOCS-README.md)); this pillar defines the monitoring and evidence that are *required*.

---

## Tier guidance

| | T1 | T2 | T3 | T4 | T5 |
|---|----|----|----|----|----|
| Reconstruction-grade logging | Basic | Required (verified) | Required (verified) | Required (verified) | Required (verified) |
| Tamper-evidence & retention | - | Recommended | Required | Required | Required |
| Anomaly detection & alerting | - | - | Recommended | Required | Required |
| Response-path integration | - | - | Recommended | Required | Required |

---

## Evidence

The [AI Monitoring, Logging & Evidence template](../templates/ai-monitoring-logging-evidence-template.md) captures the logging design, integrity/retention, and detection. This pillar produces the durable record that every other pillar's evidence ultimately rests on, and that an [assurance](14-pillar-assurance-and-testing.md) or audit pass consumes.

---

## Standards crosswalk

Maps to NIST AI RMF **Measure/Manage**, ISO/IEC 42001 (logging, monitoring, operational control), EU AI Act (automatic logging and record-keeping, Art. 12; post-market monitoring), NYDFS Part 500 (audit trails, monitoring), and SR 11-7 (ongoing monitoring). See [`mappings/`](../mappings/MAPPINGS-README.md).

---

## Failure modes

- Logs that cannot reconstruct what the AI saw or did.
- Records that can be altered, or that were not retained long enough to matter.
- A failure that ran undetected because nothing was watching.
- Monitoring that fires but reaches no one who can act.

---

**Next:** [16 · Incident Containment & Recovery](16-pillar-containment-and-recovery.md)

*Version 0.1.0 · Licensed under the terms in [LICENSE.md](../LICENSE.md).*
