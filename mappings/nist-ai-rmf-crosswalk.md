# NIST AI RMF Crosswalk

This document maps the AI Control Architecture to the NIST AI Risk Management Framework.

The purpose of this crosswalk is to show how the AI Control Architecture can help enterprises operationalize the NIST AI RMF through practical controls, evidence, assurance, and incident readiness.

The AI Control Architecture is not a replacement for the NIST AI RMF.

It is an implementation layer that helps translate AI risk management outcomes into enterprise control activities.

---

# 1. Positioning

The NIST AI Risk Management Framework provides a structured way to manage AI risks.

The AI Control Architecture helps answer:

```text
How do we implement those risk management expectations inside enterprise systems, data, identity, workflows, vendors, assurance, and incident response?
```

NIST AI RMF focuses on managing AI risk.

AI Control Architecture focuses on operational control.

Together, they can be used as:

```text
NIST AI RMF = Risk management structure
AI Control Architecture = Control implementation layer
```

---

# 2. NIST AI RMF Core Functions

The NIST AI RMF Core is organized around four high-level functions:

```text
Govern
Map
Measure
Manage
```

These functions help organizations establish AI risk governance, understand AI context and risks, assess and monitor risk, and prioritize and respond to risk.

---

# 3. AI Control Architecture Pillars

The AI Control Architecture uses ten pillars:

```text
1. AI inventory and classification
2. AI identity and access control
3. Data boundary control
4. Prompt and input control
5. Output and decision control
6. Tool and action control
7. Human accountability model
8. AI assurance and testing
9. Monitoring, logging, and evidence
10. Incident containment and recovery
```

These pillars provide the operational control structure that can support NIST AI RMF outcomes.

---

# 4. High-Level Crosswalk

| NIST AI RMF Function | Primary AI Control Architecture Support |
|---|---|
| Govern | AI inventory and classification; human accountability; governance and operating model; metrics and reporting |
| Map | AI inventory; risk tiering; data boundary; identity and access; AI pattern classification; vendor AI review |
| Measure | AI assurance and testing; output validation; monitoring, logging, and evidence; maturity model |
| Manage | incident containment and recovery; tool/action control; exception management; remediation; risk acceptance |

---

# 5. Govern Function Crosswalk

## NIST AI RMF Intent

The Govern function establishes the organizational structures, policies, processes, roles, responsibilities, and culture needed to manage AI risk.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture operationalizes Govern by requiring that AI use cases are visible, owned, risk-tiered, governed through clear decision rights, and connected to enterprise operating processes.

## Relevant AI Control Architecture Pillars

| Pillar | Contribution to Govern |
|---|---|
| AI inventory and classification | Establishes visibility of AI use cases and lifecycle status. |
| Human accountability model | Assigns business, technical, data, decision, risk, vendor, assurance, and incident owners. |
| Monitoring, logging, and evidence | Provides governance evidence and reporting data. |
| Incident containment and recovery | Defines ownership for AI incident response and recovery. |
| AI assurance and testing | Provides governance confidence through control validation. |

## Implementation Activities

```text
Create AI inventory.
Assign business owners.
Assign technical owners.
Assign data owners where required.
Assign decision owners where AI influences decisions.
Assign vendor owners where vendor AI is involved.
Define AI risk tiers.
Define governance forums and decision rights.
Define exception management.
Define incident ownership.
Define reporting cadence.
Track metrics and maturity.
```

## Example Evidence

```text
AI inventory
AI use case intake record
Risk tier record
Ownership record
RACI matrix
Governance meeting record
Exception record
Risk acceptance record
Maturity report
Metrics dashboard
Incident ownership record
```

## Related Project Files

```text
docs/06-requirements-catalogue.md
docs/18-control-maturity-model.md
docs/21-adoption-playbook.md
docs/22-governance-and-operating-model.md
docs/23-metrics-and-reporting.md
templates/ai-use-case-intake-template.md
templates/ai-risk-assessment-template.md
templates/ai-control-assessment-template.md
templates/ai-exception-record-template.md
```

---

# 6. Map Function Crosswalk

## NIST AI RMF Intent

The Map function helps organizations understand the context, intended purpose, users, benefits, risks, impacts, and system characteristics of AI use.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture operationalizes Map by forcing enterprises to define what AI exists, what pattern it follows, what data it can access, what decisions it may influence, what tools or actions it can use, and which risks apply.

## Relevant AI Control Architecture Pillars

| Pillar | Contribution to Map |
|---|---|
| AI inventory and classification | Captures AI use case, lifecycle, pattern, owner, and risk tier. |
| AI identity and access control | Maps identities, authority, delegated access, and revocation. |
| Data boundary control | Maps data sources, classifications, retrieval boundaries, retention, and reuse. |
| Prompt and input control | Maps input surfaces, external content, uploaded files, and prompt injection exposure. |
| Output and decision control | Maps outputs, decisions, generated records, and downstream use. |
| Tool and action control | Maps tools, APIs, workflows, action types, approval gates, and blast radius. |
| Human accountability model | Maps owners, reviewers, approvers, decision owners, and risk owners. |

## Implementation Activities

```text
Identify AI use case.
Classify AI pattern.
Assign lifecycle status.
Identify user population.
Identify vendor involvement.
Map data sources.
Classify data sensitivity.
Map retrieval boundaries.
Map prompt and input surfaces.
Map output types.
Identify decision impact.
Identify tool and action capability.
Assign initial risk tier.
Identify affected stakeholders.
Identify failure scenarios.
```

## Example Evidence

```text
AI use case intake
AI inventory record
AI pattern classification
Risk assessment
Data source map
Data classification record
Retrieval boundary record
Prompt/input control record
Output classification
Decision impact assessment
Tool inventory
Action classification
Vendor assessment
Stakeholder map
```

## Related Project Files

```text
QUICKSTART.md
docs/17-implementation-checklists.md
docs/19-common-ai-control-patterns.md
docs/20-common-failure-scenarios.md
templates/ai-use-case-intake-template.md
templates/ai-risk-assessment-template.md
templates/ai-inventory-record-template.md
templates/ai-risk-tiering-template.md
templates/ai-data-boundary-template.md
templates/ai-vendor-assessment-template.md
```

---

# 7. Measure Function Crosswalk

## NIST AI RMF Intent

The Measure function focuses on analyzing, assessing, benchmarking, testing, monitoring, and tracking AI risks and trustworthiness characteristics.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture operationalizes Measure by defining assurance tests, control tests, evidence requirements, monitoring expectations, metrics, maturity assessment, and reconstructability checks.

## Relevant AI Control Architecture Pillars

| Pillar | Contribution to Measure |
|---|---|
| AI assurance and testing | Defines testing of AI behavior and control effectiveness. |
| Monitoring, logging, and evidence | Defines logs, evidence, retention, event taxonomy, and reconstructability. |
| Output and decision control | Defines output validation and decision evidence. |
| Prompt and input control | Defines prompt injection and input control testing. |
| Data boundary control | Defines retrieval boundary and data leakage testing. |
| Tool and action control | Defines unauthorized tool use, approval gate, and rollback testing. |
| Incident containment and recovery | Defines containment tests, kill switch tests, and incident tabletop exercises. |

## Implementation Activities

```text
Define assurance scope.
Create assurance test plan.
Test data boundaries.
Test retrieval boundaries.
Test prompt injection.
Test output validation.
Test decision evidence.
Test tool/action controls.
Test approval gates.
Test logging completeness.
Test evidence reconstruction.
Test kill switch.
Test rollback or compensation.
Track findings.
Track maturity metrics.
Track incidents and near misses.
```

## Example Evidence

```text
Assurance test plan
Test cases
Test results
Prompt injection test results
Retrieval boundary test results
Data leakage test results
Output validation evidence
Decision evidence
Tool/action test results
Approval gate test results
Logging completeness test
Evidence reconstruction test
Kill switch test
Rollback test
Findings register
Maturity assessment
Metrics dashboard
```

## Related Project Files

```text
docs/18-control-maturity-model.md
docs/23-metrics-and-reporting.md
docs/24-assurance-and-audit-guide.md
templates/ai-assurance-test-plan-template.md
templates/ai-control-evidence-package-template.md
templates/ai-control-assessment-template.md
```

---

# 8. Manage Function Crosswalk

## NIST AI RMF Intent

The Manage function focuses on prioritizing, responding to, treating, monitoring, and improving risk management activities based on measured and mapped AI risks.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture operationalizes Manage by requiring risk-tiered controls, remediation, exception management, incident containment, recovery, restart criteria, vendor remediation, and continuous improvement.

## Relevant AI Control Architecture Pillars

| Pillar | Contribution to Manage |
|---|---|
| AI inventory and classification | Prioritizes use cases by risk tier and lifecycle status. |
| Tool and action control | Limits high-risk actions and supports containment. |
| Human accountability model | Assigns risk acceptance, remediation, and incident ownership. |
| AI assurance and testing | Produces findings and retest requirements. |
| Monitoring, logging, and evidence | Supports ongoing review and detection. |
| Incident containment and recovery | Defines containment, recovery, restart criteria, and lessons learned. |

## Implementation Activities

```text
Prioritize high-risk AI.
Apply minimum controls by risk tier.
Approve, conditionally approve, defer, or reject AI use cases.
Track findings.
Assign remediation owners.
Approve exceptions where justified.
Define compensating controls.
Accept residual risk where appropriate.
Contain AI incidents.
Disable AI capabilities where required.
Revoke AI identities or tool access.
Correct outputs, records, or workflows.
Conduct post-incident review.
Update controls and tests.
Update roadmap and maturity plan.
```

## Example Evidence

```text
Risk-tiered control baseline
Control assessment
Approval decision
Conditional approval record
Finding record
Remediation plan
Exception record
Risk acceptance record
Incident record
Containment evidence
Recovery evidence
Restart approval
Post-incident review
Updated requirement
Updated assurance test
```

## Related Project Files

```text
docs/17-implementation-checklists.md
docs/21-adoption-playbook.md
docs/22-governance-and-operating-model.md
docs/23-metrics-and-reporting.md
docs/24-assurance-and-audit-guide.md
templates/ai-control-assessment-template.md
templates/ai-exception-record-template.md
templates/ai-incident-record-template.md
templates/ai-incident-containment-recovery-template.md
```

---

# 9. Pillar-to-NIST Function Matrix

| AI Control Architecture Pillar | Govern | Map | Measure | Manage |
|---|---:|---:|---:|---:|
| AI inventory and classification | Primary | Primary | Supporting | Primary |
| AI identity and access control | Supporting | Primary | Supporting | Supporting |
| Data boundary control | Supporting | Primary | Primary | Supporting |
| Prompt and input control | Supporting | Primary | Primary | Supporting |
| Output and decision control | Supporting | Primary | Primary | Supporting |
| Tool and action control | Supporting | Primary | Primary | Primary |
| Human accountability model | Primary | Primary | Supporting | Primary |
| AI assurance and testing | Supporting | Supporting | Primary | Primary |
| Monitoring, logging, and evidence | Primary | Supporting | Primary | Primary |
| Incident containment and recovery | Supporting | Supporting | Primary | Primary |

---

# 10. NIST Function to Example AI Control Activities

## Govern

| Control Activity | Example Evidence |
|---|---|
| Define AI governance roles | RACI matrix |
| Maintain AI inventory | AI inventory record |
| Assign AI owners | ownership record |
| Define AI risk tiers | risk tiering model |
| Define exception process | exception record |
| Report AI metrics | governance dashboard |

---

## Map

| Control Activity | Example Evidence |
|---|---|
| Identify AI pattern | intake record |
| Map data sources | data source map |
| Identify decision impact | decision impact assessment |
| Identify tool/action capability | tool inventory |
| Identify vendor involvement | vendor assessment |
| Identify affected stakeholders | use case intake |

---

## Measure

| Control Activity | Example Evidence |
|---|---|
| Test retrieval boundary | retrieval test result |
| Test prompt injection | prompt injection test result |
| Test output validation | output validation result |
| Test approval gate | approval gate test result |
| Test logging completeness | logging test result |
| Test evidence reconstruction | reconstruction test result |

---

## Manage

| Control Activity | Example Evidence |
|---|---|
| Apply controls by risk tier | control assessment |
| Track findings | findings register |
| Approve exceptions | exception record |
| Accept residual risk | risk acceptance record |
| Contain incident | incident containment record |
| Update controls after incident | post-incident review |

---

# 11. Example: Mapping a RAG Assistant

## Use Case

```text
Internal policy knowledge assistant using retrieval-augmented generation.
```

## NIST Function Mapping

| NIST Function | AI Control Architecture Implementation |
|---|---|
| Govern | Assign business owner, technical owner, data owner, and governance review. |
| Map | Map approved policy sources, data classifications, retrieval boundaries, users, and decision impact. |
| Measure | Test retrieval boundaries, prompt injection, source attribution, output accuracy, and evidence reconstruction. |
| Manage | Restrict retrieval sources, remediate findings, disable unsafe sources, track incidents, and update controls. |

## Example Evidence

```text
AI use case intake
Data source map
Data owner approval
Retrieval boundary test
Prompt injection test
Output validation result
Evidence reconstruction result
Incident containment path
```

Related example:

```text
examples/rag-assistant-example.md
```

---

# 12. Example: Mapping an AI Agent

## Use Case

```text
IT service desk ticket triage agent.
```

## NIST Function Mapping

| NIST Function | AI Control Architecture Implementation |
|---|---|
| Govern | Assign business owner, technical owner, security owner, incident owner, and approval authority. |
| Map | Map agent identity, autonomy level, tools, action types, data sources, and blast radius. |
| Measure | Test prompt injection, tool misuse, approval bypass, logging completeness, kill switch, and evidence reconstruction. |
| Manage | Enforce approval gates, restrict tools, disable agent identity, roll back incorrect routing, and update incident playbook. |

## Example Evidence

```text
Agent control record
Tool inventory
Action classification
Approval gate configuration
Tool/action test results
Kill switch test
Rollback test
Incident containment plan
```

Related example:

```text
examples/agentic-ai-example.md
```

---

# 13. How to Use This Crosswalk

Use this crosswalk when:

```text
An enterprise wants to align AI control work with NIST AI RMF.
A risk or compliance team asks how the architecture maps to NIST.
An assurance team wants to translate NIST functions into evidence.
An architecture team wants to show that AI control design supports recognized AI risk management practices.
A governance team wants to avoid creating a competing framework.
```

Suggested use:

```text
1. Identify the AI use case.
2. Complete intake and risk tiering.
3. Map the use case to Govern, Map, Measure, and Manage.
4. Identify which AI Control Architecture pillars apply.
5. Identify required evidence.
6. Identify assurance tests.
7. Track findings, exceptions, and incidents.
8. Report maturity and improvement.
```

---

# 14. Limitations

This crosswalk is intended to support AI risk management and control implementation.

It is not:

```text
A formal NIST certification
A compliance guarantee
A legal opinion
An audit opinion
A complete mapping to every NIST AI RMF category or subcategory
```

Organizations should tailor this crosswalk to their own governance, risk, compliance, legal, privacy, audit, and assurance requirements.

---

# 15. Future Enhancements

Future versions may add:

```text
Detailed mapping to NIST AI RMF categories and subcategories
Mapping to NIST AI RMF Playbook actions
Mapping to NIST AI 600-1 Generative AI Profile
Machine-readable crosswalk format
Evidence catalogue aligned to NIST functions
Assurance test catalogue aligned to NIST functions
```

---

# 16. Summary

The NIST AI RMF helps organizations structure AI risk management.

The AI Control Architecture helps enterprises implement that structure through practical controls.

Together, they support a movement from:

```text
Risk management intention
```

to:

```text
Operational AI control
```