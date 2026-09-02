# Copilot Use Case Example

This example shows how the AI Control Architecture can be applied to an enterprise copilot deployment.

This is a filled example, not a blank template.

---

# 1. Use Case Summary

## Use Case Name

```text
Enterprise Productivity Copilot
```

## Description

```text
The enterprise is enabling a productivity copilot for employees to help draft emails, summarize documents, summarize meetings, generate internal content, and answer questions based on user-accessible enterprise information.
```

## Business Purpose

```text
Improve employee productivity by reducing time spent drafting, summarizing, searching, and preparing routine internal communications.
```

## AI Pattern

```text
[ ] Copilot
[ ] Internal LLM application
[ ] RAG system
[x] AI-enabled SaaS
[x] Embedded vendor AI
[ ] Agent
[ ] AI-enabled workflow automation
[ ] Customer-facing AI
[x] Employee-facing AI
[ ] Developer AI tool
[ ] Security operations AI
[ ] Decision-supporting AI
[ ] Action-capable AI
```

## Lifecycle Status

```text
Pilot
```

---

# 2. Ownership

## Business Owner

```text
Name: Head of Digital Workplace
Function: Technology / Workplace Services
Responsibility: Owns business outcome, user adoption, acceptable use, and productivity impact.
```

## Technical Owner

```text
Name: Collaboration Platform Owner
Function: IT Platforms
Responsibility: Owns configuration, tenant settings, integrations, access controls, and support.
```

## Data Owner

```text
Name: Enterprise Data Governance Lead
Function: Data Governance
Responsibility: Reviews enterprise data exposure, classification, retention, and sensitive data handling.
```

## Vendor Owner

```text
Name: SaaS Vendor Manager
Function: Procurement / Vendor Management
Responsibility: Owns vendor relationship, contract review, vendor evidence, and feature enablement tracking.
```

## Incident Contact

```text
Name: Security Operations Lead
Function: Cybersecurity
Responsibility: Coordinates investigation and containment if copilot causes data exposure, unsafe output, or policy violation.
```

---

# 3. Initial Risk Tier

## Assigned Tier

```text
Tier 2: Internal productivity with enterprise data
```

## Tier Rationale

```text
The copilot is employee-facing and primarily supports productivity tasks. It may process internal enterprise data, user-accessible files, emails, meetings, and chats.

It does not directly make decisions, approve actions, modify records, or trigger workflows in this pilot scope.

Risk may increase to Tier 3 if outputs are used for business decisions or official records, and to Tier 4 if tool/action capability is enabled.
```

## Risk Drivers

```text
[x] Internal enterprise data
[x] Confidential data possible
[x] Vendor processing
[x] Broad user population
[x] Output may be reused in internal communications
[ ] Formal decision impact
[ ] Tool/action capability
[ ] Customer-facing exposure
[ ] Regulated decisioning
```

---

# 4. What Can AI See?

The copilot may access or process:

```text
User prompts
User-accessible documents
User-accessible emails
User-accessible chats
Meeting transcripts
Calendar context
Internal files
Generated outputs
Usage metadata
```

## Data Boundary

```text
The copilot should only access information the user is already authorized to access.

The copilot must not be used to process secrets, credentials, private keys, regulated data, legal privileged content, or highly sensitive customer or employee data unless explicitly approved.
```

## Data Classification

```text
Highest expected classification: Internal / Confidential

Restricted or regulated data is not approved for pilot use.
```

## Data Boundary Controls

```text
[x] User permission inheritance reviewed
[x] Sensitive data guidance provided
[x] Prohibited input types defined
[x] Vendor processing reviewed
[x] Retention settings reviewed
[ ] DLP integration enabled
[ ] Sensitive prompt blocking enabled
[ ] Formal data leakage testing completed
```

---

# 5. What Can AI Decide?

The copilot should not make formal decisions.

It may influence:

```text
Employee drafting
Employee summaries
Internal analysis
Meeting follow-ups
Email wording
Document preparation
Informal user judgment
```

## Decision Boundary

```text
Copilot output is advisory and draft-only.

Users remain responsible for reviewing, validating, editing, and approving any output before relying on it or sharing it.
```

## Decision Controls

```text
[x] Output labeled as AI-generated or draft where possible
[x] User guidance states that outputs must be reviewed
[x] High-impact decision use is prohibited during pilot
[x] Customer commitments are prohibited
[x] Legal, HR, finance, security, and regulated decisions require separate review
```

---

# 6. What Can AI Do?

In this pilot scope, the copilot can:

```text
Draft text
Summarize content
Answer questions
Generate internal content
Assist with meeting summaries
```

The copilot must not:

```text
Approve decisions
Send external communications without user review
Modify enterprise records automatically
Grant or revoke access
Trigger production workflows
Execute code
Perform financial transactions
Perform security enforcement actions
```

## Tool and Action Capability

```text
Current status: No autonomous action capability approved.

If plugins, extensions, workflow actions, or API tool use are enabled later, the use case must be reassessed as Tier 4.
```

---

# 7. Prompt and Input Controls

## Allowed Inputs

```text
General drafting requests
Internal meeting notes
Internal non-sensitive documents
Public information
Non-sensitive internal summaries
Routine productivity requests
```

## Prohibited Inputs

```text
Passwords
API keys
Private keys
Secrets
Access tokens
Customer regulated data
Employee sensitive data
Legal privileged content
Payment card data
Health data
Production credentials
Confidential merger/acquisition information
Material non-public financial information
```

## Prompt Injection Risk

```text
Moderate
```

## Prompt/Input Controls

```text
[x] Acceptable use guidance published
[x] Prohibited inputs defined
[x] User training planned
[x] Sensitive data warning included in guidance
[ ] Automated prompt blocking implemented
[ ] Prompt injection testing completed
```

---

# 8. Output Controls

## Output Types

```text
Draft email
Document summary
Meeting summary
Internal content draft
Internal Q&A response
Brainstorming output
```

## Output Use Rules

```text
Users must review all outputs before use.

AI-generated summaries must not be treated as authoritative records unless reviewed and approved by the responsible human owner.

AI output must not be used for legal, HR, financial, security, customer-impacting, or regulated decisions without additional review.
```

## Output Risks

```text
Incorrect summary
Missing context
Hallucinated detail
Overconfident tone
Sensitive information included in output
Output copied into official record without review
```

## Output Controls

```text
[x] User review required
[x] Output use restrictions defined
[x] High-risk use prohibited during pilot
[ ] Output quality sampling implemented
[ ] Formal correction process defined
```

---

# 9. Vendor AI Review

## Vendor Involvement

```text
Vendor AI is involved.
```

## Vendor Processing Questions

| Question | Status |
|---|---|
| Does vendor process prompts? | Yes |
| Does vendor process outputs? | Yes |
| Does vendor retain prompts or outputs? | Under review |
| Does vendor use data for training? | Must be contractually disabled or confirmed not applicable |
| Does vendor use data for product improvement? | Under review |
| Are logs available? | Partial |
| Can admin disable feature? | Yes |
| Is incident support path defined? | Pending |

## Vendor Controls Required

```text
[x] Vendor AI assessment
[x] Data processing review
[x] Retention review
[x] Training/reuse review
[x] Admin configuration review
[x] Logging/evidence review
[x] Incident support review
```

Related template:

```text
templates/ai-vendor-assessment-template.md
```

---

# 10. Human Accountability

## Accountability Statement

```text
The copilot may assist employees, but employees remain accountable for reviewing and validating outputs before use.

The business owner remains accountable for approved enterprise use of the copilot.

The technical owner remains accountable for configuration and access controls.

The vendor owner remains accountable for vendor risk review and evidence collection.
```

## Review Expectations

```text
Users must review generated text before sending, publishing, uploading, or relying on it.

Managers remain accountable for business decisions.

Specialist teams remain accountable for legal, privacy, security, HR, finance, compliance, and customer-impacting decisions.
```

---

# 11. Monitoring and Evidence

## Evidence Required for Pilot

```text
Inventory record
Risk assessment
Vendor assessment
Configuration record
User guidance
Approved user population
Data processing review
Retention/training/reuse review
Incident escalation path
Pilot approval record
```

## Logging Approach

```text
Usage metadata logging required.

Full prompt and output logging should be avoided unless privacy, legal, and data governance approve the approach.

Where prompt or output content is logged, sensitive data protection and access restrictions must be applied.
```

## Evidence Gaps

```text
Vendor prompt/output retention details still under review.
Vendor log export capability is partial.
Sensitive prompt detection is not yet automated.
```

---

# 12. Assurance Tests

## Pilot Assurance Checklist

```text
[x] Inventory record created
[x] Business owner assigned
[x] Technical owner assigned
[x] Vendor owner assigned
[x] Risk tier assigned
[x] Vendor assessment started
[x] User guidance drafted
[ ] Vendor retention confirmed
[ ] Vendor training/reuse confirmed
[ ] Admin settings reviewed
[ ] Pilot user group approved
[ ] Incident escalation tested
[ ] Evidence package created
```

## Required Tests Before Broader Rollout

```text
[ ] Permission inheritance review
[ ] Sensitive data handling review
[ ] Vendor logging review
[ ] User guidance review
[ ] Output quality sampling
[ ] Incident escalation test
[ ] Feature disablement test
```

---

# 13. Incident Containment

## Potential Incident Scenarios

```text
Sensitive data entered into prompt
Confidential data exposed in output
User relies on incorrect summary
Vendor retention issue identified
Copilot generates inappropriate or unsafe content
AI output used for prohibited decision
```

## Containment Actions

```text
Disable copilot feature for affected users
Restrict pilot population
Remove access to sensitive data source
Preserve available logs
Notify business owner
Notify data/privacy/legal/security depending on incident type
Contact vendor support if vendor evidence is required
Update user guidance
Pause rollout until remediation
```

## Restart Criteria

```text
Incident contained
Evidence preserved
Root cause understood
Configuration or guidance updated
Required approvals obtained
Pilot users notified if needed
Retest completed where required
```

---

# 14. Open Issues

| Issue | Owner | Due Date | Status |
|---|---|---|---|
| Confirm vendor prompt/output retention | Vendor Owner | TBD | Open |
| Confirm vendor training/reuse settings | Vendor Owner | TBD | Open |
| Review admin controls | Technical Owner | TBD | Open |
| Finalize user guidance | Business Owner | TBD | Open |
| Define evidence location | Evidence Owner | TBD | Open |
| Test feature disablement | Technical Owner | TBD | Open |

---

# 15. Decision

## Pilot Decision

```text
Approved for limited pilot with conditions.
```

## Conditions

```text
1. Vendor training/reuse settings must be confirmed before broader rollout.
2. Vendor retention settings must be documented.
3. User guidance must be published before pilot starts.
4. Pilot must exclude restricted or regulated data use.
5. Incident escalation path must be defined.
6. Feature disablement path must be tested before expansion.
```

---

# 16. Summary

```text
Use case: Enterprise Productivity Copilot
Pattern: AI-enabled SaaS / Embedded vendor AI / Employee-facing copilot
Risk tier: Tier 2 for pilot
Business owner: Head of Digital Workplace
Technical owner: Collaboration Platform Owner
Vendor owner: SaaS Vendor Manager
Data boundary: User-accessible internal data only; restricted/regulated data excluded
Decision impact: Advisory/draft only
Tool/action capability: Not approved in pilot
Key controls: Inventory, ownership, vendor review, data guidance, output review, logging approach, incident path
Pilot decision: Approved with conditions
```