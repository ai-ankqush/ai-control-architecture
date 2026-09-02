# ISO/IEC 42001 Crosswalk

This document maps the AI Control Architecture to ISO/IEC 42001.

The purpose of this crosswalk is to show how the AI Control Architecture can help enterprises operationalize an Artificial Intelligence Management System through practical controls, evidence, assurance, and operating processes.

The AI Control Architecture is not a replacement for ISO/IEC 42001.

It is an implementation layer that can support an AI management system.

---

# 1. Positioning

ISO/IEC 42001 provides requirements and guidance for establishing, implementing, maintaining, and continually improving an AI management system.

The AI Control Architecture helps answer:

```text
How do we operationalize AI management system expectations inside enterprise systems, data, identity, vendors, workflows, assurance, and incident response?
```

A useful positioning is:

```text
ISO/IEC 42001 = AI management system requirements
AI Control Architecture = practical control architecture and implementation layer
```

This crosswalk does not claim certification readiness.

It helps organizations structure implementation work that may support AI management system objectives.

---

# 2. AI Management System Interpretation

An AI management system should help an organization define how AI is governed, risk-managed, operated, monitored, reviewed, improved, and aligned to organizational objectives.

The AI Control Architecture supports this by defining how AI is:

```text
Inventoried
Owned
Risk-tiered
Access-controlled
Data-bounded
Input-controlled
Output-validated
Action-limited
Human-accountable
Tested
Monitored
Evidenced
Contained
Recovered
Improved
```

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

These pillars provide practical implementation structures that can support AI management system requirements.

---

# 4. High-Level Crosswalk

| ISO/IEC 42001 Management System Area | AI Control Architecture Support |
|---|---|
| Organizational context | AI inventory, AI patterns, business purpose, stakeholder and risk context |
| Leadership and accountability | Human accountability model, governance and operating model, decision rights |
| Planning and risk management | Risk tiering, requirements catalogue, risk assessment, control assessment |
| Support and resources | ownership model, evidence strategy, training/guidance, documentation |
| Operation | control implementation across identity, data, prompt, output, tools, vendors, incidents |
| Performance evaluation | assurance testing, maturity model, metrics and reporting, evidence packages |
| Improvement | findings, exceptions, incidents, post-incident review, roadmap and control updates |

---

# 5. Organizational Context Crosswalk

## ISO/IEC 42001 Intent

An AI management system should be grounded in the organization’s context, objectives, interested parties, AI use, and obligations.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture operationalizes organizational context by requiring every AI use case to be inventoried, owned, classified, and linked to business purpose, AI pattern, data, decisions, vendors, and risk tier.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| AI inventory and classification | Captures AI use cases, lifecycle status, risk tier, and patterns. |
| Human accountability model | Assigns ownership for business, technical, data, vendor, risk, and incident responsibilities. |
| Data boundary control | Identifies data context, classifications, owners, and restrictions. |
| Output and decision control | Identifies decision and business impact. |
| Tool and action control | Identifies operational impact and action capability. |

## Implementation Activities

```text
Define AI inventory scope.
Identify AI use cases.
Classify AI patterns.
Record business purpose.
Record lifecycle status.
Identify internal and external stakeholders.
Identify data sources and owners.
Identify vendor involvement.
Identify decision impact.
Identify tool/action capability.
Assign risk tier.
```

## Example Evidence

```text
AI inventory
AI use case intake record
Business owner record
AI pattern classification
Risk assessment
Data source map
Vendor assessment
Decision impact assessment
Tool inventory
Lifecycle status
```

## Related Project Files

```text
README.md
QUICKSTART.md
docs/17-implementation-checklists.md
docs/19-common-ai-control-patterns.md
templates/ai-use-case-intake-template.md
templates/ai-inventory-record-template.md
templates/ai-risk-assessment-template.md
```

---

# 6. Leadership and Accountability Crosswalk

## ISO/IEC 42001 Intent

An AI management system requires leadership commitment, roles, responsibilities, accountability, governance, and policy direction.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture operationalizes leadership and accountability by defining human ownership for AI outcomes, risk, decisions, approvals, exceptions, vendors, assurance, evidence, and incidents.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| Human accountability model | Defines who owns outcomes, decisions, approvals, exceptions, and incidents. |
| AI inventory and classification | Ensures each AI use case has assigned owners. |
| Output and decision control | Assigns decision ownership where AI influences decisions. |
| Tool and action control | Assigns action approval and tool ownership. |
| Incident containment and recovery | Assigns incident and recovery ownership. |

## Implementation Activities

```text
Assign business owner.
Assign technical owner.
Assign data owner where required.
Assign decision owner where required.
Assign vendor owner where applicable.
Assign assurance owner.
Assign evidence owner.
Assign incident owner.
Define governance forums.
Define decision rights.
Define risk acceptance authority.
Define escalation paths.
```

## Example Evidence

```text
RACI matrix
Ownership record
Governance operating model
Decision rights matrix
Approval matrix
Risk acceptance record
Exception record
Incident owner record
Governance meeting record
```

## Related Project Files

```text
docs/13-pillar-human-accountability.md
docs/22-governance-and-operating-model.md
templates/ai-human-accountability-template.md
templates/ai-exception-record-template.md
templates/ai-incident-record-template.md
```

---

# 7. Planning and Risk Management Crosswalk

## ISO/IEC 42001 Intent

An AI management system should plan how AI risks and opportunities are identified, assessed, treated, monitored, and improved.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture operationalizes planning and risk management through risk tiering, control requirements, control assessments, exceptions, assurance planning, incident planning, and maturity roadmaps.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| AI inventory and classification | Establishes visibility and risk tiering. |
| Data boundary control | Identifies data-related risk. |
| Prompt and input control | Identifies input and prompt injection risk. |
| Output and decision control | Identifies output, decision, and record risk. |
| Tool and action control | Identifies action, autonomy, and blast-radius risk. |
| AI assurance and testing | Defines testing plans based on risk. |
| Incident containment and recovery | Defines failure and containment planning. |

## Implementation Activities

```text
Define AI risk tiering model.
Assess risk drivers.
Classify AI use cases by risk tier.
Map required controls by tier.
Define minimum control baseline.
Assess control readiness.
Identify gaps.
Document exceptions.
Define compensating controls.
Plan assurance testing.
Define incident scenarios.
Create maturity roadmap.
```

## Example Evidence

```text
Risk tiering model
Risk assessment
Control assessment
Requirements mapping
Exception record
Compensating control record
Assurance test plan
Incident containment plan
Maturity assessment
Roadmap
```

## Related Project Files

```text
docs/06-requirements-catalogue.md
docs/17-implementation-checklists.md
docs/18-control-maturity-model.md
docs/20-common-failure-scenarios.md
docs/21-adoption-playbook.md
templates/ai-risk-assessment-template.md
templates/ai-risk-tiering-template.md
templates/ai-control-assessment-template.md
templates/ai-assurance-test-plan-template.md
```

---

# 8. Support and Documentation Crosswalk

## ISO/IEC 42001 Intent

An AI management system requires resources, competence, awareness, communication, documented information, and support processes.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture supports documented information and operational support through templates, evidence packages, quickstart guidance, examples, contribution rules, and documentation of responsibilities, controls, tests, and incidents.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| Human accountability model | Defines roles, responsibilities, and required awareness. |
| Monitoring, logging, and evidence | Defines evidence ownership, retention, and reconstructability. |
| AI assurance and testing | Defines test plans, results, findings, and remediation evidence. |
| AI inventory and classification | Creates documented information about AI use. |
| Incident containment and recovery | Creates incident playbooks and recovery documentation. |

## Implementation Activities

```text
Maintain documented AI inventory.
Maintain risk and control records.
Maintain architecture decision records.
Maintain vendor assessments.
Maintain evidence packages.
Maintain assurance test plans and results.
Maintain incident records.
Maintain exception records.
Provide user guidance.
Provide owner guidance.
Provide reviewer guidance.
```

## Example Evidence

```text
Documented AI inventory
Templates
Completed assessments
Architecture decision records
Evidence packages
User guidance
Training or awareness records
Assurance reports
Incident records
Exception records
Changelog
Version file
```

## Related Project Files

```text
QUICKSTART.md
CONTRIBUTING.md
CHANGELOG.md
VERSION
templates/TEMPLATES-README.md
examples/EXAMPLES-README.md
templates/ai-control-evidence-package-template.md
templates/ai-architecture-decision-record-template.md
```

---

# 9. Operation Crosswalk

## ISO/IEC 42001 Intent

An AI management system should control operational activities related to AI systems and ensure planned processes are implemented.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture operationalizes AI system operation through control pillars that define how AI is accessed, bounded, validated, monitored, and contained.

## Relevant Pillars

| Pillar | Operational Control Focus |
|---|---|
| AI identity and access control | Defines AI identities, delegated authority, least privilege, and revocation. |
| Data boundary control | Defines approved data sources, retrieval boundaries, retention, and reuse. |
| Prompt and input control | Defines allowed/prohibited inputs, external content handling, and prompt injection controls. |
| Output and decision control | Defines output validation, decision separation, generated records, and correction paths. |
| Tool and action control | Defines tool inventory, action classification, approval gates, logging, kill switch, and rollback. |
| Monitoring, logging, and evidence | Defines operational monitoring, event logging, and evidence retention. |
| Incident containment and recovery | Defines operational response to AI failure. |

## Implementation Activities

```text
Implement AI access controls.
Implement data source restrictions.
Implement retrieval boundaries.
Implement prompt/input rules.
Implement output validation.
Implement decision review.
Implement tool allowlists and denylists.
Implement approval gates.
Implement logging.
Implement monitoring.
Implement evidence retention.
Implement kill switches.
Implement rollback or compensation paths.
```

## Example Evidence

```text
Access approval
IAM/PAM configuration
Data source allowlist
Retrieval configuration
Prompt/input control record
Output validation rule
Decision evidence
Tool inventory
Action classification
Approval logs
Tool/action logs
Monitoring alerts
Kill switch test
Rollback plan
```

## Related Project Files

```text
docs/08-pillar-ai-identity-and-access-control.md
docs/09-pillar-data-boundary-control.md
docs/10-pillar-input-control.md
docs/11-pillar-output-and-decision-control.md
docs/12-pillar-tool-and-action-control.md
docs/17-implementation-checklists.md
templates/ai-identity-and-access-control-template.md
templates/ai-data-boundary-template.md
templates/ai-prompt-and-input-control-template.md
templates/ai-output-and-decision-control-template.md
templates/ai-tool-and-action-control-template.md
```

---

# 10. Performance Evaluation Crosswalk

## ISO/IEC 42001 Intent

An AI management system should evaluate performance, monitor effectiveness, conduct reviews, and support audit and management review.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture operationalizes performance evaluation through assurance testing, metrics, maturity assessment, audit guidance, evidence packages, and reporting.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| AI assurance and testing | Tests AI behavior and control effectiveness. |
| Monitoring, logging, and evidence | Provides evidence for review, audit, and incident response. |
| Output and decision control | Supports quality, validation, and decision review. |
| Tool and action control | Supports testing of action controls and approval gates. |
| Incident containment and recovery | Supports tabletop exercises and containment testing. |
| AI inventory and classification | Enables portfolio-level reporting. |

## Implementation Activities

```text
Define AI assurance scope.
Perform control testing.
Perform adversarial testing where required.
Test logging completeness.
Test evidence reconstruction.
Test kill switches.
Track findings.
Track remediation.
Assess control maturity.
Report metrics.
Conduct governance review.
Conduct audit review.
Conduct post-incident review.
```

## Example Evidence

```text
Assurance test plan
Assurance report
Test results
Findings register
Retest evidence
Evidence package
Maturity assessment
Metrics dashboard
Audit report
Governance review minutes
Incident tabletop results
Post-incident review
```

## Related Project Files

```text
docs/18-control-maturity-model.md
docs/23-metrics-and-reporting.md
docs/24-assurance-and-audit-guide.md
templates/ai-assurance-test-plan-template.md
templates/ai-control-evidence-package-template.md
```

---

# 11. Improvement Crosswalk

## ISO/IEC 42001 Intent

An AI management system should support corrective action, continual improvement, and response to nonconformities, incidents, findings, and changing conditions.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture operationalizes improvement through findings, exceptions, incident lessons learned, roadmap updates, requirements updates, assurance retesting, and maturity improvement.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| AI assurance and testing | Produces findings and retest requirements. |
| Monitoring, logging, and evidence | Reveals evidence gaps and monitoring gaps. |
| Incident containment and recovery | Produces lessons learned and control updates. |
| Human accountability model | Assigns remediation and risk acceptance owners. |
| AI inventory and classification | Updates lifecycle, risk tier, and scope after change. |

## Implementation Activities

```text
Track assurance findings.
Assign remediation owners.
Define corrective actions.
Retest failed controls.
Track exceptions and expiry.
Review incidents and near misses.
Update requirements after incidents.
Update templates after control gaps.
Update assurance tests after new failure scenarios.
Update risk tiers after material change.
Update maturity roadmap.
```

## Example Evidence

```text
Findings register
Corrective action plan
Retest result
Exception review
Incident report
Post-incident review
Updated control requirement
Updated assurance test
Updated template
Updated roadmap
Maturity trend report
```

## Related Project Files

```text
ROADMAP.md
CHANGELOG.md
docs/20-common-failure-scenarios.md
docs/21-adoption-playbook.md
docs/23-metrics-and-reporting.md
docs/24-assurance-and-audit-guide.md
templates/ai-exception-record-template.md
templates/ai-incident-record-template.md
```

---

# 12. Pillar-to-ISO Management System Area Matrix

| AI Control Architecture Pillar | Context | Leadership | Planning | Support | Operation | Evaluation | Improvement |
|---|---:|---:|---:|---:|---:|---:|---:|
| AI inventory and classification | Primary | Supporting | Primary | Primary | Supporting | Primary | Supporting |
| AI identity and access control | Supporting | Supporting | Primary | Supporting | Primary | Supporting | Supporting |
| Data boundary control | Primary | Supporting | Primary | Supporting | Primary | Primary | Supporting |
| Prompt and input control | Supporting | Supporting | Primary | Supporting | Primary | Primary | Supporting |
| Output and decision control | Primary | Primary | Primary | Supporting | Primary | Primary | Supporting |
| Tool and action control | Primary | Primary | Primary | Supporting | Primary | Primary | Primary |
| Human accountability model | Supporting | Primary | Primary | Primary | Supporting | Supporting | Primary |
| AI assurance and testing | Supporting | Supporting | Primary | Primary | Supporting | Primary | Primary |
| Monitoring, logging, and evidence | Supporting | Supporting | Supporting | Primary | Primary | Primary | Primary |
| Incident containment and recovery | Supporting | Primary | Primary | Supporting | Primary | Primary | Primary |

---

# 13. Example: Applying ISO/IEC 42001 Alignment to Vendor AI

## Use Case

```text
AI-enabled SaaS feature that summarizes customer support cases.
```

## AI Control Architecture Implementation

| Management System Area | Implementation Activity |
|---|---|
| Context | Identify vendor AI feature, business purpose, customer data exposure, and stakeholders. |
| Leadership | Assign business owner, vendor owner, data owner, privacy/legal owner, and incident contact. |
| Planning | Assess risk tier, vendor data processing, retention, training/reuse, and evidence gaps. |
| Support | Maintain vendor assessment, admin configuration record, user guidance, and evidence package. |
| Operation | Disable auto-send, auto-close, refund, credit, and entitlement actions unless approved. |
| Evaluation | Test feature disablement, logging availability, output quality, and escalation triggers. |
| Improvement | Track vendor evidence gaps, incidents, findings, and contract remediation. |

## Related Example

```text
examples/vendor-ai-example.md
```

---

# 14. Example: Applying ISO/IEC 42001 Alignment to Agentic AI

## Use Case

```text
IT service desk ticket triage agent.
```

## AI Control Architecture Implementation

| Management System Area | Implementation Activity |
|---|---|
| Context | Identify agent purpose, autonomy level, data sources, tools, users, and operational scope. |
| Leadership | Assign business owner, technical owner, security owner, data owner, and incident owner. |
| Planning | Assign Tier 4 risk level and define required controls for tool/action capability. |
| Support | Maintain agent control record, tool inventory, approval matrix, and analyst guidance. |
| Operation | Enforce approval gates, blast-radius limits, logging, tool restrictions, and kill switch. |
| Evaluation | Test prompt injection, approval bypass, denied action logging, kill switch, and evidence reconstruction. |
| Improvement | Update action boundaries, incident playbooks, tests, and controls based on findings. |

## Related Example

```text
examples/agentic-ai-example.md
```

---

# 15. How to Use This Crosswalk

Use this crosswalk when:

```text
An enterprise wants to align AI Control Architecture work with ISO/IEC 42001.
An AI governance team is designing an AI management system.
A risk team wants evidence of AI control implementation.
An audit or assurance team wants to identify evidence for AI management system operation.
A vendor or business owner asks how AI control work supports management system expectations.
```

Suggested use:

```text
1. Identify the AI use case or AI portfolio in scope.
2. Complete intake and inventory.
3. Assign owners.
4. Assign risk tier.
5. Map the use case to relevant AI management system areas.
6. Identify required controls.
7. Identify required evidence.
8. Identify assurance tests.
9. Track findings and improvements.
```

---

# 16. Limitations

This crosswalk is intended to support AI management system implementation planning.

It is not:

```text
A formal ISO/IEC 42001 certification claim
A certification readiness assessment
A complete clause-by-clause legal interpretation
An audit opinion
A substitute for qualified ISO implementation or certification advice
```

Organizations seeking certification should work with qualified ISO/IEC 42001 advisors, auditors, or certification bodies.

---

# 17. Future Enhancements

Future versions may add:

```text
Clause-by-clause ISO/IEC 42001 mapping
Annex A control mapping
Evidence catalogue aligned to ISO/IEC 42001
Management review checklist
Internal audit checklist
Machine-readable ISO crosswalk
ISO readiness assessment template
```

---

# 18. Summary

ISO/IEC 42001 provides a management system structure for responsible AI development, provision, and use.

The AI Control Architecture provides practical enterprise controls that can support that management system.

Together, they help organizations move from:

```text
AI management system intention
```

to:

```text
Operational AI control, evidence, assurance, and improvement
```