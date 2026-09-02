# AI Incident Record Template

This template is used to document, classify, contain, investigate, recover from, and learn from AI-related incidents.

An AI incident may involve data exposure, prompt injection, unsafe output, incorrect decision support, unauthorized tool use, approval bypass, agent malfunction, vendor AI failure, logging failure, or other AI-related control failure.

The purpose of this template is to ensure AI incidents are handled consistently and that evidence, accountability, containment, recovery, and lessons learned are captured.

---

# 1. Incident Information

## Incident Title

```text
[Enter short incident title]
```

## Incident ID

```text
[Enter incident ID]
```

## Date and Time Detected

```text
[Enter date and time]
```

## Reported By

```text
Name:
Function:
Email:
```

## Detection Source

Select all that apply:

```text
[ ] User report
[ ] Customer complaint
[ ] Monitoring alert
[ ] SIEM/SOC alert
[ ] DLP alert
[ ] Audit finding
[ ] Assurance testing
[ ] Vendor notification
[ ] Application log
[ ] Tool/action log
[ ] Business process exception
[ ] Privacy/legal escalation
[ ] Other
```

## AI Use Case Name

```text
[Enter AI use case name]
```

## Related AI Inventory Record

```text
[Enter inventory record reference or link]
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

---

# 2. Incident Classification

## Incident Category

Select all that apply:

```text
[ ] Sensitive data exposure
[ ] Prompt injection
[ ] Unsafe output
[ ] Incorrect AI-assisted decision
[ ] Unauthorized retrieval
[ ] Unauthorized tool use
[ ] Approval bypass
[ ] Agent malfunction
[ ] Excessive or unsafe action
[ ] Vendor AI incident
[ ] Model behavior change
[ ] Logging or evidence failure
[ ] Data retention or reuse issue
[ ] Customer-facing AI failure
[ ] Regulatory or legal exposure
[ ] Accountability failure
[ ] Other
```

## Incident Severity

Select one:

```text
[ ] Low
[ ] Medium
[ ] High
[ ] Critical
```

## Severity Rationale

```text
[Explain why this severity was selected]
```

## Current Incident Status

Select one:

```text
[ ] New
[ ] Triage in progress
[ ] Confirmed incident
[ ] Containment in progress
[ ] Contained
[ ] Investigation in progress
[ ] Recovery in progress
[ ] Monitoring after recovery
[ ] Closed
[ ] False positive
```

---

# 3. Initial Impact Assessment

## Affected Data

Select all that apply:

```text
[ ] No data affected
[ ] Public data
[ ] Internal data
[ ] Confidential data
[ ] Restricted data
[ ] Regulated data
[ ] Personal data
[ ] Customer data
[ ] Employee data
[ ] Financial data
[ ] Legal or privileged data
[ ] Security-sensitive data
[ ] Source code
[ ] Secrets or credentials
[ ] Production data
[ ] Unknown
```

## Estimated Records Affected

```text
[Enter number or unknown]
```

## Affected Users or Parties

Select all that apply:

```text
[ ] Employees
[ ] Contractors
[ ] Customers
[ ] Suppliers
[ ] Partners
[ ] Public users
[ ] Regulators
[ ] Internal business process
[ ] Production system
[ ] Unknown
```

## Impact Types

Select all that apply:

```text
[ ] No known impact
[ ] Productivity impact
[ ] Operational impact
[ ] Customer impact
[ ] Employee impact
[ ] Financial impact
[ ] Legal impact
[ ] Privacy impact
[ ] Compliance impact
[ ] Security impact
[ ] Production impact
[ ] Regulatory impact
[ ] Reputational impact
[ ] Unknown
```

## Initial Impact Notes

```text
[Describe known or suspected impact]
```

---

# 4. Ownership and Response Team

## Incident Owner

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

## Data Owner

```text
Name:
Function:
Email:
Not applicable reason, if any:
```

## Vendor Owner

```text
Name:
Function:
Email:
Not applicable reason, if any:
```

## Legal / Privacy Contact

```text
Name:
Function:
Email:
Not applicable reason, if any:
```

## Security / SOC Contact

```text
Name:
Function:
Email:
Not applicable reason, if any:
```

## Communications Contact

```text
Name:
Function:
Email:
Not applicable reason, if any:
```

---

# 5. Timeline

| Date / Time | Event | Source | Notes |
|---|---|---|---|
| [Timestamp] | [Event] | [Source] | [Notes] |

## Timeline Notes

```text
[Document key sequence of events]
```

---

# 6. AI Activity Details

## Initiating Actor

Select one:

```text
[ ] Human user
[ ] Application
[ ] Workflow
[ ] Agent
[ ] Vendor AI feature
[ ] External user
[ ] Unknown
```

## Initiating User or Process

```text
Name or process:
Role:
System:
```

## AI System / Model / Vendor

```text
AI system:
Model/service:
Vendor/platform:
Version/configuration if known:
```

## AI Identity or Authority Used

Select all that apply:

```text
[ ] User identity
[ ] Delegated user authority
[ ] Service identity
[ ] Application identity
[ ] Agent identity
[ ] Vendor-managed identity
[ ] Unknown
```

## Identity / Access Notes

```text
[Describe identity, delegated authority, service account, agent identity, or access used]
```

---

# 7. Prompt, Input, Context, and Output

## Prompt or Input Involved?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Prompt / Input Evidence Location

```text
[Reference prompt/input log, evidence package, or location]
```

## External or Untrusted Input Involved?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Prompt Injection Suspected?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Retrieved Context Involved?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Retrieved Context Evidence

```text
[Reference source documents, retrieval logs, context records, or unknown]
```

## AI Output Involved?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Output Evidence Location

```text
[Reference output log, generated record, communication, or evidence package]
```

## Prompt / Context / Output Notes

```text
[Describe relevant prompt, input, retrieved context, output, or generated record]
```

---

# 8. Tool, Action, Workflow, or Agent Activity

## Tool or Action Involved?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Tool / API / Workflow Used

| Tool / API / Workflow | Action Requested | Action Executed? | Approval Required? | Approval Obtained? |
|---|---|---|---|---|
| [Tool] | [Action] | [Yes/No/Unknown] | [Yes/No] | [Yes/No/Unknown] |

## Agent Involved?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Agent Name / ID

```text
[Enter agent name or ID]
```

## Action Impact

```text
[Describe records changed, workflows triggered, communications sent, systems affected, or actions attempted]
```

## Tool / Action Evidence Location

```text
[Reference tool call logs, action logs, workflow logs, approval records, or evidence package]
```

---

# 9. Containment

## Containment Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Containment Actions Taken

Select all that apply:

```text
[ ] Disabled AI capability
[ ] Suspended agent
[ ] Revoked AI identity
[ ] Revoked delegated authority
[ ] Removed data source access
[ ] Disabled retrieval
[ ] Disabled tool
[ ] Blocked API
[ ] Stopped workflow
[ ] Disabled vendor AI feature
[ ] Quarantined output
[ ] Blocked customer-facing response
[ ] Rolled back action
[ ] Rotated credentials
[ ] Restricted user group
[ ] Opened broader incident
[ ] Other
```

## Containment Owner

```text
Name:
Function:
Email:
```

## Time Containment Started

```text
[Enter date/time]
```

## Time Containment Completed

```text
[Enter date/time]
```

## Containment Status

Select one:

```text
[ ] Not required
[ ] Pending
[ ] In progress
[ ] Completed
[ ] Partially completed
[ ] Failed
[ ] Unknown
```

## Containment Notes

```text
[Describe containment actions, scope, limitations, and open issues]
```

---

# 10. Evidence Preservation

## Evidence Preservation Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Evidence Preserved

Select all that apply:

```text
[ ] AI inventory record
[ ] Risk assessment
[ ] Prompt/input logs
[ ] Uploaded files
[ ] Retrieved context references
[ ] Source documents
[ ] Output logs
[ ] Generated records
[ ] Tool call logs
[ ] Action logs
[ ] Approval records
[ ] Exception records
[ ] Identity/access records
[ ] Data access logs
[ ] System prompt version
[ ] Model/vendor configuration
[ ] Vendor logs
[ ] Monitoring alerts
[ ] User reports
[ ] Customer complaints
[ ] Communications
[ ] Screenshots or exports
[ ] Other
```

## Evidence Package Location

```text
[Enter evidence storage location or reference]
```

## Legal Hold Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Evidence Preservation Notes

```text
[Describe evidence preservation actions, gaps, vendor dependencies, or access restrictions]
```

---

# 11. Investigation

## Investigation Questions

| Question | Answer |
|---|---|
| What happened? | [Answer] |
| What AI system was involved? | [Answer] |
| Who or what initiated the interaction? | [Answer] |
| What identity or authority was used? | [Answer] |
| What data was accessed? | [Answer] |
| What input or prompt was submitted? | [Answer] |
| Was untrusted content involved? | [Answer] |
| Was prompt injection involved? | [Answer] |
| What output was generated? | [Answer] |
| Was output reviewed or approved? | [Answer] |
| What tool or action was involved? | [Answer] |
| Was approval required? | [Answer] |
| Was approval obtained? | [Answer] |
| What downstream process was affected? | [Answer] |
| What controls worked? | [Answer] |
| What controls failed? | [Answer] |

## Root Cause Category

Select all that apply:

```text
[ ] Design gap
[ ] Implementation gap
[ ] Configuration issue
[ ] Access control failure
[ ] Data boundary failure
[ ] Prompt/input control failure
[ ] Output validation failure
[ ] Tool/action control failure
[ ] Human review failure
[ ] Logging/evidence failure
[ ] Vendor limitation
[ ] User misuse
[ ] Malicious input
[ ] Model behavior issue
[ ] Change management failure
[ ] Unknown
```

## Root Cause Summary

```text
[Describe root cause or suspected root cause]
```

---

# 12. Recovery and Correction

## Recovery Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Recovery Actions

Select all that apply:

```text
[ ] Corrected AI output
[ ] Withdrew AI output
[ ] Corrected generated record
[ ] Re-ran workflow
[ ] Rolled back system action
[ ] Reversed transaction
[ ] Revoked improper access
[ ] Restored configuration
[ ] Notified customer
[ ] Notified employee
[ ] Notified vendor
[ ] Applied compensating control
[ ] Updated prompt or configuration
[ ] Updated retrieval boundary
[ ] Updated tool permissions
[ ] Retested AI capability
[ ] Other
```

## Recovery Owner

```text
Name:
Function:
Email:
```

## Recovery Status

Select one:

```text
[ ] Not required
[ ] Pending
[ ] In progress
[ ] Completed
[ ] Partially completed
[ ] Failed
[ ] Unknown
```

## Recovery Evidence

```text
[Reference records, rollback logs, correction evidence, notifications, approvals, or retest results]
```

## Recovery Notes

```text
[Describe recovery actions, open issues, and restart conditions]
```

---

# 13. Communications and Notifications

## Stakeholders Notified

Select all that apply:

```text
[ ] Business owner
[ ] Technical owner
[ ] Data owner
[ ] Security/SOC
[ ] Incident response
[ ] Legal
[ ] Privacy
[ ] Compliance
[ ] Risk
[ ] Audit
[ ] Vendor management
[ ] Vendor
[ ] Customers
[ ] Employees
[ ] Regulators
[ ] Executive leadership
[ ] Communications team
[ ] Other
```

## Notification Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Notification Summary

| Stakeholder | Notification Required? | Date/Time | Owner | Notes |
|---|---|---|---|---|
| [Stakeholder] | [Yes/No] | [Date/time] | [Owner] | [Notes] |

## Communication Notes

```text
[Describe communications, legal/privacy review, customer notification, vendor communication, or regulatory notification]
```

---

# 14. Vendor AI Incident Handling

## Vendor Involved?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Vendor Name

```text
[Enter vendor name]
```

## Vendor Contacted?

```text
[ ] No
[ ] Yes
[ ] Pending
[ ] Not applicable
```

## Vendor Evidence Requested

Select all that apply:

```text
[ ] Prompt logs
[ ] Output logs
[ ] Data processing logs
[ ] Audit logs
[ ] Configuration records
[ ] Feature enablement records
[ ] Retention records
[ ] Training/reuse confirmation
[ ] Incident report
[ ] Root cause analysis
[ ] Remediation confirmation
[ ] Subprocessor information
[ ] Other
```

## Vendor Response Summary

```text
[Describe vendor response, evidence received, gaps, commitments, and next steps]
```

---

# 15. Post-Incident Review

## Review Date

```text
[Enter date]
```

## Review Participants

```text
[List participants]
```

## What Worked

```text
[Describe controls, processes, monitoring, containment, or ownership that worked]
```

## What Failed or Was Weak

```text
[Describe control failures, process gaps, evidence gaps, ownership gaps, or vendor limitations]
```

## Lessons Learned

```text
[Document lessons learned]
```

## Recurrence Risk

Select one:

```text
[ ] Low
[ ] Medium
[ ] High
[ ] Critical
```

## Recurrence Notes

```text
[Describe likelihood and conditions for recurrence]
```

---

# 16. Remediation and Improvement Actions

| Action ID | Action | Owner | Due Date | Status | Evidence |
|---|---|---|---|---|---|
| [Action ID] | [Action] | [Owner] | [Date] | [Not started/In progress/Complete] | [Evidence] |

## Control Updates Required

Select all that apply:

```text
[ ] Update AI inventory
[ ] Update risk assessment
[ ] Update identity/access controls
[ ] Update data boundary controls
[ ] Update prompt/input controls
[ ] Update output/decision controls
[ ] Update tool/action controls
[ ] Update accountability model
[ ] Update assurance tests
[ ] Update logging/monitoring
[ ] Update incident playbook
[ ] Update vendor controls
[ ] Update user training
[ ] Update architecture documentation
[ ] Other
```

## Improvement Notes

```text
[Describe architecture, control, monitoring, assurance, or operating model improvements required]
```

---

# 17. Closure

## Closure Criteria

Select all that apply:

```text
[ ] Incident contained
[ ] Evidence preserved
[ ] Investigation completed
[ ] Impact assessed
[ ] Required notifications completed
[ ] Recovery completed
[ ] Vendor response completed
[ ] Remediation actions assigned
[ ] High-risk remediation completed
[ ] Residual risk accepted
[ ] Post-incident review completed
```

## Residual Risk

```text
[Describe residual risk after closure]
```

## Closure Decision

Select one:

```text
[ ] Closed
[ ] Closed with residual risk accepted
[ ] Remains open
[ ] Reclassified as non-incident
[ ] Escalated to broader incident
```

## Closure Approved By

```text
Name:
Function:
Date:
Notes:
```

---

# 18. Summary

```text
Incident ID:
AI use case:
Incident category:
Severity:
Status:
Affected data:
Affected users/processes:
Containment action:
Recovery action:
Root cause:
Key control failures:
Remediation actions:
Residual risk:
Closure decision:
```