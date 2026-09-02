# AI Prompt and Input Control Template

This template is used to define, approve, test, and evidence prompt and input controls for an AI use case.

Prompts and inputs are control surfaces.

They can shape AI behavior, expose sensitive data, introduce malicious instructions, override intended controls, contaminate context, or cause unsafe outputs and actions.

The purpose of this template is to define what inputs are allowed, what inputs are prohibited, how system prompts are protected, how prompt injection is managed, how context is isolated, and how prompt/input evidence is retained.

---

# 1. Prompt and Input Control Information

## AI Use Case Name

```text
[Enter AI use case name]
```

## Prompt/Input Control ID

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

# 3. Input Source Mapping

## Input Sources

Select all that apply:

```text
[ ] Human user prompt
[ ] System prompt
[ ] Developer prompt
[ ] Policy prompt
[ ] Retrieved enterprise document
[ ] Uploaded file
[ ] Email
[ ] Ticket
[ ] Chat message
[ ] Customer submission
[ ] Web content
[ ] API payload
[ ] Tool response
[ ] Workflow state
[ ] Conversation history
[ ] Memory
[ ] Code
[ ] Logs
[ ] Other
```

## Input Source Table

| Input Source | Source Owner | Trust Level | Data Classification | External/Untrusted? | Notes |
|---|---|---|---|---|---|
| [Source] | [Owner] | [Trusted/Untrusted/Mixed] | [Classification] | [Yes/No] | [Notes] |

## Input Source Notes

```text
[Describe important input sources, trust boundaries, and risks]
```

---

# 4. Allowed Inputs

## Allowed Input Types

```text
[List input types allowed for this AI use case]
```

## Allowed Data Classes

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
[ ] Production data
[ ] Other
```

## Allowed Input Conditions

```text
[Describe conditions under which inputs are allowed]
```

## Allowed Input Notes

```text
[Describe input rules, user guidance, or approval requirements]
```

---

# 5. Prohibited Inputs

## Prohibited Input Types

Select all that apply:

```text
[ ] Passwords
[ ] API keys
[ ] Private keys
[ ] Secrets
[ ] Access tokens
[ ] Credentials
[ ] Unapproved personal data
[ ] Regulated data without approval
[ ] Legal privileged material without approval
[ ] Highly confidential data
[ ] Payment card data
[ ] Production secrets
[ ] Customer data outside approved use case
[ ] Employee sensitive data outside approved use case
[ ] Unauthorized source code
[ ] Data restricted by contract
[ ] Malicious instructions
[ ] Policy bypass requests
[ ] Other
```

## Prohibited Input Handling

Select all that apply:

```text
[ ] Warn user
[ ] Block input
[ ] Redact input
[ ] Mask input
[ ] Route for approval
[ ] Log event
[ ] Escalate to owner
[ ] Trigger security monitoring
[ ] Open incident
[ ] Other
```

## Prohibited Input Notes

```text
[Describe how prohibited inputs are detected and handled]
```

---

# 6. Sensitive Data Detection

## Sensitive Data Detection Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Detection Targets

Select all that apply:

```text
[ ] Personal data
[ ] Customer records
[ ] Employee records
[ ] Financial data
[ ] Health or safety information
[ ] Legal privileged content
[ ] Security credentials
[ ] API keys
[ ] Access tokens
[ ] Secrets
[ ] Confidential business information
[ ] Regulated records
[ ] Source code
[ ] Intellectual property
[ ] Other
```

## Detection Methods

Select all that apply:

```text
[ ] User guidance
[ ] Warning banner
[ ] Pattern matching
[ ] DLP integration
[ ] Classification labels
[ ] Metadata inspection
[ ] File scanning
[ ] Redaction
[ ] Masking
[ ] Blocking
[ ] Manual review
[ ] Other
```

## Detection Notes

```text
[Describe detection approach, limitations, and evidence]
```

---

# 7. System Prompt Protection

## System Prompt Used?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## System Prompt Owner

```text
Name:
Function:
Email:
```

## System Prompt Access Control

```text
[Describe who can view, edit, approve, and deploy system prompts]
```

## System Prompt Versioning

```text
Version:
Repository/location:
Last updated:
Approved by:
```

## System Prompt Change Control

Select all that apply:

```text
[ ] Version control
[ ] Peer review
[ ] Security review
[ ] Business owner approval
[ ] Testing before deployment
[ ] Regression testing
[ ] Rollback capability
[ ] Deployment approval
[ ] Evidence retention
```

## System Prompt Protection Notes

```text
[Describe leakage, tampering, override, and change-control protections]
```

---

# 8. Prompt Injection Control

## Prompt Injection Risk Rating

Select one:

```text
[ ] Low
[ ] Moderate
[ ] High
[ ] Critical
[ ] Unknown
```

## Prompt Injection Sources

Select all that apply:

```text
[ ] Web content
[ ] Retrieved documents
[ ] Uploaded files
[ ] Emails
[ ] Tickets
[ ] Chat messages
[ ] Customer submissions
[ ] Tool responses
[ ] Code comments
[ ] Logs
[ ] Third-party content
[ ] Other
```

## Prompt Injection Controls

Select all that apply:

```text
[ ] Treat external content as untrusted
[ ] Separate trusted instructions from untrusted content
[ ] Prevent untrusted content from overriding system prompts
[ ] Restrict tool use based on untrusted input
[ ] Detect suspicious instruction patterns
[ ] Require approval for high-risk actions
[ ] Test prompt injection scenarios
[ ] Monitor policy violations
[ ] Other
```

## Prompt Injection Test Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Prompt Injection Notes

```text
[Describe prompt injection threat model, controls, tests, and residual risk]
```

---

# 9. Context Isolation

## Context Isolation Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Context Boundaries

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
[ ] Tool response vs system instruction
[ ] Other
```

## Context Isolation Controls

```text
[Describe how context is separated, cleared, labeled, minimized, or restricted]
```

## Memory or Conversation History Used?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Memory / History Controls

```text
[Describe memory, conversation history, retention, clearing, or persistence controls]
```

## Context Isolation Notes

```text
[Describe context contamination, cross-user, cross-tenant, or stale-context risks]
```

---

# 10. External and Untrusted Input Control

## External Inputs Processed?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## External Input Sources

Select all that apply:

```text
[ ] Customers
[ ] Suppliers
[ ] Partners
[ ] Public web
[ ] Third-party documents
[ ] Email
[ ] Chat
[ ] Forms
[ ] Uploaded files
[ ] API feeds
[ ] External logs
[ ] Vendor systems
[ ] Other
```

## External Input Controls

Select all that apply:

```text
[ ] Source validation
[ ] Format validation
[ ] Malware scanning
[ ] Prompt injection scanning
[ ] Sensitive data detection
[ ] Trusted/untrusted separation
[ ] Tool-use restriction
[ ] Human approval
[ ] Logging
[ ] Escalation
[ ] Other
```

## External Input Notes

```text
[Describe external input controls and limitations]
```

---

# 11. Tool Response Input Control

Complete this section if AI receives tool responses.

## Tool Responses Used?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Tool Response Sources

| Tool | Response Type | Trust Level | Validation Required? | Notes |
|---|---|---|---|---|
| [Tool] | [Response] | [Trusted/Untrusted/Mixed] | [Yes/No] | [Notes] |

## Tool Response Controls

```text
[Describe how tool responses are validated before being treated as context or instructions]
```

## Tool Response Notes

```text
[Describe risks of tool response contamination or unsafe action chaining]
```

---

# 12. Prompt and Input Logging

## Logging Approach

Select one:

```text
[ ] No prompt content logging
[ ] Metadata-only logging
[ ] Redacted prompt logging
[ ] Full prompt logging
[ ] Hash/reference-only logging
[ ] Violation-only logging
[ ] Sampling
[ ] Unknown
```

## Logged Fields

Select all that apply:

```text
[ ] User identity
[ ] AI system identity
[ ] Session ID
[ ] Timestamp
[ ] Prompt metadata
[ ] Prompt content
[ ] Redacted prompt content
[ ] Input source
[ ] Data classification
[ ] Policy decision
[ ] Warning shown
[ ] Block decision
[ ] Approval decision
[ ] Violation type
[ ] Other
```

## Log Location

```text
[Describe where logs are stored]
```

## Retention Period

```text
[Describe retention period]
```

## Log Access Restrictions

```text
[Describe who can access prompt/input logs]
```

## Logging Notes

```text
[Describe privacy, confidentiality, retention, and evidence considerations]
```

---

# 13. Prompt Change Management

## Prompt Changes Require Review?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Prompt Types Under Change Control

Select all that apply:

```text
[ ] System prompt
[ ] Developer prompt
[ ] Policy prompt
[ ] Guardrail prompt
[ ] Tool instruction
[ ] Retrieval prompt
[ ] Agent planning prompt
[ ] Classification prompt
[ ] Customer-facing prompt
[ ] Other
```

## Change Review Requirements

Select all that apply:

```text
[ ] Business owner review
[ ] Technical owner review
[ ] Security review
[ ] Architecture review
[ ] Privacy/legal review
[ ] Testing before deployment
[ ] Regression testing
[ ] Rollback plan
[ ] Evidence retention
```

## Change Record Location

```text
[Describe where prompt changes are recorded]
```

## Prompt Change Notes

```text
[Describe change triggers, testing, approval, and rollback expectations]
```

---

# 14. Input Policy Violations

## Violation Types Monitored

Select all that apply:

```text
[ ] Prohibited sensitive data
[ ] Secrets or credentials
[ ] Malicious instructions
[ ] Prompt injection attempt
[ ] Unauthorized file type
[ ] Unapproved data source
[ ] Policy bypass attempt
[ ] Excessive input size
[ ] Cross-boundary context attempt
[ ] Unsafe request
[ ] Prohibited use case
[ ] Other
```

## Violation Response

Select all that apply:

```text
[ ] Warn
[ ] Block
[ ] Redact
[ ] Route for approval
[ ] Log
[ ] Escalate
[ ] Suspend session
[ ] Trigger incident response
[ ] Update policy
[ ] Educate user
[ ] Other
```

## Violation Evidence

```text
[Describe evidence captured for input policy violations]
```

---

# 15. Testing and Assurance

## Required Tests

Select all that apply:

```text
[ ] Allowed input test
[ ] Prohibited input test
[ ] Sensitive data input test
[ ] Prompt injection test
[ ] System prompt protection test
[ ] System prompt change test
[ ] Context isolation test
[ ] External input test
[ ] Tool response validation test
[ ] Prompt/input logging test
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

# 16. Exceptions

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

# 17. Approval

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

## Security / Architecture Approval

```text
Name or forum:
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

## Final Prompt/Input Control Decision

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

# 18. Review Triggers

Review this prompt and input control design if any of the following occur:

```text
[ ] System prompt changes
[ ] Policy prompt changes
[ ] Tool instruction changes
[ ] Retrieval prompt changes
[ ] External input source changes
[ ] Data classification changes
[ ] Context isolation changes
[ ] Memory or history behavior changes
[ ] Tool response behavior changes
[ ] Prompt injection finding occurs
[ ] Input policy violation increases
[ ] Incident occurs
[ ] Risk tier changes
```

## Next Review Date

```text
[Enter date]
```

---

# 19. Summary

```text
Use case:
Risk tier:
Input sources:
Allowed inputs:
Prohibited inputs:
System prompt control:
Prompt injection risk:
Context isolation:
External input control:
Logging approach:
Required testing:
Exceptions:
Approval status:
Next review date:
```