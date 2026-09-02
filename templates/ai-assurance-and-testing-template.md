# AI Assurance and Testing Template

This template is used to define, approve, execute, evidence, and review assurance and testing for an AI use case.

AI must be tested before and after deployment.

AI assurance must validate both:

1. AI behavior
2. AI control effectiveness

The purpose of this template is to ensure that AI systems are not trusted based only on usefulness, vendor claims, or user confidence. They must be tested against the risks, controls, evidence, and failure modes that apply to their assigned risk tier.

---

# 1. Assurance and Testing Information

## AI Use Case Name

```text
[Enter AI use case name]
```

## Assurance Record ID

```text
[Enter assurance record ID]
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

## Assurance Owner

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

## Assurance Summary

```text
[Summarize what assurance must prove for this AI use case]
```

---

# 3. Assurance Scope

## Assurance Scope

Select all that apply:

```text
[ ] AI behavior
[ ] AI output quality
[ ] AI decision impact
[ ] AI identity and access controls
[ ] AI data boundaries
[ ] Prompt and input controls
[ ] Prompt injection resistance
[ ] Output and decision controls
[ ] Tool and action controls
[ ] Human accountability
[ ] Monitoring and logging
[ ] Evidence reconstruction
[ ] Incident containment
[ ] Vendor AI controls
[ ] Regression testing
[ ] Other
```

## Systems in Scope

```text
[List applications, models, vendors, platforms, data sources, tools, APIs, workflows, and environments in scope]
```

## Systems Out of Scope

```text
[List systems, tools, data sources, or processes excluded from this assurance activity]
```

## Assurance Scope Notes

```text
[Describe scope assumptions, constraints, and limitations]
```

---

# 4. Assurance Requirement by Risk Tier

## Required Assurance Level

Select one:

```text
[ ] Basic review
[ ] Targeted control review
[ ] Pre-deployment assurance
[ ] Full control assurance
[ ] Enhanced or independent assurance
[ ] Unknown
```

## Assurance Rationale

```text
[Explain why this level of assurance is required based on risk tier and risk drivers]
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

# 5. Assurance Types Required

## Assurance Types

Select all that apply:

```text
[ ] Design assurance
[ ] Behavioral assurance
[ ] Control assurance
[ ] Security assurance
[ ] Privacy and data assurance
[ ] Operational assurance
[ ] Vendor assurance
[ ] Regression assurance
[ ] Independent assurance
```

## Design Assurance Notes

```text
[Describe architecture, design, and control mapping review required]
```

## Behavioral Assurance Notes

```text
[Describe AI behavior, accuracy, consistency, hallucination, and output quality review required]
```

## Control Assurance Notes

```text
[Describe control effectiveness testing required]
```

## Security Assurance Notes

```text
[Describe prompt injection, data leakage, tool misuse, privilege, or adversarial testing required]
```

## Privacy and Data Assurance Notes

```text
[Describe privacy, data processing, retention, reuse, and data boundary review required]
```

## Operational Assurance Notes

```text
[Describe monitoring, incident response, kill switch, rollback, and support model testing required]
```

## Vendor Assurance Notes

```text
[Describe vendor AI review, evidence, contractual, retention, logging, and incident support review required]
```

---

# 6. Pre-Deployment Testing

## Pre-Deployment Testing Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Pre-Deployment Test Areas

Select all that apply:

```text
[ ] Use case classification
[ ] Risk tier validation
[ ] Architecture review
[ ] Identity and access review
[ ] Data boundary review
[ ] Prompt/input control review
[ ] Output/decision control review
[ ] Tool/action control review
[ ] Human accountability review
[ ] Logging/evidence review
[ ] Incident containment review
[ ] Vendor review
[ ] Other
```

## Pre-Deployment Acceptance Criteria

```text
[Describe what must pass before pilot, production, scaling, or continued use]
```

## Pre-Deployment Notes

```text
[Document pre-deployment findings, open issues, and conditions]
```

---

# 7. Prompt Injection Testing

## Prompt Injection Testing Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Prompt Injection Test Sources

Select all that apply:

```text
[ ] User prompts
[ ] Retrieved documents
[ ] Uploaded files
[ ] Emails
[ ] Tickets
[ ] Chat messages
[ ] Customer submissions
[ ] Web content
[ ] Tool responses
[ ] Code comments
[ ] Logs
[ ] Third-party content
[ ] Other
```

## Prompt Injection Test Cases

| Test Case | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|
| [Test case] | [Expected] | [Actual] | [Pass/Fail/Partial/Not Run] | [Evidence] |

## Prompt Injection Findings

```text
[Document findings, weaknesses, residual risk, and remediation actions]
```

---

# 8. Data Leakage Testing

## Data Leakage Testing Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Data Leakage Test Areas

Select all that apply:

```text
[ ] Prompt leakage
[ ] Output leakage
[ ] Retrieval boundary leakage
[ ] Cross-user leakage
[ ] Cross-tenant leakage
[ ] Cross-classification leakage
[ ] Vendor processing leakage
[ ] Log leakage
[ ] Tool output leakage
[ ] Memory or history leakage
[ ] Other
```

## Data Leakage Test Cases

| Test Case | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|
| [Test case] | [Expected] | [Actual] | [Pass/Fail/Partial/Not Run] | [Evidence] |

## Data Leakage Findings

```text
[Document findings, affected data, control gaps, and remediation actions]
```

---

# 9. Output Validation Testing

## Output Validation Testing Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Output Validation Criteria

Select all that apply:

```text
[ ] Accuracy
[ ] Completeness
[ ] Consistency
[ ] Source grounding
[ ] Hallucination resistance
[ ] Policy compliance
[ ] Sensitivity handling
[ ] Decision readiness
[ ] Customer-facing appropriateness
[ ] Generated record quality
[ ] Bias or fairness where relevant
[ ] Other
```

## Output Validation Test Cases

| Test Case | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|
| [Test case] | [Expected] | [Actual] | [Pass/Fail/Partial/Not Run] | [Evidence] |

## Output Validation Findings

```text
[Document output quality issues, hallucinations, validation gaps, or review weaknesses]
```

---

# 10. Retrieval Boundary Testing

Complete this section if the AI use case uses retrieval, search, RAG, enterprise knowledge, or document grounding.

## Retrieval Boundary Testing Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Retrieval Boundary Test Areas

Select all that apply:

```text
[ ] Repository boundary
[ ] Document-level permission
[ ] User permission inheritance
[ ] Role-based retrieval
[ ] Attribute-based retrieval
[ ] Data classification filtering
[ ] Tenant boundary
[ ] Customer/account boundary
[ ] Project or workspace boundary
[ ] External content boundary
[ ] Sensitive source exclusion
[ ] Other
```

## Retrieval Boundary Test Cases

| Test Case | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|
| [Test case] | [Expected] | [Actual] | [Pass/Fail/Partial/Not Run] | [Evidence] |

## Retrieval Boundary Findings

```text
[Document retrieval boundary findings and remediation actions]
```

---

# 11. Tool and Action Testing

Complete this section if the AI can call tools, APIs, workflows, or execute actions.

## Tool and Action Testing Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Tool and Action Test Areas

Select all that apply:

```text
[ ] Tool inventory validation
[ ] Tool permission validation
[ ] Unauthorized tool call test
[ ] Action classification test
[ ] Action boundary test
[ ] Approval gate test
[ ] Approval bypass test
[ ] Blast-radius limit test
[ ] Autonomous execution limit test
[ ] Tool call logging test
[ ] Action logging test
[ ] Kill switch test
[ ] Rollback test
[ ] Other
```

## Tool and Action Test Cases

| Test Case | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|
| [Test case] | [Expected] | [Actual] | [Pass/Fail/Partial/Not Run] | [Evidence] |

## Tool and Action Findings

```text
[Document tool misuse, approval, action boundary, or rollback findings]
```

---

# 12. Human Accountability Testing

## Accountability Testing Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Accountability Test Areas

Select all that apply:

```text
[ ] Business owner assigned
[ ] Technical owner assigned
[ ] Data owner assigned where required
[ ] Decision owner assigned where required
[ ] Human review model defined
[ ] Approval responsibilities defined
[ ] Escalation path defined
[ ] Override rights defined
[ ] Exception ownership defined
[ ] Incident ownership defined
[ ] RACI reviewed
[ ] Accountability evidence retained
```

## Accountability Test Cases

| Test Case | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|
| [Test case] | [Expected] | [Actual] | [Pass/Fail/Partial/Not Run] | [Evidence] |

## Accountability Findings

```text
[Document accountability gaps or ownership weaknesses]
```

---

# 13. Logging and Evidence Testing

## Logging and Evidence Testing Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Logging and Evidence Test Areas

Select all that apply:

```text
[ ] Logging requirements defined
[ ] Prompt/input logging
[ ] Retrieval logging
[ ] Output logging
[ ] Decision evidence
[ ] Tool/action logging
[ ] Approval logging
[ ] Exception logging
[ ] Policy violation alert
[ ] Monitoring integration
[ ] Log protection
[ ] Evidence retention
[ ] Evidence reconstruction
[ ] Vendor evidence
[ ] Other
```

## Logging and Evidence Test Cases

| Test Case | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|
| [Test case] | [Expected] | [Actual] | [Pass/Fail/Partial/Not Run] | [Evidence] |

## Logging and Evidence Findings

```text
[Document logging, monitoring, retention, or reconstruction findings]
```

---

# 14. Incident Containment Testing

## Incident Containment Testing Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Incident Containment Test Areas

Select all that apply:

```text
[ ] Access revocation test
[ ] Agent kill switch test
[ ] Tool disablement test
[ ] Workflow stop test
[ ] Vendor feature disablement test
[ ] Output quarantine test
[ ] Evidence preservation test
[ ] Recovery test
[ ] Rollback test
[ ] Restart approval test
[ ] Incident tabletop
[ ] Other
```

## Incident Containment Test Cases

| Test Case | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|
| [Test case] | [Expected] | [Actual] | [Pass/Fail/Partial/Not Run] | [Evidence] |

## Incident Containment Findings

```text
[Document containment, evidence preservation, recovery, or restart findings]
```

---

# 15. Vendor Assurance

Complete this section if vendor AI is involved.

## Vendor Assurance Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Vendor Assurance Areas

Select all that apply:

```text
[ ] Vendor AI feature behavior
[ ] Vendor data processing
[ ] Vendor retention
[ ] Vendor training/reuse
[ ] Vendor logging
[ ] Vendor evidence export
[ ] Vendor admin controls
[ ] Vendor identity model
[ ] Vendor incident support
[ ] Vendor contractual commitments
[ ] Vendor assurance reports
[ ] Vendor subprocessors
[ ] Other
```

## Vendor Assurance Findings

| Finding ID | Finding | Severity | Owner | Due Date | Status |
|---|---|---|---|---|---|
| [Finding ID] | [Finding] | [Low/Medium/High/Critical] | [Owner] | [Date] | [Status] |

## Vendor Assurance Notes

```text
[Document vendor evidence reviewed, gaps, conditions, and residual risk]
```

---

# 16. Regression Testing

## Regression Testing Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Regression Triggers

Select all that apply:

```text
[ ] Model changed
[ ] Model provider changed
[ ] System prompt changed
[ ] Policy prompt changed
[ ] Retrieval prompt changed
[ ] Retrieval logic changed
[ ] Data source changed
[ ] Vector index changed
[ ] Embedding model changed
[ ] Tool permission changed
[ ] API integration changed
[ ] Workflow logic changed
[ ] Approval gate changed
[ ] Logging configuration changed
[ ] Vendor feature changed
[ ] Risk tier changed
[ ] Business process changed
[ ] Other
```

## Regression Test Scope

```text
[Describe what must be retested after change]
```

## Regression Notes

```text
[Document regression test results or required future regression triggers]
```

---

# 17. Findings Register

## Findings

| Finding ID | Test Area | Finding Description | Severity | Owner | Due Date | Status |
|---|---|---|---|---|---|---|
| [Finding ID] | [Area] | [Description] | [Low/Medium/High/Critical] | [Owner] | [Date] | [Status] |

## Finding Severity Definitions

| Severity | Description |
|---|---|
| Critical | AI can cause high-impact harm without effective control. |
| High | Significant control weakness affecting sensitive data, decisions, actions, or evidence. |
| Medium | Control weakness with limited impact or compensating controls. |
| Low | Minor gap or improvement opportunity. |

---

# 18. Remediation and Retest

## Remediation Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Remediation Actions

| Action ID | Related Finding | Remediation Action | Owner | Due Date | Status | Evidence |
|---|---|---|---|---|---|---|
| [Action ID] | [Finding] | [Action] | [Owner] | [Date] | [Status] | [Evidence] |

## Retest Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Retest Results

```text
[Document retest results, remaining gaps, or accepted residual risk]
```

---

# 19. Risk Acceptance

## Risk Acceptance Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Risk Acceptance Summary

| Risk | Owner | Acceptance Decision | Expiry | Evidence |
|---|---|---|---|---|
| [Risk] | [Owner] | [Decision] | [Expiry] | [Evidence] |

## Residual Risk

```text
[Describe residual risk after remediation and retesting]
```

---

# 20. Assurance Decision

## Overall Assurance Result

Select one:

```text
[ ] Passed
[ ] Passed with minor findings
[ ] Passed with conditions
[ ] Failed
[ ] Incomplete
[ ] Deferred
```

## Readiness Decision

Select one:

```text
[ ] Ready for approved use
[ ] Ready for pilot only
[ ] Ready after remediation
[ ] Requires risk acceptance
[ ] Not ready
[ ] Requires additional testing
```

## Conditions for Approval

```text
[List required conditions before production, scaling, or continued use]
```

## Assurance Decision Notes

```text
[Document final assurance conclusion and reasoning]
```

---

# 21. Approval

## Assurance Owner Sign-Off

```text
Name:
Decision:
Date:
Notes:
```

## Business Owner Sign-Off

```text
Name:
Decision:
Date:
Notes:
```

## Technical Owner Sign-Off

```text
Name:
Decision:
Date:
Notes:
```

## Security / Architecture Sign-Off

```text
Name or forum:
Decision:
Date:
Notes:
```

## Risk / Governance Sign-Off

```text
Name or forum:
Decision:
Date:
Notes:
```

---

# 22. Review Triggers

Review or repeat assurance if any of the following occur:

```text
[ ] Model changes
[ ] Provider changes
[ ] Vendor feature changes
[ ] System prompt changes
[ ] Data source changes
[ ] Retrieval logic changes
[ ] Tool/API access changes
[ ] Workflow changes
[ ] Approval gate changes
[ ] Logging changes
[ ] Risk tier changes
[ ] User population changes
[ ] Incident occurs
[ ] Assurance finding occurs
[ ] Regulatory or legal requirement changes
```

## Next Assurance Review Date

```text
[Enter date]
```

---

# 23. Summary

```text
Use case:
Risk tier:
Assurance scope:
Required tests:
Prompt injection result:
Data leakage result:
Output validation result:
Tool/action result:
Logging/evidence result:
Incident containment result:
Vendor assurance result:
Critical findings:
High findings:
Residual risk:
Readiness decision:
Approval status:
Next review date:
```