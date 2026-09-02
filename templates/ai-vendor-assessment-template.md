# AI Vendor Assessment Template

This template is used to assess vendors, platforms, SaaS products, model providers, embedded AI features, and third-party AI services that process, generate, retain, expose, or act on enterprise data.

The purpose of this template is to ensure vendor AI is identified, reviewed, controlled, evidenced, and managed before it is enabled, purchased, integrated, scaled, or relied upon.

Vendor AI must be mapped into the enterprise AI Control Architecture rather than treated as a standalone product feature.

---

# 1. Vendor Assessment Information

## Vendor Name

```text
[Enter vendor name]
```

## Product / Platform / Service Name

```text
[Enter product, platform, or service name]
```

## AI Feature or Capability Name

```text
[Enter AI feature or capability name]
```

## Assessment Date

```text
[Enter date]
```

## Assessment Owner

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

## Vendor Owner

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

## Related AI Use Case

```text
[Enter related AI use case name]
```

## Related AI Inventory Record

```text
[Enter inventory record reference or link]
```

---

# 2. Vendor AI Capability Overview

## AI Capability Description

```text
[Describe what the vendor AI capability does]
```

## AI Capability Type

Select all that apply:

```text
[ ] AI-enabled SaaS feature
[ ] Embedded vendor AI
[ ] Hosted model API
[ ] Cloud AI service
[ ] AI agent
[ ] AI workflow automation
[ ] AI search or RAG capability
[ ] AI summarization
[ ] AI drafting
[ ] AI classification
[ ] AI recommendation
[ ] AI decision support
[ ] AI tool/action execution
[ ] Customer-facing AI
[ ] Security operations AI
[ ] Developer AI tool
[ ] Other
```

## Current Enablement Status

Select one:

```text
[ ] Not enabled
[ ] Enabled for pilot
[ ] Enabled for limited users
[ ] Enabled in production
[ ] Enabled by default
[ ] Disabled
[ ] Unknown
```

## Is the AI Feature Optional?

```text
[ ] Yes
[ ] No
[ ] Unknown
```

## Can the AI Feature Be Disabled?

```text
[ ] Yes
[ ] No
[ ] Partially
[ ] Unknown
```

## Admin Control Notes

```text
[Describe admin controls, feature flags, tenant settings, user-level settings, or limitations]
```

---

# 3. Business Use and Scope

## Intended Business Use

```text
[Describe how the enterprise intends to use the vendor AI capability]
```

## Business Process Affected

```text
[Describe business process, workflow, or function affected]
```

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

## External Exposure

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

## Scope Limitations

```text
[Describe any user, business unit, geography, data, workflow, or feature restrictions]
```

---

# 4. Data Processing Assessment

## Data Processed by Vendor AI

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

| Data Source | Classification | Owner | Vendor Access? | Notes |
|---|---|---|---|---|
| [Source] | [Classification] | [Owner] | [Yes/No/Unknown] | [Notes] |

## Does Vendor AI Process Prompts?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Does Vendor AI Process Outputs?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Does Vendor AI Process Uploaded Files?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Does Vendor AI Process Retrieved Context?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Data Processing Notes

```text
[Describe how data is sent to, processed by, or accessed by the vendor AI capability]
```

---

# 5. Data Retention and Reuse

## Does the Vendor Retain Prompts?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Does the Vendor Retain Outputs?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Does the Vendor Retain Uploaded Files?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Does the Vendor Retain Logs or Telemetry?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Retention Period

```text
[Describe retention period for prompts, outputs, files, logs, telemetry, and generated content]
```

## Can Retained Data Be Deleted?

```text
[ ] Yes
[ ] No
[ ] Partially
[ ] Unknown
```

## Can Vendor Use Enterprise Data for Training?

```text
[ ] No
[ ] Yes
[ ] Opt-out available
[ ] Unknown
```

## Can Vendor Use Enterprise Data for Product Improvement?

```text
[ ] No
[ ] Yes
[ ] Opt-out available
[ ] Unknown
```

## Training / Reuse Configuration

```text
[Describe training, fine-tuning, telemetry, product improvement, analytics, or reuse settings]
```

## Retention and Reuse Notes

```text
[Describe risks, restrictions, contractual terms, or required controls]
```

---

# 6. Processing Location and Subprocessors

## Processing Location

```text
[Describe where AI processing occurs, including regions or data centers if known]
```

## Data Residency Requirements

```text
[Describe applicable data residency or jurisdictional requirements]
```

## Cross-Border Transfer Involved?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Subprocessors Involved?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Subprocessor Summary

| Subprocessor | Role | Data Processed | Location | Notes |
|---|---|---|---|---|
| [Name] | [Role] | [Data] | [Location] | [Notes] |

## Processing Location Notes

```text
[Describe cross-border transfer, subprocessors, residency, or jurisdiction concerns]
```

---

# 7. Identity and Access

## Vendor AI Identity Model

Select all that apply:

```text
[ ] Uses user identity
[ ] Uses delegated user authority
[ ] Uses application identity
[ ] Uses service identity
[ ] Uses vendor-managed identity
[ ] Uses agent identity
[ ] Hybrid identity
[ ] Unknown
```

## Permission Model

```text
[Describe how the vendor AI determines what data, records, users, tools, or workflows it can access]
```

## Does Vendor AI Respect Existing User Permissions?

```text
[ ] Yes
[ ] No
[ ] Partially
[ ] Unknown
```

## Can AI-Mediated Activity Be Distinguished?

```text
[ ] Yes
[ ] No
[ ] Partially
[ ] Unknown
```

## Access Review Available?

```text
[ ] Yes
[ ] No
[ ] Partially
[ ] Unknown
```

## Revocation Path

```text
[Describe how AI access, user access, service access, or feature access can be revoked]
```

## Identity and Access Notes

```text
[Describe identity, access, delegated authority, permission inheritance, attribution, and revocation concerns]
```

---

# 8. Prompt and Input Controls

## System Prompt or Vendor Instructions Visible?

```text
[ ] No
[ ] Yes
[ ] Partially
[ ] Unknown
```

## Can Enterprise Configure AI Instructions or Guardrails?

```text
[ ] Yes
[ ] No
[ ] Partially
[ ] Unknown
```

## Does Vendor Provide Prompt/Input Filtering?

```text
[ ] Yes
[ ] No
[ ] Partially
[ ] Unknown
```

## Does Vendor Detect Sensitive Data in Inputs?

```text
[ ] Yes
[ ] No
[ ] Partially
[ ] Unknown
```

## Does Vendor Address Prompt Injection Risk?

```text
[ ] Yes
[ ] No
[ ] Partially
[ ] Unknown
```

## External or Untrusted Inputs Processed?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Prompt and Input Notes

```text
[Describe input validation, prohibited inputs, prompt injection, system prompt protection, and configuration limitations]
```

---

# 9. Output and Decision Controls

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

## Does Output Become a Record?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Does Output Reach Customers or External Parties?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Vendor Output Controls Available

Select all that apply:

```text
[ ] Output review workflow
[ ] Human approval workflow
[ ] Output labeling
[ ] Source attribution
[ ] Confidence indicator
[ ] Generated content marker
[ ] Customer-facing restrictions
[ ] Output logging
[ ] Correction or retraction support
[ ] None
[ ] Unknown
```

## Output and Decision Notes

```text
[Describe output validation, decision impact, generated records, customer-facing controls, and correction paths]
```

---

# 10. Tool and Action Capability

## Can Vendor AI Use Tools, APIs, or Workflows?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Vendor AI Action Capability

Select all that apply:

```text
[ ] No action capability
[ ] Read-only retrieval
[ ] Draft-only action
[ ] Workflow trigger
[ ] Record creation
[ ] Record modification
[ ] Communication sending
[ ] Access request or approval
[ ] Financial transaction
[ ] Security action
[ ] Production change
[ ] Administrative action
[ ] Other
```

## Tool / Action Summary

| Tool / Workflow / Action | Risk Level | Approval Available? | Logging Available? | Disable Available? |
|---|---|---|---|---|
| [Tool/action] | [Low/Medium/High/Critical] | [Yes/No/Unknown] | [Yes/No/Unknown] | [Yes/No/Unknown] |

## Approval Gates Available?

```text
[ ] Yes
[ ] No
[ ] Partially
[ ] Unknown
```

## Action Boundaries Available?

```text
[ ] Yes
[ ] No
[ ] Partially
[ ] Unknown
```

## Kill Switch Available?

```text
[ ] Yes
[ ] No
[ ] Partially
[ ] Unknown
```

## Rollback or Correction Available?

```text
[ ] Yes
[ ] No
[ ] Partially
[ ] Unknown
```

## Tool and Action Notes

```text
[Describe action risks, approval gates, action limits, kill switches, rollback, and vendor limitations]
```

---

# 11. Monitoring, Logging, and Evidence

## Vendor Logs Available

Select all that apply:

```text
[ ] Admin activity logs
[ ] User activity logs
[ ] AI usage logs
[ ] Prompt logs
[ ] Prompt metadata
[ ] Output logs
[ ] Output metadata
[ ] Retrieval logs
[ ] Data access logs
[ ] Tool call logs
[ ] Action logs
[ ] Approval logs
[ ] Policy violation logs
[ ] Incident logs
[ ] None
[ ] Unknown
```

## Log Retention Period

```text
[Describe vendor log retention period]
```

## Can Logs Be Exported?

```text
[ ] Yes
[ ] No
[ ] Partially
[ ] Unknown
```

## Can Logs Be Integrated with SIEM/SOC?

```text
[ ] Yes
[ ] No
[ ] Partially
[ ] Unknown
```

## Evidence Available for Audit?

```text
[ ] Yes
[ ] No
[ ] Partially
[ ] Unknown
```

## Evidence Notes

```text
[Describe logging gaps, evidence limitations, export options, audit support, and monitoring concerns]
```

---

# 12. Security, Privacy, Legal, and Compliance

## Security Review Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Privacy Review Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Legal Review Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Compliance Review Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Regulatory Impact

Select all that apply:

```text
[ ] No known regulatory impact
[ ] Personal data regulation
[ ] Financial regulation
[ ] Health or safety regulation
[ ] Employment regulation
[ ] Consumer protection
[ ] Sector-specific regulation
[ ] Cross-border data transfer
[ ] Records retention
[ ] Legal privilege
[ ] Unknown
```

## Contractual Requirements

Select all that apply:

```text
[ ] Data processing agreement
[ ] AI-specific data use restrictions
[ ] Training/reuse restriction
[ ] Audit rights
[ ] Incident notification terms
[ ] Subprocessor disclosure
[ ] Data deletion obligation
[ ] Data residency obligation
[ ] Security assurance evidence
[ ] Service change notification
[ ] Liability or indemnity review
[ ] Other
```

## Security / Privacy / Legal Notes

```text
[Describe key legal, privacy, compliance, or security issues]
```

---

# 13. Vendor Assurance and Evidence

## Assurance Evidence Provided

Select all that apply:

```text
[ ] Security certification
[ ] SOC report
[ ] ISO certification
[ ] Penetration test summary
[ ] AI risk documentation
[ ] Model card or system card
[ ] Data processing documentation
[ ] Privacy documentation
[ ] Subprocessor list
[ ] Audit log documentation
[ ] Incident response documentation
[ ] Responsible AI documentation
[ ] Admin control documentation
[ ] None
[ ] Unknown
```

## Vendor AI Documentation Reviewed?

```text
[ ] No
[ ] Yes
[ ] Partially
[ ] Unknown
```

## Vendor Assurance Findings

| Finding ID | Finding | Severity | Owner | Status |
|---|---|---|---|---|
| [Finding ID] | [Finding] | [Low/Medium/High/Critical] | [Owner] | [Status] |

## Vendor Assurance Notes

```text
[Summarize evidence received, evidence gaps, findings, and unresolved questions]
```

---

# 14. Vendor Incident Support

## Vendor AI Incident Process Available?

```text
[ ] Yes
[ ] No
[ ] Partially
[ ] Unknown
```

## Incident Notification Terms Defined?

```text
[ ] Yes
[ ] No
[ ] Partially
[ ] Unknown
```

## Vendor Support Contact

```text
Name:
Role:
Email:
Support channel:
```

## Vendor Evidence During Incident

Select all available:

```text
[ ] Prompt logs
[ ] Output logs
[ ] User activity logs
[ ] Admin logs
[ ] Data access logs
[ ] Tool/action logs
[ ] Configuration history
[ ] Feature enablement history
[ ] Retention evidence
[ ] RCA / incident report
[ ] Unknown
```

## Vendor Incident Notes

```text
[Describe incident support, evidence availability, timelines, and escalation path]
```

---

# 15. Risk Assessment

## Vendor AI Risk Drivers

Select all that apply:

```text
[ ] Sensitive data processing
[ ] Regulated data processing
[ ] Personal data processing
[ ] Customer-facing output
[ ] Decision-supporting output
[ ] Tool or action capability
[ ] Vendor-managed identity
[ ] Limited logs
[ ] Limited admin controls
[ ] Vendor retention
[ ] Vendor training/reuse
[ ] Cross-border transfer
[ ] Subprocessor dependency
[ ] Feature enabled by default
[ ] Cannot fully disable feature
[ ] Weak incident support
[ ] Unknown vendor behavior
```

## Vendor AI Risk Rating

Select one:

```text
[ ] Low
[ ] Medium
[ ] High
[ ] Critical
```

## Risk Rating Rationale

```text
[Explain why this rating was selected]
```

## Required Controls

Select all that apply:

```text
[ ] Inventory record
[ ] Business owner assigned
[ ] Vendor owner assigned
[ ] Data owner approval
[ ] Data processing review
[ ] Training/reuse restriction
[ ] Retention restriction
[ ] Admin configuration control
[ ] Feature enablement approval
[ ] Access review
[ ] Output review
[ ] Tool/action review
[ ] Logging review
[ ] SIEM/SOC integration
[ ] Vendor incident process
[ ] Contract update
[ ] Assurance evidence
[ ] Exception record
```

---

# 16. Approval Decision

## Assessment Outcome

Select one:

```text
[ ] Approved for use
[ ] Approved with conditions
[ ] Approved for pilot only
[ ] Requires remediation before approval
[ ] Requires contract update
[ ] Requires additional review
[ ] Requires exception approval
[ ] Rejected
[ ] Deferred
```

## Conditions for Approval

```text
[List required conditions before enablement, purchase, production use, or scaling]
```

## Required Remediation

| Action ID | Remediation Action | Owner | Due Date | Status |
|---|---|---|---|---|
| [Action ID] | [Action] | [Owner] | [Date] | [Status] |

## Exceptions Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Residual Risk

```text
[Describe residual risk after required controls and conditions]
```

---

# 17. Review and Approval

## Business Owner Decision

```text
Name:
Decision:
Date:
Notes:
```

## Vendor Risk Decision

```text
Name or forum:
Decision:
Date:
Notes:
```

## Security Decision

```text
Name or forum:
Decision:
Date:
Notes:
```

## Privacy / Legal Decision

```text
Name or forum:
Decision:
Date:
Notes:
Not applicable reason, if any:
```

## Architecture Decision

```text
Name or forum:
Decision:
Date:
Notes:
```

---

# 18. Ongoing Review

## Review Frequency

Select one:

```text
[ ] Monthly
[ ] Quarterly
[ ] Semi-annually
[ ] Annually
[ ] At contract renewal
[ ] At vendor feature change
[ ] At material AI change
[ ] After incident
[ ] Other
```

## Review Triggers

Select all that apply:

```text
[ ] Vendor changes AI feature
[ ] Vendor changes data processing terms
[ ] Vendor changes retention terms
[ ] Vendor changes training/reuse terms
[ ] Vendor adds subprocessor
[ ] Vendor changes logging capability
[ ] Vendor changes admin controls
[ ] Vendor incident occurs
[ ] Enterprise use case changes
[ ] Data classification changes
[ ] Risk tier changes
[ ] Contract renewal
[ ] Regulatory change
```

## Next Review Date

```text
[Enter date]
```

---

# 19. Summary

```text
Vendor:
Product/platform:
AI feature:
Business owner:
Vendor owner:
AI pattern:
Data processed:
Vendor retention:
Training/reuse:
Identity model:
Output impact:
Action capability:
Logs available:
Incident support:
Risk rating:
Approval decision:
Conditions:
Next review date:
```