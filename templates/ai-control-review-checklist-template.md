# AI Control Review Checklist Template

This checklist is used to perform a structured review of an AI use case before approval, pilot, production deployment, major change, or continued operation.

It is designed as a practical checklist for architecture, security, risk, data governance, privacy, legal, vendor risk, audit, and business owners.

Use this checklist when a full control assessment is not required, or as a lightweight review before deeper assessment.

---

# 1. Review Information

## AI Use Case Name

```text
[Enter AI use case name]
```

## Review Date

```text
[Enter date]
```

## Review Type

Select one:

```text
[ ] Initial review
[ ] Pilot review
[ ] Production readiness review
[ ] Major change review
[ ] Vendor AI feature review
[ ] Agentic AI review
[ ] Exception review
[ ] Post-incident review
[ ] Periodic review
```

## Reviewer

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
[ ] Unknown
```

---

# 2. Intake and Inventory Checklist

| Check | Response | Notes |
|---|---|---|
| AI use case is recorded in inventory. | [Yes/No/Partial/NA] | [Notes] |
| Business owner is assigned. | [Yes/No/Partial/NA] | [Notes] |
| Technical owner is assigned where required. | [Yes/No/Partial/NA] | [Notes] |
| AI pattern is classified. | [Yes/No/Partial/NA] | [Notes] |
| Lifecycle status is current. | [Yes/No/Partial/NA] | [Notes] |
| Risk tier is assigned. | [Yes/No/Partial/NA] | [Notes] |
| Required controls are mapped to risk tier. | [Yes/No/Partial/NA] | [Notes] |

## Inventory Review Notes

```text
[Document inventory and classification findings]
```

---

# 3. Identity and Access Checklist

| Check | Response | Notes |
|---|---|---|
| AI identity model is defined. | [Yes/No/Partial/NA] | [Notes] |
| AI actor or service identity is documented where applicable. | [Yes/No/Partial/NA] | [Notes] |
| Delegated authority is documented where applicable. | [Yes/No/Partial/NA] | [Notes] |
| AI access is approved. | [Yes/No/Partial/NA] | [Notes] |
| AI access is least privilege. | [Yes/No/Partial/NA] | [Notes] |
| Privileged AI access is identified and controlled. | [Yes/No/Partial/NA] | [Notes] |
| AI access review frequency is defined. | [Yes/No/Partial/NA] | [Notes] |
| AI access can be revoked. | [Yes/No/Partial/NA] | [Notes] |
| AI-mediated activity can be attributed where required. | [Yes/No/Partial/NA] | [Notes] |

## Identity and Access Review Notes

```text
[Document identity, access, delegation, privilege, and revocation findings]
```

---

# 4. Data Boundary Checklist

| Check | Response | Notes |
|---|---|---|
| Data sources are mapped. | [Yes/No/Partial/NA] | [Notes] |
| Data owners are identified. | [Yes/No/Partial/NA] | [Notes] |
| Data classification is documented. | [Yes/No/Partial/NA] | [Notes] |
| Sensitive data exposure is approved. | [Yes/No/Partial/NA] | [Notes] |
| Retrieval boundaries are defined where applicable. | [Yes/No/Partial/NA] | [Notes] |
| Training and reuse restrictions are defined. | [Yes/No/Partial/NA] | [Notes] |
| Retention requirements are defined. | [Yes/No/Partial/NA] | [Notes] |
| Vendor processing is reviewed where applicable. | [Yes/No/Partial/NA] | [Notes] |
| Output sensitivity is considered. | [Yes/No/Partial/NA] | [Notes] |

## Data Boundary Review Notes

```text
[Document data access, retrieval, retention, reuse, and vendor processing findings]
```

---

# 5. Prompt and Input Checklist

| Check | Response | Notes |
|---|---|---|
| Allowed inputs are defined. | [Yes/No/Partial/NA] | [Notes] |
| Prohibited inputs are defined. | [Yes/No/Partial/NA] | [Notes] |
| Sensitive input restrictions are defined. | [Yes/No/Partial/NA] | [Notes] |
| External or untrusted inputs are identified. | [Yes/No/Partial/NA] | [Notes] |
| Prompt injection risk is assessed. | [Yes/No/Partial/NA] | [Notes] |
| Prompt injection testing is required where applicable. | [Yes/No/Partial/NA] | [Notes] |
| System prompts are protected where applicable. | [Yes/No/Partial/NA] | [Notes] |
| Prompt changes are versioned and reviewed where applicable. | [Yes/No/Partial/NA] | [Notes] |
| Context isolation is defined where required. | [Yes/No/Partial/NA] | [Notes] |

## Prompt and Input Review Notes

```text
[Document prompt, input, system prompt, context, and prompt injection findings]
```

---

# 6. Output and Decision Checklist

| Check | Response | Notes |
|---|---|---|
| Output types are classified. | [Yes/No/Partial/NA] | [Notes] |
| Decision impact is classified. | [Yes/No/Partial/NA] | [Notes] |
| Validation rules are defined for high-impact outputs. | [Yes/No/Partial/NA] | [Notes] |
| AI recommendation is separated from final decision where required. | [Yes/No/Partial/NA] | [Notes] |
| Human review is defined where required. | [Yes/No/Partial/NA] | [Notes] |
| Customer-facing output controls are defined where applicable. | [Yes/No/Partial/NA] | [Notes] |
| Generated record handling is defined where applicable. | [Yes/No/Partial/NA] | [Notes] |
| Correction or override path is defined. | [Yes/No/Partial/NA] | [Notes] |
| Decision evidence is retained where required. | [Yes/No/Partial/NA] | [Notes] |

## Output and Decision Review Notes

```text
[Document output validation, decision, review, generated record, and downstream use findings]
```

---

# 7. Tool and Action Checklist

| Check | Response | Notes |
|---|---|---|
| AI-accessible tools are inventoried. | [Yes/No/Partial/NA] | [Notes] |
| Tool owners are identified. | [Yes/No/Partial/NA] | [Notes] |
| AI actions are classified by risk. | [Yes/No/Partial/NA] | [Notes] |
| Tool access is approved. | [Yes/No/Partial/NA] | [Notes] |
| Tool access is least privilege. | [Yes/No/Partial/NA] | [Notes] |
| Action boundaries are defined. | [Yes/No/Partial/NA] | [Notes] |
| Approval gates are defined for high-risk actions. | [Yes/No/Partial/NA] | [Notes] |
| Blast-radius limits are defined where required. | [Yes/No/Partial/NA] | [Notes] |
| Tool calls and actions are logged. | [Yes/No/Partial/NA] | [Notes] |
| Kill switch or revocation path is defined. | [Yes/No/Partial/NA] | [Notes] |
| Rollback or compensation is assessed. | [Yes/No/Partial/NA] | [Notes] |

## Tool and Action Review Notes

```text
[Document tool, action, approval, boundary, logging, kill switch, and rollback findings]
```

---

# 8. Human Accountability Checklist

| Check | Response | Notes |
|---|---|---|
| Business owner is accountable for outcome. | [Yes/No/Partial/NA] | [Notes] |
| Technical owner is accountable for implementation. | [Yes/No/Partial/NA] | [Notes] |
| Data owner is identified where required. | [Yes/No/Partial/NA] | [Notes] |
| Decision owner is assigned where AI influences decisions. | [Yes/No/Partial/NA] | [Notes] |
| Human review model is defined. | [Yes/No/Partial/NA] | [Notes] |
| Approval responsibilities are defined. | [Yes/No/Partial/NA] | [Notes] |
| Escalation path is defined. | [Yes/No/Partial/NA] | [Notes] |
| Override rights are defined. | [Yes/No/Partial/NA] | [Notes] |
| Risk acceptance owner is identified where required. | [Yes/No/Partial/NA] | [Notes] |

## Human Accountability Review Notes

```text
[Document ownership, decision authority, approval, escalation, override, and risk acceptance findings]
```

---

# 9. Assurance and Testing Checklist

| Check | Response | Notes |
|---|---|---|
| Assurance requirements are defined by risk tier. | [Yes/No/Partial/NA] | [Notes] |
| Pre-deployment testing is required where applicable. | [Yes/No/Partial/NA] | [Notes] |
| Prompt injection testing is required where applicable. | [Yes/No/Partial/NA] | [Notes] |
| Data leakage testing is required where applicable. | [Yes/No/Partial/NA] | [Notes] |
| Retrieval boundary testing is required where applicable. | [Yes/No/Partial/NA] | [Notes] |
| Output validation testing is required where applicable. | [Yes/No/Partial/NA] | [Notes] |
| Tool/action testing is required where applicable. | [Yes/No/Partial/NA] | [Notes] |
| Logging completeness testing is required where applicable. | [Yes/No/Partial/NA] | [Notes] |
| Kill switch testing is required where applicable. | [Yes/No/Partial/NA] | [Notes] |
| Regression testing triggers are defined. | [Yes/No/Partial/NA] | [Notes] |

## Assurance Review Notes

```text
[Document testing, validation, assurance, finding, and regression requirements]
```

---

# 10. Monitoring, Logging, and Evidence Checklist

| Check | Response | Notes |
|---|---|---|
| Logging requirements are defined by risk tier. | [Yes/No/Partial/NA] | [Notes] |
| Prompt/input logging approach is defined. | [Yes/No/Partial/NA] | [Notes] |
| Output logging approach is defined. | [Yes/No/Partial/NA] | [Notes] |
| Data access logging is defined where required. | [Yes/No/Partial/NA] | [Notes] |
| Retrieval logging is defined where required. | [Yes/No/Partial/NA] | [Notes] |
| Tool/action logging is defined where required. | [Yes/No/Partial/NA] | [Notes] |
| Approval and exception logging is defined. | [Yes/No/Partial/NA] | [Notes] |
| Evidence retention is defined. | [Yes/No/Partial/NA] | [Notes] |
| Logs are protected. | [Yes/No/Partial/NA] | [Notes] |
| AI activity is reconstructable where required. | [Yes/No/Partial/NA] | [Notes] |

## Monitoring and Evidence Review Notes

```text
[Document logging, monitoring, evidence, retention, reconstruction, and audit findings]
```

---

# 11. Incident Containment and Recovery Checklist

| Check | Response | Notes |
|---|---|---|
| AI incident scenarios are identified. | [Yes/No/Partial/NA] | [Notes] |
| AI incident severity model applies. | [Yes/No/Partial/NA] | [Notes] |
| Incident owner is identified. | [Yes/No/Partial/NA] | [Notes] |
| Access revocation path is defined. | [Yes/No/Partial/NA] | [Notes] |
| Agent or tool kill switch is defined where required. | [Yes/No/Partial/NA] | [Notes] |
| Evidence preservation path is defined. | [Yes/No/Partial/NA] | [Notes] |
| Recovery or correction process is defined. | [Yes/No/Partial/NA] | [Notes] |
| Vendor incident path is defined where applicable. | [Yes/No/Partial/NA] | [Notes] |
| Post-incident review path is defined. | [Yes/No/Partial/NA] | [Notes] |

## Incident Review Notes

```text
[Document incident, containment, recovery, vendor escalation, and evidence preservation findings]
```

---

# 12. Vendor AI Checklist

Complete this section if a vendor AI capability is involved.

| Check | Response | Notes |
|---|---|---|
| Vendor AI feature is identified. | [Yes/No/Partial/NA] | [Notes] |
| Vendor AI feature enablement status is known. | [Yes/No/Partial/NA] | [Notes] |
| Vendor data processing is understood. | [Yes/No/Partial/NA] | [Notes] |
| Vendor retention is understood. | [Yes/No/Partial/NA] | [Notes] |
| Vendor training/reuse settings are understood. | [Yes/No/Partial/NA] | [Notes] |
| Vendor logs are available where required. | [Yes/No/Partial/NA] | [Notes] |
| Vendor incident support is defined. | [Yes/No/Partial/NA] | [Notes] |
| Contractual terms are reviewed where required. | [Yes/No/Partial/NA] | [Notes] |
| Vendor AI risk is recorded. | [Yes/No/Partial/NA] | [Notes] |

## Vendor Review Notes

```text
[Document vendor AI findings, gaps, evidence limits, and required conditions]
```

---

# 13. Review Outcome

## Overall Review Result

Select one:

```text
[ ] Approved
[ ] Approved with conditions
[ ] Approved for pilot only
[ ] Requires remediation before approval
[ ] Requires exception approval
[ ] Requires additional review
[ ] Rejected
[ ] Deferred
```

## Key Findings

| Finding ID | Finding | Severity | Owner | Due Date |
|---|---|---|---|---|
| [Finding ID] | [Finding] | [Low/Medium/High/Critical] | [Owner] | [Date] |

## Required Conditions

```text
[List conditions that must be met before approval, production deployment, scaling, or continued operation]
```

## Exceptions Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Residual Risk

```text
[Describe residual risk after controls and conditions]
```

---

# 14. Approval

## Reviewer Decision

```text
Name:
Decision:
Date:
Notes:
```

## Business Owner Decision

```text
Name:
Decision:
Date:
Notes:
```

## Architecture / Security Decision

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

# 15. Summary

```text
Use case:
Review type:
Risk tier:
Overall result:
Key gaps:
Required conditions:
Exceptions:
Residual risk:
Approval status:
Next review date:
```