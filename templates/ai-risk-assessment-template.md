# AI Risk Assessment Template

This template is used to assess the risk of an AI use case and assign an initial AI risk tier.

It should be completed after the AI use case has been captured in the AI Use Case Intake Template.

The purpose of this template is to determine how much control is required based on data exposure, decision impact, action capability, autonomy, external exposure, vendor involvement, business criticality, and recoverability.

---

# 1. Assessment Information

## AI Use Case Name

```text
[Enter use case name]
```

## Assessment Date

```text
[Enter date]
```

## Assessor

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
Not applicable reason, if any:
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

# 2. AI Pattern Risk

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

## Pattern Risk Notes

```text
[Describe why this AI pattern creates risk or why the risk is limited]
```

## Pattern Risk Rating

Select one:

```text
[ ] Low
[ ] Moderate
[ ] High
[ ] Critical
```

---

# 3. Data Sensitivity Risk

## Data Used by the AI

Select all that apply:

```text
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

## Data Source Summary

| Data Source | Classification | Owner | Approved for AI Use? | Notes |
|---|---|---|---|---|
| [Source] | [Classification] | [Owner] | [Yes/No/Pending] | [Notes] |

## Data Sensitivity Risk Rating

Select one:

```text
[ ] Low: public or low-sensitivity data only
[ ] Moderate: internal or limited confidential data
[ ] High: sensitive, customer, employee, financial, legal, security, or restricted data
[ ] Critical: regulated, privileged, highly sensitive, secrets, credentials, or production-critical data
```

## Data Risk Notes

```text
[Describe data sensitivity, exposure, retention, retrieval, or leakage concerns]
```

---

# 4. Decision Impact Risk

## Does AI Influence Decisions?

Select one:

```text
[ ] No decision impact
[ ] Informal user support only
[ ] Operational decision support
[ ] Customer-impacting decision support
[ ] Employee-impacting decision support
[ ] Financial decision support
[ ] Legal or compliance decision support
[ ] Security decision support
[ ] Regulated or high-impact decision support
[ ] Unknown
```

## Decision Description

```text
[Describe the decision or judgment influenced by AI]
```

## Final Decision Owner

```text
Name:
Function:
Email:
Not applicable reason, if any:
```

## Decision Impact Risk Rating

Select one:

```text
[ ] Low: no material decision impact
[ ] Moderate: internal operational decision support
[ ] High: customer, employee, financial, legal, security, or compliance decision support
[ ] Critical: regulated, high-impact, rights-affecting, safety, access, money, or production decision support
```

## Decision Risk Notes

```text
[Describe how AI output could influence decisions and what could go wrong]
```

---

# 5. Output Risk

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

## Output Risk Rating

Select one:

```text
[ ] Low: informal or low-impact output
[ ] Moderate: internal operational output
[ ] High: customer-facing, decision-supporting, record-generating, or workflow-impacting output
[ ] Critical: regulated, legal, financial, HR, security, production, or high-impact output
```

## Output Risk Notes

```text
[Describe output accuracy, hallucination, sensitivity, customer-facing, record, or downstream use risks]
```

---

# 6. Tool and Action Risk

## Can AI Use Tools, APIs, or Workflows?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Tool or Action Capability

Select all that apply:

```text
[ ] No tool or action capability
[ ] Read-only search or retrieval
[ ] Draft-only capability
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

## Tool and Action Summary

| Tool / API / Workflow | Action Type | Risk Level | Approval Required? | Reversible? |
|---|---|---|---|---|
| [Tool] | [Action] | [Low/Moderate/High/Critical] | [Yes/No] | [Yes/No/Partial] |

## Tool and Action Risk Rating

Select one:

```text
[ ] Low: no tool use or draft-only capability
[ ] Moderate: read-only or low-impact bounded actions
[ ] High: workflow, record, customer, access, or system-impacting actions
[ ] Critical: financial, privileged, production, security, regulated, or hard-to-reverse actions
```

## Tool and Action Risk Notes

```text
[Describe action capability, approval, reversibility, blast-radius, and containment concerns]
```

---

# 7. Autonomy Risk

## Autonomy Level

Select one:

```text
[ ] Level 0: AI generates text only
[ ] Level 1: AI suggests actions but cannot execute
[ ] Level 2: AI prepares drafts but human executes
[ ] Level 3: AI requests actions but approval is required
[ ] Level 4: AI executes bounded low-risk actions
[ ] Level 5: AI executes high-impact actions under strict controls
[ ] Unknown
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

## Autonomy Risk Rating

Select one:

```text
[ ] Low: human prompts and reviews all meaningful outputs
[ ] Moderate: AI operates with limited autonomy or draft-only capability
[ ] High: AI can request or execute bounded actions
[ ] Critical: AI can execute high-impact or multi-step autonomous actions
```

## Autonomy Risk Notes

```text
[Describe autonomy, human supervision, approval, escalation, and override concerns]
```

---

# 8. External Exposure Risk

## External Exposure

Select all that apply:

```text
[ ] Internal only
[ ] Internal with vendor processing
[ ] Partner-facing
[ ] Supplier-facing
[ ] Customer-facing
[ ] Public-facing
[ ] Regulator-facing
[ ] Unknown
```

## External Exposure Risk Rating

Select one:

```text
[ ] Low: internal only, no external exposure
[ ] Moderate: internal use with vendor processing or limited external dependency
[ ] High: customer, supplier, partner, or external-facing output
[ ] Critical: public-facing, regulator-facing, or high-impact external exposure
```

## External Exposure Risk Notes

```text
[Describe external users, customer impact, vendor exposure, public exposure, or reputational concerns]
```

---

# 9. Vendor and Third-Party Risk

## Vendor Involvement

Select all that apply:

```text
[ ] No vendor involvement
[ ] Hosted model provider
[ ] Cloud AI service
[ ] AI-enabled SaaS
[ ] Embedded vendor AI
[ ] Third-party agent
[ ] External processing
[ ] Vendor retention of prompts or outputs
[ ] Vendor training or product improvement use
[ ] Unknown
```

## Vendor Review Status

Select one:

```text
[ ] Not applicable
[ ] Not started
[ ] In progress
[ ] Completed
[ ] Completed with conditions
[ ] Exception required
[ ] Unknown
```

## Vendor Risk Rating

Select one:

```text
[ ] Low: no vendor or low-risk vendor processing
[ ] Moderate: vendor processing with known controls
[ ] High: vendor processes sensitive data or provides limited evidence
[ ] Critical: vendor processes regulated/highly sensitive data, retains data, or controls critical AI behavior
```

## Vendor Risk Notes

```text
[Describe vendor processing, retention, training/reuse, logs, contractual, subprocessor, or incident support risks]
```

---

# 10. Business Criticality Risk

## Process Criticality

Select one:

```text
[ ] Low: productivity or non-critical process
[ ] Moderate: internal operational process
[ ] High: important business process
[ ] Critical: mission-critical, regulated, customer-critical, security-critical, or production-critical process
```

## Business Impact If AI Fails

Select all that apply:

```text
[ ] Minimal inconvenience
[ ] Productivity loss
[ ] Operational delay
[ ] Incorrect business record
[ ] Customer dissatisfaction
[ ] Customer harm
[ ] Employee impact
[ ] Financial loss
[ ] Legal or compliance issue
[ ] Security issue
[ ] Production outage
[ ] Regulatory exposure
[ ] Reputational harm
```

## Business Criticality Risk Rating

Select one:

```text
[ ] Low
[ ] Moderate
[ ] High
[ ] Critical
```

## Business Criticality Notes

```text
[Describe business process dependency, impact, resilience, and fallback concerns]
```

---

# 11. Recoverability Risk

## Can Harmful Output or Action Be Reversed?

Select one:

```text
[ ] Easily reversible
[ ] Reversible with manual effort
[ ] Partially reversible
[ ] Difficult to reverse
[ ] Irreversible
[ ] Unknown
```

## Recovery Options

Select all that apply:

```text
[ ] User can discard output
[ ] Output can be corrected
[ ] Record can be amended
[ ] Workflow can be re-run
[ ] Transaction can be reversed
[ ] Access can be revoked
[ ] Tool action can be rolled back
[ ] Customer can be notified
[ ] Manual remediation possible
[ ] Vendor remediation required
[ ] No clear recovery path
```

## Recoverability Risk Rating

Select one:

```text
[ ] Low: output/action is easy to correct or discard
[ ] Moderate: recovery requires manual effort but is practical
[ ] High: recovery is difficult, time-sensitive, or may affect customers/processes
[ ] Critical: action is irreversible, regulated, high-impact, or recovery path is unclear
```

## Recoverability Notes

```text
[Describe rollback, correction, compensation, remediation, and restart concerns]
```

---

# 12. Overall Risk Tier

Use the ratings above to assign the initial AI risk tier.

## Suggested Risk Tier

Select one:

```text
[ ] Tier 1: Low-risk productivity or public-data use
[ ] Tier 2: Internal productivity with enterprise data
[ ] Tier 3: Decision-supporting AI
[ ] Tier 4: Action-capable AI
[ ] Tier 5: High-impact autonomous or regulated AI
```

## Risk Tier Rationale

```text
[Explain why this tier was selected. Reference the highest risk factors.]
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

---

# 13. Required Control Domains

Based on the risk assessment, select required control domains.

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

## Control Notes

```text
[Describe control domains requiring priority attention]
```

---

# 14. Required Reviews

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
```

## Review Rationale

```text
[Explain why these reviews are required]
```

---

# 15. Required Assurance

Select all required assurance activities:

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
[ ] Evidence reconstruction testing
[ ] Kill switch testing
[ ] Rollback testing
[ ] Vendor assurance review
[ ] Regression testing
[ ] Incident tabletop
```

## Assurance Rationale

```text
[Explain assurance activities required based on the risk tier and risk drivers]
```

---

# 16. Risk Decision

## Assessment Outcome

Select one:

```text
[ ] Approved to proceed
[ ] Approved with required controls
[ ] Approved for pilot only
[ ] Requires remediation before approval
[ ] Requires additional review
[ ] Requires exception approval
[ ] Rejected
[ ] Deferred
```

## Required Conditions

```text
[List controls, reviews, evidence, or remediation required before proceeding]
```

## Residual Risk

```text
[Describe residual risk after planned controls]
```

## Risk Acceptance Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Risk Acceptance Owner

```text
Name:
Function:
Email:
Not applicable reason, if any:
```

---

# 17. Approval Record

## Business Owner Decision

```text
Name:
Decision:
Date:
Notes:
```

## Risk / Governance Decision

```text
Name or forum:
Decision:
Date:
Notes:
```

## Architecture / Security Decision

```text
Name or forum:
Decision:
Date:
Notes:
```

---

# 18. Summary

```text
Use case:
AI pattern:
Highest risk drivers:
Overall risk tier:
Required controls:
Required reviews:
Required assurance:
Decision:
Conditions:
Risk owner:
```