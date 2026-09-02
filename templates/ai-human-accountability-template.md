# AI Human Accountability Template

This template is used to define, approve, evidence, and review human accountability for an AI use case.

AI can assist, recommend, summarize, classify, draft, retrieve, or execute bounded actions.

But AI must not become the accountable owner of enterprise outcomes.

The purpose of this template is to ensure that business ownership, technical ownership, decision ownership, review responsibilities, approval authority, escalation paths, override rights, exception ownership, and incident ownership are clearly assigned.

---

# 1. Accountability Information

## AI Use Case Name

```text
[Enter AI use case name]
```

## Accountability Record ID

```text
[Enter accountability record ID]
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

## Related AI Inventory Record

```text
[Enter inventory record reference or link]
```

## Related Risk Assessment

```text
[Enter risk assessment reference or link]
```

## Related Control Assessment

```text
[Enter control assessment reference or link]
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

## Accountability Summary

```text
[Summarize who is accountable for the AI use case, its outputs, decisions, actions, exceptions, and incidents]
```

---

# 3. Business Accountability

## Business Owner

```text
Name:
Function:
Email:
```

## Business Outcome Owned

```text
[Describe the business outcome owned by the business owner]
```

## Business Owner Responsibilities

Select all that apply:

```text
[ ] Defines business purpose
[ ] Owns business outcome
[ ] Owns operational use
[ ] Accepts business risk
[ ] Approves high-risk use
[ ] Owns user adoption
[ ] Owns business process impact
[ ] Supports incident response
[ ] Reviews continued use
[ ] Owns customer or stakeholder impact
[ ] Other
```

## Business Accountability Notes

```text
[Describe business ownership, accountability limits, and open issues]
```

---

# 4. Technical Accountability

## Technical Owner

```text
Name:
Function:
Email:
```

## Technical Scope Owned

```text
[Describe the systems, integrations, configurations, prompts, data flows, tools, or workflows owned by the technical owner]
```

## Technical Owner Responsibilities

Select all that apply:

```text
[ ] Owns technical implementation
[ ] Owns configuration
[ ] Owns model or vendor integration
[ ] Owns identity and access implementation
[ ] Owns data boundary implementation
[ ] Owns prompt/input control implementation
[ ] Owns output control implementation
[ ] Owns tool/action integration
[ ] Owns logging implementation
[ ] Owns change management
[ ] Owns technical remediation
[ ] Supports incident response
[ ] Other
```

## Technical Accountability Notes

```text
[Describe technical ownership, support model, and constraints]
```

---

# 5. Data Accountability

## Data Owner

```text
Name:
Function:
Email:
Not applicable reason, if any:
```

## Data Scope Owned

```text
[Describe data sources, classifications, repositories, or records owned]
```

## Data Owner Responsibilities

Select all that apply:

```text
[ ] Approves data access
[ ] Confirms data classification
[ ] Defines sensitive data restrictions
[ ] Defines retrieval boundaries
[ ] Defines retention requirements
[ ] Defines training/reuse restrictions
[ ] Reviews data-related exceptions
[ ] Supports data incident response
[ ] Approves cross-boundary data movement
[ ] Other
```

## Data Accountability Notes

```text
[Describe data ownership, approval conditions, and data handling requirements]
```

---

# 6. Decision Accountability

## Does AI Influence a Decision?

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

## Decision Type

Select all that apply:

```text
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

## Final Decision Authority

```text
[Describe who makes or approves the final decision and how it is recorded]
```

## AI Recommendation vs Final Decision Separation

```text
[Describe how AI output is separated from the final accountable decision]
```

## Decision Evidence

```text
[Describe evidence retained for AI-assisted decisions]
```

---

# 7. Human Review Model

## Human Review Required?

```text
[ ] No
[ ] Yes
[ ] Conditional
[ ] Unknown
```

## Human Review Pattern

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

## Reviewer

```text
Name or role:
Function:
Email or group:
```

## Reviewer Responsibilities

Select all that apply:

```text
[ ] Reviews AI output
[ ] Validates sources
[ ] Checks accuracy
[ ] Checks policy compliance
[ ] Approves output
[ ] Rejects output
[ ] Modifies output
[ ] Escalates concern
[ ] Records review decision
[ ] Other
```

## Meaningful Review Conditions

Select all that apply:

```text
[ ] Reviewer has sufficient context
[ ] Reviewer has access to source material
[ ] Reviewer has authority to reject
[ ] Reviewer has authority to escalate
[ ] Reviewer has time to review
[ ] Reviewer understands AI limitations
[ ] Review decision is logged
[ ] Other
```

## Human Review Notes

```text
[Describe review process and how blind reliance or ceremonial review is avoided]
```

---

# 8. Approval Authority

## Approval Required?

```text
[ ] No
[ ] Yes
[ ] Conditional
[ ] Unknown
```

## Approval Areas

Select all that apply:

```text
[ ] AI use case approval
[ ] Data access approval
[ ] Vendor AI approval
[ ] Prompt change approval
[ ] High-risk output approval
[ ] Customer-facing output approval
[ ] Decision approval
[ ] Tool access approval
[ ] High-risk action approval
[ ] Exception approval
[ ] Risk acceptance approval
[ ] Production deployment approval
[ ] Restart after incident approval
[ ] Other
```

## Approval Matrix

| Approval Area | Approver | Trigger | Evidence Required | Expiry / Review |
|---|---|---|---|---|
| [Area] | [Approver] | [Trigger] | [Evidence] | [Expiry/review] |

## Approval Notes

```text
[Describe approval authority, limits, conditions, and escalation]
```

---

# 9. Escalation Path

## Escalation Required?

```text
[ ] No
[ ] Yes
[ ] Conditional
[ ] Unknown
```

## Escalation Triggers

Select all that apply:

```text
[ ] Uncertain output
[ ] Disputed output
[ ] High-impact decision
[ ] Policy violation
[ ] Sensitive data exposure
[ ] Unsafe recommendation
[ ] Customer complaint
[ ] Prompt injection concern
[ ] Abnormal tool use
[ ] Failed approval
[ ] Incident indicator
[ ] Control exception
[ ] Vendor issue
[ ] Other
```

## Escalation Matrix

| Trigger | Escalation Destination | Required Response | Evidence |
|---|---|---|---|
| [Trigger] | [Team/person] | [Response] | [Evidence] |

## Escalation Notes

```text
[Describe escalation path, response expectations, and ownership]
```

---

# 10. Override Rights

## Override Required?

```text
[ ] No
[ ] Yes
[ ] Conditional
[ ] Unknown
```

## Override Rights

Select all that apply:

```text
[ ] Reject AI-generated output
[ ] Edit AI-generated draft
[ ] Override AI recommendation
[ ] Stop workflow action
[ ] Suspend agent
[ ] Revoke tool access
[ ] Reverse record update
[ ] Escalate decision
[ ] Quarantine generated output
[ ] Block customer communication
[ ] Open incident
[ ] Other
```

## Override Authority

| Override Type | Authorized Role | Conditions | Evidence Required |
|---|---|---|---|
| [Override] | [Role] | [Conditions] | [Evidence] |

## Override Notes

```text
[Describe how override works and how it is recorded]
```

---

# 11. Risk Acceptance

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

## Risk Accepted

```text
[Describe residual risk accepted]
```

## Risk Acceptance Conditions

```text
[Describe conditions, compensating controls, expiry, and review frequency]
```

## Risk Acceptance Evidence

```text
[Describe where risk acceptance is recorded]
```

---

# 12. Exception Ownership

## Exceptions Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Exception Owner

```text
Name:
Function:
Email:
Not applicable reason, if any:
```

## Exception Summary

| Exception | Requirement Affected | Owner | Expiry | Review Frequency |
|---|---|---|---|---|
| [Exception] | [Requirement] | [Owner] | [Expiry] | [Frequency] |

## Exception Ownership Notes

```text
[Describe who owns exception risk, remediation, review, and closure]
```

---

# 13. Incident Accountability

## Incident Owner

```text
Name:
Function:
Email:
```

## Incident Roles

| Incident Role | Owner / Team | Responsibility |
|---|---|---|
| Business impact owner | [Owner] | [Responsibility] |
| Technical containment owner | [Owner] | [Responsibility] |
| Data exposure owner | [Owner] | [Responsibility] |
| Vendor escalation owner | [Owner] | [Responsibility] |
| Communications owner | [Owner] | [Responsibility] |
| Recovery owner | [Owner] | [Responsibility] |
| Post-incident review owner | [Owner] | [Responsibility] |

## Incident Accountability Notes

```text
[Describe how accountability works during AI incident response]
```

---

# 14. Vendor Accountability

Complete this section if vendor AI is involved.

## Vendor Involved?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Vendor Owner

```text
Name:
Function:
Email:
```

## Vendor Accountability Areas

Select all that apply:

```text
[ ] Vendor feature approval
[ ] Vendor data processing review
[ ] Vendor retention review
[ ] Vendor training/reuse review
[ ] Vendor logs/evidence review
[ ] Vendor incident escalation
[ ] Vendor contract review
[ ] Vendor assurance review
[ ] Vendor remediation tracking
[ ] Continued-use decision
[ ] Other
```

## Internal Accountability for Vendor AI Use

```text
[Describe who inside the enterprise remains accountable for how vendor AI is used]
```

## Vendor Accountability Notes

```text
[Describe vendor shared responsibility, evidence limits, and escalation path]
```

---

# 15. RACI Matrix

Use this section to define responsibility, accountability, consultation, and information flows.

| Activity | Business Owner | Technical Owner | Data Owner | Decision Owner | Security | Legal/Privacy | Vendor Owner | Risk/Governance |
|---|---|---|---|---|---|---|---|---|
| AI use case approval | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] |
| Data access approval | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] |
| Output review | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] |
| Decision approval | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] |
| Tool/action approval | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] |
| Exception approval | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] |
| Incident response | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] |
| Post-incident review | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] | [R/A/C/I] |

---

# 16. Accountability Evidence

## Evidence Required

Select all that apply:

```text
[ ] Business owner record
[ ] Technical owner record
[ ] Data owner approval
[ ] Decision owner mapping
[ ] Human review record
[ ] Approval record
[ ] Rejection record
[ ] Modification record
[ ] Override record
[ ] Escalation record
[ ] Exception record
[ ] Risk acceptance record
[ ] Incident ownership record
[ ] Post-incident review record
[ ] RACI record
[ ] Governance decision
[ ] Other
```

## Evidence Location

```text
[Describe where accountability evidence is stored]
```

## Evidence Retention

```text
[Describe retention period]
```

## Evidence Access Restrictions

```text
[Describe who can access accountability evidence]
```

---

# 17. Testing and Review

## Accountability Review Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Review Checks

Select all that apply:

```text
[ ] Business owner assigned
[ ] Technical owner assigned
[ ] Data owner assigned where required
[ ] Decision owner assigned where required
[ ] Human review model defined
[ ] Approval authority defined
[ ] Escalation path tested
[ ] Override path tested
[ ] Exception ownership defined
[ ] Incident ownership defined
[ ] RACI reviewed
[ ] Evidence retained
```

## Review Results

| Check | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|
| [Check] | [Expected] | [Actual] | [Pass/Fail/Partial/Not Run] | [Evidence] |

## Open Findings

| Finding ID | Finding | Severity | Owner | Due Date | Status |
|---|---|---|---|---|---|
| [Finding ID] | [Finding] | [Low/Medium/High/Critical] | [Owner] | [Date] | [Status] |

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

## Decision Owner Approval, If Required

```text
Name:
Decision:
Date:
Notes:
Not applicable reason, if any:
```

## Risk / Governance Approval

```text
Name or forum:
Decision:
Date:
Notes:
```

## Final Accountability Decision

Select one:

```text
[ ] Approved
[ ] Approved with conditions
[ ] Requires remediation
[ ] Requires exception approval
[ ] Requires additional review
[ ] Rejected
[ ] Deferred
```

## Approval Conditions

```text
[List conditions required before approval, production use, scaling, or continued operation]
```

---

# 19. Review Triggers

Review this accountability model if any of the following occur:

```text
[ ] Business owner changes
[ ] Technical owner changes
[ ] Data owner changes
[ ] Decision owner changes
[ ] AI use case changes
[ ] Output or decision impact changes
[ ] Tool/action capability changes
[ ] Autonomy level changes
[ ] Vendor involvement changes
[ ] Risk tier changes
[ ] Exception is requested
[ ] Incident occurs
[ ] Audit finding occurs
[ ] Governance model changes
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
Business owner:
Technical owner:
Data owner:
Decision owner:
Human review model:
Approval authority:
Escalation path:
Override rights:
Exception owner:
Risk acceptance owner:
Incident owner:
Vendor owner:
Evidence location:
Approval status:
Next review date:
```