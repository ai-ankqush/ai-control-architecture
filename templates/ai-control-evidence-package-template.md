# AI Control Evidence Package Template

This template is used to assemble evidence for an AI use case, AI control review, assurance assessment, audit, governance decision, incident investigation, or regulatory response.

AI control is not complete unless evidence exists.

The purpose of this template is to create a structured evidence package showing what AI is, who owns it, what risk tier applies, what controls are required, what controls operate, what testing was performed, what exceptions exist, and how incidents can be reconstructed.

---

# 1. Evidence Package Information

## Evidence Package Name

```text
[Enter evidence package name]
```

## Evidence Package ID

```text
[Enter evidence package ID]
```

## Date Created

```text
[Enter date]
```

## Date Last Updated

```text
[Enter date]
```

## Prepared By

```text
Name:
Function:
Email:
```

## Evidence Owner

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

## Package Purpose

Select all that apply:

```text
[ ] AI governance review
[ ] Architecture review
[ ] Security review
[ ] Privacy/legal review
[ ] Vendor review
[ ] Assurance testing
[ ] Control assessment
[ ] Audit
[ ] Incident investigation
[ ] Regulatory response
[ ] Risk acceptance
[ ] Exception review
[ ] Periodic review
[ ] Other
```

---

# 2. AI Use Case Summary

## AI Use Case Name

```text
[Enter AI use case name]
```

## Related AI Inventory Record

```text
[Enter inventory record reference or link]
```

## Short Description

```text
[Describe the AI use case]
```

## AI Pattern

Select all that apply:

```text
[ ] Copilot
[ ] Internal LLM application
[ ] RAG system
[ ] AI-enabled SaaS
[ ] Embedded vendor AI
[ ] Agent
[ ] AI-enabled workflow automation
[ ] Customer-facing AI
[ ] Employee-facing AI
[ ] Developer AI tool
[ ] Security operations AI
[ ] Decision-supporting AI
[ ] Action-capable AI
[ ] Other
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

---

# 3. Evidence Package Scope

## Scope Included

```text
[Describe what is included in this evidence package]
```

## Scope Excluded

```text
[Describe what is excluded from this evidence package]
```

## Evidence Time Period

```text
Start date:
End date:
```

## Systems in Scope

```text
[List systems, applications, models, vendors, tools, APIs, workflows, repositories, and platforms in scope]
```

## Data Sources in Scope

```text
[List data sources in scope]
```

---

# 4. Evidence Index

Use this section as the master index for all evidence included in the package.

| Evidence ID | Evidence Type | Description | Owner | Location / Link | Status |
|---|---|---|---|---|---|
| EVID-001 | [Type] | [Description] | [Owner] | [Location] | [Available/Missing/Partial] |

---

# 5. Inventory and Classification Evidence

## Required Evidence

Select all that apply:

```text
[ ] AI inventory record
[ ] AI use case intake record
[ ] Business owner record
[ ] Technical owner record
[ ] AI pattern classification
[ ] Lifecycle status
[ ] Risk tier record
[ ] Business process mapping
[ ] Embedded vendor AI identification
[ ] Shadow AI discovery record
```

## Evidence Table

| Evidence | Required? | Available? | Location / Link | Notes |
|---|---|---|---|---|
| AI inventory record | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Use case intake | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Risk tier record | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Lifecycle status | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |

## Inventory Evidence Notes

```text
[Describe inventory evidence gaps, assumptions, or review findings]
```

---

# 6. Risk Assessment Evidence

## Required Evidence

Select all that apply:

```text
[ ] AI risk assessment
[ ] AI risk tiering record
[ ] Highest risk drivers
[ ] Data risk assessment
[ ] Decision impact assessment
[ ] Output risk assessment
[ ] Tool/action risk assessment
[ ] Autonomy risk assessment
[ ] Vendor risk assessment
[ ] Recoverability assessment
[ ] Risk acceptance record
```

## Evidence Table

| Evidence | Required? | Available? | Location / Link | Notes |
|---|---|---|---|---|
| Risk assessment | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Risk tiering record | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Risk acceptance | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |

## Risk Evidence Notes

```text
[Describe risk evidence gaps, assumptions, or review findings]
```

---

# 7. Architecture Decision Evidence

## Required Evidence

Select all that apply:

```text
[ ] Architecture decision record
[ ] Architecture review notes
[ ] Design diagrams
[ ] Control design decisions
[ ] Identity model decision
[ ] Data boundary decision
[ ] Prompt/input decision
[ ] Output/decision decision
[ ] Tool/action decision
[ ] Logging/evidence decision
[ ] Incident containment decision
[ ] Approval conditions
```

## Evidence Table

| Evidence | Required? | Available? | Location / Link | Notes |
|---|---|---|---|---|
| Architecture decision record | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Design diagrams | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Approval conditions | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |

## Architecture Evidence Notes

```text
[Describe architecture evidence gaps, assumptions, or review findings]
```

---

# 8. Identity and Access Evidence

## Required Evidence

Select all that apply:

```text
[ ] AI identity model
[ ] AI actor record
[ ] Service account record
[ ] Agent identity record
[ ] Delegated authority record
[ ] Access approval
[ ] Least privilege review
[ ] Privileged access review
[ ] Access review record
[ ] Access revocation test
[ ] Attribution logs
[ ] Vendor identity evidence
```

## Evidence Table

| Evidence | Required? | Available? | Location / Link | Notes |
|---|---|---|---|---|
| Identity model | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Access approval | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Access review | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Revocation evidence | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |

## Identity Evidence Notes

```text
[Describe identity evidence gaps, assumptions, or review findings]
```

---

# 9. Data Boundary Evidence

## Required Evidence

Select all that apply:

```text
[ ] Data source map
[ ] Data owner approval
[ ] Data classification record
[ ] Approved data boundary
[ ] Retrieval boundary design
[ ] Retrieval boundary test result
[ ] Sensitive data restriction
[ ] Retention rule
[ ] Training/reuse restriction
[ ] Vendor data processing record
[ ] Cross-boundary transfer record
[ ] Data leakage test result
```

## Evidence Table

| Evidence | Required? | Available? | Location / Link | Notes |
|---|---|---|---|---|
| Data source map | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Data owner approval | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Retrieval boundary evidence | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Data leakage test | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |

## Data Evidence Notes

```text
[Describe data evidence gaps, assumptions, or review findings]
```

---

# 10. Prompt and Input Evidence

## Required Evidence

Select all that apply:

```text
[ ] Prompt/input control record
[ ] Allowed input definition
[ ] Prohibited input definition
[ ] Sensitive input handling rule
[ ] System prompt owner
[ ] System prompt version
[ ] System prompt change record
[ ] Prompt injection risk assessment
[ ] Prompt injection test result
[ ] Context isolation design
[ ] Input policy violation logs
```

## Evidence Table

| Evidence | Required? | Available? | Location / Link | Notes |
|---|---|---|---|---|
| Prompt/input control record | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| System prompt version | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Prompt injection testing | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Context isolation evidence | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |

## Prompt/Input Evidence Notes

```text
[Describe prompt/input evidence gaps, assumptions, or review findings]
```

---

# 11. Output and Decision Evidence

## Required Evidence

Select all that apply:

```text
[ ] Output classification
[ ] Decision impact classification
[ ] Output validation rule
[ ] Output validation record
[ ] Reviewer record
[ ] Approval record
[ ] Rejection record
[ ] Modification record
[ ] Override record
[ ] Decision owner record
[ ] Final decision evidence
[ ] Generated record metadata
[ ] Customer-facing output review
[ ] Correction record
[ ] Output quality metrics
```

## Evidence Table

| Evidence | Required? | Available? | Location / Link | Notes |
|---|---|---|---|---|
| Output classification | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Validation evidence | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Decision evidence | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Correction evidence | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |

## Output/Decision Evidence Notes

```text
[Describe output and decision evidence gaps, assumptions, or review findings]
```

---

# 12. Tool and Action Evidence

## Required Evidence

Select all that apply:

```text
[ ] Tool inventory
[ ] Tool owner record
[ ] Tool access approval
[ ] Action classification
[ ] Action boundary configuration
[ ] Approval gate configuration
[ ] Approval record
[ ] Tool call logs
[ ] Action logs
[ ] Blocked action logs
[ ] Abnormal tool use alerts
[ ] Kill switch design
[ ] Kill switch test record
[ ] Rollback plan
[ ] Rollback test record
```

## Evidence Table

| Evidence | Required? | Available? | Location / Link | Notes |
|---|---|---|---|---|
| Tool inventory | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Action classification | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Tool/action logs | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Kill switch test | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Rollback test | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |

## Tool/Action Evidence Notes

```text
[Describe tool/action evidence gaps, assumptions, or review findings]
```

---

# 13. Human Accountability Evidence

## Required Evidence

Select all that apply:

```text
[ ] Business owner record
[ ] Technical owner record
[ ] Data owner approval
[ ] Decision owner mapping
[ ] Human review model
[ ] Approval authority matrix
[ ] Escalation path
[ ] Override rights
[ ] Exception owner record
[ ] Risk acceptance owner record
[ ] Incident owner record
[ ] RACI record
[ ] Accountability approval record
```

## Evidence Table

| Evidence | Required? | Available? | Location / Link | Notes |
|---|---|---|---|---|
| Business owner record | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Decision owner mapping | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| RACI record | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Risk acceptance owner | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |

## Accountability Evidence Notes

```text
[Describe accountability evidence gaps, assumptions, or review findings]
```

---

# 14. Assurance and Testing Evidence

## Required Evidence

Select all that apply:

```text
[ ] Assurance test plan
[ ] Test cases
[ ] Test results
[ ] Prompt injection test result
[ ] Data leakage test result
[ ] Retrieval boundary test result
[ ] Output validation test result
[ ] Tool/action test result
[ ] Logging completeness test result
[ ] Evidence reconstruction test result
[ ] Incident containment test result
[ ] Vendor assurance review
[ ] Findings register
[ ] Remediation evidence
[ ] Retest evidence
[ ] Assurance sign-off
```

## Evidence Table

| Evidence | Required? | Available? | Location / Link | Notes |
|---|---|---|---|---|
| Assurance test plan | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Test results | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Findings register | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Remediation evidence | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |

## Assurance Evidence Notes

```text
[Describe assurance evidence gaps, assumptions, or review findings]
```

---

# 15. Monitoring and Logging Evidence

## Required Evidence

Select all that apply:

```text
[ ] AI logging requirements
[ ] AI event taxonomy
[ ] Logging configuration
[ ] Prompt/input logs or metadata
[ ] Retrieval logs
[ ] Output logs or metadata
[ ] Decision evidence logs
[ ] Tool call logs
[ ] Action logs
[ ] Approval logs
[ ] Exception logs
[ ] Policy violation alerts
[ ] Monitoring rules
[ ] SIEM/SOC integration record
[ ] Retention schedule
[ ] Log access record
[ ] Evidence reconstruction test
```

## Evidence Table

| Evidence | Required? | Available? | Location / Link | Notes |
|---|---|---|---|---|
| Logging requirements | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| AI event taxonomy | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Monitoring rules | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Evidence reconstruction test | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |

## Monitoring Evidence Notes

```text
[Describe monitoring/logging evidence gaps, assumptions, or review findings]
```

---

# 16. Incident Containment and Recovery Evidence

## Required Evidence

Select all that apply:

```text
[ ] AI incident taxonomy
[ ] Incident severity model
[ ] Incident owner record
[ ] Escalation path
[ ] Access revocation path
[ ] Agent/tool kill switch design
[ ] Kill switch test record
[ ] Evidence preservation checklist
[ ] Recovery plan
[ ] Rollback plan
[ ] Rollback test record
[ ] Vendor incident process
[ ] Incident tabletop result
[ ] Restart criteria
[ ] Post-incident review record
```

## Evidence Table

| Evidence | Required? | Available? | Location / Link | Notes |
|---|---|---|---|---|
| Incident taxonomy | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Kill switch evidence | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Evidence preservation checklist | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Recovery plan | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |

## Incident Evidence Notes

```text
[Describe incident containment/recovery evidence gaps, assumptions, or review findings]
```

---

# 17. Vendor Evidence

Complete this section if vendor AI is involved.

## Required Evidence

Select all that apply:

```text
[ ] Vendor AI assessment
[ ] Vendor data processing terms
[ ] Vendor retention terms
[ ] Vendor training/reuse terms
[ ] Vendor subprocessor list
[ ] Vendor security assurance
[ ] Vendor AI documentation
[ ] Vendor admin control evidence
[ ] Vendor logging documentation
[ ] Vendor incident process
[ ] Vendor evidence export capability
[ ] Vendor contract terms
[ ] Vendor remediation evidence
```

## Evidence Table

| Evidence | Required? | Available? | Location / Link | Notes |
|---|---|---|---|---|
| Vendor assessment | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Vendor data terms | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Vendor logging evidence | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |
| Vendor incident process | [Yes/No] | [Yes/No/Partial] | [Location] | [Notes] |

## Vendor Evidence Notes

```text
[Describe vendor evidence gaps, limitations, assumptions, or required follow-up]
```

---

# 18. Exception Evidence

## Exceptions Exist?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Exception Evidence

| Exception ID | Requirement Affected | Evidence Location | Expiry | Status |
|---|---|---|---|---|
| [Exception ID] | [Requirement] | [Location] | [Date] | [Status] |

## Exception Evidence Notes

```text
[Describe open exceptions, expired exceptions, compensating controls, and remediation evidence]
```

---

# 19. Evidence Completeness Assessment

## Evidence Completeness Rating

Select one:

```text
[ ] Complete
[ ] Mostly complete
[ ] Partial
[ ] Significant gaps
[ ] Not sufficient
```

## Missing Evidence

| Missing Evidence | Risk Impact | Owner | Due Date |
|---|---|---|---|
| [Evidence] | [Impact] | [Owner] | [Date] |

## Evidence Quality Notes

```text
[Describe whether evidence is current, reliable, accessible, and sufficient for review]
```

---

# 20. Reconstructability Assessment

## Can AI Activity Be Reconstructed?

```text
[ ] No
[ ] Yes
[ ] Partially
[ ] Unknown
```

## Reconstruction Questions

| Question | Evidence Available? | Evidence Source |
|---|---|---|
| What AI use case was involved? | [Yes/No/Partial] | [Source] |
| Who initiated the interaction? | [Yes/No/Partial] | [Source] |
| What identity did AI use? | [Yes/No/Partial] | [Source] |
| What data was accessed? | [Yes/No/Partial] | [Source] |
| What prompt or input was submitted? | [Yes/No/Partial] | [Source] |
| What context was retrieved? | [Yes/No/Partial] | [Source] |
| What output was generated? | [Yes/No/Partial] | [Source] |
| What tool was called? | [Yes/No/Partial] | [Source] |
| What action was requested? | [Yes/No/Partial] | [Source] |
| Was approval required? | [Yes/No/Partial] | [Source] |
| Was approval obtained? | [Yes/No/Partial] | [Source] |
| What action executed? | [Yes/No/Partial] | [Source] |
| What downstream system was affected? | [Yes/No/Partial] | [Source] |
| What exception occurred? | [Yes/No/Partial] | [Source] |
| What incident response action was taken? | [Yes/No/Partial] | [Source] |

## Reconstructability Notes

```text
[Describe reconstruction gaps and required remediation]
```

---

# 21. Evidence Protection

## Evidence Sensitivity

Select all that apply:

```text
[ ] Public
[ ] Internal
[ ] Confidential
[ ] Restricted
[ ] Regulated
[ ] Personal data
[ ] Customer data
[ ] Employee data
[ ] Legal privileged data
[ ] Security-sensitive data
[ ] Secrets or credentials
[ ] Unknown
```

## Evidence Protection Controls

Select all that apply:

```text
[ ] Access control
[ ] Encryption
[ ] Role-based viewing
[ ] Masking
[ ] Redaction
[ ] Segregation of duties
[ ] Immutable logging
[ ] Tamper detection
[ ] Audit trail
[ ] Retention controls
[ ] Legal hold controls
[ ] Secure export controls
[ ] Other
```

## Authorized Evidence Users

Select all that apply:

```text
[ ] Business owner
[ ] Technical owner
[ ] Control owner
[ ] Auditor
[ ] Incident responder
[ ] Security analyst
[ ] Privacy/legal team
[ ] Assurance team
[ ] Authorized administrator
[ ] Other
```

## Evidence Protection Notes

```text
[Describe how evidence is protected from unauthorized access, tampering, or over-retention]
```

---

# 22. Evidence Retention

## Retention Requirements

| Evidence Type | Retention Period | Owner | Legal Hold Applies? |
|---|---|---|---|
| [Evidence type] | [Period] | [Owner] | [Yes/No/Unknown] |

## Deletion Requirements

```text
[Describe deletion, expiry, privacy rights, and legal hold process]
```

## Retention Notes

```text
[Describe retention constraints, vendor log expiry, or audit requirements]
```

---

# 23. Package Approval

## Evidence Package Prepared By

```text
Name:
Function:
Date:
```

## Evidence Owner Review

```text
Name:
Decision:
Date:
Notes:
```

## Business Owner Review

```text
Name:
Decision:
Date:
Notes:
```

## Security / Architecture Review

```text
Name or forum:
Decision:
Date:
Notes:
```

## Audit / Assurance Review, If Required

```text
Name or forum:
Decision:
Date:
Notes:
Not applicable reason, if any:
```

## Final Evidence Package Decision

Select one:

```text
[ ] Accepted
[ ] Accepted with evidence gaps
[ ] Requires remediation
[ ] Not sufficient
[ ] Deferred
```

---

# 24. Summary

```text
Evidence package:
Use case:
Risk tier:
Package purpose:
Evidence completeness:
Reconstructability:
Missing evidence:
Open exceptions:
Open findings:
Evidence repository:
Retention:
Approval status:
Next evidence review date:
```