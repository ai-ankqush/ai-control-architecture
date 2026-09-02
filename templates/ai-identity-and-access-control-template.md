# AI Identity and Access Control Template

This template is used to define, approve, test, and evidence the identity and access control model for an AI use case.

AI must not receive authority without identity.

The purpose of this template is to ensure AI actors, agents, applications, copilots, vendor AI features, service identities, delegated authority, access scopes, privileged access, access reviews, attribution, and revocation paths are clearly defined and controlled.

---

# 1. Identity and Access Control Information

## AI Use Case Name

```text
[Enter AI use case name]
```

## Identity / Access Control ID

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

## IAM Owner

```text
Name:
Function:
Email:
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

# 3. AI Actor Identification

## AI Actors In Scope

Select all that apply:

```text
[ ] Human user using AI
[ ] Copilot
[ ] Internal AI application
[ ] AI agent
[ ] AI workflow
[ ] Service account
[ ] Application identity
[ ] Vendor-managed AI identity
[ ] Embedded SaaS AI feature
[ ] API-based AI service
[ ] Tool-calling AI
[ ] Other
```

## AI Actor Summary

| AI Actor | Description | Owner | Identity Required? | Notes |
|---|---|---|---|---|
| [Actor] | [Description] | [Owner] | [Yes/No] | [Notes] |

## Actor Notes

```text
[Describe all AI actors, users, services, agents, vendors, and delegated processes involved]
```

---

# 4. Identity Model

## Identity Model Selected

Select all that apply:

```text
[ ] Direct user identity
[ ] Delegated user authority
[ ] Service identity
[ ] Application identity
[ ] Agent identity
[ ] Vendor-managed identity
[ ] Hybrid identity
[ ] Not applicable
[ ] Unknown
```

## Identity Model Description

```text
[Describe how AI identity is represented and how AI activity is distinguished from human activity]
```

## Identity Records

| Identity | Type | Owner | Purpose | Approved? |
|---|---|---|---|---|
| [Identity] | [User/Service/App/Agent/Vendor] | [Owner] | [Purpose] | [Yes/No/Pending] |

## Identity Model Rationale

```text
[Explain why this identity model is appropriate for the AI use case and risk tier]
```

---

# 5. Delegated Authority

## Delegated Authority Used?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Delegation Model

Select all that apply:

```text
[ ] AI acts only as current user
[ ] AI acts on behalf of user with explicit consent
[ ] AI acts on behalf of user with session-based delegation
[ ] AI acts through service account
[ ] AI acts through agent identity
[ ] AI acts through vendor-managed identity
[ ] AI acts through workflow identity
[ ] Other
```

## Delegated Authority Scope

```text
[Describe what authority is delegated, by whom, for what purpose, and under what conditions]
```

## Delegation Constraints

```text
[Describe limits on delegated authority, such as time, system, data, action, workflow, or approval boundaries]
```

## Delegation Evidence

```text
[Describe where delegation approvals, consent, logs, or records are stored]
```

---

# 6. Access Scope

## Systems Accessible to AI

| System / Platform | Access Type | Identity Used | Owner | Approved? |
|---|---|---|---|---|
| [System] | [Read/Write/Admin/Tool/API] | [Identity] | [Owner] | [Yes/No/Pending] |

## Data Sources Accessible to AI

| Data Source | Classification | Access Type | Boundary | Approved? |
|---|---|---|---|---|
| [Data source] | [Classification] | [Read/Retrieve/Process] | [Boundary] | [Yes/No/Pending] |

## Tools / APIs Accessible to AI

| Tool / API | Action Type | Identity Used | Risk Level | Approved? |
|---|---|---|---|---|
| [Tool/API] | [Read/Write/Action/Admin] | [Identity] | [Low/Medium/High/Critical] | [Yes/No/Pending] |

## Access Scope Notes

```text
[Describe approved access scope and restrictions]
```

---

# 7. Least Privilege

## Least Privilege Applied?

```text
[ ] No
[ ] Yes
[ ] Partial
[ ] Unknown
```

## Least Privilege Controls

Select all that apply:

```text
[ ] Role-based access
[ ] Attribute-based access
[ ] Policy-based access
[ ] Data classification filtering
[ ] Repository allowlist
[ ] Repository denylist
[ ] Tool allowlist
[ ] Tool denylist
[ ] API method restriction
[ ] Environment restriction
[ ] Time-bound access
[ ] Rate limits
[ ] Transaction limits
[ ] Approval-gated access
[ ] Other
```

## Access Justification

```text
[Explain why each access permission is necessary for the approved use case]
```

## Excessive Access Identified?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Excessive Access Notes

```text
[Describe excessive access, remediation actions, or compensating controls]
```

---

# 8. Privileged Access

## Privileged Access Used?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Privileged Access Types

Select all that apply:

```text
[ ] Administrative access
[ ] Production access
[ ] Security tool access
[ ] Access grant/revoke capability
[ ] Configuration change capability
[ ] Financial transaction capability
[ ] Data export capability
[ ] Secret or credential access
[ ] System command execution
[ ] Code deployment
[ ] Other
```

## Privileged Access Controls

Select all that apply:

```text
[ ] PAM control
[ ] Just-in-time access
[ ] Approval required
[ ] Dual approval
[ ] Session recording
[ ] Break-glass process
[ ] Segregation of duties
[ ] Enhanced logging
[ ] Periodic access review
[ ] Immediate revocation path
[ ] Other
```

## Privileged Access Notes

```text
[Describe privileged access risk, approvals, monitoring, and restrictions]
```

---

# 9. Access Approval

## Access Approval Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Access Approval Matrix

| Access Requested | Approver | Approval Date | Evidence | Expiry |
|---|---|---|---|---|
| [Access] | [Approver] | [Date] | [Evidence] | [Expiry] |

## Approval Conditions

```text
[Describe conditions that apply to access approval]
```

## Access Approval Notes

```text
[Describe approval gaps, pending approvals, or required remediation]
```

---

# 10. Access Review

## Access Review Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Access Review Frequency

Select one:

```text
[ ] Monthly
[ ] Quarterly
[ ] Semi-annually
[ ] Annually
[ ] At material change
[ ] After incident
[ ] Other
```

## Access Review Scope

Select all that apply:

```text
[ ] AI identities
[ ] Agent identities
[ ] Service accounts
[ ] Application permissions
[ ] Delegated authority
[ ] Data source access
[ ] Tool access
[ ] API access
[ ] Privileged access
[ ] Vendor-managed access
[ ] Other
```

## Last Access Review

```text
Date:
Reviewer:
Result:
Evidence:
```

## Next Access Review

```text
[Enter date]
```

## Access Review Notes

```text
[Describe findings, removals, confirmations, or open access issues]
```

---

# 11. Attribution and Auditability

## AI-Mediated Activity Distinguishable?

```text
[ ] No
[ ] Yes
[ ] Partial
[ ] Unknown
```

## Attribution Requirements

Select all that apply:

```text
[ ] Identify initiating user
[ ] Identify AI system
[ ] Identify AI identity
[ ] Identify agent identity
[ ] Identify delegated authority
[ ] Identify service account
[ ] Identify tool or API used
[ ] Identify action performed
[ ] Identify approval record
[ ] Identify downstream system affected
[ ] Other
```

## Attribution Evidence

```text
[Describe logs or records that show who or what performed AI-mediated activity]
```

## Attribution Notes

```text
[Describe attribution gaps or investigation limitations]
```

---

# 12. Session and Token Control

## Sessions or Tokens Used?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Session / Token Controls

Select all that apply:

```text
[ ] Session timeout
[ ] Token expiry
[ ] Token rotation
[ ] Scope-limited token
[ ] User-bound token
[ ] Service-bound token
[ ] Approval-bound token
[ ] Revocable token
[ ] Refresh token restrictions
[ ] Secret storage control
[ ] Other
```

## Session / Token Notes

```text
[Describe session, token, credential, and secret handling controls]
```

---

# 13. Vendor-Managed Identity

Complete this section if vendor AI is involved.

## Vendor-Managed Identity Used?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Vendor Identity Model

```text
[Describe how the vendor represents user, application, AI, agent, or service identity]
```

## Does Vendor AI Respect Enterprise Permissions?

```text
[ ] No
[ ] Yes
[ ] Partial
[ ] Unknown
```

## Can Vendor AI Activity Be Audited?

```text
[ ] No
[ ] Yes
[ ] Partial
[ ] Unknown
```

## Vendor Access Revocation

```text
[Describe how vendor AI access can be disabled or restricted]
```

## Vendor Identity Notes

```text
[Describe vendor identity limitations, evidence gaps, or contractual needs]
```

---

# 14. Access Revocation and Emergency Disablement

## Revocation Path Defined?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Revocation Options

Select all that apply:

```text
[ ] Disable AI identity
[ ] Disable agent identity
[ ] Disable service account
[ ] Remove application permission
[ ] Revoke delegated authority
[ ] Revoke tool permission
[ ] Revoke API key
[ ] Rotate credentials
[ ] Remove data source access
[ ] Disable vendor AI feature
[ ] Disable user group access
[ ] Disable workflow integration
[ ] Other
```

## Revocation Matrix

| Access Type | Revocation Method | Owner | Expected Time | Evidence |
|---|---|---|---|---|
| [Access] | [Method] | [Owner] | [Time] | [Evidence] |

## Emergency Disablement Notes

```text
[Describe emergency access revocation process, dependencies, and limitations]
```

---

# 15. Monitoring and Logging

## Identity and Access Logging Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Required Logs

Select all that apply:

```text
[ ] AI identity creation
[ ] AI identity change
[ ] AI identity disablement
[ ] Access request
[ ] Access approval
[ ] Access denial
[ ] Access review
[ ] Delegated authority granted
[ ] Delegated authority used
[ ] Data access
[ ] Tool access
[ ] API access
[ ] Privileged access
[ ] Revocation event
[ ] Failed access attempt
[ ] Policy violation
[ ] Other
```

## Log Location

```text
[Describe where identity and access logs are stored]
```

## Monitoring Rules

Select all that apply:

```text
[ ] Unusual access volume
[ ] Access outside approved scope
[ ] Privileged access use
[ ] Failed access attempts
[ ] Access after revocation
[ ] Delegated authority anomaly
[ ] Vendor access anomaly
[ ] Agent access anomaly
[ ] Other
```

## Monitoring Notes

```text
[Describe monitoring, alerting, routing, and escalation]
```

---

# 16. Testing and Assurance

## Required Tests

Select all that apply:

```text
[ ] Identity model review
[ ] Access approval test
[ ] Least privilege test
[ ] Delegated authority test
[ ] Privileged access test
[ ] Attribution test
[ ] Session/token control test
[ ] Vendor identity review
[ ] Access revocation test
[ ] Access logging test
[ ] Policy violation alert test
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

## IAM / Security Approval

```text
Name or forum:
Decision:
Date:
Notes:
```

## Data Owner Approval, If Required

```text
Name:
Decision:
Date:
Notes:
Not applicable reason, if any:
```

## Final Identity and Access Decision

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
[List conditions required before approval, production use, scaling, or continued operation]
```

---

# 19. Review Triggers

Review this identity and access control design if any of the following occur:

```text
[ ] AI identity changes
[ ] Agent identity changes
[ ] Service account changes
[ ] Delegated authority changes
[ ] Data source access changes
[ ] Tool/API access changes
[ ] Privileged access changes
[ ] Vendor identity model changes
[ ] User population changes
[ ] Risk tier changes
[ ] Incident occurs
[ ] Assurance finding occurs
[ ] Access review finding occurs
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
AI actors:
Identity model:
Delegated authority:
Systems accessible:
Data accessible:
Tools/APIs accessible:
Privileged access:
Least privilege status:
Access review frequency:
Attribution:
Revocation path:
Monitoring:
Required testing:
Exceptions:
Approval status:
Next review date:
```