# AI Data Boundary Template

This template is used to define, approve, test, and evidence the data boundaries for an AI use case.

AI data control does not end at access.

AI systems may expose data through prompts, retrieved context, embeddings, outputs, logs, vendor processing, downstream workflows, retained history, and inference.

The purpose of this template is to define what data AI can access, process, retrieve, retain, expose, reuse, or send to vendors.

---

# 1. Data Boundary Information

## AI Use Case Name

```text
[Enter AI use case name]
```

## Data Boundary ID

```text
[Enter data boundary ID]
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

## Data Owner

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

# 3. Data Boundary Statement

## Approved Data Boundary

```text
[Describe the approved data boundary for this AI use case]
```

## Business Purpose for Data Use

```text
[Explain why this AI use case needs access to the data]
```

## Data Minimization Statement

```text
[Describe how data access is limited to the minimum required for the approved use case]
```

## Prohibited Data Use

```text
[Describe data that must not be accessed, processed, retrieved, retained, exposed, or reused]
```

---

# 4. Data Source Mapping

| Data Source | System / Repository | Data Owner | Classification | Access Type | Approved? |
|---|---|---|---|---|---|
| [Source] | [System] | [Owner] | [Classification] | [Prompt/Retrieval/API/File/Vendor] | [Yes/No/Pending] |

## Data Source Notes

```text
[Describe source-specific restrictions, approvals, or concerns]
```

---

# 5. Data Classification

## Data Classes In Scope

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

## Classification Notes

```text
[Describe classification rationale and handling expectations]
```

---

# 6. Allowed Data

## Allowed Data Types

```text
[List data types the AI is allowed to access, process, retrieve, or generate]
```

## Allowed Repositories or Systems

```text
[List approved repositories, systems, databases, SaaS platforms, or knowledge sources]
```

## Allowed User Groups

```text
[List users, roles, business units, or groups allowed to use this data through the AI system]
```

## Allowed Use Cases

```text
[List approved purposes for which this data may be used by AI]
```

---

# 7. Restricted or Prohibited Data

## Restricted Data Types

```text
[List data types that require special approval or additional controls]
```

## Prohibited Data Types

```text
[List data types that must not be used by this AI system]
```

## Prohibited Sources

```text
[List repositories, systems, or sources that AI must not access]
```

## Secrets and Credentials

```text
[Describe controls to prevent secrets, tokens, credentials, private keys, and production secrets from entering prompts, context, outputs, or logs]
```

---

# 8. Retrieval Boundary

Complete this section if the AI use case uses retrieval, search, RAG, enterprise knowledge, or document grounding.

## Retrieval Used?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Retrieval Boundary Description

```text
[Describe what the AI can retrieve and what it cannot retrieve]
```

## Retrieval Controls

Select all that apply:

```text
[ ] User permission inheritance
[ ] Role-based retrieval
[ ] Attribute-based retrieval
[ ] Repository allowlist
[ ] Repository denylist
[ ] Document-level permissions
[ ] Metadata filtering
[ ] Classification filtering
[ ] Tenant filtering
[ ] Project or workspace filtering
[ ] Customer/account filtering
[ ] Geographic filtering
[ ] Sensitive source exclusion
[ ] Manual data owner approval
[ ] Other
```

## Retrieval Boundary Table

| Boundary Type | Rule | Enforcement Method | Owner | Evidence |
|---|---|---|---|---|
| [Boundary] | [Rule] | [Method] | [Owner] | [Evidence] |

## Retrieval Testing Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Retrieval Test Notes

```text
[Describe tests required to verify retrieval boundaries]
```

---

# 9. Prompt and Input Data Boundary

## Prompt/Input Data Allowed

```text
[Describe what users or systems may submit into the AI system]
```

## Prompt/Input Data Prohibited

```text
[Describe what users or systems must not submit]
```

## Sensitive Data Detection

Select all that apply:

```text
[ ] Not required
[ ] User guidance only
[ ] Warning
[ ] Redaction
[ ] Masking
[ ] Blocking
[ ] DLP integration
[ ] Manual approval
[ ] Escalation
[ ] Unknown
```

## Prompt/Input Logging Approach

Select one:

```text
[ ] No prompt content logging
[ ] Metadata-only logging
[ ] Redacted prompt logging
[ ] Full prompt logging
[ ] Reference or hash only
[ ] Violation-only logging
[ ] Unknown
```

## Prompt/Input Notes

```text
[Describe prompt data risks, restrictions, and logging approach]
```

---

# 10. Context Assembly Boundary

## Context Sources

Select all that apply:

```text
[ ] User prompt
[ ] System prompt
[ ] Retrieved documents
[ ] Conversation history
[ ] Memory
[ ] Tool responses
[ ] Workflow state
[ ] User metadata
[ ] Application metadata
[ ] External content
[ ] Other
```

## Context Isolation Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Context Isolation Boundaries

Select all that apply:

```text
[ ] User
[ ] Session
[ ] Tenant
[ ] Business unit
[ ] Project
[ ] Repository
[ ] Customer account
[ ] Data classification
[ ] Trust level
[ ] Internal vs external
[ ] Production vs non-production
[ ] Other
```

## Context Assembly Controls

```text
[Describe how context is selected, minimized, labeled, isolated, and protected]
```

---

# 11. Model, Vendor, and Processing Boundary

## AI Processing Model

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

## Vendor or Platform

```text
Vendor/platform:
Model/service:
Processing location:
```

## Does Data Leave the Enterprise Boundary?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Cross-Boundary Movement

Select all that apply:

```text
[ ] No cross-boundary movement
[ ] Vendor boundary
[ ] Cloud boundary
[ ] Geographic boundary
[ ] Jurisdictional boundary
[ ] Tenant boundary
[ ] Business unit boundary
[ ] Production/non-production boundary
[ ] Internal/external boundary
[ ] Unknown
```

## Vendor Processing Notes

```text
[Describe vendor processing, location, subprocessors, contractual restrictions, and shared responsibility]
```

---

# 12. Retention and Reuse

## Data Retained

Select all that apply:

```text
[ ] Prompts
[ ] Uploaded files
[ ] Retrieved context
[ ] Embeddings
[ ] Model inputs
[ ] Model outputs
[ ] Conversation history
[ ] Memory
[ ] Tool call logs
[ ] Approval logs
[ ] Generated records
[ ] Audit evidence
[ ] Vendor telemetry
[ ] Training datasets
[ ] Fine-tuning datasets
[ ] None
[ ] Unknown
```

## Retention Period

```text
[Describe retention period by data type]
```

## Deletion Process

```text
[Describe how data is deleted and who owns deletion]
```

## Training Allowed?

```text
[ ] No
[ ] Yes
[ ] Only with approval
[ ] Unknown
```

## Product Improvement or Analytics Allowed?

```text
[ ] No
[ ] Yes
[ ] Only with approval
[ ] Unknown
```

## Fine-Tuning Allowed?

```text
[ ] No
[ ] Yes
[ ] Only with approval
[ ] Unknown
```

## Retention and Reuse Notes

```text
[Describe restrictions on retention, training, fine-tuning, analytics, telemetry, or product improvement]
```

---

# 13. Output Data Boundary

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

## Output Sensitivity Rule

```text
[Describe whether output inherits classification from source data and how sensitivity is preserved]
```

## Output Sharing Restrictions

```text
[Describe who can receive or use AI outputs]
```

## Output Logging Approach

Select one:

```text
[ ] No output content logging
[ ] Metadata-only logging
[ ] Redacted output logging
[ ] Full output logging
[ ] Reference or hash only
[ ] Violation-only logging
[ ] Unknown
```

## Output Boundary Notes

```text
[Describe output sensitivity, sharing, downstream use, generated records, and correction requirements]
```

---

# 14. Downstream Use Boundary

## Downstream Use Allowed?

```text
[ ] No
[ ] Yes
[ ] Conditional
[ ] Unknown
```

## Downstream Systems or Workflows

| Downstream System / Workflow | Output Used | Control Required | Owner |
|---|---|---|---|
| [System] | [Output] | [Control] | [Owner] |

## Downstream Use Restrictions

```text
[Describe restrictions before AI output can be used by downstream systems, workflows, records, or decisions]
```

## Decision or Action Impact

```text
[Describe whether output influences decisions, records, workflows, or actions]
```

---

# 15. Logging and Evidence Boundary

## Required Evidence

Select all that apply:

```text
[ ] Data source map
[ ] Data owner approval
[ ] Data classification
[ ] Retrieval configuration
[ ] Retrieval logs
[ ] Data access logs
[ ] Prompt/input logs or metadata
[ ] Output logs or metadata
[ ] Training/reuse restriction
[ ] Retention rule
[ ] Vendor processing record
[ ] Cross-boundary transfer record
[ ] Leakage test result
[ ] Exception record
```

## Evidence Location

```text
[Describe where evidence is stored]
```

## Evidence Access Restrictions

```text
[Describe who can access evidence and how evidence is protected]
```

## Evidence Retention

```text
[Describe how long evidence is retained]
```

---

# 16. Data Boundary Testing

## Tests Required

Select all that apply:

```text
[ ] Data source approval check
[ ] Data classification check
[ ] Retrieval boundary test
[ ] Cross-user retrieval test
[ ] Cross-tenant retrieval test
[ ] Sensitive data prompt test
[ ] Sensitive data output leakage test
[ ] Prompt injection through retrieved content test
[ ] Vendor retention setting review
[ ] Training/reuse setting review
[ ] Output sensitivity review
[ ] Log sensitivity review
[ ] Cross-boundary transfer review
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

## Data Owner Approval

```text
Name:
Decision:
Date:
Notes:
```

## Business Owner Approval

```text
Name:
Decision:
Date:
Notes:
```

## Privacy / Legal Approval, If Required

```text
Name or forum:
Decision:
Date:
Notes:
Not applicable reason, if any:
```

## Security / Architecture Approval

```text
Name or forum:
Decision:
Date:
Notes:
```

## Final Data Boundary Decision

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
```

## Approval Conditions

```text
[List conditions required before approval, production use, or scaling]
```

---

# 19. Review Triggers

Review this data boundary if any of the following occur:

```text
[ ] Data source changes
[ ] Data classification changes
[ ] Vendor processing changes
[ ] Retention setting changes
[ ] Training/reuse setting changes
[ ] Retrieval logic changes
[ ] User population changes
[ ] Output use changes
[ ] Downstream workflow changes
[ ] Risk tier changes
[ ] Incident occurs
[ ] Assurance finding occurs
[ ] Regulatory or legal requirement changes
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
Data sources:
Highest data classification:
Retrieval boundary:
Vendor processing:
Retention:
Training/reuse:
Output sensitivity:
Required evidence:
Required testing:
Exceptions:
Approval status:
Next review date:
```