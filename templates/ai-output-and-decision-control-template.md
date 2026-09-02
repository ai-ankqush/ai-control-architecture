# AI Output and Decision Control Template

This template is used to define, approve, test, and evidence how AI-generated outputs are validated, reviewed, approved, used, corrected, logged, and governed.

AI output must not silently become a decision, record, customer communication, workflow instruction, or system action without appropriate control.

The purpose of this template is to define how AI outputs are classified, validated, reviewed, approved, monitored, corrected, and evidenced.

---

# 1. Output and Decision Control Information

## AI Use Case Name

```text
[Enter AI use case name]
```

## Output/Decision Control ID

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

## Decision Owner

```text
Name:
Function:
Email:
Not applicable reason, if any:
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

# 3. Output Classification

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

## Output Category

Select all that apply:

```text
[ ] Informational
[ ] Advisory
[ ] Operational
[ ] Decision-supporting
[ ] Customer-facing
[ ] Regulated
[ ] Action-triggering
[ ] Record-generating
[ ] Unknown
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

## Output Classification Notes

```text
[Describe output type, audience, impact, and classification rationale]
```

---

# 4. Decision Impact

## Does AI Output Influence a Decision?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Decision Impact Level

Select one:

```text
[ ] None
[ ] Low
[ ] Moderate
[ ] High
[ ] Critical
[ ] Unknown
```

## Decision Types Influenced

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

## Decision Description

```text
[Describe the decision or judgment influenced by AI output]
```

## Final Decision Owner

```text
Name:
Function:
Email:
```

## Decision Impact Notes

```text
[Describe how AI output influences the decision and what could go wrong]
```

---

# 5. Recommendation vs Final Decision Separation

## AI Recommendation Separate From Final Decision?

```text
[ ] No
[ ] Yes
[ ] Not applicable
[ ] Unknown
```

## Separation Method

Select all that apply:

```text
[ ] AI output is labeled as recommendation
[ ] Final decision requires human approval
[ ] Final decision is recorded separately
[ ] Reviewer identity is captured
[ ] Decision owner is captured
[ ] Downstream action is blocked until approval
[ ] System distinguishes draft from final
[ ] Other
```

## Recommendation Label

```text
[Describe how AI-generated recommendations are labeled]
```

## Final Decision Record

```text
[Describe where and how the final decision is recorded]
```

## Separation Notes

```text
[Describe how recommendation, review, approval, and final decision are separated]
```

---

# 6. Output Validation

## Validation Required?

```text
[ ] No
[ ] Yes
[ ] Conditional
[ ] Unknown
```

## Validation Methods

Select all that apply:

```text
[ ] User review
[ ] Human approval
[ ] Source checking
[ ] Automated rule check
[ ] Peer review
[ ] Supervisor approval
[ ] Second-line review
[ ] Legal review
[ ] Privacy review
[ ] Compliance review
[ ] Data owner review
[ ] Fact checking
[ ] Sampling
[ ] Confidence threshold
[ ] Comparison with authoritative system
[ ] Regression testing
[ ] Other
```

## Validation Criteria

Select all that apply:

```text
[ ] Accuracy
[ ] Completeness
[ ] Source grounding
[ ] Policy compliance
[ ] Data sensitivity
[ ] Harmful content
[ ] Decision readiness
[ ] Customer impact
[ ] Legal or regulatory impact
[ ] Operational impact
[ ] Security impact
[ ] Bias or fairness where relevant
[ ] Other
```

## Validation Rule

```text
[Describe validation rule before output can be used]
```

## Validation Evidence Required

```text
[Describe evidence required to prove validation occurred]
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

## Review Pattern

Select one:

```text
[ ] No review
[ ] User review
[ ] Required approval
[ ] Second-line review
[ ] Sampling review
[ ] Exception-based review
[ ] Continuous monitoring
[ ] Not yet defined
```

## Reviewer Role

```text
Reviewer role:
Reviewer name or group:
Approval authority:
```

## Reviewer Requirements

Select all that apply:

```text
[ ] Reviewer has source material
[ ] Reviewer has sufficient context
[ ] Reviewer can reject output
[ ] Reviewer can modify output
[ ] Reviewer can escalate
[ ] Reviewer has time to review
[ ] Reviewer understands AI limitations
[ ] Review decision is logged
[ ] Other
```

## Review Notes

```text
[Describe how review is performed and how ceremonial review is avoided]
```

---

# 8. Customer-Facing or External Output

## Customer-Facing or External Output?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## External Output Type

Select all that apply:

```text
[ ] Customer response
[ ] Supplier communication
[ ] Partner communication
[ ] Public communication
[ ] Regulator communication
[ ] Legal communication
[ ] Financial communication
[ ] Marketing or public content
[ ] Other
```

## External Output Controls

Select all that apply:

```text
[ ] Approved response boundaries
[ ] Human review
[ ] Supervisor approval
[ ] Legal/compliance review
[ ] Customer escalation path
[ ] Content quality monitoring
[ ] Complaint handling
[ ] Correction process
[ ] Output logging
[ ] Disclosure where appropriate
[ ] Other
```

## External Output Notes

```text
[Describe customer-facing or external output risk and control expectations]
```

---

# 9. Generated Record Control

## Does Output Become an Enterprise Record?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Generated Record Type

Select all that apply:

```text
[ ] Case note
[ ] Customer summary
[ ] Investigation note
[ ] Audit narrative
[ ] HR summary
[ ] Legal draft
[ ] Compliance report
[ ] Financial narrative
[ ] Security incident summary
[ ] Operational report
[ ] Board or executive material
[ ] Other
```

## Generated Record Controls

Select all that apply:

```text
[ ] AI involvement identified
[ ] Provenance preserved
[ ] Source references retained
[ ] Human review required
[ ] Record owner assigned
[ ] Retention requirement applied
[ ] Sensitivity classification applied
[ ] Correction path defined
[ ] Approval logged
[ ] Other
```

## Generated Record Notes

```text
[Describe provenance, retention, correction, and record ownership]
```

---

# 10. Downstream Use Control

## Does Output Feed a Downstream System or Workflow?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Downstream Use

Select all that apply:

```text
[ ] Workflow routing
[ ] Case prioritization
[ ] Customer response
[ ] HR review
[ ] Financial approval
[ ] Security triage
[ ] Legal drafting
[ ] Compliance reporting
[ ] Ticket closure
[ ] Record update
[ ] API call
[ ] Agent action
[ ] Other
```

## Downstream Use Controls

Select all that apply:

```text
[ ] Validation required before downstream use
[ ] Approval required before downstream use
[ ] Output labeled as AI-generated
[ ] Output separated from final decision
[ ] Provenance retained
[ ] Downstream action blocked until approval
[ ] Rollback or correction path defined
[ ] Downstream system logs use
[ ] Other
```

## Downstream Use Notes

```text
[Describe how AI output is prevented from silently becoming trusted downstream input]
```

---

# 11. Prohibited or Restricted Output Uses

## Prohibited Uses

Select all that apply unless specifically approved:

```text
[ ] Legal conclusions
[ ] Regulated decisions
[ ] HR actions
[ ] Disciplinary decisions
[ ] Financial approvals
[ ] Payment decisions
[ ] Customer commitments
[ ] Medical or safety advice
[ ] Security enforcement actions
[ ] Production changes
[ ] Access grants or revocations
[ ] Compliance submissions
[ ] Contractual commitments
[ ] Public communications
[ ] Board or investor communications
[ ] Other
```

## Restricted Use Conditions

```text
[Describe conditions under which restricted output use may be allowed]
```

## Prohibited Use Handling

```text
[Describe what happens if AI output is used or attempted for prohibited purposes]
```

---

# 12. Output Uncertainty and Limitations

## Uncertainty or Limitation Disclosure Required?

```text
[ ] No
[ ] Yes
[ ] Conditional
[ ] Unknown
```

## Uncertainty Controls

Select all that apply:

```text
[ ] Confidence indicator
[ ] Source references
[ ] Limitation statement
[ ] Missing data indicator
[ ] Review reminder
[ ] Draft label
[ ] Recommendation-only label
[ ] Requires-approval label
[ ] Validation status
[ ] Source freshness indicator
[ ] Other
```

## Uncertainty Notes

```text
[Describe how uncertainty, assumptions, missing information, or limitations are communicated]
```

---

# 13. Output Quality Monitoring

## Output Quality Monitoring Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Monitoring Methods

Select all that apply:

```text
[ ] Sampling
[ ] Reviewer feedback
[ ] User feedback
[ ] Customer complaint analysis
[ ] Error tracking
[ ] Hallucination tracking
[ ] Quality scoring
[ ] Drift monitoring
[ ] Incident review
[ ] Red-team findings
[ ] Regression testing
[ ] Business outcome monitoring
[ ] Other
```

## Quality Metrics

Select all that apply:

```text
[ ] Accuracy
[ ] Completeness
[ ] Consistency
[ ] Source grounding
[ ] Hallucination rate
[ ] Policy violation rate
[ ] Escalation rate
[ ] Correction rate
[ ] Complaint rate
[ ] Reviewer override rate
[ ] Rejected output rate
[ ] Other
```

## Monitoring Notes

```text
[Describe monitoring frequency, owner, evidence, and escalation process]
```

---

# 14. Output Logging and Evidence

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

## Evidence Required

Select all that apply:

```text
[ ] Output log
[ ] Output classification
[ ] Source reference
[ ] Validation record
[ ] Reviewer record
[ ] Approval record
[ ] Rejection record
[ ] Modification record
[ ] Override record
[ ] Decision owner record
[ ] Downstream use record
[ ] Generated record metadata
[ ] Correction record
[ ] Quality monitoring result
[ ] Assurance test result
[ ] Exception record
```

## Evidence Location

```text
[Describe where output and decision evidence is stored]
```

## Retention Period

```text
[Describe retention period]
```

## Evidence Access Restrictions

```text
[Describe who can access output and decision evidence]
```

---

# 15. Correction, Override, and Remediation

## Correction Path Defined?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Override Path Defined?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Correction and Override Options

Select all that apply:

```text
[ ] User can reject output
[ ] User can edit output
[ ] Reviewer can override recommendation
[ ] Supervisor can reject final decision
[ ] Generated record can be amended
[ ] Customer communication can be corrected
[ ] Workflow can be stopped
[ ] Downstream action can be reversed
[ ] Incident can be opened
[ ] Other
```

## Correction Notes

```text
[Describe how incorrect, harmful, misleading, or unauthorized output is corrected or remediated]
```

---

# 16. Testing and Assurance

## Required Tests

Select all that apply:

```text
[ ] Output classification test
[ ] Output validation test
[ ] Source grounding test
[ ] Hallucination test
[ ] Recommendation vs decision separation test
[ ] Human review evidence test
[ ] Customer-facing output test
[ ] Generated record provenance test
[ ] Downstream use control test
[ ] Correction/override path test
[ ] Output logging test
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

# 17. Exceptions

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

# 18. Approval

## Business Owner Approval

```text
Name:
Decision:
Date:
Notes:
```

## Decision Owner Approval

```text
Name:
Decision:
Date:
Notes:
Not applicable reason, if any:
```

## Security / Architecture Approval

```text
Name or forum:
Decision:
Date:
Notes:
```

## Legal / Compliance / Privacy Approval, If Required

```text
Name or forum:
Decision:
Date:
Notes:
Not applicable reason, if any:
```

## Final Output/Decision Control Decision

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

# 19. Review Triggers

Review this output and decision control design if any of the following occur:

```text
[ ] Output type changes
[ ] Decision impact changes
[ ] Customer-facing use changes
[ ] Generated record use changes
[ ] Downstream workflow changes
[ ] Validation process changes
[ ] Human review model changes
[ ] Model or prompt changes
[ ] Data source changes
[ ] Risk tier changes
[ ] Output quality findings increase
[ ] Incident occurs
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
Risk tier:
Output types:
Decision impact:
Decision owner:
Validation required:
Human review model:
Customer-facing output:
Generated record:
Downstream use:
Logging approach:
Correction path:
Required testing:
Exceptions:
Approval status:
Next review date:
```