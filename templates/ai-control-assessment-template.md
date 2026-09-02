# AI Control Assessment Template

This template is used to assess whether the required AI controls are defined, implemented, operating, evidenced, and sufficient for the assigned AI risk tier.

It should be completed after the AI Use Case Intake Template and AI Risk Assessment Template.

The purpose of this template is to evaluate control readiness across the ten AI Control Architecture pillars.

---

# 1. Assessment Information

## AI Use Case Name

```text
[Enter use case name]
```

## Assessment Date

```text
[Enter date]
```

## Assessor

```text
Name:
Function:
Email:
```

## Business Owner

```text
Name:
Function:
Email:
```

## Technical Owner

```text
Name:
Function:
Email:
```

## Assigned Risk Tier

Select one:

```text
[ ] Tier 1: Low-risk productivity or public-data use
[ ] Tier 2: Internal productivity with enterprise data
[ ] Tier 3: Decision-supporting AI
[ ] Tier 4: Action-capable AI
[ ] Tier 5: High-impact autonomous or regulated AI
```

## Assessment Scope

```text
[Describe what is in scope for this control assessment]
```

---

# 2. Control Assessment Rating Scale

Use the following rating scale for each control area.

| Rating | Meaning |
|---|---|
| Not Applicable | Control does not apply to this use case. |
| Not Started | Control is required but has not been defined. |
| Designed | Control has been designed but not implemented. |
| Implemented | Control has been implemented but not yet validated. |
| Operating | Control is operating and evidence exists. |
| Needs Improvement | Control exists but has a gap, weakness, or exception. |
| Failed | Control is required but ineffective or not operating. |

---

# 3. Pillar 1: AI Inventory and Classification

## Control Questions

| Question | Response |
|---|---|
| Is the AI use case recorded in the AI inventory? | [Yes/No/Partial/Not Applicable] |
| Is the business owner assigned? | [Yes/No/Partial/Not Applicable] |
| Is the technical owner assigned where required? | [Yes/No/Partial/Not Applicable] |
| Is the AI pattern classified? | [Yes/No/Partial/Not Applicable] |
| Is the lifecycle status recorded? | [Yes/No/Partial/Not Applicable] |
| Is the risk tier recorded? | [Yes/No/Partial/Not Applicable] |
| Are required controls linked to the risk tier? | [Yes/No/Partial/Not Applicable] |

## Control Rating

```text
[Not Applicable / Not Started / Designed / Implemented / Operating / Needs Improvement / Failed]
```

## Evidence

```text
[Reference inventory record, owner record, classification record, lifecycle status, risk tier, or control mapping]
```

## Gaps

```text
[Describe gaps or weaknesses]
```

## Required Actions

```text
[Describe remediation actions, owner, and due date]
```

---

# 4. Pillar 2: AI Identity and Access Control

## Control Questions

| Question | Response |
|---|---|
| Is the AI identity model defined? | [Yes/No/Partial/Not Applicable] |
| Is delegated authority defined where applicable? | [Yes/No/Partial/Not Applicable] |
| Is AI access approved? | [Yes/No/Partial/Not Applicable] |
| Is AI access least privilege? | [Yes/No/Partial/Not Applicable] |
| Is privileged AI access identified and controlled? | [Yes/No/Partial/Not Applicable] |
| Is AI access reviewed periodically? | [Yes/No/Partial/Not Applicable] |
| Can AI access be revoked? | [Yes/No/Partial/Not Applicable] |
| Is AI-mediated activity attributable where required? | [Yes/No/Partial/Not Applicable] |

## Control Rating

```text
[Not Applicable / Not Started / Designed / Implemented / Operating / Needs Improvement / Failed]
```

## Evidence

```text
[Reference identity model, access approval, delegated authority record, access review, PAM record, revocation record, or logs]
```

## Gaps

```text
[Describe gaps or weaknesses]
```

## Required Actions

```text
[Describe remediation actions, owner, and due date]
```

---

# 5. Pillar 3: Data Boundary Control

## Control Questions

| Question | Response |
|---|---|
| Are AI data sources mapped? | [Yes/No/Partial/Not Applicable] |
| Is data classification documented? | [Yes/No/Partial/Not Applicable] |
| Are retrieval boundaries defined where applicable? | [Yes/No/Partial/Not Applicable] |
| Is sensitive data exposure approved? | [Yes/No/Partial/Not Applicable] |
| Are training and reuse restrictions defined? | [Yes/No/Partial/Not Applicable] |
| Are retention requirements defined? | [Yes/No/Partial/Not Applicable] |
| Are output sensitivity controls defined? | [Yes/No/Partial/Not Applicable] |
| Is AI data access logged where required? | [Yes/No/Partial/Not Applicable] |

## Control Rating

```text
[Not Applicable / Not Started / Designed / Implemented / Operating / Needs Improvement / Failed]
```

## Evidence

```text
[Reference data source map, classification record, data owner approval, retrieval configuration, retention rule, training/reuse restriction, or data access logs]
```

## Gaps

```text
[Describe gaps or weaknesses]
```

## Required Actions

```text
[Describe remediation actions, owner, and due date]
```

---

# 6. Pillar 4: Prompt and Input Control

## Control Questions

| Question | Response |
|---|---|
| Are allowed inputs defined? | [Yes/No/Partial/Not Applicable] |
| Are prohibited inputs defined? | [Yes/No/Partial/Not Applicable] |
| Are sensitive data input restrictions defined? | [Yes/No/Partial/Not Applicable] |
| Are system prompts protected where applicable? | [Yes/No/Partial/Not Applicable] |
| Is prompt injection risk assessed? | [Yes/No/Partial/Not Applicable] |
| Are prompt injection controls defined where required? | [Yes/No/Partial/Not Applicable] |
| Is context isolation defined where required? | [Yes/No/Partial/Not Applicable] |
| Are prompt and input logs defined where required? | [Yes/No/Partial/Not Applicable] |
| Are prompt changes controlled where required? | [Yes/No/Partial/Not Applicable] |

## Control Rating

```text
[Not Applicable / Not Started / Designed / Implemented / Operating / Needs Improvement / Failed]
```

## Evidence

```text
[Reference input policy, prohibited input rules, prompt version, prompt change record, prompt injection test, context isolation design, or input logs]
```

## Gaps

```text
[Describe gaps or weaknesses]
```

## Required Actions

```text
[Describe remediation actions, owner, and due date]
```

---

# 7. Pillar 5: Output and Decision Control

## Control Questions

| Question | Response |
|---|---|
| Are AI output types classified? | [Yes/No/Partial/Not Applicable] |
| Is decision impact classified? | [Yes/No/Partial/Not Applicable] |
| Are validation rules defined for high-impact outputs? | [Yes/No/Partial/Not Applicable] |
| Is recommendation separated from final decision where required? | [Yes/No/Partial/Not Applicable] |
| Is human review defined where required? | [Yes/No/Partial/Not Applicable] |
| Are customer-facing outputs controlled where applicable? | [Yes/No/Partial/Not Applicable] |
| Are generated records controlled where applicable? | [Yes/No/Partial/Not Applicable] |
| Is decision evidence captured where required? | [Yes/No/Partial/Not Applicable] |
| Is a correction or override path defined? | [Yes/No/Partial/Not Applicable] |

## Control Rating

```text
[Not Applicable / Not Started / Designed / Implemented / Operating / Needs Improvement / Failed]
```

## Evidence

```text
[Reference output classification, validation rule, review record, approval record, decision evidence, generated record metadata, or correction record]
```

## Gaps

```text
[Describe gaps or weaknesses]
```

## Required Actions

```text
[Describe remediation actions, owner, and due date]
```

---

# 8. Pillar 6: Tool and Action Control

## Control Questions

| Question | Response |
|---|---|
| Are AI-accessible tools inventoried? | [Yes/No/Partial/Not Applicable] |
| Are AI actions classified by risk? | [Yes/No/Partial/Not Applicable] |
| Is tool access approved? | [Yes/No/Partial/Not Applicable] |
| Is tool access least privilege? | [Yes/No/Partial/Not Applicable] |
| Are action boundaries defined? | [Yes/No/Partial/Not Applicable] |
| Are approval gates defined for high-risk actions? | [Yes/No/Partial/Not Applicable] |
| Are autonomous execution limits defined? | [Yes/No/Partial/Not Applicable] |
| Are tool calls and actions logged? | [Yes/No/Partial/Not Applicable] |
| Is a kill switch or revocation path defined? | [Yes/No/Partial/Not Applicable] |
| Is rollback or compensation assessed? | [Yes/No/Partial/Not Applicable] |

## Control Rating

```text
[Not Applicable / Not Started / Designed / Implemented / Operating / Needs Improvement / Failed]
```

## Evidence

```text
[Reference tool inventory, action classification, tool approval, approval gate, action boundary, tool log, kill switch design, or rollback plan]
```

## Gaps

```text
[Describe gaps or weaknesses]
```

## Required Actions

```text
[Describe remediation actions, owner, and due date]
```

---

# 9. Pillar 7: Human Accountability Model

## Control Questions

| Question | Response |
|---|---|
| Is the business owner assigned? | [Yes/No/Partial/Not Applicable] |
| Is the technical owner assigned where required? | [Yes/No/Partial/Not Applicable] |
| Is the decision owner assigned where required? | [Yes/No/Partial/Not Applicable] |
| Is the human review model defined? | [Yes/No/Partial/Not Applicable] |
| Are approval responsibilities defined? | [Yes/No/Partial/Not Applicable] |
| Are escalation paths defined? | [Yes/No/Partial/Not Applicable] |
| Are override rights defined? | [Yes/No/Partial/Not Applicable] |
| Is exception ownership defined? | [Yes/No/Partial/Not Applicable] |
| Is accountability evidence retained where required? | [Yes/No/Partial/Not Applicable] |

## Control Rating

```text
[Not Applicable / Not Started / Designed / Implemented / Operating / Needs Improvement / Failed]
```

## Evidence

```text
[Reference owner records, decision owner mapping, approval records, escalation path, override records, exception records, or RACI]
```

## Gaps

```text
[Describe gaps or weaknesses]
```

## Required Actions

```text
[Describe remediation actions, owner, and due date]
```

---

# 10. Pillar 8: AI Assurance and Testing

## Control Questions

| Question | Response |
|---|---|
| Are assurance requirements defined by risk tier? | [Yes/No/Partial/Not Applicable] |
| Has pre-deployment testing been completed where required? | [Yes/No/Partial/Not Applicable] |
| Has prompt injection testing been completed where required? | [Yes/No/Partial/Not Applicable] |
| Has data leakage testing been completed where required? | [Yes/No/Partial/Not Applicable] |
| Has output validation testing been completed where required? | [Yes/No/Partial/Not Applicable] |
| Has tool/action testing been completed where required? | [Yes/No/Partial/Not Applicable] |
| Has logging and evidence testing been completed? | [Yes/No/Partial/Not Applicable] |
| Has containment testing been completed where required? | [Yes/No/Partial/Not Applicable] |
| Are findings tracked to closure or risk acceptance? | [Yes/No/Partial/Not Applicable] |

## Control Rating

```text
[Not Applicable / Not Started / Designed / Implemented / Operating / Needs Improvement / Failed]
```

## Evidence

```text
[Reference test plan, test results, findings, remediation records, retest records, assurance sign-off, or risk acceptance]
```

## Gaps

```text
[Describe gaps or weaknesses]
```

## Required Actions

```text
[Describe remediation actions, owner, and due date]
```

---

# 11. Pillar 9: Monitoring, Logging, and Evidence

## Control Questions

| Question | Response |
|---|---|
| Are logging requirements defined by risk tier? | [Yes/No/Partial/Not Applicable] |
| Are AI interactions logged where required? | [Yes/No/Partial/Not Applicable] |
| Is AI data access logged where required? | [Yes/No/Partial/Not Applicable] |
| Are tool calls and actions logged where required? | [Yes/No/Partial/Not Applicable] |
| Are approvals and exceptions logged? | [Yes/No/Partial/Not Applicable] |
| Are policy violations detectable? | [Yes/No/Partial/Not Applicable] |
| Are logs protected? | [Yes/No/Partial/Not Applicable] |
| Are retention requirements defined? | [Yes/No/Partial/Not Applicable] |
| Can AI activity be reconstructed where required? | [Yes/No/Partial/Not Applicable] |
| Is incident evidence preservation defined? | [Yes/No/Partial/Not Applicable] |

## Control Rating

```text
[Not Applicable / Not Started / Designed / Implemented / Operating / Needs Improvement / Failed]
```

## Evidence

```text
[Reference logging standard, AI event taxonomy, log records, SIEM integration, retention schedule, evidence package, or reconstruction test]
```

## Gaps

```text
[Describe gaps or weaknesses]
```

## Required Actions

```text
[Describe remediation actions, owner, and due date]
```

---

# 12. Pillar 10: Incident Containment and Recovery

## Control Questions

| Question | Response |
|---|---|
| Are AI incident scenarios defined? | [Yes/No/Partial/Not Applicable] |
| Is AI incident severity defined? | [Yes/No/Partial/Not Applicable] |
| Is an incident owner defined? | [Yes/No/Partial/Not Applicable] |
| Is access revocation defined? | [Yes/No/Partial/Not Applicable] |
| Is agent or tool kill switch defined where required? | [Yes/No/Partial/Not Applicable] |
| Is evidence preservation defined? | [Yes/No/Partial/Not Applicable] |
| Are escalation paths defined? | [Yes/No/Partial/Not Applicable] |
| Are recovery or correction actions defined? | [Yes/No/Partial/Not Applicable] |
| Is vendor AI incident handling defined where applicable? | [Yes/No/Partial/Not Applicable] |
| Are post-incident review and improvement actions defined? | [Yes/No/Partial/Not Applicable] |

## Control Rating

```text
[Not Applicable / Not Started / Designed / Implemented / Operating / Needs Improvement / Failed]
```

## Evidence

```text
[Reference incident playbook, severity model, revocation path, kill switch design, evidence checklist, recovery plan, vendor escalation process, or post-incident review record]
```

## Gaps

```text
[Describe gaps or weaknesses]
```

## Required Actions

```text
[Describe remediation actions, owner, and due date]
```

---

# 13. Overall Control Readiness

## Overall Rating

Select one:

```text
[ ] Ready for approved use
[ ] Ready with minor conditions
[ ] Ready for pilot only
[ ] Not ready until remediation is complete
[ ] Requires exception approval
[ ] Rejected
[ ] Deferred
```

## Summary of Key Gaps

| Gap ID | Pillar | Gap Description | Severity | Owner | Due Date |
|---|---|---|---|---|---|
| [Gap ID] | [Pillar] | [Description] | [Low/Medium/High/Critical] | [Owner] | [Date] |

## Required Conditions Before Approval

```text
[List mandatory conditions before approval, production use, scaling, or continued operation]
```

## Residual Risk

```text
[Describe remaining risk after controls and remediation]
```

---

# 14. Control Exceptions

## Are Exceptions Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Exception Summary

| Requirement | Exception Needed | Business Justification | Compensating Control | Expiry Date | Owner |
|---|---|---|---|---|---|
| [Requirement] | [Yes/No] | [Reason] | [Control] | [Date] | [Owner] |

---

# 15. Approval

## Business Owner Decision

```text
Name:
Decision:
Date:
Notes:
```

## Control Owner / Architecture Decision

```text
Name or forum:
Decision:
Date:
Notes:
```

## Risk / Governance Decision

```text
Name or forum:
Decision:
Date:
Notes:
```

---

# 16. Summary

```text
Use case:
Risk tier:
Overall control readiness:
Highest control gaps:
Required remediation:
Exceptions required:
Residual risk:
Approval decision:
Next review date:
```