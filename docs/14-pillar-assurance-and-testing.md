# Pillar 14: AI Assurance & Testing

**Control question:** *Do the controls actually hold?*
**Surface:** proves the boundedness of See, Decide, and Do.

---

## Purpose

A control that has never been tested is a *claim*, not a control. This pillar makes control strength **provable**: it requires that a use case's controls be tested proportionate to its tier, that high-impact and autonomous use cases face adversarial testing, and that results are retained as evidence and re-run when the use case changes. It is how a boundary moves from *declared* or *evidenced* to *verified*.

---

## Why it matters

AI controls fail quietly. A data boundary looks configured but leaks under a certain query; an injection filter blocks the obvious cases and misses the crafted one; an action allow-list is bypassed through an unexpected tool path. None of this shows up until someone looks, deliberately, adversarially, before an incident does the looking for you. Assurance is the pillar that turns "we have controls" into "we have *tested* controls," and it is the difference between a architecture that documents intentions and one that can survive its own show-me.

---

## Control objectives

- **Test controls before go-live**: proportionate to tier.
- Subject high-impact and autonomous use cases to **adversarial testing** of input, output, and action controls.
- **Retain results** as evidence and **re-run** on material change.

---

## Requirements

From the [Requirements Catalogue](06-requirements-catalogue.md):

| ID | Requirement | From | Boundary |
|----|-------------|------|----------|
| ACA-14-01 | Controls are tested before go-live, proportionate to tier. | T3 | Verified |
| ACA-14-02 | High-impact and autonomous use cases undergo adversarial testing of input, output, and action controls. | T5 | Verified |
| ACA-14-03 | Test results are retained as evidence and re-run on material change. | T3 | Verified |

---

## Key controls

- **Control test plan**: for each in-scope control, a defined way to test that it holds, and the expected result (see the [AI Assurance Test Plan template](../templates/ai-assurance-test-plan-template.md)).
- **Pre-go-live gate**: controls are tested before a decision-supporting or higher use case is allowed live; failures block or tier-down.
- **Adversarial / red-team testing**: for high-impact and autonomous use cases, actively try to break input, output, and action controls (prompt injection, boundary escape, unauthorized action) rather than only confirming happy paths.
- **Regression on change**: model updates, new tools, new data sources, or scope changes re-trigger the relevant tests; a control verified last quarter is not assumed to hold today.
- **Evidence capture**: results are recorded as the *verified* boundary evidence the other pillars point to.

The how-to for running assurance and audit lives in the operating guide ([Assurance & Audit Guide](DOCS-README.md)); this pillar defines what assurance is *required*.

---

## Tier guidance

| | T1 | T2 | T3 | T4 | T5 |
|---|----|----|----|----|----|
| Pre-go-live control test | - | Recommended | Required | Required | Required |
| Adversarial testing | - | - | - | Recommended | Required |
| Retain results as evidence | - | - | Required | Required | Required |
| Re-test on material change | - | - | Required | Required | Required |

---

## Evidence

The [AI Assurance & Testing template](../templates/ai-assurance-and-testing-template.md) and [AI Assurance Test Plan template](../templates/ai-assurance-test-plan-template.md) capture the test plan, execution, and results. This pillar is what *produces* the *Verified* boundary source that pillars 08–12 rely on, assurance is how their controls earn that grade.

---

## Standards crosswalk

Maps to NIST AI RMF **Measure**, ISO/IEC 42001 (verification, validation, performance evaluation), EU AI Act (testing, accuracy, robustness, Arts. 9, 15), and SR 11-7 (model validation and effective challenge). See [`mappings/`](../mappings/MAPPINGS-README.md).

---

## Failure modes

- Controls documented but never tested, claims dressed as controls.
- Happy-path testing only; no adversarial attempt to break them.
- A model or tool change that silently invalidates a previously verified control.
- Test results that exist but were never captured as evidence.

---

**Next:** [15 · Monitoring, Logging & Evidence](15-pillar-monitoring-and-evidence.md)

*Version 0.1.0 · Licensed under the terms in [LICENSE.md](../LICENSE.md).*
