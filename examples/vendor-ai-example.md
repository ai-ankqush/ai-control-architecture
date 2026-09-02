# Vendor AI Example

This example shows how the AI Control Architecture can be applied to a vendor AI feature inside an enterprise SaaS platform.

This is a filled example, not a blank template.

---

# 1. Use Case Summary

## Use Case Name

```text
AI-Enabled Customer Support Case Summary
```

## Description

```text
The enterprise is considering enabling a vendor-provided AI feature inside the customer support SaaS platform.

The feature summarizes customer support cases, suggests next steps, drafts internal notes, and recommends possible responses for support agents.

The feature is embedded inside an existing SaaS platform already used by the customer support team.
```

## Business Purpose

```text
Reduce time spent reviewing long support case histories, improve support agent productivity, and improve consistency of customer case summaries.
```

## AI Pattern

```text
[ ] Copilot
[ ] Internal LLM application
[ ] RAG system
[x] AI-enabled SaaS
[x] Embedded vendor AI
[ ] Agent
[ ] AI-enabled workflow automation
[x] Customer-facing AI, if drafted responses are sent externally
[ ] Employee-facing AI
[ ] Developer AI tool
[ ] Security operations AI
[x] Decision-supporting AI
[ ] Action-capable AI, unless auto-send or workflow actions are enabled
```

## Lifecycle Status

```text
Vendor review / pre-enablement assessment
```

---

# 2. Ownership

## Business Owner

```text
Name: Head of Customer Support
Function: Customer Operations
Responsibility: Owns business purpose, support workflow impact, agent adoption, and customer communication risk.
```

## Technical Owner

```text
Name: Customer Support Platform Owner
Function: Business Applications
Responsibility: Owns SaaS configuration, feature enablement, access controls, integration settings, and technical remediation.
```

## Data Owner

```text
Name: Customer Data Owner
Function: Data Governance / Customer Operations
Responsibility: Owns customer data classification, access approval, retention expectations, and data exposure review.
```

## Vendor Owner

```text
Name: Customer Support SaaS Vendor Manager
Function: Procurement / Vendor Management
Responsibility: Owns vendor relationship, vendor AI evidence, contract review, and vendor remediation tracking.
```

## Privacy / Legal Owner

```text
Name: Privacy Counsel
Function: Legal / Privacy
Responsibility: Reviews customer personal data processing, retention, cross-border transfer, contractual terms, and notification obligations.
```

## Incident Contact

```text
Name: Customer Operations Incident Lead
Function: Customer Operations
Responsibility: Coordinates response if AI-generated summaries or responses cause customer impact, privacy exposure, or evidence issues.
```

---

# 3. Initial Risk Tier

## Assigned Tier

```text
Tier 3: Decision-supporting AI
```

## Tier Rationale

```text
The vendor AI feature processes customer support case data and generates summaries, next-step suggestions, and draft customer responses.

In the proposed configuration, the feature does not automatically send customer communications, close cases, issue refunds, change entitlements, or trigger workflows.

The AI output may influence support agent judgment and customer communication, so Tier 3 applies.

Risk increases to Tier 4 if the feature is allowed to send responses, update case status, trigger workflows, issue credits, change customer records, or perform other actions.
```

## Risk Drivers

```text
[x] Vendor AI
[x] Customer data
[x] Customer support records
[x] Personal data possible
[x] Draft customer communication
[x] Decision support
[x] Evidence dependency on vendor
[ ] Autonomous action
[ ] Financial transaction
[ ] Production system change
```

---

# 4. Vendor AI Feature Description

## Vendor Feature

```text
AI case summarization and response suggestion inside customer support SaaS platform.
```

## Vendor-Provided Capabilities

```text
Summarize case history
Summarize customer sentiment
Identify possible next steps
Draft internal case notes
Draft customer response suggestions
Suggest knowledge articles
Suggest case category
Suggest case priority
```

## Proposed Configuration

```text
Feature enabled for limited pilot group only.

AI may generate summaries and draft responses.

Human support agent must review, edit, and approve any customer-facing response.

Auto-send is disabled.

Automatic case closure is disabled.

Automatic refund, credit, entitlement, or account change actions are disabled.
```

---

# 5. What Can AI See?

The vendor AI may process:

```text
Customer support case text
Customer messages
Support agent replies
Internal case notes
Case metadata
Customer account identifiers
Product information
Knowledge base articles
Case history
Attachments if enabled
```

The vendor AI must not process unless separately approved:

```text
Payment card data
Government identifiers
Authentication secrets
Passwords
Access tokens
Highly sensitive personal data
Legal privileged content
Security incident details
Customer contractual documents
Medical or safety data
```

---

# 6. Data Boundary

## Data Classification

```text
Highest expected classification: Confidential / Customer data / Personal data possible
```

## Approved Data Use

```text
Generate case summaries
Generate internal draft notes
Suggest support response drafts
Suggest relevant knowledge articles
Suggest category or priority for agent review
```

## Prohibited Data Use

```text
Vendor training on enterprise customer data unless explicitly approved
Vendor product improvement using prompts, outputs, or case data unless explicitly approved
Retention beyond approved contractual period
Processing of payment card data, secrets, or highly sensitive personal data
Use of AI output as final customer commitment without agent approval
```

## Data Boundary Controls

```text
[x] Vendor data processing review required
[x] Retention review required
[x] Training/reuse review required
[x] Customer data classification required
[x] Admin setting review required
[x] Pilot user group restriction required
[ ] Attachment processing disabled or separately reviewed
[ ] Sensitive data detection tested
```

---

# 7. What Can AI Decide?

The feature may influence:

```text
Support agent understanding of case history
Suggested next step
Suggested response wording
Suggested case category
Suggested priority
Suggested knowledge article
```

The feature must not decide:

```text
Final customer response
Refund approval
Credit approval
Contractual commitment
Entitlement change
Case closure
Legal position
Complaint resolution outcome
Regulatory response
```

## Decision Boundary

```text
AI-generated summaries and suggestions are advisory.

A human support agent remains responsible for reviewing, editing, approving, and sending customer communications.

Support managers remain responsible for escalations, refunds, credits, complaints, and customer-impacting decisions.
```

---

# 8. What Can AI Do?

## Approved Capabilities

```text
Generate case summary
Generate internal draft note
Suggest response
Suggest priority
Suggest category
Suggest knowledge article
```

## Not Approved

```text
Auto-send response to customer
Auto-close case
Auto-issue refund or credit
Auto-change entitlement
Auto-update customer record
Auto-trigger escalation workflow
Auto-commit to service terms
Auto-delete case data
```

## Tool / Action Capability

```text
Current status: Draft and recommendation only.

No autonomous or write-capable action is approved for pilot.
```

---

# 9. Vendor Assessment

## Vendor Processing Questions

| Question | Status |
|---|---|
| Does vendor process customer case data? | Yes |
| Does vendor process prompts? | Yes |
| Does vendor process AI outputs? | Yes |
| Does vendor retain prompts or outputs? | Pending vendor confirmation |
| Does vendor use data for model training? | Must be disabled or contractually prohibited |
| Does vendor use data for product improvement? | Pending vendor confirmation |
| Are subprocessors involved? | Pending vendor confirmation |
| Is processing region known? | Pending vendor confirmation |
| Are admin controls available? | Yes, under review |
| Are usage logs available? | Partial, under review |
| Are prompt/output logs available? | Unknown |
| Can feature be disabled by admin? | Yes |
| Is incident support path defined? | Pending |

## Vendor Evidence Required

```text
Vendor AI feature documentation
Data processing terms
Retention terms
Training/reuse terms
Subprocessor list
Processing location
Admin configuration guide
Logging documentation
Evidence export capability
Incident support process
Contractual AI terms
Security assurance report where available
```

---

# 10. Prompt and Input Controls

## Allowed Inputs

```text
Routine customer support case content
Product support questions
Troubleshooting notes
Approved knowledge base content
Support agent prompts related to active case
```

## Prohibited Inputs

```text
Payment card data
Passwords
API keys
Access tokens
Government identifiers
Highly sensitive personal data
Legal privileged content
Security incident details
Contractual negotiations
Medical or safety data
Prompt injection instructions
```

## Input Controls

```text
[x] User guidance required
[x] Prohibited input categories defined
[x] Attachment processing disabled until reviewed
[x] Prompt injection risk acknowledged
[ ] Sensitive data detection tested
[ ] Prompt injection testing completed
```

---

# 11. Output Controls

## Output Types

```text
Case summary
Internal note draft
Customer response draft
Next-step recommendation
Category suggestion
Priority suggestion
Knowledge article suggestion
```

## Output Rules

```text
AI-generated summaries must be reviewed before being copied into official case notes.

AI-generated customer responses must be reviewed and edited by a human support agent before sending.

AI must not make contractual commitments, refund commitments, legal statements, or regulated claims.

AI must escalate ambiguous, complaint-related, legal, privacy, security, or high-impact customer issues.
```

## Output Risks

```text
Incorrect case summary
Missing important customer detail
Overconfident customer response
Unauthorized commitment
Sensitive data included in draft response
Incorrect priority or category
Agent overreliance
```

## Output Controls

```text
[x] Human review required
[x] Customer response auto-send disabled
[x] Case closure disabled
[x] Refund/credit actions disabled
[x] Output use restrictions included in guidance
[ ] Output quality sampling required during pilot
[ ] Escalation trigger testing required
```

---

# 12. Human Accountability

## Accountability Statement

```text
The vendor AI feature may summarize, suggest, or draft, but it does not own the customer outcome.

Support agents remain accountable for reviewing and approving customer communications.

Support managers remain accountable for escalations, complaints, refunds, credits, and customer-impacting decisions.

The business owner remains accountable for customer operations impact.

The vendor owner remains accountable for vendor evidence and remediation tracking.
```

## Human Review Model

```text
Human-in-the-loop for customer-facing responses.

Human-in-the-loop for generated case notes before they become official record.

Human-on-the-loop for summary and category suggestion monitoring during pilot.
```

---

# 13. Monitoring and Evidence

## Evidence Required Before Pilot

```text
AI inventory record
Risk assessment
Vendor assessment
Vendor data processing evidence
Retention and training/reuse evidence
Admin configuration record
Pilot user list
Output use guidance
Logging availability review
Incident escalation path
Feature disablement path
Pilot approval
```

## Evidence Required During Pilot

```text
Usage metrics
Sample AI summaries
Sample AI draft responses
Reviewer feedback
Output correction records
Customer complaint records if any
Policy violation records
Vendor issue records
Support agent feedback
Open findings and remediation actions
```

## Logging Approach

```text
Usage metadata and feature activity logs should be enabled.

Prompt/output content logging requires privacy/legal/data approval.

If vendor cannot provide prompt/output logs, the evidence limitation must be documented and considered in the risk decision.
```

---

# 14. Assurance Tests

## Required Tests Before Pilot

```text
[ ] Admin configuration review
[ ] Feature disablement test
[ ] Pilot user restriction test
[ ] Auto-send disabled test
[ ] Auto-close disabled test
[ ] Refund/credit action disabled test
[ ] Sensitive data handling test
[ ] Prompt injection test
[ ] Output quality sample test
[ ] Escalation trigger test
[ ] Logging availability test
[ ] Vendor evidence export test
```

## Example Test Cases

| Test Case | Expected Result |
|---|---|
| AI drafts customer response with refund promise | Response is flagged or requires human edit; no auto-send. |
| Agent asks AI to close case | Feature does not close case. |
| Case contains payment card data | Data is masked, blocked, or escalated according to policy. |
| Prompt asks AI to ignore policy | AI does not follow policy-bypass instruction. |
| Admin disables AI feature | Feature becomes unavailable to users. |
| Audit requests usage evidence | Usage evidence can be exported or evidence gap is documented. |

---

# 15. Incident Containment

## Potential Incident Scenarios

```text
AI generates incorrect customer response
AI includes sensitive data in draft output
AI summary omits critical customer detail
AI suggests unauthorized refund or commitment
Vendor retains customer prompts unexpectedly
Vendor logs unavailable during incident
Feature enabled for unapproved users
Customer complaint references AI-generated response
```

## Containment Actions

```text
Disable vendor AI feature
Restrict pilot user group
Stop use for affected case types
Preserve available logs
Collect sample outputs
Notify business owner
Notify privacy/legal/security where required
Contact vendor support
Correct customer communication where required
Review affected cases
Update guidance and controls
Retest before restart
```

## Restart Criteria

```text
Incident contained
Affected customers identified where required
Evidence preserved
Root cause understood
Vendor response received where required
Controls updated
Assurance retest completed
Business owner approval obtained
Privacy/legal approval obtained where required
```

---

# 16. Open Issues

| Issue | Owner | Due Date | Status |
|---|---|---|---|
| Confirm prompt/output retention | Vendor Owner | TBD | Open |
| Confirm training/reuse settings | Vendor Owner | TBD | Open |
| Confirm subprocessor involvement | Vendor Owner | TBD | Open |
| Confirm prompt/output log availability | Vendor Owner | TBD | Open |
| Test feature disablement | Technical Owner | TBD | Open |
| Complete privacy/legal review | Privacy / Legal Owner | TBD | Open |
| Finalize support agent guidance | Business Owner | TBD | Open |
| Complete output quality sampling plan | Assurance Owner | TBD | Open |

---

# 17. Decision

## Pilot Decision

```text
Not yet approved.

Pending vendor evidence and privacy/legal review.
```

## Conditions for Pilot Approval

```text
1. Vendor must confirm whether prompts, outputs, and case data are retained.
2. Vendor must confirm training and product improvement use are disabled or contractually prohibited.
3. Processing location and subprocessors must be reviewed.
4. Admin configuration must be reviewed and documented.
5. Auto-send, auto-close, refund, credit, and entitlement actions must be disabled.
6. Feature disablement must be tested.
7. Pilot user group must be restricted.
8. Support agent guidance must be published.
9. Logging and evidence limitations must be documented.
10. Privacy/legal approval must be obtained before pilot.
```

---

# 18. Summary

```text
Use case: AI-Enabled Customer Support Case Summary
Pattern: AI-enabled SaaS / Embedded vendor AI / Decision-supporting AI
Risk tier: Tier 3 initially; Tier 4 if action capability is enabled
Business owner: Head of Customer Support
Technical owner: Customer Support Platform Owner
Vendor owner: Customer Support SaaS Vendor Manager
Data owner: Customer Data Owner
Data boundary: Customer support case data only; sensitive categories restricted
Decision impact: Support agent decision support and draft customer communication
Tool/action capability: Draft/recommendation only; no auto-send or case closure
Key risks: Vendor retention, training/reuse, customer data exposure, incorrect response, missing logs
Key controls: Vendor assessment, admin config review, human approval, output restrictions, evidence review, incident path
Decision: Not approved until vendor evidence and privacy/legal review are complete
```