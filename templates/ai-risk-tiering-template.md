# AI Risk Tiering Template

This template is used to assign an AI use case to a risk tier.

Risk tiering determines the level of control, review, assurance, monitoring, evidence, and incident readiness required for an AI capability.

The purpose of this template is to make AI risk classification consistent, explainable, and repeatable across different AI patterns, vendors, business processes, and levels of autonomy.

---

# 1. Risk Tiering Information

## AI Use Case Name

```text
[Enter AI use case name]
```

## Risk Tiering Record ID

```text
[Enter record ID]
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

## Related AI Inventory Record

```text
[Enter inventory record reference or link]
```

## Related Intake Record

```text
[Enter intake record reference or link]
```

---

# 2. AI Use Case Summary

## Short Description

```text
[Describe what the AI capability does]
```

## Business Purpose

```text
[Describe why this AI capability is needed]
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

## Lifecycle Status

Select one:

```text
[ ] Proposed
[ ] Pilot
[ ] Production
[ ] Under review
[ ] Restricted
[ ] Suspended
[ ] Retired
[ ] Unknown
```

---

# 3. Tiering Model

Use the following AI risk tiers.

| Tier | Name | Description |
|---|---|---|
| Tier 1 | Low-risk productivity or public-data use | AI supports low-risk productivity, drafting, summarization, or public information use with no sensitive data, no decision impact, and no action capability. |
| Tier 2 | Internal productivity with enterprise data | AI uses internal enterprise data but does not materially influence high-impact decisions or execute actions. |
| Tier 3 | Decision-supporting AI | AI output influences business, customer, employee, financial, legal, compliance, security, or operational decisions. |
| Tier 4 | Action-capable AI | AI can call tools, trigger workflows, modify records, send communications, or perform bounded actions. |
| Tier 5 | High-impact autonomous or regulated AI | AI affects regulated, rights-impacting, production-critical, financial, security, safety, legal, HR, or high-autonomy processes. |

---

# 4. Data Risk

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

## Data Risk Indicator

Select one:

```text
[ ] Low: public or non-sensitive data only
[ ] Moderate: internal or limited confidential data
[ ] High: customer, employee, financial, legal, security, restricted, or sensitive data
[ ] Critical: regulated, privileged, highly sensitive, secrets, credentials, or production-critical data
```

## Data Risk Notes

```text
[Describe data exposure, sensitivity, retention, retrieval, vendor processing, or leakage concerns]
```

---

# 5. Decision Risk

## Does AI Influence a Decision?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Decision Type

Select all that apply:

```text
[ ] No decision impact
[ ] Informal user judgment
[ ] Internal operational decision
[ ] Case prioritization
[ ] Customer-impacting decision
[ ] Employee-impacting decision
[ ] Financial decision
[ ] Legal or compliance decision
[ ] Security decision
[ ] Access decision
[ ] Production or operational decision
[ ] Regulated or high-impact decision
[ ] Other
```

## Decision Risk Indicator

Select one:

```text
[ ] Low: no material decision impact
[ ] Moderate: informal or internal operational decision support
[ ] High: customer, employee, financial, legal, security, or compliance decision support
[ ] Critical: regulated, rights-affecting, production, access, money, safety, or high-impact decision support
```

## Decision Risk Notes

```text
[Describe how AI output influences decisions and what could go wrong]
```

---

# 6. Output Risk

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

## Output Becomes a Record?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Output Risk Indicator

Select one:

```text
[ ] Low: informal or low-impact output
[ ] Moderate: internal operational output
[ ] High: customer-facing, decision-supporting, record-generating, or workflow-impacting output
[ ] Critical: regulated, legal, financial, HR, security, production, or high-impact output
```

## Output Risk Notes

```text
[Describe hallucination, sensitivity, external communication, generated record, or downstream use risk]
```

---

# 7. Tool and Action Risk

## Can AI Use Tools, APIs, or Workflows?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Action Capability

Select all that apply:

```text
[ ] No tool or action capability
[ ] Read-only retrieval
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
[ ] Code execution
[ ] Other
```

## Tool and Action Risk Indicator

Select one:

```text
[ ] Low: no tool use or draft-only capability
[ ] Moderate: read-only or bounded low-impact actions
[ ] High: workflow, record, customer, access, system, or security-impacting actions
[ ] Critical: financial, privileged, production, regulated, irreversible, or hard-to-reverse actions
```

## Tool and Action Risk Notes

```text
[Describe tool use, approval gates, reversibility, blast radius, and containment concerns]
```

---

# 8. Autonomy Risk

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
[ ] Sampling review
[ ] Continuous monitoring
[ ] Not yet defined
```

## Autonomy Risk Indicator

Select one:

```text
[ ] Low: human initiates and reviews meaningful use
[ ] Moderate: AI prepares or recommends but does not execute
[ ] High: AI can request or execute bounded actions
[ ] Critical: AI can execute multi-step, high-impact, or difficult-to-contain actions
```

## Autonomy Risk Notes

```text
[Describe autonomy, supervision, review, approval, override, and escalation concerns]
```

---

# 9. External Exposure Risk

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

## External Exposure Risk Indicator

Select one:

```text
[ ] Low: internal only, no external exposure
[ ] Moderate: internal use with vendor processing or limited external dependency
[ ] High: customer, supplier, partner, or external-facing output
[ ] Critical: public-facing, regulator-facing, or high-impact external exposure
```

## External Exposure Notes

```text
[Describe external users, customer impact, public exposure, vendor exposure, or reputational risk]
```

---

# 10. Vendor Risk

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

## Vendor Risk Indicator

Select one:

```text
[ ] Low: no vendor or low-risk vendor processing
[ ] Moderate: vendor processing with known controls
[ ] High: vendor processes sensitive data or provides limited evidence
[ ] Critical: vendor processes regulated/highly sensitive data, retains data, trains on data, or controls critical AI behavior
```

## Vendor Risk Notes

```text
[Describe vendor data processing, retention, training/reuse, evidence, contractual, and incident response concerns]
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

## Recoverability Risk Indicator

Select one:

```text
[ ] Low: output or action is easy to correct or discard
[ ] Moderate: recovery requires manual effort but is practical
[ ] High: recovery is difficult, time-sensitive, or may affect customers or processes
[ ] Critical: action is irreversible, regulated, high-impact, or recovery path is unclear
```

## Recoverability Notes

```text
[Describe rollback, correction, compensation, remediation, and restart concerns]
```

---

# 12. Tier Assignment Rules

Use the following guidance to assign the risk tier.

## Tier 1

Use Tier 1 when all are true:

```text
[ ] No sensitive enterprise data
[ ] No material decision impact
[ ] No customer-facing or external-facing output
[ ] No tool/action capability
[ ] Output is easy to discard or correct
```

## Tier 2

Use Tier 2 when the AI uses internal enterprise data but all are true:

```text
[ ] No high-impact decision support
[ ] No high-risk action capability
[ ] No regulated or highly sensitive data
[ ] No material customer, employee, financial, legal, security, or production impact
```

## Tier 3

Use Tier 3 when one or more are true:

```text
[ ] AI output materially influences decisions
[ ] AI output becomes part of a business process
[ ] AI output becomes an enterprise record
[ ] AI output supports customer, employee, financial, legal, compliance, security, or operational judgment
```

## Tier 4

Use Tier 4 when one or more are true:

```text
[ ] AI can call tools
[ ] AI can trigger workflows
[ ] AI can modify records
[ ] AI can send communications
[ ] AI can request or perform actions
[ ] AI has bounded autonomous execution
```

## Tier 5

Use Tier 5 when one or more are true:

```text
[ ] AI is high-autonomy
[ ] AI affects regulated or rights-impacting decisions
[ ] AI can perform privileged, financial, security, production, or hard-to-reverse actions
[ ] AI is customer-facing or public-facing with high impact
[ ] AI uses highly sensitive, regulated, privileged, or secret data
[ ] AI failure could create material legal, regulatory, financial, security, safety, or reputational harm
```

---

# 13. Assigned Risk Tier

## Assigned Tier

Select one:

```text
[ ] Tier 1: Low-risk productivity or public-data use
[ ] Tier 2: Internal productivity with enterprise data
[ ] Tier 3: Decision-supporting AI
[ ] Tier 4: Action-capable AI
[ ] Tier 5: High-impact autonomous or regulated AI
```

## Tier Rationale

```text
[Explain why this tier was selected. Reference the highest risk indicators.]
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

# 14. Required Controls by Tier

## Tier 1 Minimum Controls

```text
[ ] Inventory record
[ ] Business owner
[ ] Acceptable use guidance
[ ] Basic data restriction
[ ] Basic review at material change
```

## Tier 2 Minimum Controls

```text
[ ] Inventory record
[ ] Business owner
[ ] Data source mapping
[ ] Data classification
[ ] Access boundary
[ ] Prompt/input guidance
[ ] Logging approach
[ ] Vendor review where applicable
```

## Tier 3 Minimum Controls

```text
[ ] Tier 2 controls
[ ] Decision owner
[ ] Output classification
[ ] Validation rule
[ ] Human review model
[ ] Decision evidence
[ ] Correction or override path
[ ] Assurance testing
```

## Tier 4 Minimum Controls

```text
[ ] Tier 3 controls
[ ] Tool inventory
[ ] Action classification
[ ] Tool access approval
[ ] Approval gate for high-risk actions
[ ] Tool/action logging
[ ] Kill switch or revocation path
[ ] Rollback or compensation assessment
```

## Tier 5 Minimum Controls

```text
[ ] Tier 4 controls
[ ] Independent or enhanced assurance
[ ] Strong identity and access control
[ ] Strong data boundary control
[ ] Detailed reconstructable evidence
[ ] Incident tabletop
[ ] Kill switch testing
[ ] Recovery testing
[ ] Risk acceptance
[ ] Ongoing monitoring and periodic review
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
```

## Review Rationale

```text
[Explain why these reviews are required based on the assigned tier]
```

---

# 16. Required Assurance

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
[Explain required assurance activities]
```

---

# 17. Tiering Decision

## Tiering Outcome

Select one:

```text
[ ] Tier assigned
[ ] Tier assigned with conditions
[ ] Requires additional information
[ ] Requires escalation
[ ] Deferred
```

## Required Conditions

```text
[List conditions required before the tier is accepted]
```

## Open Questions

```text
[List unknowns or assumptions that must be resolved]
```

---

# 18. Approval

## Business Owner Review

```text
Name:
Decision:
Date:
Notes:
```

## Risk / Governance Review

```text
Name or forum:
Decision:
Date:
Notes:
```

## Architecture / Security Review

```text
Name or forum:
Decision:
Date:
Notes:
```

## Final Tiering Decision

Select one:

```text
[ ] Approved
[ ] Approved with conditions
[ ] Requires additional review
[ ] Rejected
[ ] Deferred
```

---

# 19. Review Triggers

Review this risk tier if any of the following occur:

```text
[ ] Data source changes
[ ] Data classification changes
[ ] User population changes
[ ] External exposure changes
[ ] Output use changes
[ ] Decision impact changes
[ ] Tool/action capability changes
[ ] Autonomy level changes
[ ] Vendor processing changes
[ ] Model or platform changes
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
AI pattern:
Data risk:
Decision risk:
Output risk:
Tool/action risk:
Autonomy risk:
External exposure risk:
Vendor risk:
Recoverability risk:
Assigned tier:
Highest risk drivers:
Required controls:
Required reviews:
Required assurance:
Approval status:
Next review date:
```