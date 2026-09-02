# AI Architecture Decision Record Template

This template is used to document architecture decisions for AI use cases, AI control designs, AI patterns, AI integrations, AI vendors, AI agents, and AI-enabled workflows.

An Architecture Decision Record captures the decision, context, options considered, rationale, consequences, controls required, evidence required, and review conditions.

The purpose is to make AI architecture decisions traceable, reviewable, and reusable.

---

# 1. Decision Information

## Decision Title

```text
[Enter short decision title]
```

## Decision ID

```text
[Enter decision ID]
```

## Date

```text
[Enter date]
```

## Status

Select one:

```text
[ ] Proposed
[ ] Under review
[ ] Approved
[ ] Approved with conditions
[ ] Rejected
[ ] Superseded
[ ] Deprecated
[ ] Deferred
```

## Decision Owner

```text
Name:
Function:
Email:
```

## Related AI Use Case

```text
[Enter AI use case name]
```

## Related AI Inventory Record

```text
[Enter inventory record reference or link]
```

## Related Documents

```text
[Reference intake, risk assessment, control assessment, assurance plan, vendor assessment, incident record, or other related documents]
```

---

# 2. Decision Context

## Background

```text
[Describe the context that led to this architecture decision]
```

## Business Need

```text
[Describe the business need or problem this decision addresses]
```

## Technical Context

```text
[Describe the technical environment, systems, platforms, data sources, vendors, tools, workflows, or integrations involved]
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
[ ] Unknown / pending assessment
```

---

# 3. Decision Statement

## Architecture Decision

```text
[State the decision clearly. Example: The AI use case will use user-delegated identity for retrieval and a separate agent identity for tool execution.]
```

## Decision Summary

```text
[Summarize the decision in one or two paragraphs]
```

## Decision Scope

Select all that apply:

```text
[ ] AI pattern
[ ] Model or AI service
[ ] Vendor or platform
[ ] Identity model
[ ] Data boundary
[ ] Retrieval architecture
[ ] Prompt/input control
[ ] Output/decision control
[ ] Tool/action control
[ ] Human accountability
[ ] Monitoring/logging/evidence
[ ] Assurance/testing
[ ] Incident containment/recovery
[ ] Operating model
[ ] Other
```

---

# 4. Options Considered

## Option 1

```text
Option name:
Description:
Benefits:
Risks:
Control implications:
Reason accepted or rejected:
```

## Option 2

```text
Option name:
Description:
Benefits:
Risks:
Control implications:
Reason accepted or rejected:
```

## Option 3

```text
Option name:
Description:
Benefits:
Risks:
Control implications:
Reason accepted or rejected:
```

## Additional Options

```text
[Add additional options if required]
```

---

# 5. Architecture Principles Considered

Select all applicable principles:

```text
[ ] AI must be inventoried before it is trusted.
[ ] AI must not receive authority without identity.
[ ] AI must not access data without boundaries.
[ ] AI inputs must be treated as control surfaces.
[ ] AI outputs must not become decisions without control.
[ ] AI must not execute actions without control.
[ ] Human accountability must remain assigned.
[ ] AI must be tested before and after deployment.
[ ] AI must be observable and reconstructable.
[ ] AI failure must be containable.
```

## Principle Alignment Notes

```text
[Describe how the decision aligns with or deviates from relevant principles]
```

---

# 6. Control Impact Assessment

## AI Inventory and Classification

```text
[Describe inventory, classification, lifecycle, and risk-tier implications]
```

## AI Identity and Access Control

```text
[Describe identity model, delegated authority, service accounts, agent identities, access review, and revocation implications]
```

## Data Boundary Control

```text
[Describe data sources, data classification, retrieval boundaries, retention, training/reuse, and output sensitivity implications]
```

## Prompt and Input Control

```text
[Describe allowed inputs, prohibited inputs, prompt injection risk, system prompt protection, context isolation, and input logging implications]
```

## Output and Decision Control

```text
[Describe output classification, validation, review, approval, generated records, downstream use, and correction implications]
```

## Tool and Action Control

```text
[Describe tools, APIs, workflows, action classification, approval gates, blast-radius limits, kill switches, and rollback implications]
```

## Human Accountability Model

```text
[Describe business owner, technical owner, decision owner, approver, escalation, override, and exception ownership implications]
```

## AI Assurance and Testing

```text
[Describe required testing, validation, prompt injection testing, data leakage testing, tool/action testing, regression testing, and assurance evidence]
```

## Monitoring, Logging, and Evidence

```text
[Describe required logs, evidence, monitoring, retention, reconstruction, SIEM/SOC/GRC integration, and audit needs]
```

## Incident Containment and Recovery

```text
[Describe containment paths, revocation, kill switches, evidence preservation, rollback, vendor escalation, and recovery implications]
```

---

# 7. Identity and Access Decision

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
```

## Identity Decision Rationale

```text
[Explain why this identity model was selected]
```

## Access Boundary

```text
[Describe systems, data, tools, APIs, workflows, and environments AI can access]
```

## Revocation Path

```text
[Describe how access can be revoked, suspended, disabled, or rotated]
```

---

# 8. Data Boundary Decision

## Data Sources Approved

| Data Source | Classification | Owner | Boundary / Restriction |
|---|---|---|---|
| [Source] | [Classification] | [Owner] | [Boundary] |

## Retrieval Boundary

```text
[Describe retrieval scope, filtering, access enforcement, classification restrictions, and tenant/user/session boundaries]
```

## Retention and Reuse Decision

```text
[Describe whether prompts, outputs, context, logs, embeddings, or interaction history may be retained or reused]
```

## Vendor Data Processing Decision

```text
[Describe whether data is processed by a vendor, retained by a vendor, or used for training/product improvement]
```

---

# 9. Prompt and Input Decision

## Allowed Inputs

```text
[Describe allowed inputs]
```

## Prohibited Inputs

```text
[Describe prohibited inputs]
```

## System Prompt Control

```text
[Describe system prompt ownership, versioning, access control, testing, and rollback]
```

## Prompt Injection Control

```text
[Describe prompt injection mitigation, trusted/untrusted content separation, external content handling, and testing requirements]
```

## Context Isolation

```text
[Describe context isolation across users, tenants, sessions, repositories, trust zones, and data classifications]
```

---

# 10. Output and Decision Decision

## Output Classification

```text
[Describe output types and impact]
```

## Validation Requirement

```text
[Describe validation, review, approval, or sampling requirements]
```

## Recommendation vs Decision Separation

```text
[Describe how AI recommendation is separated from final decision]
```

## Generated Record Handling

```text
[Describe provenance, retention, correction, and record ownership]
```

## Downstream Use Controls

```text
[Describe controls before AI output is used by downstream systems or workflows]
```

---

# 11. Tool and Action Decision

## Tools or APIs Approved

| Tool / API / Workflow | Action Type | Risk Level | Approval Required | Logging Required |
|---|---|---|---|---|
| [Tool] | [Action] | [Low/Medium/High/Critical] | [Yes/No] | [Yes/No] |

## Action Boundaries

```text
[Describe allowed and prohibited actions]
```

## Approval Gates

```text
[Describe approval gates for high-risk actions]
```

## Blast-Radius Limits

```text
[Describe limits on records, users, amount, rate, systems, environments, or action scope]
```

## Kill Switch and Rollback

```text
[Describe kill switch, revocation, rollback, or compensation path]
```

---

# 12. Evidence and Monitoring Decision

## Required Evidence

Select all that apply:

```text
[ ] Inventory record
[ ] Risk assessment
[ ] Identity/access approval
[ ] Data source approval
[ ] Prompt/input evidence
[ ] Retrieval logs
[ ] Output logs
[ ] Validation records
[ ] Decision evidence
[ ] Tool call logs
[ ] Action logs
[ ] Approval records
[ ] Exception records
[ ] Assurance test results
[ ] Incident evidence
[ ] Vendor evidence
```

## Logging Approach

```text
[Describe logging approach, metadata/full content/redaction/reference-only, retention, and access control]
```

## Monitoring Approach

```text
[Describe monitoring, alerts, anomaly detection, policy violations, SIEM/SOC integration, or manual review]
```

## Evidence Retention

```text
[Describe evidence retention period and storage location]
```

---

# 13. Assurance Decision

## Required Assurance

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

## Assurance Acceptance Criteria

```text
[Describe what must pass before this architecture decision is considered ready]
```

## Regression Triggers

```text
[Describe changes that require retesting or architecture review]
```

---

# 14. Consequences

## Positive Consequences

```text
[Describe benefits of the decision]
```

## Negative Consequences

```text
[Describe tradeoffs, limitations, risks, or operational burden]
```

## Residual Risks

```text
[Describe risks that remain after the decision and required controls]
```

## Required Compensating Controls

```text
[Describe compensating controls if any control requirement cannot be fully met]
```

---

# 15. Exceptions and Conditions

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

## Approval Conditions

```text
[List conditions required for approval]
```

---

# 16. Review and Approval

## Reviewers

| Reviewer | Function | Review Area | Decision | Date |
|---|---|---|---|---|
| [Name] | [Function] | [Area] | [Approved/Rejected/Conditional] | [Date] |

## Final Decision

Select one:

```text
[ ] Approved
[ ] Approved with conditions
[ ] Rejected
[ ] Deferred
[ ] Requires additional review
```

## Final Decision Notes

```text
[Document approval, conditions, rejection rationale, or next steps]
```

## Approved By

```text
Name:
Function:
Date:
```

---

# 17. Review Triggers

This decision should be reviewed if any of the following occur:

```text
[ ] Model or provider changes
[ ] Vendor feature changes
[ ] System prompt changes
[ ] Retrieval logic changes
[ ] Data source changes
[ ] Tool/API access changes
[ ] Workflow changes
[ ] Risk tier changes
[ ] Incident occurs
[ ] Assurance finding is opened
[ ] Regulatory requirement changes
[ ] Business process changes
[ ] External exposure changes
[ ] Production scale increases
[ ] Exception expires
```

## Next Review Date

```text
[Enter date]
```

---

# 18. Summary

```text
Decision ID:
Decision title:
Use case:
AI pattern:
Risk tier:
Decision:
Key rationale:
Required controls:
Required evidence:
Required assurance:
Exceptions:
Approval status:
Next review date:
```