# AI Exception Record Template

This template is used to document, approve, track, review, and close exceptions to AI Control Architecture requirements.

An exception is a temporary, approved deviation from a required control.

Exceptions should not become unmanaged risk.

Every exception should have a business justification, risk assessment, accountable owner, compensating control where possible, approval, expiry date, review date, and remediation plan.

---

# 1. Exception Information

## Exception Title

```text
[Enter short exception title]
```

## Exception ID

```text
[Enter exception ID]
```

## Date Requested

```text
[Enter date]
```

## Requested By

```text
Name:
Function:
Email:
```

## AI Use Case Name

```text
[Enter AI use case name]
```

## Related AI Inventory Record

```text
[Enter inventory record reference or link]
```

## Current Lifecycle Status

Select one:

```text
[ ] Proposed
[ ] Under review
[ ] Approved
[ ] Pilot
[ ] Production
[ ] Restricted
[ ] Suspended
[ ] Under remediation
[ ] Retired
[ ] Rejected
[ ] Exception approved
```

---

# 2. Ownership

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
Not applicable reason, if any:
```

## Exception Owner

```text
Name:
Function:
Email:
```

## Risk Acceptance Owner

```text
Name:
Function:
Email:
```

## Control Owner

```text
Name:
Function:
Email:
Control domain:
```

---

# 3. Exception Scope

## Requirement Affected

```text
[Enter requirement ID and requirement name]
```

## Control Objective Affected

```text
[Enter control objective ID and control objective name]
```

## AI Control Pillar Affected

Select all that apply:

```text
[ ] AI inventory and classification
[ ] AI identity and access control
[ ] Data boundary control
[ ] Prompt and input control
[ ] Output and decision control
[ ] Tool and action control
[ ] Human accountability model
[ ] AI assurance and testing
[ ] Monitoring, logging, and evidence
[ ] Incident containment and recovery
```

## Exception Type

Select one:

```text
[ ] Temporary delay in control implementation
[ ] Control not technically feasible
[ ] Control partially implemented
[ ] Alternative control used
[ ] Vendor limitation
[ ] Legacy system limitation
[ ] Business continuity constraint
[ ] Pilot or limited-scope exception
[ ] Emergency exception
[ ] Other
```

## Exception Description

```text
[Describe the control requirement that cannot currently be met and why an exception is requested]
```

---

# 4. Business Justification

## Business Reason for Exception

```text
[Explain why the AI use case needs to proceed without the required control fully implemented]
```

## Business Impact If Exception Is Not Approved

```text
[Describe operational, business, customer, security, legal, financial, or delivery impact if the exception is rejected]
```

## Is This Exception Required for Production Use?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Is This Exception Required for Pilot Use Only?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

---

# 5. Risk Assessment

## Assigned AI Risk Tier

Select one:

```text
[ ] Tier 1: Low-risk productivity or public-data use
[ ] Tier 2: Internal productivity with enterprise data
[ ] Tier 3: Decision-supporting AI
[ ] Tier 4: Action-capable AI
[ ] Tier 5: High-impact autonomous or regulated AI
```

## Risk Created by Exception

Select all that apply:

```text
[ ] Unknown AI use
[ ] Undefined ownership
[ ] Excessive AI access
[ ] Sensitive data exposure
[ ] Weak retrieval boundary
[ ] Prohibited prompt or input risk
[ ] Prompt injection risk
[ ] Unvalidated output
[ ] AI recommendation treated as decision
[ ] Tool or action misuse
[ ] Approval bypass
[ ] Weak human accountability
[ ] Missing assurance testing
[ ] Missing logs or evidence
[ ] Weak incident containment
[ ] Vendor evidence limitation
[ ] Weak recovery or rollback
[ ] Other
```

## Risk Severity

Select one:

```text
[ ] Low
[ ] Medium
[ ] High
[ ] Critical
```

## Risk Description

```text
[Describe what could go wrong because this exception is approved]
```

## Potential Impact

Select all that apply:

```text
[ ] Minimal impact
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
```

## Risk Rationale

```text
[Explain why the severity and impact ratings were selected]
```

---

# 6. Compensating Controls

## Are Compensating Controls Available?

```text
[ ] No
[ ] Yes
[ ] Partial
[ ] Unknown
```

## Compensating Control Summary

| Compensating Control | Owner | Implemented? | Evidence |
|---|---|---|---|
| [Control] | [Owner] | [Yes/No/Partial] | [Evidence] |

## Compensating Control Description

```text
[Describe how compensating controls reduce the risk created by the exception]
```

## Residual Risk After Compensating Controls

Select one:

```text
[ ] Low
[ ] Medium
[ ] High
[ ] Critical
```

## Residual Risk Notes

```text
[Describe remaining risk after compensating controls]
```

---

# 7. Exception Duration

## Exception Start Date

```text
[Enter date]
```

## Exception Expiry Date

```text
[Enter date]
```

## Review Frequency

Select one:

```text
[ ] Weekly
[ ] Monthly
[ ] Quarterly
[ ] Before production release
[ ] Before scaling
[ ] At next major change
[ ] Other
```

## Review Date

```text
[Enter next review date]
```

## Is Extension Allowed?

```text
[ ] No
[ ] Yes, with re-approval
[ ] Unknown
```

## Extension Conditions

```text
[Describe conditions under which this exception may be extended]
```

---

# 8. Remediation Plan

## Remediation Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Target Control State

```text
[Describe the expected compliant control state after remediation]
```

## Remediation Actions

| Action ID | Remediation Action | Owner | Due Date | Status |
|---|---|---|---|---|
| [Action ID] | [Action] | [Owner] | [Date] | [Not started/In progress/Complete] |

## Dependencies

```text
[Describe dependencies such as vendor feature, platform change, funding, architecture decision, or technical implementation]
```

## Remediation Evidence Required

```text
[Describe evidence needed to close the exception]
```

---

# 9. Monitoring and Evidence During Exception

## Additional Monitoring Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Monitoring Requirements

Select all that apply:

```text
[ ] Usage monitoring
[ ] Prompt/input monitoring
[ ] Sensitive data monitoring
[ ] Retrieval monitoring
[ ] Output review
[ ] Tool call monitoring
[ ] Action monitoring
[ ] Approval monitoring
[ ] Exception-specific alerts
[ ] Manual review
[ ] Business owner review
[ ] Security review
[ ] Audit review
```

## Evidence Required During Exception

Select all that apply:

```text
[ ] Usage logs
[ ] Prompt/input logs or metadata
[ ] Retrieval logs
[ ] Output logs
[ ] Review records
[ ] Approval records
[ ] Tool call logs
[ ] Action logs
[ ] Monitoring alerts
[ ] Incident records
[ ] Compensating control evidence
[ ] Remediation progress evidence
```

## Evidence Location

```text
[Describe where exception evidence is stored]
```

---

# 10. Incident and Escalation Conditions

## Escalation Triggers

Select all that apply:

```text
[ ] Sensitive data exposure
[ ] Policy violation
[ ] Prompt injection event
[ ] Unsafe output
[ ] Incorrect decision
[ ] Unauthorized tool use
[ ] Approval bypass
[ ] Customer complaint
[ ] Vendor issue
[ ] Missing evidence
[ ] Exception expiry reached
[ ] Remediation overdue
[ ] Risk severity increases
[ ] Other
```

## Escalation Path

```text
[Describe who must be notified and how escalation occurs]
```

## Containment Actions If Risk Materializes

Select all that apply:

```text
[ ] Disable AI use case
[ ] Restrict use case scope
[ ] Revoke AI access
[ ] Remove data source access
[ ] Disable tool access
[ ] Stop workflow
[ ] Disable vendor feature
[ ] Quarantine output
[ ] Require manual review
[ ] Suspend production use
[ ] Open incident
```

## Incident Contact

```text
Name:
Function:
Email:
```

---

# 11. Approval

## Business Owner Approval

```text
Name:
Decision:
Date:
Notes:
```

## Control Owner Approval

```text
Name:
Control domain:
Decision:
Date:
Notes:
```

## Risk Owner Approval

```text
Name:
Decision:
Date:
Notes:
```

## Security / Architecture Approval

```text
Name or forum:
Decision:
Date:
Notes:
```

## Legal / Privacy Approval, If Required

```text
Name or forum:
Decision:
Date:
Notes:
Not applicable reason, if any:
```

## Final Exception Decision

Select one:

```text
[ ] Approved
[ ] Approved with conditions
[ ] Rejected
[ ] Deferred
[ ] Requires additional review
```

## Approval Conditions

```text
[List conditions that must be met while the exception remains active]
```

---

# 12. Exception Review

## Review Date

```text
[Enter review date]
```

## Review Performed By

```text
Name:
Function:
Email:
```

## Current Status

Select one:

```text
[ ] Active
[ ] On track
[ ] Remediation in progress
[ ] Overdue
[ ] Risk increased
[ ] Risk reduced
[ ] Ready to close
[ ] Extension requested
[ ] Escalated
```

## Review Notes

```text
[Document review outcome, evidence checked, risk changes, and next actions]
```

## Extension Requested?

```text
[ ] No
[ ] Yes
```

## Extension Rationale

```text
[Explain why extension is requested]
```

---

# 13. Exception Closure

## Closure Date

```text
[Enter date]
```

## Closure Reason

Select one:

```text
[ ] Required control implemented
[ ] Use case retired
[ ] Use case rejected
[ ] Risk eliminated
[ ] Alternative control accepted permanently
[ ] Exception replaced by new exception
[ ] Other
```

## Closure Evidence

```text
[Reference evidence proving the exception can be closed]
```

## Closure Approved By

```text
Name:
Function:
Date:
Notes:
```

---

# 14. Summary

```text
Exception ID:
Use case:
Requirement affected:
Risk tier:
Risk severity:
Compensating control:
Residual risk:
Exception owner:
Approval status:
Start date:
Expiry date:
Review date:
Remediation due date:
Closure status:
```