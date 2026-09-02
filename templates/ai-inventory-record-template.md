# AI Inventory Record Template

This template is used to record an AI capability in the enterprise AI inventory.

AI must be inventoried before it is trusted.

The purpose of this template is to make AI systems, AI-enabled features, agents, copilots, RAG systems, vendor AI, internal applications, and embedded AI capabilities visible, owned, classified, risk-tiered, and lifecycle-managed.

---

# 1. Inventory Record Information

## AI Inventory Record ID

```text
[Enter inventory record ID]
```

## AI Use Case Name

```text
[Enter AI use case name]
```

## Date Created

```text
[Enter date]
```

## Last Updated

```text
[Enter date]
```

## Record Owner

```text
Name:
Function:
Email:
```

## Inventory Status

Select one:

```text
[ ] Draft
[ ] Under review
[ ] Active
[ ] Approved
[ ] Pilot
[ ] Production
[ ] Restricted
[ ] Suspended
[ ] Retired
[ ] Rejected
[ ] Archived
```

---

# 2. AI Capability Summary

## Short Description

```text
[Describe what the AI capability does in plain language]
```

## Business Purpose

```text
[Describe the business purpose or outcome supported by this AI capability]
```

## Business Process Supported

```text
[Describe the business process, workflow, product, service, or function supported]
```

## AI Capability Category

Select all that apply:

```text
[ ] Productivity assistant
[ ] Knowledge assistant
[ ] Search or retrieval assistant
[ ] Summarization
[ ] Drafting
[ ] Classification
[ ] Recommendation
[ ] Decision support
[ ] Workflow automation
[ ] Agentic AI
[ ] Customer-facing AI
[ ] Developer AI
[ ] Security operations AI
[ ] Embedded vendor AI
[ ] AI-enabled SaaS
[ ] Internal AI application
[ ] Other
```

## Capability Notes

```text
[Describe any additional context]
```

---

# 3. Ownership

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

## Risk Owner

```text
Name:
Function:
Email:
Not applicable reason, if any:
```

## Incident Contact

```text
Name:
Function:
Email:
Escalation path:
```

---

# 4. AI Pattern Classification

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

## AI Pattern Description

```text
[Describe the AI pattern and how the capability works]
```

## Is This Agentic AI?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Is This Vendor AI?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Is This Customer-Facing?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Is This Action-Capable?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

---

# 5. Lifecycle Status

## Current Lifecycle Stage

Select one:

```text
[ ] Idea
[ ] Proposed
[ ] Intake submitted
[ ] Risk assessment in progress
[ ] Architecture review in progress
[ ] Control assessment in progress
[ ] Assurance testing in progress
[ ] Approved for pilot
[ ] Pilot
[ ] Approved for production
[ ] Production
[ ] Restricted
[ ] Suspended
[ ] Under remediation
[ ] Retired
[ ] Rejected
```

## Lifecycle Notes

```text
[Describe current lifecycle status, constraints, and next steps]
```

## Approval Status

Select one:

```text
[ ] Not submitted
[ ] Submitted
[ ] Approved
[ ] Approved with conditions
[ ] Approved for pilot only
[ ] Requires remediation
[ ] Requires exception approval
[ ] Rejected
[ ] Deferred
```

## Approval Reference

```text
[Enter approval reference or link]
```

---

# 6. Users and Exposure

## Intended Users

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

## User Population Size

```text
Estimated number of users:
```

## Exposure Type

Select one:

```text
[ ] Internal only
[ ] Internal with vendor processing
[ ] Partner-facing
[ ] Supplier-facing
[ ] Customer-facing
[ ] Public-facing
[ ] Unknown
```

## Geography / Region

```text
[Describe regions, countries, jurisdictions, or business units where this AI capability is used]
```

---

# 7. Data Classification

## Data Used by AI

Select all that apply:

```text
[ ] No enterprise data
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

## Data Sources

| Data Source | System / Repository | Owner | Classification | Approved? |
|---|---|---|---|---|
| [Source] | [System] | [Owner] | [Classification] | [Yes/No/Pending] |

## Highest Data Classification

Select one:

```text
[ ] Public
[ ] Internal
[ ] Confidential
[ ] Restricted
[ ] Regulated
[ ] Highly sensitive
[ ] Unknown
```

## Data Boundary Reference

```text
[Enter data boundary record reference or link]
```

---

# 8. Model, Vendor, and Platform

## AI Model or Service

```text
Model/service name:
Provider:
Version, if known:
```

## Hosting / Delivery Model

Select one:

```text
[ ] Internal model
[ ] Hosted model API
[ ] Cloud AI service
[ ] SaaS AI feature
[ ] Embedded vendor AI
[ ] Open-source model hosted internally
[ ] Open-source model hosted externally
[ ] Unknown
[ ] Other
```

## Vendor / Platform

```text
Vendor/platform name:
Contract owner:
Vendor assessment reference:
```

## Vendor Processing

Select all that apply:

```text
[ ] No vendor processing
[ ] Vendor processes prompts
[ ] Vendor processes outputs
[ ] Vendor processes uploaded files
[ ] Vendor processes retrieved context
[ ] Vendor retains prompts
[ ] Vendor retains outputs
[ ] Vendor uses data for training
[ ] Vendor uses data for product improvement
[ ] Unknown
```

## Vendor Notes

```text
[Describe vendor processing, retention, reuse, evidence, and incident support]
```

---

# 9. Identity and Access

## AI Identity Model

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

## AI Identity Description

```text
[Describe how AI identity and authority are represented]
```

## Access Scope

```text
[Describe systems, data, tools, APIs, workflows, or environments AI can access]
```

## Access Approval Reference

```text
[Enter access approval reference or link]
```

## Access Review Frequency

Select one:

```text
[ ] Monthly
[ ] Quarterly
[ ] Semi-annually
[ ] Annually
[ ] At material change
[ ] Not defined
[ ] Not applicable
```

## Revocation Path

```text
[Describe how access can be revoked, suspended, disabled, or rotated]
```

---

# 10. Prompt and Input Profile

## Input Types

Select all that apply:

```text
[ ] User prompts
[ ] System prompts
[ ] Developer prompts
[ ] Uploaded files
[ ] Retrieved documents
[ ] Emails
[ ] Tickets
[ ] Chat messages
[ ] Customer submissions
[ ] API payloads
[ ] Tool responses
[ ] Web content
[ ] Code
[ ] Logs
[ ] Workflow data
[ ] Conversation history
[ ] Memory
[ ] Other
```

## External or Untrusted Inputs

```text
[ ] No
[ ] Yes
[ ] Unknown
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

## Prompt/Input Control Reference

```text
[Enter prompt and input control record reference or link]
```

---

# 11. Output and Decision Profile

## Output Types

Select all that apply:

```text
[ ] Informational answer
[ ] Summary
[ ] Draft
[ ] Classification
[ ] Recommendation
[ ] Score
[ ] Extracted data
[ ] Generated code
[ ] Customer response
[ ] Internal communication
[ ] Decision support
[ ] Workflow instruction
[ ] Action request
[ ] Generated record
[ ] Other
```

## Does Output Influence Decisions?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Decision Impact Level

Select one:

```text
[ ] None
[ ] Low
[ ] Moderate
[ ] High
[ ] Critical
[ ] Unknown
```

## Does Output Become a Record?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Output and Decision Control Reference

```text
[Enter output and decision control record reference or link]
```

---

# 12. Tool and Action Capability

## Can AI Use Tools, APIs, or Workflows?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Tool / Action Types

Select all that apply:

```text
[ ] No tool or action capability
[ ] Read-only retrieval
[ ] Draft-only action
[ ] API call
[ ] Workflow trigger
[ ] Ticket creation
[ ] Record creation
[ ] Record modification
[ ] Communication sending
[ ] Access request or approval
[ ] Financial transaction
[ ] Security action
[ ] Production system change
[ ] Administrative action
[ ] Code execution
[ ] Other
```

## Highest Action Risk

Select one:

```text
[ ] None
[ ] Low
[ ] Moderate
[ ] High
[ ] Critical
[ ] Unknown
```

## Tool and Action Control Reference

```text
[Enter tool/action control record reference or link]
```

---

# 13. Human Accountability

## Human Review Model

Select one:

```text
[ ] No human review
[ ] Human-in-the-loop
[ ] Human-on-the-loop
[ ] Human-over-the-loop
[ ] Exception-based review
[ ] Sampling review
[ ] Continuous monitoring
[ ] Not yet defined
```

## Decision Owner Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Decision Owner

```text
Name:
Function:
Email:
Not applicable reason, if any:
```

## Accountability Reference

```text
[Enter human accountability record reference or link]
```

---

# 14. Risk Tier

## Assigned Risk Tier

Select one:

```text
[ ] Tier 1: Low-risk productivity or public-data use
[ ] Tier 2: Internal productivity with enterprise data
[ ] Tier 3: Decision-supporting AI
[ ] Tier 4: Action-capable AI
[ ] Tier 5: High-impact autonomous or regulated AI
[ ] Unknown / pending assessment
```

## Risk Tier Rationale

```text
[Explain why this risk tier was selected]
```

## Highest Risk Drivers

Select all that apply:

```text
[ ] Sensitive data
[ ] Regulated data
[ ] Personal data
[ ] Customer impact
[ ] Employee impact
[ ] Financial impact
[ ] Legal or compliance impact
[ ] Security impact
[ ] Production impact
[ ] Decision influence
[ ] Tool/action capability
[ ] Agentic autonomy
[ ] External exposure
[ ] Vendor dependency
[ ] Low recoverability
[ ] Weak evidence
[ ] Unknown risk
```

## Risk Assessment Reference

```text
[Enter risk assessment record reference or link]
```

---

# 15. Required Control Records

## Control Records

| Control Record | Required? | Reference / Link | Status |
|---|---|---|---|
| AI use case intake | [Yes/No] | [Reference] | [Status] |
| AI risk assessment | [Yes/No] | [Reference] | [Status] |
| AI control assessment | [Yes/No] | [Reference] | [Status] |
| AI architecture decision record | [Yes/No] | [Reference] | [Status] |
| AI data boundary record | [Yes/No] | [Reference] | [Status] |
| AI prompt/input control record | [Yes/No] | [Reference] | [Status] |
| AI output/decision control record | [Yes/No] | [Reference] | [Status] |
| AI tool/action control record | [Yes/No] | [Reference] | [Status] |
| AI human accountability record | [Yes/No] | [Reference] | [Status] |
| AI monitoring/evidence record | [Yes/No] | [Reference] | [Status] |
| AI incident containment/recovery record | [Yes/No] | [Reference] | [Status] |
| AI vendor assessment | [Yes/No] | [Reference] | [Status] |
| AI assurance test plan | [Yes/No] | [Reference] | [Status] |
| AI exception record | [Yes/No] | [Reference] | [Status] |

---

# 16. Assurance and Testing

## Assurance Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Required Assurance Activities

Select all that apply:

```text
[ ] Design review
[ ] Pre-deployment testing
[ ] Prompt injection testing
[ ] Data leakage testing
[ ] Retrieval boundary testing
[ ] Output validation testing
[ ] Tool misuse testing
[ ] Approval gate testing
[ ] Logging completeness testing
[ ] Evidence reconstruction testing
[ ] Kill switch testing
[ ] Rollback testing
[ ] Vendor assurance review
[ ] Regression testing
[ ] Incident tabletop
```

## Assurance Test Plan Reference

```text
[Enter assurance test plan reference or link]
```

## Assurance Status

Select one:

```text
[ ] Not required
[ ] Not started
[ ] In progress
[ ] Passed
[ ] Passed with conditions
[ ] Failed
[ ] Deferred
```

---

# 17. Monitoring, Logging, and Evidence

## Logging Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Logging Depth

Select one:

```text
[ ] Basic usage metadata
[ ] Usage logs and input/output metadata
[ ] Output, validation, reviewer, and decision evidence
[ ] Tool call, action, approval, and boundary evidence
[ ] Full reconstructable evidence
[ ] Unknown
```

## Monitoring Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Evidence Repository

```text
[Describe evidence location or repository]
```

## Monitoring / Evidence Reference

```text
[Enter monitoring/logging/evidence record reference or link]
```

---

# 18. Incident Containment and Recovery

## AI Incident Scenarios Identified?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Kill Switch Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Recovery or Correction Path Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Incident Containment / Recovery Reference

```text
[Enter incident containment and recovery record reference or link]
```

---

# 19. Exceptions

## Exceptions Exist?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Exception Summary

| Exception ID | Requirement Affected | Expiry Date | Owner | Status |
|---|---|---|---|---|
| [Exception] | [Requirement] | [Date] | [Owner] | [Status] |

## Exception Notes

```text
[Describe exception risk, compensating controls, and remediation]
```

---

# 20. Review and Recertification

## Inventory Review Frequency

Select one:

```text
[ ] Monthly
[ ] Quarterly
[ ] Semi-annually
[ ] Annually
[ ] At material change
[ ] Other
```

## Last Reviewed

```text
[Enter date]
```

## Next Review Date

```text
[Enter date]
```

## Review Triggers

Select all that apply:

```text
[ ] Business owner changes
[ ] Technical owner changes
[ ] Vendor changes
[ ] Model changes
[ ] Data source changes
[ ] Risk tier changes
[ ] User population changes
[ ] Output use changes
[ ] Tool/action capability changes
[ ] Incident occurs
[ ] Assurance finding occurs
[ ] Exception expires
[ ] Regulatory or legal requirement changes
```

---

# 21. Approval

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

## Governance / Architecture Approval

```text
Name or forum:
Decision:
Date:
Notes:
```

## Final Inventory Decision

Select one:

```text
[ ] Approved
[ ] Approved with conditions
[ ] Approved for pilot only
[ ] Requires remediation
[ ] Requires exception approval
[ ] Requires additional review
[ ] Rejected
[ ] Deferred
[ ] Retired
```

## Approval Conditions

```text
[List conditions required before approval, production use, scaling, or continued operation]
```

---

# 22. Summary

```text
Inventory ID:
Use case:
Business owner:
Technical owner:
AI pattern:
Lifecycle status:
User population:
Data classification:
Vendor involvement:
Identity model:
Decision impact:
Tool/action capability:
Risk tier:
Required controls:
Assurance status:
Logging status:
Incident containment status:
Exceptions:
Approval status:
Next review date:
```