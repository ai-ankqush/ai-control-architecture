# AI Agent Control Template

This template is used to assess, design, approve, monitor, and contain AI agents.

An AI agent is an AI system that can pursue a goal, plan steps, use tools, call APIs, trigger workflows, retrieve data, or perform actions with some level of autonomy.

Agentic AI requires stronger control than passive AI because it can move from generating output to executing actions.

---

# 1. Agent Information

## Agent Name

```text
[Enter agent name]
```

## Agent ID

```text
[Enter agent ID]
```

## Date

```text
[Enter date]
```

## Agent Status

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
```

## Related AI Use Case

```text
[Enter related AI use case name]
```

## Related AI Inventory Record

```text
[Enter inventory record reference or link]
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

## Agent Owner

```text
Name:
Function:
Email:
```

## Incident Contact

```text
Name:
Function:
Email:
Escalation path:
```

---

# 2. Agent Purpose

## Business Purpose

```text
[Describe why this agent is needed and what business outcome it supports]
```

## Agent Goal

```text
[Describe the goal the agent is designed to pursue]
```

## Approved Use Cases

```text
[List approved use cases for this agent]
```

## Prohibited Use Cases

```text
[List prohibited or restricted uses]
```

## User Population

Select all that apply:

```text
[ ] Employees
[ ] Contractors
[ ] Developers
[ ] Security team
[ ] Customer support team
[ ] HR team
[ ] Finance team
[ ] Legal or compliance team
[ ] Business operations team
[ ] Customers
[ ] Suppliers
[ ] Partners
[ ] Public users
[ ] Other
```

---

# 3. Agent Autonomy

## Autonomy Level

Select one:

```text
[ ] Level 0: AI generates text only
[ ] Level 1: AI suggests actions but cannot execute
[ ] Level 2: AI prepares drafts but human executes
[ ] Level 3: AI requests actions but approval is required
[ ] Level 4: AI executes bounded low-risk actions
[ ] Level 5: AI executes high-impact actions under strict controls
```

## Autonomy Description

```text
[Describe what the agent can do independently and where human involvement is required]
```

## Human Review Model

Select one:

```text
[ ] Human-in-the-loop
[ ] Human-on-the-loop
[ ] Human-over-the-loop
[ ] Exception-based review
[ ] Not yet defined
```

## Autonomy Limits

```text
[Describe limits on planning, tool use, action execution, workflow scope, session length, or decision authority]
```

---

# 4. Agent Identity and Authority

## Agent Identity Model

Select all that apply:

```text
[ ] Direct user identity
[ ] Delegated user authority
[ ] Service identity
[ ] Application identity
[ ] Agent identity
[ ] Vendor-managed identity
[ ] Hybrid identity
[ ] Unknown
```

## Agent Identity Details

```text
Agent identity:
Service account:
Application identity:
Vendor identity:
Other:
```

## Delegated Authority

```text
[Describe whose authority the agent acts under, what is delegated, and under what conditions]
```

## Access Scope

```text
[Describe systems, repositories, APIs, workflows, tools, and data the agent can access]
```

## Access Approval

```text
Approver:
Date approved:
Approval reference:
```

## Access Review Frequency

Select one:

```text
[ ] Monthly
[ ] Quarterly
[ ] Semi-annually
[ ] Annually
[ ] At material change
[ ] Other
```

## Revocation Path

```text
[Describe how agent identity, delegated authority, tool access, API access, or service credentials can be revoked]
```

---

# 5. Data Boundary

## Data Sources Accessible to Agent

| Data Source | Classification | Owner | Access Type | Approved? |
|---|---|---|---|---|
| [Source] | [Classification] | [Owner] | [Read/Write/Retrieve] | [Yes/No/Pending] |

## Data Classes Accessible

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
[ ] Financial data
[ ] Legal or privileged data
[ ] Security-sensitive data
[ ] Source code
[ ] Secrets or credentials
[ ] Production data
[ ] Other sensitive data
```

## Retrieval Boundaries

```text
[Describe what the agent can and cannot retrieve]
```

## Data Restrictions

```text
[Describe restricted data, prohibited data, masking, minimization, retention, or reuse restrictions]
```

## Vendor Processing

```text
[Describe whether agent inputs, context, outputs, logs, or tool calls are processed by a vendor]
```

---

# 6. Prompt and Input Control

## Input Sources

Select all that apply:

```text
[ ] User prompt
[ ] System prompt
[ ] Retrieved document
[ ] Email
[ ] Ticket
[ ] Chat message
[ ] Customer submission
[ ] API payload
[ ] Tool response
[ ] Web content
[ ] Code
[ ] Log data
[ ] Workflow state
[ ] Conversation history
[ ] Memory
[ ] Other
```

## External or Untrusted Inputs

```text
[Describe external or untrusted inputs processed by the agent]
```

## Prompt Injection Risk

Select one:

```text
[ ] Low
[ ] Moderate
[ ] High
[ ] Critical
[ ] Unknown
```

## Prompt Injection Controls

```text
[Describe controls to prevent untrusted content from overriding system instructions or causing unsafe tool use]
```

## System Prompt Protection

```text
[Describe system prompt ownership, versioning, access control, testing, and rollback]
```

## Context Isolation

```text
[Describe how context is isolated across users, sessions, tenants, repositories, trust levels, and data classifications]
```

---

# 7. Tool Inventory

## Tools Available to Agent

| Tool / API / Workflow | Owner | Action Type | Risk Level | Approval Required? | Logging Available? |
|---|---|---|---|---|---|
| [Tool] | [Owner] | [Read/Draft/Write/Action/Admin] | [Low/Medium/High/Critical] | [Yes/No] | [Yes/No] |

## Tool Permissioning

```text
[Describe which tools are allowed, restricted, prohibited, or conditionally available]
```

## Prohibited Tools

```text
[List tools, APIs, workflows, or actions the agent must not use]
```

## Tool Access Review

```text
Review frequency:
Reviewer:
Last reviewed:
Next review:
```

---

# 8. Action Classification

## Agent Actions

| Action | Description | Risk Level | Reversible? | Approval Required? |
|---|---|---|---|---|
| [Action] | [Description] | [Low/Medium/High/Critical] | [Yes/No/Partial] | [Yes/No] |

## High-Risk Actions

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
[ ] Other
```

## Action Notes

```text
[Describe action risks, reversibility, downstream impact, and approval expectations]
```

---

# 9. Approval Gates

## Approval Required Before Execution?

```text
[ ] No
[ ] Yes
[ ] Conditional
[ ] Unknown
```

## Approval Gate Summary

| Action / Tool | Approval Trigger | Approver | Evidence Required | Expiry |
|---|---|---|---|---|
| [Action] | [Trigger] | [Approver] | [Evidence] | [Expiry] |

## Approval Conditions

```text
[Describe thresholds, conditions, or exceptions that require approval]
```

## Approval Bypass Prevention

```text
[Describe controls that prevent the agent from bypassing approval]
```

---

# 10. Execution Boundaries

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

## Boundary Details

```text
[Describe exact execution boundaries]
```

## Boundary Enforcement

```text
[Describe how boundaries are technically or procedurally enforced]
```

## Boundary Violation Response

```text
[Describe what happens if the agent attempts to exceed boundaries]
```

---

# 11. Blast-Radius Limits

## Limits Applied

| Limit Type | Limit Value | Enforcement Method | Owner |
|---|---|---|---|
| Number of records | [Limit] | [Method] | [Owner] |
| Transaction value | [Limit] | [Method] | [Owner] |
| Number of users affected | [Limit] | [Method] | [Owner] |
| API calls | [Limit] | [Method] | [Owner] |
| Time window | [Limit] | [Method] | [Owner] |
| Systems affected | [Limit] | [Method] | [Owner] |
| Environment | [Limit] | [Method] | [Owner] |
| Other | [Limit] | [Method] | [Owner] |

## Blast-Radius Notes

```text
[Describe maximum potential impact if the agent fails or is misused]
```

---

# 12. Monitoring and Logging

## Logs Required

Select all that apply:

```text
[ ] Agent session logs
[ ] User prompt logs
[ ] Prompt metadata
[ ] Retrieved context logs
[ ] Tool call logs
[ ] Action logs
[ ] Approval logs
[ ] Policy decision logs
[ ] Boundary violation logs
[ ] Error logs
[ ] Output logs
[ ] Monitoring alerts
[ ] Incident records
```

## Required Log Fields

Select all that apply:

```text
[ ] User identity
[ ] Agent identity
[ ] Delegated authority
[ ] Session ID
[ ] Goal or request
[ ] Plan or reasoning summary
[ ] Tool selected
[ ] Tool input
[ ] Tool output
[ ] Action requested
[ ] Action executed
[ ] Approval status
[ ] Result
[ ] Exception
[ ] Timestamp
[ ] Policy decision
[ ] Error or failure
```

## Log Location

```text
[Describe where logs are stored]
```

## Log Retention

```text
[Describe retention period and access restrictions]
```

## Monitoring Rules

```text
[Describe monitoring rules for abnormal tool use, action volume, policy violations, failed approvals, prompt injection, or unusual behavior]
```

---

# 13. Kill Switch and Containment

## Kill Switch Available?

```text
[ ] No
[ ] Yes
[ ] Partial
[ ] Unknown
```

## Kill Switch Level

Select all that apply:

```text
[ ] Agent level
[ ] Tool level
[ ] API level
[ ] Workflow level
[ ] Identity level
[ ] Data source level
[ ] Vendor feature level
[ ] User group level
[ ] Action category level
[ ] Environment level
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

## Restart Conditions

```text
[Describe approval and testing required before restart]
```

## Last Kill Switch Test

```text
Date:
Result:
Evidence:
```

---

# 14. Rollback and Recovery

## Rollback Available?

```text
[ ] No
[ ] Yes
[ ] Partial
[ ] Unknown
```

## Rollback / Recovery Summary

| Action Type | Recovery Method | Owner | Tested? | Evidence |
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
[Describe compensation, correction, customer notification, manual remediation, or record amendment]
```

## Recovery Notes

```text
[Describe recovery constraints, dependencies, and approval requirements]
```

---

# 15. Assurance and Testing

## Required Agent Tests

Select all that apply:

```text
[ ] Agent identity test
[ ] Tool permission test
[ ] Unauthorized tool call test
[ ] Prompt injection to action test
[ ] Approval bypass test
[ ] Action boundary test
[ ] Blast-radius limit test
[ ] Logging completeness test
[ ] Kill switch test
[ ] Rollback test
[ ] Incident tabletop
[ ] Regression test
```

## Test Results Summary

| Test | Result | Evidence | Finding |
|---|---|---|---|
| [Test] | [Pass/Fail/Partial/Not Run] | [Evidence] | [Finding] |

## Open Findings

| Finding ID | Finding | Severity | Owner | Due Date | Status |
|---|---|---|---|---|---|
| [Finding ID] | [Finding] | [Low/Medium/High/Critical] | [Owner] | [Date] | [Status] |

---

# 16. Incident Scenarios

## Relevant Agent Incident Scenarios

Select all that apply:

```text
[ ] Agent performs unauthorized action
[ ] Agent calls unauthorized tool
[ ] Agent follows prompt injection
[ ] Agent leaks data through tool use
[ ] Agent modifies incorrect record
[ ] Agent sends unauthorized communication
[ ] Agent loops or retries excessively
[ ] Agent exceeds blast-radius limit
[ ] Agent bypasses approval
[ ] Agent causes customer impact
[ ] Agent causes production impact
[ ] Agent causes security impact
[ ] Agent cannot be stopped quickly
[ ] Agent action cannot be rolled back
```

## Incident Response Path

```text
[Describe escalation, containment, evidence preservation, investigation, recovery, and communication path]
```

---

# 17. Risk Assessment

## Agent Risk Rating

Select one:

```text
[ ] Low
[ ] Medium
[ ] High
[ ] Critical
```

## Risk Drivers

Select all that apply:

```text
[ ] Sensitive data access
[ ] Regulated data access
[ ] Tool/action capability
[ ] High autonomy
[ ] Customer impact
[ ] Employee impact
[ ] Financial impact
[ ] Security impact
[ ] Production impact
[ ] External communication
[ ] Vendor dependency
[ ] Weak logs
[ ] Weak rollback
[ ] Weak kill switch
[ ] Prompt injection exposure
[ ] Approval bypass risk
```

## Risk Notes

```text
[Describe agent risk and residual risk]
```

---

# 18. Approval Decision

## Decision

Select one:

```text
[ ] Approved
[ ] Approved with conditions
[ ] Approved for pilot only
[ ] Requires remediation
[ ] Requires additional testing
[ ] Requires exception approval
[ ] Rejected
[ ] Deferred
```

## Conditions

```text
[List required conditions before agent approval, production use, scaling, or restart]
```

## Exceptions Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Residual Risk Acceptance Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

---

# 19. Approval Record

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

## Incident Response Approval, If Required

```text
Name or forum:
Decision:
Date:
Notes:
```

---

# 20. Summary

```text
Agent:
Use case:
Owner:
Autonomy level:
Identity model:
Data accessed:
Tools available:
High-risk actions:
Approval gates:
Blast-radius limits:
Kill switch:
Rollback:
Logging:
Testing status:
Risk rating:
Approval status:
Next review date:
```