# AI Tool and Action Control Template

This template is used to define, approve, test, monitor, and evidence what tools, APIs, workflows, systems, and actions an AI capability can access or execute.

AI that can act creates a different risk profile from AI that only generates text.

The purpose of this template is to ensure AI tool use and action capability are explicitly inventoried, permissioned, classified, approval-gated, logged, monitored, reversible where possible, and containable.

---

# 1. Tool and Action Control Information

## AI Use Case Name

```text
[Enter AI use case name]
```

## Tool/Action Control ID

```text
[Enter control ID]
```

## Date

```text
[Enter date]
```

## Prepared By

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

## Tool / Platform Owner

```text
Name:
Function:
Email:
Not applicable reason, if any:
```

## Related AI Inventory Record

```text
[Enter inventory record reference or link]
```

## Related Risk Assessment

```text
[Enter risk assessment reference or link]
```

---

# 2. AI Use Case Summary

## Short Description

```text
[Describe the AI use case]
```

## AI Pattern

Select all that apply:

```text
[ ] Copilot with tool access
[ ] Internal LLM application with tools
[ ] RAG system with tools
[ ] AI-enabled SaaS workflow
[ ] Embedded vendor AI action
[ ] Agent
[ ] AI-enabled workflow automation
[ ] Customer-facing AI with actions
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

# 3. Tool and Action Capability Summary

## Can AI Use Tools, APIs, or Workflows?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Capability Type

Select all that apply:

```text
[ ] Read-only retrieval
[ ] Search
[ ] Draft-only action
[ ] API call
[ ] Workflow trigger
[ ] Ticket creation
[ ] Record creation
[ ] Record modification
[ ] Communication sending
[ ] Access request
[ ] Access approval
[ ] Financial transaction
[ ] Security action
[ ] Production system change
[ ] Administrative action
[ ] Code execution
[ ] Other
```

## Tool and Action Summary

```text
[Describe what the AI can do through tools, APIs, workflows, or integrations]
```

---

# 4. Tool Inventory

| Tool / API / Workflow | Connected System | Tool Owner | Tool Type | Approved? |
|---|---|---|---|---|
| [Tool] | [System] | [Owner] | [Read/Draft/Write/Action/Admin] | [Yes/No/Pending] |

## Tool Type

Select all that apply:

```text
[ ] Read-only tool
[ ] Draft-only tool
[ ] Workflow tool
[ ] Write-capable tool
[ ] Communication tool
[ ] Transaction tool
[ ] Administrative tool
[ ] Security tool
[ ] Developer tool
[ ] External tool
[ ] Other
```

## Tool Inventory Notes

```text
[Describe tool ownership, scope, connected systems, and approval status]
```

---

# 5. Tool Permissioning

## Permission Model

Select all that apply:

```text
[ ] User permission inheritance
[ ] Delegated user authority
[ ] Service account permissions
[ ] Application identity permissions
[ ] Agent identity permissions
[ ] Vendor-managed permissions
[ ] Role-based permissions
[ ] Attribute-based permissions
[ ] Policy-based permissions
[ ] Other
```

## Tool Permission Scope

| Tool | Allowed Methods / Actions | Prohibited Methods / Actions | Permission Boundary |
|---|---|---|---|
| [Tool] | [Allowed] | [Prohibited] | [Boundary] |

## Least Privilege Review Completed?

```text
[ ] No
[ ] Yes
[ ] Partial
[ ] Unknown
```

## Permission Notes

```text
[Describe how tool access is limited to the approved use case]
```

---

# 6. Action Classification

## Action Risk Classification

| Action | Description | Risk Level | Reversible? | Approval Required? |
|---|---|---|---|---|
| [Action] | [Description] | [Low/Moderate/High/Critical] | [Yes/No/Partial] | [Yes/No/Conditional] |

## High-Risk Action Types

Select all that apply:

```text
[ ] Customer-impacting action
[ ] Employee-impacting action
[ ] Financial action
[ ] Legal or compliance action
[ ] Security action
[ ] Production change
[ ] Access grant or revocation
[ ] Record modification
[ ] External communication
[ ] Regulated workflow action
[ ] Irreversible or hard-to-reverse action
[ ] Administrative action
[ ] Other
```

## Action Classification Notes

```text
[Describe action risk, reversibility, business impact, and classification rationale]
```

---

# 7. Action Boundaries

## Boundaries Applied

Select all that apply:

```text
[ ] Tool boundary
[ ] Data boundary
[ ] System boundary
[ ] Environment boundary
[ ] User boundary
[ ] Role boundary
[ ] Workflow boundary
[ ] Action boundary
[ ] Time boundary
[ ] Rate boundary
[ ] Amount boundary
[ ] Geography boundary
[ ] Customer segment boundary
[ ] Other
```

## Boundary Table

| Boundary Type | Boundary Rule | Enforcement Method | Owner | Evidence |
|---|---|---|---|---|
| [Boundary] | [Rule] | [Method] | [Owner] | [Evidence] |

## Boundary Violation Response

```text
[Describe what happens if AI attempts to exceed approved boundaries]
```

---

# 8. Approval Gates

## Approval Required Before Action?

```text
[ ] No
[ ] Yes
[ ] Conditional
[ ] Unknown
```

## Approval Gate Summary

| Tool / Action | Approval Trigger | Approver | Evidence Required | Expiry |
|---|---|---|---|---|
| [Action] | [Trigger] | [Approver] | [Evidence] | [Expiry] |

## Approval Gate Type

Select all that apply:

```text
[ ] User approval
[ ] Business owner approval
[ ] Technical owner approval
[ ] System policy approval
[ ] Workflow approval
[ ] Dual approval
[ ] Risk-based approval
[ ] Threshold-based approval
[ ] Exception approval
[ ] Security approval
[ ] Other
```

## Approval Bypass Prevention

```text
[Describe controls that prevent AI from executing high-risk actions without approval]
```

## Approval Notes

```text
[Describe approval flow, reviewer context, evidence, and escalation]
```

---

# 9. Autonomous Execution Limits

## Autonomy Level

Select one:

```text
[ ] Level 0: AI generates text only. No tool use.
[ ] Level 1: AI can suggest actions but not execute.
[ ] Level 2: AI can prepare actions as drafts. Human executes.
[ ] Level 3: AI can request actions but approval is required.
[ ] Level 4: AI can execute bounded low-risk actions.
[ ] Level 5: AI can execute high-impact actions only under strict controls.
```

## Autonomous Execution Allowed?

```text
[ ] No
[ ] Yes, low-risk only
[ ] Yes, with approval gates
[ ] Yes, with strict controls
[ ] Unknown
```

## Autonomy Limits

```text
[Describe limits on autonomous execution, planning, tool chaining, retries, escalation, and session duration]
```

---

# 10. Blast-Radius Limits

## Blast-Radius Limits Applied

| Limit Type | Limit Value | Enforcement Method | Owner |
|---|---|---|---|
| Number of records | [Limit] | [Method] | [Owner] |
| Transaction value | [Limit] | [Method] | [Owner] |
| Number of users affected | [Limit] | [Method] | [Owner] |
| API calls | [Limit] | [Method] | [Owner] |
| Rate of actions | [Limit] | [Method] | [Owner] |
| Time window | [Limit] | [Method] | [Owner] |
| Systems affected | [Limit] | [Method] | [Owner] |
| Environment | [Limit] | [Method] | [Owner] |
| Customer segment | [Limit] | [Method] | [Owner] |
| Other | [Limit] | [Method] | [Owner] |

## Maximum Potential Impact

```text
[Describe maximum potential harm if AI fails, is misused, or is abused]
```

## Blast-Radius Notes

```text
[Describe how impact is constrained]
```

---

# 11. Tool Call and Action Logging

## Tool Call Logging Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Action Logging Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Required Log Fields

Select all that apply:

```text
[ ] AI system identity
[ ] Agent identity
[ ] Initiating user
[ ] Delegated authority
[ ] Session ID
[ ] Workflow ID
[ ] Tool called
[ ] Action requested
[ ] Parameters supplied
[ ] Data accessed
[ ] Approval required
[ ] Approval result
[ ] Action executed
[ ] Execution result
[ ] Error or exception
[ ] Timestamp
[ ] Downstream system affected
[ ] Rollback status
[ ] Policy decision
[ ] Other
```

## Log Location

```text
[Describe where tool call and action logs are stored]
```

## Log Retention

```text
[Describe retention period]
```

## Log Access Restrictions

```text
[Describe who can access tool/action logs]
```

---

# 12. Monitoring for Abnormal Tool Use

## Monitoring Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Monitoring Signals

Select all that apply:

```text
[ ] Unusual tool call volume
[ ] Unusual action timing
[ ] Repeated failures
[ ] Excessive retries
[ ] Unauthorized tool call attempt
[ ] Approval bypass attempt
[ ] Blocked action attempt
[ ] Excessive data access
[ ] High transaction value
[ ] Action outside normal workflow
[ ] Tool use after policy violation
[ ] Prompt injection indicator
[ ] Unusual user-agent pairing
[ ] Other
```

## Monitoring Response

Select all that apply:

```text
[ ] Alert
[ ] Block
[ ] Require approval
[ ] Suspend tool access
[ ] Suspend agent
[ ] Revoke credentials
[ ] Open incident
[ ] Preserve evidence
[ ] Trigger review
[ ] Update controls
[ ] Other
```

## Monitoring Notes

```text
[Describe monitoring owner, alert routing, thresholds, and escalation]
```

---

# 13. Kill Switch and Revocation

## Kill Switch Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Kill Switch Levels

Select all that apply:

```text
[ ] AI capability
[ ] Agent
[ ] Tool
[ ] API
[ ] Workflow
[ ] Identity
[ ] Vendor feature
[ ] User group
[ ] Action class
[ ] Data source
[ ] Environment
[ ] Other
```

## Kill Switch Owner

```text
Name:
Function:
Email:
```

## Activation Conditions

```text
[Describe when the kill switch should be activated]
```

## Activation Process

```text
[Describe how the kill switch is activated]
```

## Expected Time to Disable

```text
[Enter expected time]
```

## Restart Criteria

```text
[Describe approval, testing, and evidence required before restart]
```

## Kill Switch Test

```text
Last tested:
Result:
Evidence:
Next test:
```

---

# 14. Rollback and Compensation

## Rollback Available?

```text
[ ] No
[ ] Yes
[ ] Partial
[ ] Unknown
```

## Rollback / Recovery Table

| Tool / Action | Recovery Method | Owner | Tested? | Evidence |
|---|---|---|---|---|
| [Action] | [Method] | [Owner] | [Yes/No] | [Evidence] |

## Compensation Required If Rollback Is Not Possible?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Compensation Method

```text
[Describe compensation, correction, notification, manual remediation, or record amendment]
```

## Recovery Notes

```text
[Describe rollback limitations, dependencies, approvals, and residual risk]
```

---

# 15. Incident Scenarios

## Relevant Tool/Action Incident Scenarios

Select all that apply:

```text
[ ] AI calls unauthorized tool
[ ] AI calls approved tool for unauthorized purpose
[ ] AI exceeds action boundary
[ ] AI bypasses approval gate
[ ] AI modifies incorrect record
[ ] AI sends unauthorized communication
[ ] AI triggers incorrect workflow
[ ] AI grants or revokes access incorrectly
[ ] AI executes financial action incorrectly
[ ] AI performs security action incorrectly
[ ] AI causes production impact
[ ] AI action cannot be rolled back
[ ] Tool logs are missing
[ ] Kill switch fails
[ ] Other
```

## Incident Response Path

```text
[Describe escalation, containment, evidence preservation, investigation, recovery, and communication path]
```

---

# 16. Testing and Assurance

## Required Tests

Select all that apply:

```text
[ ] Tool inventory test
[ ] Tool permission test
[ ] Unauthorized tool call test
[ ] Action boundary test
[ ] Approval gate test
[ ] Approval bypass test
[ ] Autonomous execution limit test
[ ] Blast-radius limit test
[ ] Tool call logging test
[ ] Action logging test
[ ] Abnormal tool use alert test
[ ] Kill switch test
[ ] Rollback test
[ ] Incident tabletop
[ ] Regression test
```

## Test Results

| Test | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|
| [Test] | [Expected] | [Actual] | [Pass/Fail/Partial/Not Run] | [Evidence] |

## Open Findings

| Finding ID | Finding | Severity | Owner | Due Date | Status |
|---|---|---|---|---|---|
| [Finding ID] | [Finding] | [Low/Medium/High/Critical] | [Owner] | [Date] | [Status] |

---

# 17. Exceptions

## Exceptions Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Exception Summary

| Requirement | Exception Needed | Rationale | Compensating Control | Expiry |
|---|---|---|---|---|
| [Requirement] | [Yes/No] | [Rationale] | [Control] | [Date] |

---

# 18. Approval

## Business Owner Approval

```text
Name:
Decision:
Date:
Notes:
```

## Technical Owner Approval

```text
Name:
Decision:
Date:
Notes:
```

## Tool Owner Approval

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

## Risk / Governance Approval

```text
Name or forum:
Decision:
Date:
Notes:
```

## Final Tool/Action Control Decision

Select one:

```text
[ ] Approved
[ ] Approved with conditions
[ ] Approved for pilot only
[ ] Requires remediation
[ ] Requires exception approval
[ ] Requires additional testing
[ ] Rejected
[ ] Deferred
```

## Approval Conditions

```text
[List conditions required before approval, production use, scaling, or restart]
```

---

# 19. Review Triggers

Review this tool and action control design if any of the following occur:

```text
[ ] New tool added
[ ] Tool permission changes
[ ] API integration changes
[ ] Workflow changes
[ ] Action classification changes
[ ] Approval gate changes
[ ] Autonomy level changes
[ ] User population changes
[ ] Data classification changes
[ ] Vendor feature changes
[ ] Risk tier changes
[ ] Incident occurs
[ ] Assurance finding occurs
[ ] Kill switch test fails
[ ] Rollback test fails
```

## Next Review Date

```text
[Enter date]
```

---

# 20. Summary

```text
Use case:
Risk tier:
Tools available:
Action capability:
Highest-risk actions:
Approval gates:
Autonomy level:
Boundaries:
Blast-radius limits:
Logging:
Monitoring:
Kill switch:
Rollback:
Required testing:
Exceptions:
Approval status:
Next review date:
```