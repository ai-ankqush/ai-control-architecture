# AI Incident Containment and Recovery Template

This template is used to define, approve, test, and evidence how an AI use case can be contained and recovered if it fails, is misused, exposes data, produces harmful output, triggers unauthorized action, or causes business impact.

AI failure must be assumed.

The purpose of this template is to ensure the enterprise knows how to stop AI-related harm, preserve evidence, investigate the incident, recover affected processes, communicate appropriately, and improve controls.

---

# 1. Containment and Recovery Information

## AI Use Case Name

```text
[Enter AI use case name]
```

## Containment / Recovery Record ID

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

## Incident Owner

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

## Containment and Recovery Summary

```text
[Summarize how this AI use case can be contained, investigated, recovered, and restarted]
```

---

# 3. AI Incident Scenarios

## Relevant Incident Scenarios

Select all that apply:

```text
[ ] Sensitive data exposure
[ ] Prompt injection
[ ] Unsafe output
[ ] Incorrect AI-assisted decision
[ ] Unauthorized retrieval
[ ] Unauthorized tool use
[ ] Approval bypass
[ ] Agent malfunction
[ ] Excessive or unsafe action
[ ] Vendor AI incident
[ ] Model behavior change
[ ] Logging or evidence failure
[ ] Data retention or reuse issue
[ ] Customer-facing AI failure
[ ] Regulatory or legal exposure
[ ] Accountability failure
[ ] Other
```

## Scenario Summary

| Scenario | Likelihood | Impact | Containment Required? | Recovery Required? |
|---|---|---|---|---|
| [Scenario] | [Low/Medium/High] | [Low/Medium/High/Critical] | [Yes/No] | [Yes/No] |

## Scenario Notes

```text
[Describe the most important AI incident scenarios for this use case]
```

---

# 4. Incident Severity Model

## Severity Criteria

| Severity | Criteria for This Use Case | Example |
|---|---|---|
| Low | [Criteria] | [Example] |
| Medium | [Criteria] | [Example] |
| High | [Criteria] | [Example] |
| Critical | [Criteria] | [Example] |

## Severity Escalation Triggers

Select all that apply:

```text
[ ] Regulated data exposed
[ ] Customer data exposed
[ ] Employee data exposed
[ ] Legal or privileged data exposed
[ ] Secrets or credentials exposed
[ ] Customer-impacting output sent
[ ] Employee-impacting decision affected
[ ] Financial action triggered
[ ] Security action triggered
[ ] Production system affected
[ ] Approval bypass occurred
[ ] Agent cannot be stopped
[ ] Vendor evidence unavailable
[ ] Incident is ongoing
[ ] Regulatory notification may be required
[ ] Other
```

## Severity Notes

```text
[Describe how severity should be assessed for this use case]
```

---

# 5. Detection Sources

## Detection Sources

Select all that apply:

```text
[ ] User report
[ ] Customer complaint
[ ] Monitoring alert
[ ] SIEM/SOC alert
[ ] DLP alert
[ ] Audit finding
[ ] Assurance testing
[ ] Vendor notification
[ ] Application log
[ ] Tool/action log
[ ] Business process exception
[ ] Privacy/legal escalation
[ ] Output quality monitoring
[ ] Reviewer feedback
[ ] Other
```

## Detection Owner

```text
Name or team:
Function:
Contact:
```

## Detection Notes

```text
[Describe how AI incidents or near misses are detected]
```

---

# 6. Containment Mechanisms

## Containment Mechanisms Available

Select all that apply:

```text
[ ] Disable AI capability
[ ] Suspend agent
[ ] Revoke AI identity
[ ] Revoke delegated authority
[ ] Disable service account
[ ] Remove data source access
[ ] Disable retrieval
[ ] Remove vector index
[ ] Disable tool
[ ] Block API
[ ] Stop workflow
[ ] Disable vendor AI feature
[ ] Restrict user group
[ ] Block action category
[ ] Quarantine output
[ ] Block customer-facing response
[ ] Rotate credentials
[ ] Suspend production use
[ ] Other
```

## Containment Matrix

| Incident Scenario | Containment Action | Owner | Expected Time | Evidence |
|---|---|---|---|---|
| [Scenario] | [Action] | [Owner] | [Time] | [Evidence] |

## Containment Notes

```text
[Describe containment limitations, dependencies, and escalation paths]
```

---

# 7. Access Revocation

## Access Revocation Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Revocation Paths

Select all that apply:

```text
[ ] Revoke user-delegated authority
[ ] Disable AI identity
[ ] Disable agent identity
[ ] Disable service account
[ ] Remove application permission
[ ] Revoke tool permission
[ ] Revoke API key
[ ] Rotate credentials
[ ] Remove data source access
[ ] Remove privileged access
[ ] Disable vendor feature access
[ ] Other
```

## Access Revocation Details

| Access Type | Revocation Method | Owner | Expected Time | Evidence |
|---|---|---|---|---|
| [Access] | [Method] | [Owner] | [Time] | [Evidence] |

## Access Revocation Notes

```text
[Describe emergency access revocation process and limitations]
```

---

# 8. Agent and Tool Kill Switch

Complete this section if the AI use case is agentic or action-capable.

## Kill Switch Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Kill Switch Levels

Select all that apply:

```text
[ ] Capability level
[ ] Agent level
[ ] Tool level
[ ] API level
[ ] Workflow level
[ ] Identity level
[ ] Vendor feature level
[ ] Data source level
[ ] User group level
[ ] Action class level
[ ] Environment level
[ ] Other
```

## Kill Switch Owner

```text
Name:
Function:
Email:
```

## Activation Criteria

```text
[Describe when kill switch should be activated]
```

## Activation Process

```text
[Describe how kill switch is activated]
```

## Expected Time to Disable

```text
[Enter expected time]
```

## Restart Criteria

```text
[Describe approval, remediation, testing, and evidence required before restart]
```

## Kill Switch Test Evidence

```text
Last tested:
Result:
Evidence:
Next test:
```

---

# 9. Output Containment

## Output Containment Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Output Containment Actions

Select all that apply:

```text
[ ] Quarantine AI output
[ ] Block output publication
[ ] Block customer-facing response
[ ] Withdraw AI-generated content
[ ] Correct AI-generated communication
[ ] Amend generated record
[ ] Notify recipients
[ ] Prevent downstream use
[ ] Open incident
[ ] Other
```

## Output Containment Details

```text
[Describe how unsafe, incorrect, sensitive, or unauthorized output is contained]
```

---

# 10. Workflow and Action Containment

## Workflow or Action Containment Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Containment Actions

Select all that apply:

```text
[ ] Stop workflow
[ ] Pause workflow queue
[ ] Disable action path
[ ] Block API call
[ ] Disable tool
[ ] Freeze affected records
[ ] Pause downstream automation
[ ] Require manual approval
[ ] Roll back action
[ ] Open broader incident
[ ] Other
```

## Workflow / Action Containment Details

| Workflow / Action | Containment Method | Owner | Evidence |
|---|---|---|---|
| [Workflow/action] | [Method] | [Owner] | [Evidence] |

---

# 11. Vendor AI Containment

Complete this section if vendor AI is involved.

## Vendor AI Involved?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Vendor Name

```text
[Enter vendor name]
```

## Vendor Containment Options

Select all that apply:

```text
[ ] Disable vendor AI feature
[ ] Disable tenant-level feature
[ ] Disable user-level feature
[ ] Restrict data sharing
[ ] Suspend integration
[ ] Change admin setting
[ ] Export vendor logs
[ ] Notify vendor support
[ ] Request vendor incident response
[ ] Request vendor root cause analysis
[ ] Other
```

## Vendor Contact

```text
Name:
Role:
Email:
Support channel:
```

## Vendor Containment Notes

```text
[Describe vendor containment limitations, evidence availability, and escalation process]
```

---

# 12. Evidence Preservation

## Evidence Preservation Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Evidence to Preserve

Select all that apply:

```text
[ ] AI inventory record
[ ] Risk assessment
[ ] Control assessment
[ ] Prompt/input logs
[ ] Uploaded files
[ ] Retrieved context references
[ ] Source documents
[ ] Output logs
[ ] Generated records
[ ] Tool call logs
[ ] Action logs
[ ] Approval records
[ ] Exception records
[ ] Identity/access records
[ ] Data access logs
[ ] System prompt version
[ ] Model/vendor configuration
[ ] Vendor logs
[ ] Monitoring alerts
[ ] User reports
[ ] Customer complaints
[ ] Communications
[ ] Screenshots or exports
[ ] Other
```

## Evidence Package Location

```text
[Describe where incident evidence will be preserved]
```

## Legal Hold Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Evidence Preservation Owner

```text
Name:
Function:
Email:
```

## Evidence Preservation Notes

```text
[Describe evidence preservation timing, access restrictions, and known gaps]
```

---

# 13. Investigation Plan

## Investigation Owner

```text
Name:
Function:
Email:
```

## Investigation Questions

| Question | Evidence Source |
|---|---|
| What AI use case was involved? | [Evidence] |
| Who or what initiated the interaction? | [Evidence] |
| What identity or authority was used? | [Evidence] |
| What data was accessed? | [Evidence] |
| What prompt or input was submitted? | [Evidence] |
| Was untrusted content involved? | [Evidence] |
| Was prompt injection involved? | [Evidence] |
| What context was retrieved? | [Evidence] |
| What output was generated? | [Evidence] |
| Was output reviewed or approved? | [Evidence] |
| What tool was called? | [Evidence] |
| What action was executed? | [Evidence] |
| Was approval required and obtained? | [Evidence] |
| What downstream system was affected? | [Evidence] |
| What controls worked? | [Evidence] |
| What controls failed? | [Evidence] |

## Investigation Notes

```text
[Describe investigation process, participants, and dependencies]
```

---

# 14. Recovery and Correction

## Recovery Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Recovery Actions

Select all that apply:

```text
[ ] Correct AI output
[ ] Withdraw AI output
[ ] Correct generated record
[ ] Re-run workflow
[ ] Roll back system action
[ ] Reverse transaction
[ ] Revoke improper access
[ ] Restore configuration
[ ] Restore backup
[ ] Notify customer
[ ] Notify employee
[ ] Notify vendor
[ ] Apply compensating control
[ ] Update prompt or configuration
[ ] Update retrieval boundary
[ ] Update tool permissions
[ ] Retest AI capability
[ ] Other
```

## Recovery Matrix

| Impact Area | Recovery Action | Owner | Evidence | Status |
|---|---|---|---|---|
| [Impact area] | [Action] | [Owner] | [Evidence] | [Status] |

## Recovery Notes

```text
[Describe recovery approach, limitations, dependencies, and residual risk]
```

---

# 15. Rollback and Compensation

## Rollback Available?

```text
[ ] No
[ ] Yes
[ ] Partial
[ ] Unknown
```

## Rollback Details

| Action / Change | Rollback Method | Owner | Tested? | Evidence |
|---|---|---|---|---|
| [Action/change] | [Method] | [Owner] | [Yes/No] | [Evidence] |

## Compensation Required If Rollback Is Not Possible?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Compensation Method

```text
[Describe compensation, correction, customer remediation, manual remediation, or record amendment]
```

---

# 16. Communication and Notification

## Communication Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Potential Stakeholders

Select all that apply:

```text
[ ] Business owner
[ ] Technical owner
[ ] Data owner
[ ] Security/SOC
[ ] Incident response
[ ] Legal
[ ] Privacy
[ ] Compliance
[ ] Risk
[ ] Audit
[ ] Vendor management
[ ] Vendor
[ ] Customers
[ ] Employees
[ ] Regulators
[ ] Executive leadership
[ ] Communications team
[ ] Other
```

## Notification Matrix

| Stakeholder | Notification Trigger | Owner | Timing | Evidence |
|---|---|---|---|---|
| [Stakeholder] | [Trigger] | [Owner] | [Timing] | [Evidence] |

## Communication Notes

```text
[Describe communication process, approval, legal/privacy review, and notification constraints]
```

---

# 17. Restart Criteria

## Restart Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Restart Conditions

Select all that apply:

```text
[ ] Incident contained
[ ] Root cause understood
[ ] Recovery completed
[ ] Required controls fixed
[ ] Evidence preserved
[ ] Owner approval obtained
[ ] Security approval obtained
[ ] Privacy/legal approval obtained where required
[ ] Vendor remediation confirmed
[ ] Assurance retest completed
[ ] Kill switch tested
[ ] Monitoring updated
[ ] Residual risk accepted
[ ] Other
```

## Restart Approval

```text
Approver:
Function:
Date:
Notes:
```

## Restart Notes

```text
[Describe conditions required before AI use case, agent, tool, workflow, or vendor feature can be restarted]
```

---

# 18. Post-Incident Review

## Post-Incident Review Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Review Owner

```text
Name:
Function:
Email:
```

## Review Questions

Select all that apply:

```text
[ ] What happened?
[ ] Why did it happen?
[ ] What AI saw?
[ ] What AI produced?
[ ] What AI triggered?
[ ] What controls worked?
[ ] What controls failed?
[ ] Was containment timely?
[ ] Was evidence complete?
[ ] Was ownership clear?
[ ] Was vendor support sufficient?
[ ] Was recovery effective?
[ ] What should change?
```

## Post-Incident Review Notes

```text
[Describe review process, participants, and expected outputs]
```

---

# 19. Control Improvement

## Control Updates Required

Select all that apply:

```text
[ ] Update AI inventory
[ ] Update risk assessment
[ ] Update control assessment
[ ] Update identity/access controls
[ ] Update data boundary controls
[ ] Update prompt/input controls
[ ] Update output/decision controls
[ ] Update tool/action controls
[ ] Update accountability model
[ ] Update assurance tests
[ ] Update logging/monitoring
[ ] Update incident playbook
[ ] Update vendor controls
[ ] Update user training
[ ] Update architecture documentation
[ ] Other
```

## Improvement Actions

| Action ID | Improvement Action | Owner | Due Date | Evidence |
|---|---|---|---|---|
| [Action ID] | [Action] | [Owner] | [Date] | [Evidence] |

## Improvement Notes

```text
[Describe how lessons learned will update the AI Control Architecture]
```

---

# 20. Testing and Assurance

## Required Tests

Select all that apply:

```text
[ ] Access revocation test
[ ] Agent kill switch test
[ ] Tool disablement test
[ ] Workflow stop test
[ ] Vendor feature disablement test
[ ] Output quarantine test
[ ] Evidence preservation test
[ ] Incident tabletop
[ ] Recovery test
[ ] Rollback test
[ ] Restart approval test
[ ] Monitoring alert test
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

# 21. Exceptions

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

# 22. Approval

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

## Incident Response Approval

```text
Name or forum:
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

## Final Containment and Recovery Decision

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

# 23. Review Triggers

Review this containment and recovery design if any of the following occur:

```text
[ ] AI pattern changes
[ ] Agent or tool capability changes
[ ] Data source changes
[ ] Vendor involvement changes
[ ] Logging capability changes
[ ] Incident scenario changes
[ ] Kill switch test fails
[ ] Recovery test fails
[ ] Vendor incident support changes
[ ] Risk tier changes
[ ] Incident occurs
[ ] Assurance finding occurs
[ ] Regulatory or legal requirement changes
```

## Next Review Date

```text
[Enter date]
```

---

# 24. Summary

```text
Use case:
Risk tier:
Incident scenarios:
Containment mechanisms:
Access revocation:
Kill switch:
Output containment:
Workflow/action containment:
Vendor containment:
Evidence preservation:
Recovery:
Rollback:
Communication:
Restart criteria:
Required testing:
Exceptions:
Approval status:
Next review date:
```