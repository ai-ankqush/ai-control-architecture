# AI Monitoring, Logging, and Evidence Template

This template is used to define, approve, test, and evidence monitoring, logging, and evidence requirements for an AI use case.

AI systems must be observable and reconstructable.

The purpose of this template is to ensure the enterprise can understand what AI saw, what it produced, what data it accessed, what tools it called, what actions it triggered, who reviewed or approved it, and how evidence is retained for assurance, audit, investigation, and incident response.

---

# 1. Monitoring and Evidence Information

## AI Use Case Name

```text
[Enter AI use case name]
```

## Monitoring / Evidence Record ID

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

## Monitoring Owner

```text
Name:
Function:
Email:
```

## Evidence Owner

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

## Evidence Requirement Summary

```text
[Summarize what evidence must exist for this AI use case]
```

---

# 3. Logging Requirement by Risk Tier

## Logging Depth Required

Select one:

```text
[ ] Basic usage metadata
[ ] Usage logs and input/output metadata
[ ] Output, validation, reviewer, and decision evidence
[ ] Tool call, action, approval, and boundary evidence
[ ] Full reconstructable evidence across identity, data, input, output, tools, actions, approvals, assurance, and containment
[ ] Unknown
```

## Logging Rationale

```text
[Explain why this logging depth is required]
```

## Logging Constraints

```text
[Describe privacy, confidentiality, legal, vendor, technical, or retention constraints]
```

---

# 4. AI Event Taxonomy

## Events to Capture

Select all that apply:

```text
[ ] Use case registration
[ ] Risk tier assignment
[ ] Lifecycle status change
[ ] AI identity creation
[ ] Delegated authority granted
[ ] Access approved
[ ] Access reviewed
[ ] Access revoked
[ ] Data source accessed
[ ] Retrieval performed
[ ] Prompt submitted
[ ] Input blocked
[ ] Prompt injection detected
[ ] Output generated
[ ] Output validated
[ ] Output rejected
[ ] Decision reviewed
[ ] Decision approved
[ ] Tool called
[ ] Tool denied
[ ] Action requested
[ ] Action approved
[ ] Action executed
[ ] Action rolled back
[ ] Exception requested
[ ] Exception approved
[ ] Policy violation detected
[ ] Assurance test executed
[ ] Finding opened
[ ] Incident opened
[ ] Containment performed
[ ] Evidence preserved
[ ] Other
```

## Event Taxonomy Notes

```text
[Describe event naming, categories, owners, and source systems]
```

---

# 5. Common Log Fields

## Required Log Fields

Select all that apply:

```text
[ ] Event ID
[ ] Timestamp
[ ] Use case ID
[ ] AI system ID
[ ] AI actor identity
[ ] User identity
[ ] Service identity
[ ] Agent identity
[ ] Session ID
[ ] Workflow ID
[ ] Risk tier
[ ] Event type
[ ] Source system
[ ] Data source
[ ] Prompt/input reference
[ ] Retrieved context reference
[ ] Output reference
[ ] Tool called
[ ] Action requested
[ ] Action executed
[ ] Approval status
[ ] Policy decision
[ ] Exception status
[ ] Result
[ ] Error code
[ ] Incident marker
[ ] Other
```

## Sensitive Fields

Select all that may contain sensitive data:

```text
[ ] Prompt content
[ ] Output content
[ ] Retrieved context
[ ] Customer data
[ ] Employee data
[ ] Regulated data
[ ] Legal content
[ ] Secrets
[ ] API parameters
[ ] Tool outputs
[ ] Other
```

## Sensitive Field Handling

```text
[Describe masking, redaction, restricted access, encryption, or reference-only logging]
```

---

# 6. Prompt and Input Logging

## Prompt/Input Logging Approach

Select one:

```text
[ ] No prompt content logging
[ ] Metadata-only logging
[ ] Redacted prompt logging
[ ] Full prompt logging
[ ] Reference or hash only
[ ] Violation-only logging
[ ] Sampling
[ ] Unknown
```

## Prompt/Input Evidence Required

Select all that apply:

```text
[ ] User identity
[ ] Timestamp
[ ] Session ID
[ ] Prompt metadata
[ ] Prompt content
[ ] Redacted prompt content
[ ] Input source
[ ] Data classification
[ ] Sensitive data detection result
[ ] Policy decision
[ ] Warning shown
[ ] Block decision
[ ] Approval decision
[ ] Violation type
[ ] Other
```

## Prompt/Input Log Location

```text
[Describe where prompt/input logs or metadata are stored]
```

## Prompt/Input Logging Notes

```text
[Describe privacy, confidentiality, retention, and investigation considerations]
```

---

# 7. Retrieval and Context Logging

Complete this section if the AI use case uses retrieval, search, RAG, enterprise knowledge, document grounding, memory, or context assembly.

## Retrieval Used?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Retrieval Evidence Required

Select all that apply:

```text
[ ] Query
[ ] User identity
[ ] AI identity
[ ] Repository
[ ] Document ID
[ ] Document classification
[ ] Retrieved excerpt reference
[ ] Relevance score
[ ] Access decision
[ ] Context inclusion decision
[ ] Retrieval timestamp
[ ] Denied retrieval event
[ ] Sensitivity label
[ ] Other
```

## Context Evidence Required

Select all that apply:

```text
[ ] Context sources
[ ] Context classification
[ ] Context size
[ ] Trusted versus untrusted context marker
[ ] Source attribution
[ ] Memory use
[ ] Session history use
[ ] Context boundary decision
[ ] Other
```

## Retrieval / Context Log Location

```text
[Describe where retrieval and context evidence is stored]
```

## Retrieval / Context Logging Notes

```text
[Describe whether full content, references, hashes, or metadata are retained]
```

---

# 8. Output Logging

## Output Logging Approach

Select one:

```text
[ ] No output content logging
[ ] Metadata-only logging
[ ] Redacted output logging
[ ] Full output logging
[ ] Reference or hash only
[ ] Violation-only logging
[ ] Sampling
[ ] Unknown
```

## Output Evidence Required

Select all that apply:

```text
[ ] Output generated
[ ] Output metadata
[ ] Output classification
[ ] Source reference
[ ] Sensitivity label
[ ] Validation status
[ ] Reviewer record
[ ] Approval record
[ ] Rejection record
[ ] Modification record
[ ] Override record
[ ] Correction record
[ ] Generated record metadata
[ ] Other
```

## Output Log Location

```text
[Describe where output logs or metadata are stored]
```

## Output Logging Notes

```text
[Describe output reconstruction, privacy, sensitivity, and retention considerations]
```

---

# 9. Decision Evidence

Complete this section if AI output influences a decision.

## Decision Evidence Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Decision Evidence Required

Select all that apply:

```text
[ ] AI recommendation
[ ] Final decision
[ ] Decision owner
[ ] Reviewer
[ ] Approver
[ ] Approval time
[ ] Modification record
[ ] Rejection record
[ ] Override record
[ ] Decision rationale
[ ] Source evidence
[ ] Downstream use record
[ ] Other
```

## Decision Evidence Location

```text
[Describe where decision evidence is stored]
```

## Decision Evidence Notes

```text
[Describe how AI recommendation is separated from final accountable decision]
```

---

# 10. Tool Call and Action Logging

Complete this section if AI can call tools, APIs, workflows, or execute actions.

## Tool or Action Capability Exists?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Tool Call Logs Required

Select all that apply:

```text
[ ] AI system identity
[ ] Agent identity
[ ] Initiating user
[ ] Delegated authority
[ ] Session ID
[ ] Workflow ID
[ ] Tool called
[ ] Tool owner
[ ] Action requested
[ ] Parameters supplied
[ ] Data accessed
[ ] Approval required
[ ] Approval received
[ ] Action executed
[ ] Result
[ ] Exception
[ ] Timestamp
[ ] Downstream system affected
[ ] Rollback status
[ ] Other
```

## Action Logs Required

Select all that apply:

```text
[ ] Action requested
[ ] Action approved
[ ] Action executed
[ ] Action failed
[ ] Action denied
[ ] Action rolled back
[ ] System affected
[ ] Records affected
[ ] User/customer affected
[ ] Approval evidence
[ ] Recovery evidence
[ ] Other
```

## Tool/Action Log Location

```text
[Describe where tool call and action logs are stored]
```

## Tool/Action Logging Notes

```text
[Describe investigation, audit, rollback, and accountability needs]
```

---

# 11. Approval and Exception Logging

## Approval Logging Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Approval Evidence Required

Select all that apply:

```text
[ ] Request
[ ] AI output or action being approved
[ ] Risk level
[ ] Approver
[ ] Approval decision
[ ] Approval time
[ ] Rationale where required
[ ] Expiry where applicable
[ ] Downstream action
[ ] Evidence link
[ ] Other
```

## Exception Logging Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Exception Evidence Required

Select all that apply:

```text
[ ] Requirement affected
[ ] Control gap
[ ] Business justification
[ ] Risk accepted
[ ] Compensating control
[ ] Exception owner
[ ] Approver
[ ] Approval date
[ ] Expiry date
[ ] Review date
[ ] Remediation plan
[ ] Closure status
[ ] Other
```

## Approval / Exception Evidence Location

```text
[Describe where approval and exception evidence is stored]
```

---

# 12. Monitoring and Alerts

## Monitoring Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Policy Violations to Monitor

Select all that apply:

```text
[ ] Unauthorized AI use
[ ] Shadow AI use
[ ] Prohibited prompt
[ ] Sensitive data in prompt
[ ] Prompt injection attempt
[ ] Unauthorized retrieval
[ ] Cross-boundary data access
[ ] Unsafe output
[ ] Customer-facing policy violation
[ ] Approval bypass
[ ] Unauthorized tool call
[ ] Abnormal tool use
[ ] Excessive action volume
[ ] Missing logs
[ ] Expired exception
[ ] Failed control
[ ] Vendor AI policy breach
[ ] Other
```

## Anomaly Signals to Monitor

Select all that apply:

```text
[ ] Unusual usage volume
[ ] Unusual user behavior
[ ] Unusual data access
[ ] Unusual retrieval pattern
[ ] Repeated output rejection
[ ] High hallucination or error rate
[ ] Tool call spike
[ ] Action failure spike
[ ] Approval bypass attempt
[ ] Excessive retries
[ ] Kill switch activation
[ ] Vendor alert
[ ] Other
```

## Alert Routing

```text
[Describe where alerts go and who responds]
```

## Monitoring Notes

```text
[Describe thresholds, rules, response actions, and escalation]
```

---

# 13. Monitoring Integration

## Integration Targets

Select all that apply:

```text
[ ] SIEM
[ ] SOC
[ ] GRC
[ ] DLP
[ ] IAM
[ ] PAM
[ ] Data governance platform
[ ] Application monitoring
[ ] API monitoring
[ ] Workflow monitoring
[ ] Incident response platform
[ ] Audit evidence repository
[ ] Vendor risk platform
[ ] Privacy case management
[ ] Other
```

## Integration Description

```text
[Describe AI event integration with existing monitoring and evidence systems]
```

## Integration Gaps

```text
[Describe integration limitations, manual processes, or vendor gaps]
```

---

# 14. Evidence Storage and Retention

## Evidence Repository

```text
[Describe where evidence is stored]
```

## Evidence Owner

```text
Name:
Function:
Email:
```

## Retention Requirements

| Evidence Type | Retention Period | Owner | Legal Hold Applies? |
|---|---|---|---|
| [Evidence type] | [Period] | [Owner] | [Yes/No/Unknown] |

## Deletion Requirements

```text
[Describe deletion process, expiry, legal hold, and privacy rights considerations]
```

## Evidence Retention Notes

```text
[Describe evidence retention risks and constraints]
```

---

# 15. Evidence Protection

## Protection Controls

Select all that apply:

```text
[ ] Access control
[ ] Encryption
[ ] Role-based viewing
[ ] Masking
[ ] Redaction
[ ] Segregation of duties
[ ] Immutable logging
[ ] Tamper detection
[ ] Audit trail
[ ] Retention controls
[ ] Legal hold controls
[ ] Secure export controls
[ ] Other
```

## Authorized Evidence Access

Select all that apply:

```text
[ ] Business owner
[ ] Technical owner
[ ] Control owner
[ ] Auditor
[ ] Incident responder
[ ] Security analyst
[ ] Privacy/legal team
[ ] Assurance team
[ ] Authorized administrator
[ ] Other
```

## Evidence Protection Notes

```text
[Describe how logs and evidence are protected from unauthorized access or tampering]
```

---

# 16. Evidence Reconstruction

## Reconstructability Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Reconstruction Questions

| Question | Evidence Source |
|---|---|
| What AI use case was involved? | [Evidence source] |
| Who initiated the interaction? | [Evidence source] |
| What identity did AI use? | [Evidence source] |
| What data was accessed? | [Evidence source] |
| What prompt or input was submitted? | [Evidence source] |
| What context was retrieved? | [Evidence source] |
| What output was generated? | [Evidence source] |
| What tool was called? | [Evidence source] |
| What action was requested? | [Evidence source] |
| Was approval required? | [Evidence source] |
| Was approval obtained? | [Evidence source] |
| What action executed? | [Evidence source] |
| What downstream system was affected? | [Evidence source] |
| What exception occurred? | [Evidence source] |
| What policy decision occurred? | [Evidence source] |
| What incident response action was taken? | [Evidence source] |

## Reconstruction Notes

```text
[Describe whether activity can be reconstructed and what gaps remain]
```

---

# 17. Vendor Evidence

Complete this section if vendor AI is involved.

## Vendor Logs Available?

```text
[ ] No
[ ] Yes
[ ] Partial
[ ] Unknown
```

## Vendor Evidence Available

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
[ ] Configuration records
[ ] Feature enablement records
[ ] Retention evidence
[ ] Training/reuse evidence
[ ] Other
```

## Vendor Log Retention

```text
[Describe vendor log retention period]
```

## Vendor Evidence Export

```text
[Describe whether evidence can be exported and how]
```

## Vendor Evidence Gaps

```text
[Describe vendor evidence limitations]
```

---

# 18. Testing and Assurance

## Required Tests

Select all that apply:

```text
[ ] Logging requirements test
[ ] Prompt/input logging test
[ ] Retrieval logging test
[ ] Output logging test
[ ] Decision evidence test
[ ] Tool/action logging test
[ ] Approval logging test
[ ] Exception logging test
[ ] Policy violation alert test
[ ] Monitoring integration test
[ ] Log protection test
[ ] Evidence reconstruction test
[ ] Evidence retention test
[ ] Incident evidence preservation test
[ ] Vendor evidence test
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

# 19. Exceptions

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

# 20. Approval

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

## Monitoring / Evidence Owner Approval

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

## Final Monitoring/Evidence Decision

Select one:

```text
[ ] Approved
[ ] Approved with conditions
[ ] Approved for pilot only
[ ] Requires remediation
[ ] Requires exception approval
[ ] Requires additional testing
[ ] Rejected
[ ] Deferred
```

## Approval Conditions

```text
[List conditions required before approval, production use, scaling, or continued operation]
```

---

# 21. Review Triggers

Review this monitoring, logging, and evidence design if any of the following occur:

```text
[ ] Risk tier changes
[ ] Data source changes
[ ] Output use changes
[ ] Decision impact changes
[ ] Tool/action capability changes
[ ] Vendor logging changes
[ ] Retention requirements change
[ ] Monitoring integration changes
[ ] Evidence gap identified
[ ] Incident occurs
[ ] Audit finding occurs
[ ] Assurance finding occurs
[ ] Legal or privacy requirement changes
```

## Next Review Date

```text
[Enter date]
```

---

# 22. Summary

```text
Use case:
Risk tier:
Logging depth:
Prompt/input logging:
Retrieval/context logging:
Output logging:
Decision evidence:
Tool/action logging:
Monitoring alerts:
Evidence repository:
Retention:
Evidence protection:
Reconstructability:
Vendor evidence:
Required testing:
Exceptions:
Approval status:
Next review date:
```