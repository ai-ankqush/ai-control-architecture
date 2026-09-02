# AI Use Case Intake Template

This template is used to register a proposed, existing, discovered, or embedded AI capability.

The purpose of the intake template is to make AI visible before it is approved, deployed, scaled, integrated, or relied upon.

Every AI use case should be recorded before the enterprise determines risk tier, control requirements, architecture review, assurance needs, monitoring requirements, and incident response expectations.

---

# 1. Basic Information

## Use Case Name

```text
[Enter the name of the AI use case]
```

## Short Description

```text
[Describe what the AI capability does in plain language]
```

## Business Purpose

```text
[Explain why the AI capability is needed and what business outcome it supports]
```

## Request Type

Select one:

```text
[ ] New AI use case
[ ] Existing AI use case
[ ] Pilot or experiment
[ ] Production AI capability
[ ] Embedded vendor AI feature
[ ] AI-enabled SaaS feature
[ ] Shadow AI discovery
[ ] Agentic AI use case
[ ] Change to existing AI use case
```

## Lifecycle Status

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

## Process Owner

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

## Incident Contact

```text
Name:
Function:
Email:
Escalation path:
```

---

# 3. AI Pattern

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

## If Other, Describe

```text
[Describe the AI pattern]
```

---

# 4. Users and Audience

## Intended Users

Select all that apply:

```text
[ ] Employees
[ ] Contractors
[ ] Developers
[ ] Security team
[ ] Customer support team
[ ] Business operations team
[ ] Legal or compliance team
[ ] HR team
[ ] Finance team
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

## External Exposure

Select one:

```text
[ ] Internal only
[ ] Internal with vendor processing
[ ] Partner-facing
[ ] Supplier-facing
[ ] Customer-facing
[ ] Public-facing
```

---

# 5. Business Process Impact

## Affected Business Process

```text
[Describe the business process, workflow, or function affected by this AI use case]
```

## Process Criticality

Select one:

```text
[ ] Low
[ ] Moderate
[ ] High
[ ] Critical
```

## Does AI Influence a Decision?

Select one:

```text
[ ] No
[ ] Yes, low-impact decision
[ ] Yes, operational decision
[ ] Yes, customer-impacting decision
[ ] Yes, employee-impacting decision
[ ] Yes, financial decision
[ ] Yes, legal or compliance decision
[ ] Yes, security decision
[ ] Yes, regulated or high-impact decision
```

## Describe Decision Impact

```text
[Describe how AI output influences or supports decisions]
```

---

# 6. Data Exposure

## Data Sources Used

List all data sources the AI can access, retrieve, process, or receive.

| Data Source | Owner | Data Classification | Access Method | Approved? |
|---|---|---|---|---|
| [Source name] | [Owner] | [Classification] | [Prompt/Retrieval/API/File/Vendor] | [Yes/No/Pending] |

## Data Classification

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

## Does the AI Process Personal Data?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Does the AI Process Regulated Data?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Does Data Leave the Enterprise Boundary?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Data Boundary Notes

```text
[Describe data access, retrieval boundaries, retention, reuse, residency, or vendor processing concerns]
```

---

# 7. Prompt and Input Handling

## Input Types

Select all that apply:

```text
[ ] User prompts
[ ] Uploaded files
[ ] Retrieved documents
[ ] Emails
[ ] Chat messages
[ ] Tickets
[ ] Customer submissions
[ ] API payloads
[ ] Tool responses
[ ] Web content
[ ] Code
[ ] Logs
[ ] Workflow data
[ ] System prompts
[ ] Conversation history
[ ] Memory
[ ] Other
```

## Are External or Untrusted Inputs Processed?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Prompt Injection Risk

Select one:

```text
[ ] Not applicable
[ ] Low
[ ] Moderate
[ ] High
[ ] Unknown
```

## Input Controls

```text
[Describe any allowed inputs, prohibited inputs, validation, filtering, redaction, or prompt injection controls]
```

---

# 8. Model, Vendor, and Platform

## Model or AI Service

```text
Model/service name:
Provider:
Hosting model:
```

## Hosting Model

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
Vendor/platform name:
Contract owner:
Vendor risk review completed? [Yes/No/Pending/Not applicable]
```

## Vendor Data Use

Select all that apply:

```text
[ ] Vendor processes prompts
[ ] Vendor processes outputs
[ ] Vendor retains prompts
[ ] Vendor retains outputs
[ ] Vendor may use data for training
[ ] Vendor may use data for product improvement
[ ] Vendor provides opt-out for training/reuse
[ ] Vendor provides audit logs
[ ] Vendor provides incident support
[ ] Unknown
[ ] Not applicable
```

## Vendor Notes

```text
[Describe vendor processing, retention, training/reuse, logs, contractual terms, or incident support]
```

---

# 9. Output and Decision Use

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

## Output Audience

Select all that apply:

```text
[ ] Individual user only
[ ] Internal team
[ ] Business process
[ ] Downstream system
[ ] Customer
[ ] Supplier
[ ] Partner
[ ] Public
[ ] Regulator
[ ] Other
```

## Does Output Become a Record?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Does Output Require Human Review?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Output Review Model

Select one:

```text
[ ] No review required
[ ] User review
[ ] Required human approval
[ ] Second-line review
[ ] Sampling review
[ ] Exception-based review
[ ] Continuous monitoring
[ ] Not yet defined
```

## Output Control Notes

```text
[Describe validation, review, approval, provenance, correction, or downstream use controls]
```

---

# 10. Tool and Action Capability

## Can AI Use Tools, APIs, or Workflows?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Tool or Action Types

Select all that apply:

```text
[ ] Read-only tool
[ ] Draft-only tool
[ ] Search or retrieval tool
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
[ ] Other
```

## Tool Inventory

| Tool / API / Workflow | Owner | Action Type | Risk Level | Approval Required? | Logging Available? |
|---|---|---|---|---|---|
| [Tool name] | [Owner] | [Read/Write/Action] | [Low/Medium/High/Critical] | [Yes/No] | [Yes/No] |

## Approval Gates

```text
[Describe approval requirements before AI can perform or trigger actions]
```

## Kill Switch or Revocation Path

```text
[Describe how tool access, agent access, or action capability can be disabled]
```

---

# 11. Human Accountability

## Decision Owner

```text
Name:
Function:
Email:
Not applicable reason, if any:
```

## Human Review Model

Select one:

```text
[ ] No human review
[ ] Human-in-the-loop
[ ] Human-on-the-loop
[ ] Human-over-the-loop
[ ] Exception-based review
[ ] Not yet defined
```

## Approver for High-Risk Output or Action

```text
Name:
Function:
Email:
Not applicable reason, if any:
```

## Override Path

```text
[Describe how AI output or action can be challenged, modified, rejected, stopped, or reversed]
```

## Accountability Notes

```text
[Describe ownership, decision authority, escalation, exception ownership, and risk acceptance]
```

---

# 12. Monitoring, Logging, and Evidence

## Logging Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Evidence Required

Select all that apply:

```text
[ ] Inventory record
[ ] Risk tier
[ ] Owner record
[ ] Access approval
[ ] Data source mapping
[ ] Prompt/input logs
[ ] Prompt/input metadata
[ ] Retrieval logs
[ ] Output logs
[ ] Output validation evidence
[ ] Decision evidence
[ ] Tool call logs
[ ] Action logs
[ ] Approval records
[ ] Exception records
[ ] Incident evidence
[ ] Assurance test results
[ ] Vendor evidence
```

## Log Location

```text
[Describe where logs are stored or expected to be stored]
```

## Retention Requirement

```text
[Describe evidence retention period and any legal/privacy constraints]
```

## Monitoring Notes

```text
[Describe alerts, monitoring, SIEM/SOC integration, policy violations, or anomaly detection]
```

---

# 13. Incident Containment and Recovery

## AI Incident Scenarios

Select all that may apply:

```text
[ ] Sensitive data exposure
[ ] Prompt injection
[ ] Unsafe output
[ ] Incorrect AI-assisted decision
[ ] Unauthorized tool use
[ ] Approval bypass
[ ] Agent malfunction
[ ] Vendor AI incident
[ ] Logging failure
[ ] Customer-facing AI failure
[ ] Regulatory or legal exposure
[ ] Other
```

## Containment Options

Select all that apply:

```text
[ ] Disable AI capability
[ ] Suspend agent
[ ] Revoke AI identity
[ ] Remove data source access
[ ] Disable tool
[ ] Block API
[ ] Stop workflow
[ ] Disable vendor AI feature
[ ] Quarantine output
[ ] Roll back action
[ ] Correct generated record
[ ] Notify vendor
[ ] Escalate to incident response
```

## Recovery Notes

```text
[Describe rollback, correction, notification, remediation, or restart process]
```

---

# 14. Initial Risk Assessment

## Risk Indicators

Select all that apply:

```text
[ ] Uses sensitive data
[ ] Uses regulated data
[ ] Uses personal data
[ ] Customer-facing
[ ] External-facing
[ ] Influences decisions
[ ] Generates records
[ ] Uses tools or APIs
[ ] Triggers workflows
[ ] Can perform actions
[ ] Uses vendor AI
[ ] Uses untrusted inputs
[ ] Uses agents
[ ] Has high autonomy
[ ] Impacts critical process
[ ] Hard to reverse or recover
```

## Suggested Initial Risk Tier

Select one:

```text
[ ] Tier 1: Low-risk productivity or public-data use
[ ] Tier 2: Internal productivity with enterprise data
[ ] Tier 3: Decision-supporting AI
[ ] Tier 4: Action-capable AI
[ ] Tier 5: High-impact autonomous or regulated AI
[ ] Unknown / requires review
```

## Risk Rationale

```text
[Explain why this tier was selected]
```

---

# 15. Required Reviews

Select all required reviews:

```text
[ ] AI governance review
[ ] Enterprise architecture review
[ ] Security architecture review
[ ] IAM/PAM review
[ ] Data governance review
[ ] Privacy review
[ ] Legal review
[ ] Vendor risk review
[ ] Compliance review
[ ] Audit consultation
[ ] SDLC / application security review
[ ] Incident response review
[ ] Business continuity review
[ ] Not yet determined
```

## Review Notes

```text
[Describe review decisions, open questions, or pending approvals]
```

---

# 16. Assurance and Testing

## Testing Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Required Test Types

Select all that apply:

```text
[ ] Pre-deployment review
[ ] Prompt injection testing
[ ] Data leakage testing
[ ] Retrieval boundary testing
[ ] Output validation testing
[ ] Bias or fairness testing where relevant
[ ] Tool misuse testing
[ ] Approval gate testing
[ ] Logging completeness testing
[ ] Kill switch testing
[ ] Rollback testing
[ ] Vendor assurance review
[ ] Regression testing
[ ] Incident tabletop
```

## Assurance Notes

```text
[Describe testing scope, findings, remediation, or risk acceptance]
```

---

# 17. Exceptions

## Are Any Control Exceptions Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Exception Summary

| Requirement | Exception Needed | Business Justification | Compensating Control | Expiry Date | Owner |
|---|---|---|---|---|---|
| [Requirement] | [Yes/No] | [Reason] | [Control] | [Date] | [Owner] |

---

# 18. Approval

## Intake Completed By

```text
Name:
Function:
Date:
```

## Business Owner Approval

```text
Name:
Decision:
Date:
Notes:
```

## Architecture / Governance Decision

Select one:

```text
[ ] Approved
[ ] Approved with conditions
[ ] Requires remediation
[ ] Requires additional review
[ ] Rejected
[ ] Deferred
```

## Decision Notes

```text
[Document final decision, conditions, required controls, or next steps]
```

---

# 19. Summary

Use this section to summarize the AI use case in a concise format.

```text
Use case:
Owner:
AI pattern:
Data involved:
Decision impact:
Action capability:
Vendor involvement:
Risk tier:
Required controls:
Required reviews:
Approval status:
```