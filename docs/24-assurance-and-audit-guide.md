# Assurance and Audit Guide

This document provides guidance for assuring and auditing the AI Control Architecture.

The purpose is to help organizations test whether AI controls are designed appropriately, operating effectively, evidenced sufficiently, and improving over time.

AI assurance must test both:

```text
AI behavior
AI control effectiveness
```

It is not enough to test whether an AI system gives useful answers.

The enterprise must also test whether the system is controlled.

---

# 1. Purpose

This guide explains how to:

- define AI assurance scope
- test AI controls by risk tier
- test AI controls by pillar
- collect evidence
- assess control effectiveness
- review vendor AI evidence
- audit AI governance
- audit AI incidents
- report findings
- track remediation
- update the control architecture

The guide is intended for:

- assurance teams
- internal audit
- risk teams
- security teams
- enterprise architecture
- AI governance teams
- privacy and legal reviewers
- vendor risk teams
- technical control owners
- business owners

---

# 2. Assurance Principles

## Principle 1: Test Controls, Not Just Models

AI assurance should not focus only on model accuracy or usefulness.

It must also test:

```text
Inventory
Ownership
Risk tiering
Identity and access
Data boundaries
Prompt and input controls
Output and decision controls
Tool and action controls
Human accountability
Logging and evidence
Incident containment
Vendor controls
```

---

## Principle 2: Assurance Must Be Risk-Tiered

Not every AI use case requires the same level of testing.

| Risk Tier | Assurance Expectation |
|---|---|
| Tier 1 | Basic review and acceptable use confirmation. |
| Tier 2 | Targeted review of data, vendor, and logging controls. |
| Tier 3 | Output validation, decision evidence, and human review testing. |
| Tier 4 | Tool/action, approval gate, logging, kill switch, and rollback testing. |
| Tier 5 | Enhanced assurance, evidence reconstruction, incident tabletop, and risk acceptance review. |

---

## Principle 3: Evidence Must Be Reviewable

A control should not be treated as effective unless evidence exists.

Evidence should show:

```text
What was approved
Who approved it
What configuration was used
What test was performed
What result occurred
What finding was raised
What remediation occurred
What residual risk remains
```

---

## Principle 4: Test the Failure Mode

AI assurance should test realistic failure modes.

Examples:

```text
Can the AI retrieve data it should not retrieve?
Can prompt injection influence output or tool use?
Can AI perform an action without approval?
Can AI-generated output become a decision without review?
Can a vendor provide logs during an incident?
Can the enterprise reconstruct what happened?
Can the AI capability be disabled quickly?
```

---

## Principle 5: Assurance Must Trigger Improvement

Assurance is not only a pass/fail activity.

Findings should update:

- requirements
- templates
- control design
- test cases
- monitoring rules
- incident playbooks
- vendor requirements
- maturity roadmap

---

# 3. Assurance Scope

AI assurance scope should be based on risk.

## Scope Inputs

Use the following inputs to define scope:

```text
AI use case intake
AI inventory record
Risk assessment
Risk tier
Architecture decision record
Control assessment
Vendor assessment
Data boundary record
Tool/action control record
Incident history
Open exceptions
Prior assurance findings
```

## Scope Questions

Before assurance begins, answer:

```text
What AI use case is being tested?
What risk tier applies?
What AI pattern applies?
What data does AI access?
Does AI influence decisions?
Can AI call tools or perform actions?
Is vendor AI involved?
What controls are required?
What evidence should exist?
What failure scenarios should be tested?
```

---

# 4. Assurance Levels

## Level 1: Basic Review

Use for low-risk AI use cases.

Typical activities:

- confirm inventory record
- confirm business owner
- confirm acceptable use guidance
- confirm no sensitive data
- confirm no decision impact
- confirm no action capability

---

## Level 2: Targeted Control Review

Use for AI that processes internal enterprise data or uses vendor AI.

Typical activities:

- review data sources
- review data classification
- review vendor processing
- review retention and training/reuse
- review access model
- review basic logging
- review incident escalation path

---

## Level 3: Pre-Deployment Assurance

Use for AI that influences decisions, records, customer communications, or operational processes.

Typical activities:

- test output validation
- test human review
- test decision evidence
- test correction path
- review accountability
- review logging and evidence
- review assurance findings before deployment

---

## Level 4: Full Control Assurance

Use for action-capable AI, agents, high-risk internal AI, or AI with sensitive data.

Typical activities:

- test identity and access
- test data boundaries
- test prompt injection
- test tool/action controls
- test approval gates
- test logging completeness
- test kill switch
- test rollback or compensation
- test evidence reconstruction

---

## Level 5: Enhanced or Independent Assurance

Use for regulated, autonomous, high-impact, privileged, production-critical, or externally exposed AI.

Typical activities:

- independent review
- adversarial testing
- extended evidence reconstruction
- incident tabletop
- vendor evidence review
- privacy/legal review
- risk acceptance review
- ongoing monitoring review
- post-deployment assurance

---

# 5. Assurance by AI Pattern

## Copilot Assurance

Test whether:

```text
[ ] Copilot is inventoried.
[ ] Business owner is assigned.
[ ] Permission model is understood.
[ ] Sensitive data guidance exists.
[ ] Vendor processing is reviewed.
[ ] Output use restrictions exist.
[ ] Usage evidence is available where required.
```

---

## RAG Assurance

Test whether:

```text
[ ] Data sources are mapped.
[ ] Data owners approved source use.
[ ] Retrieval boundaries are defined.
[ ] User permission inheritance works.
[ ] Cross-user retrieval is blocked.
[ ] Cross-tenant retrieval is blocked.
[ ] Sensitive source exclusion works.
[ ] Prompt injection through retrieved content is tested.
[ ] Retrieval evidence is available.
```

---

## Vendor AI Assurance

Test whether:

```text
[ ] Vendor AI feature is identified.
[ ] Enablement status is known.
[ ] Data processing is understood.
[ ] Retention is understood.
[ ] Training/reuse settings are reviewed.
[ ] Admin controls are reviewed.
[ ] Logs and evidence are available.
[ ] Vendor incident path is defined.
[ ] Contract terms are sufficient where required.
```

---

## Decision-Supporting AI Assurance

Test whether:

```text
[ ] Decision impact is documented.
[ ] Decision owner is assigned.
[ ] AI recommendation is separated from final decision.
[ ] Human review is meaningful.
[ ] Reviewer has source material.
[ ] Reviewer can reject or override output.
[ ] Final decision evidence is retained.
[ ] Correction path exists.
```

---

## Tool-Using AI Assurance

Test whether:

```text
[ ] Tool inventory is complete.
[ ] Tool owners are assigned.
[ ] Tool access is approved.
[ ] Tool permissions are least privilege.
[ ] Actions are classified by risk.
[ ] High-risk actions require approval.
[ ] Approval gates cannot be bypassed.
[ ] Tool calls are logged.
[ ] Tool access can be disabled.
[ ] Rollback or compensation is defined.
```

---

## Agentic AI Assurance

Test whether:

```text
[ ] Agent purpose is defined.
[ ] Agent owner is assigned.
[ ] Autonomy level is defined.
[ ] Agent identity is defined.
[ ] Delegated authority is controlled.
[ ] Tool use is bounded.
[ ] High-risk actions require approval.
[ ] Blast-radius limits exist.
[ ] Kill switch is defined and tested.
[ ] Rollback or compensation is assessed.
[ ] Agent incidents can be reconstructed.
```

---

## Customer-Facing AI Assurance

Test whether:

```text
[ ] Customer-facing use is approved.
[ ] Output boundaries are defined.
[ ] Prohibited outputs are defined.
[ ] Escalation triggers work.
[ ] Customer correction path exists.
[ ] Conversation evidence is retained where required.
[ ] Privacy/legal review is completed where required.
[ ] Incident response path exists.
```

---

# 6. Assurance by Pillar

## Pillar 1: AI Inventory and Classification

Assurance objective:

```text
Confirm that AI use cases are visible, owned, classified, risk-tiered, and lifecycle-managed.
```

Test procedures:

```text
[ ] Select sample AI use cases.
[ ] Confirm each has an inventory record.
[ ] Confirm business owner is assigned.
[ ] Confirm AI pattern is classified.
[ ] Confirm lifecycle status is current.
[ ] Confirm risk tier is assigned.
[ ] Confirm embedded vendor AI is identified.
[ ] Confirm unreviewed AI is tracked.
```

Evidence examples:

```text
AI inventory
Intake records
Owner records
Risk tiering records
Lifecycle status
Vendor AI feature list
```

Common findings:

```text
AI use case not inventoried
Owner missing
Risk tier unknown
Vendor AI feature not recorded
Lifecycle status outdated
```

---

## Pillar 2: AI Identity and Access Control

Assurance objective:

```text
Confirm that AI identity, delegated authority, access scope, privileged access, attribution, and revocation are controlled.
```

Test procedures:

```text
[ ] Review AI identity model.
[ ] Review AI identities, service accounts, agent identities, and vendor identities.
[ ] Confirm access approval exists.
[ ] Confirm least privilege review was performed.
[ ] Confirm privileged access is controlled.
[ ] Confirm AI-mediated activity is attributable.
[ ] Confirm revocation path exists.
[ ] Test access revocation where required.
```

Evidence examples:

```text
Identity model
Access approval
Service account record
Agent identity record
Delegated authority record
Access review evidence
Revocation test result
IAM/PAM logs
```

Common findings:

```text
AI uses shared account
Delegated authority unclear
Service account over-permissioned
Privileged AI access not reviewed
Revocation path untested
AI activity not distinguishable from human activity
```

---

## Pillar 3: Data Boundary Control

Assurance objective:

```text
Confirm that AI data access, retrieval, processing, retention, reuse, and exposure are bounded and approved.
```

Test procedures:

```text
[ ] Review data source map.
[ ] Confirm data classification.
[ ] Confirm data owner approval.
[ ] Review retrieval boundary.
[ ] Test sensitive source exclusion.
[ ] Test user permission inheritance.
[ ] Test cross-user or cross-tenant isolation where required.
[ ] Review retention and training/reuse restrictions.
[ ] Review vendor processing where applicable.
```

Evidence examples:

```text
Data source map
Data classification record
Data owner approval
Retrieval configuration
Retrieval test results
Data leakage test results
Retention settings
Vendor data terms
```

Common findings:

```text
Data source not approved
Classification unknown
Retrieval boundary not tested
Sensitive sources indexed without approval
Training/reuse setting unknown
Data retention not defined
```

---

## Pillar 4: Prompt and Input Control

Assurance objective:

```text
Confirm that prompts, uploaded files, retrieved content, external inputs, system prompts, and tool responses are controlled.
```

Test procedures:

```text
[ ] Review allowed inputs.
[ ] Review prohibited inputs.
[ ] Review sensitive data detection.
[ ] Review system prompt ownership and versioning.
[ ] Review prompt change process.
[ ] Test prompt injection.
[ ] Test external or untrusted input handling.
[ ] Test context isolation.
[ ] Review input policy violation logs.
```

Evidence examples:

```text
Prompt/input control record
Allowed/prohibited input rules
System prompt version history
Prompt change approvals
Prompt injection test results
Sensitive input detection logs
Context isolation evidence
```

Common findings:

```text
System prompt not versioned
Prompt injection not tested
Sensitive inputs not detected
External content treated as trusted
Prompt changes bypass review
Context isolation unclear
```

---

## Pillar 5: Output and Decision Control

Assurance objective:

```text
Confirm that AI outputs are classified, validated, reviewed, corrected, and prevented from silently becoming decisions, records, or actions.
```

Test procedures:

```text
[ ] Review output classification.
[ ] Review decision impact classification.
[ ] Confirm validation rules.
[ ] Confirm human review model.
[ ] Confirm decision owner where required.
[ ] Test separation between AI recommendation and final decision.
[ ] Confirm decision evidence exists.
[ ] Confirm correction or override path exists.
[ ] Review output quality monitoring.
```

Evidence examples:

```text
Output classification
Decision impact record
Validation rules
Reviewer records
Approval records
Final decision evidence
Correction records
Output quality metrics
Generated record metadata
```

Common findings:

```text
AI recommendation treated as final decision
Decision owner missing
Human review is ceremonial
Generated record lacks provenance
Correction path unclear
Decision evidence missing
```

---

## Pillar 6: Tool and Action Control

Assurance objective:

```text
Confirm that AI-accessible tools, APIs, workflows, and actions are inventoried, approved, bounded, logged, and containable.
```

Test procedures:

```text
[ ] Review tool inventory.
[ ] Confirm tool owners are assigned.
[ ] Review tool permissions.
[ ] Review action classification.
[ ] Test unauthorized tool call.
[ ] Test approval gate.
[ ] Test approval bypass scenario.
[ ] Test action boundary.
[ ] Review tool/action logs.
[ ] Test kill switch where required.
[ ] Test rollback or compensation where required.
```

Evidence examples:

```text
Tool inventory
Tool access approval
Action classification
Approval gate configuration
Approval logs
Tool-call logs
Action logs
Denied action logs
Kill switch test
Rollback test
```

Common findings:

```text
Tool inventory incomplete
Action risk not classified
AI can call unauthorized tool
Approval gate can be bypassed
Tool/action logs incomplete
Kill switch untested
Rollback undefined
```

---

## Pillar 7: Human Accountability Model

Assurance objective:

```text
Confirm that humans remain accountable for AI outcomes, decisions, approvals, exceptions, incidents, and risk acceptance.
```

Test procedures:

```text
[ ] Confirm business owner is assigned.
[ ] Confirm technical owner is assigned.
[ ] Confirm data owner where required.
[ ] Confirm decision owner where required.
[ ] Review human review model.
[ ] Review approval authority.
[ ] Review escalation path.
[ ] Review override rights.
[ ] Review exception ownership.
[ ] Review incident ownership.
[ ] Review risk acceptance authority.
```

Evidence examples:

```text
Accountability record
RACI matrix
Decision owner mapping
Approval matrix
Review records
Override records
Exception records
Risk acceptance records
Incident ownership records
```

Common findings:

```text
Business owner missing
Decision owner missing
Reviewer lacks authority
Risk accepted by wrong owner
Exception owner unclear
Incident owner undefined
```

---

## Pillar 8: AI Assurance and Testing

Assurance objective:

```text
Confirm that AI behavior and AI controls are tested based on risk tier and material changes.
```

Test procedures:

```text
[ ] Review assurance scope.
[ ] Review test plan.
[ ] Confirm test cases map to risks and controls.
[ ] Review test results.
[ ] Review failed and partial tests.
[ ] Confirm findings are tracked.
[ ] Confirm remediation and retesting.
[ ] Confirm regression testing triggers.
[ ] Confirm readiness decision.
```

Evidence examples:

```text
Assurance test plan
Test cases
Test results
Findings register
Remediation evidence
Retest evidence
Readiness approval
Regression test records
```

Common findings:

```text
Testing focused only on output quality
Control effectiveness not tested
Findings not tracked to closure
Regression testing missing
Vendor claims accepted without evidence
```

---

## Pillar 9: Monitoring, Logging, and Evidence

Assurance objective:

```text
Confirm that AI activity is observable, evidenced, protected, retained, and reconstructable.
```

Test procedures:

```text
[ ] Review logging requirements by risk tier.
[ ] Review AI event taxonomy.
[ ] Review prompt/input logging.
[ ] Review retrieval/context logging.
[ ] Review output logging.
[ ] Review decision evidence.
[ ] Review tool/action logging.
[ ] Review approval and exception logging.
[ ] Test evidence reconstruction.
[ ] Review evidence protection and retention.
[ ] Review vendor evidence availability.
```

Evidence examples:

```text
Logging requirements
AI event taxonomy
Prompt/input logs or metadata
Retrieval logs
Output logs
Tool/action logs
Approval logs
Exception logs
Evidence package
Reconstruction test result
Vendor log evidence
```

Common findings:

```text
Logs exist but cannot reconstruct activity
Vendor logs unavailable
Approval evidence missing
Tool/action logs incomplete
Evidence retention undefined
Sensitive evidence not protected
```

---

## Pillar 10: Incident Containment and Recovery

Assurance objective:

```text
Confirm that AI failure can be detected, contained, investigated, corrected, recovered, and used to improve controls.
```

Test procedures:

```text
[ ] Review AI incident scenarios.
[ ] Review severity model.
[ ] Review escalation path.
[ ] Review access revocation path.
[ ] Review kill switch where required.
[ ] Test tool or workflow disablement where required.
[ ] Review evidence preservation process.
[ ] Review recovery and correction process.
[ ] Review vendor incident process.
[ ] Review restart criteria.
[ ] Conduct tabletop for high-risk AI.
```

Evidence examples:

```text
Incident containment plan
Severity criteria
Escalation matrix
Access revocation record
Kill switch test
Evidence preservation checklist
Recovery plan
Rollback test
Vendor incident path
Incident tabletop results
Post-incident review
```

Common findings:

```text
AI incident scenarios not defined
Kill switch missing or untested
Evidence preservation unclear
Recovery path undefined
Vendor incident support unknown
Restart criteria missing
```

---

# 7. Core Assurance Tests

## Test 1: Inventory Completeness Test

Purpose:

```text
Confirm AI use cases are recorded and owned.
```

Procedure:

```text
[ ] Select sample of known AI tools, SaaS platforms, internal apps, and pilots.
[ ] Compare against AI inventory.
[ ] Confirm owner and lifecycle status.
[ ] Identify missing or stale records.
```

Expected result:

```text
All sampled AI use cases are inventoried, owned, classified, and current.
```

---

## Test 2: Risk Tiering Test

Purpose:

```text
Confirm risk tier is accurate and consistent.
```

Procedure:

```text
[ ] Select AI use case.
[ ] Review data, output, decision, action, autonomy, vendor, exposure, and recoverability risk.
[ ] Compare assigned tier to tiering criteria.
[ ] Challenge under-classified use cases.
```

Expected result:

```text
Assigned risk tier reflects highest relevant risk driver.
```

---

## Test 3: Data Boundary Test

Purpose:

```text
Confirm AI cannot access or expose data outside approved boundary.
```

Procedure:

```text
[ ] Identify approved data sources.
[ ] Attempt access to prohibited data.
[ ] Test user permission inheritance.
[ ] Test cross-user, cross-tenant, or cross-project access where relevant.
[ ] Review output for leakage.
```

Expected result:

```text
AI only accesses approved data and does not expose prohibited data.
```

---

## Test 4: Prompt Injection Test

Purpose:

```text
Confirm untrusted input cannot override system behavior or cause unsafe output or action.
```

Procedure:

```text
[ ] Insert malicious instructions into prompt, uploaded file, retrieved document, or tool response.
[ ] Attempt system prompt extraction.
[ ] Attempt policy bypass.
[ ] Attempt unauthorized data access.
[ ] Attempt unauthorized tool use.
[ ] Review logs and alerts.
```

Expected result:

```text
AI treats untrusted content as data, not controlling instruction, and blocks or safely handles the attempt.
```

---

## Test 5: Output Validation Test

Purpose:

```text
Confirm AI output is validated before use in decisions, records, communications, or workflows.
```

Procedure:

```text
[ ] Generate sample outputs.
[ ] Review against validation criteria.
[ ] Confirm source grounding where required.
[ ] Confirm reviewer record.
[ ] Confirm rejection or correction path works.
```

Expected result:

```text
High-impact output is validated, reviewed, evidenced, and correctable.
```

---

## Test 6: Decision Separation Test

Purpose:

```text
Confirm AI recommendation does not silently become final decision.
```

Procedure:

```text
[ ] Review decision-supporting workflow.
[ ] Confirm AI recommendation is labeled.
[ ] Confirm final decision is recorded separately.
[ ] Confirm decision owner.
[ ] Confirm reviewer can reject or override.
```

Expected result:

```text
Final decision remains human-owned and evidenced.
```

---

## Test 7: Unauthorized Tool Call Test

Purpose:

```text
Confirm AI cannot call tools outside approved scope.
```

Procedure:

```text
[ ] Identify approved tools.
[ ] Attempt unauthorized tool call.
[ ] Attempt authorized tool with unauthorized parameters.
[ ] Attempt direct lower-level API path.
[ ] Review deny logs.
```

Expected result:

```text
Unauthorized tool use is blocked and logged.
```

---

## Test 8: Approval Gate Test

Purpose:

```text
Confirm high-risk actions require approval.

```

Procedure:

```text
[ ] Attempt high-risk action without approval.
[ ] Attempt action with expired approval.
[ ] Attempt action with wrong approver.
[ ] Attempt action above threshold.
[ ] Review approval and denial evidence.
```

Expected result:

```text
High-risk action cannot execute without valid approval.
```

---

## Test 9: Logging Completeness Test

Purpose:

```text
Confirm logs capture required events.
```

Procedure:

```text
[ ] Execute representative AI interaction.
[ ] Confirm prompt/input evidence.
[ ] Confirm retrieval evidence.
[ ] Confirm output evidence.
[ ] Confirm decision evidence where applicable.
[ ] Confirm tool/action evidence where applicable.
[ ] Confirm approval evidence where applicable.
```

Expected result:

```text
Required logs exist and are usable for review, assurance, audit, and incident response.
```

---

## Test 10: Evidence Reconstruction Test

Purpose:

```text
Confirm AI activity can be reconstructed.
```

Procedure:

```text
[ ] Select sample AI interaction.
[ ] Reconstruct who initiated it.
[ ] Reconstruct what AI saw.
[ ] Reconstruct what AI produced.
[ ] Reconstruct what decision or action occurred.
[ ] Reconstruct approvals and exceptions.
[ ] Identify evidence gaps.
```

Expected result:

```text
High-risk AI activity can be reconstructed end to end.
```

---

## Test 11: Kill Switch Test

Purpose:

```text
Confirm AI capability, agent, tool, workflow, or vendor feature can be stopped.
```

Procedure:

```text
[ ] Identify kill switch level.
[ ] Activate test disablement path.
[ ] Confirm AI can no longer act.
[ ] Confirm tool/API/workflow access is disabled.
[ ] Confirm logs are preserved.
[ ] Confirm restart requires approval.
```

Expected result:

```text
AI capability can be disabled quickly and safely.
```

---

## Test 12: Rollback or Compensation Test

Purpose:

```text
Confirm harmful actions can be reversed, corrected, or compensated.
```

Procedure:

```text
[ ] Select representative action.
[ ] Test rollback or correction path.
[ ] Confirm owner and evidence.
[ ] Confirm affected records or workflows can be corrected.
[ ] Confirm compensation process where rollback is not possible.
```

Expected result:

```text
Recovery path exists, is owned, and is evidenced.
```

---

# 8. Audit Approach

Audit should assess whether AI controls are designed and operating effectively.

## Audit Objectives

An audit may assess:

```text
AI governance design
AI inventory completeness
Risk-tiering consistency
Control assessment quality
Vendor AI review
Data boundary controls
Identity and access controls
Output and decision controls
Tool and action controls
Human accountability
Assurance testing
Evidence completeness
Exception management
Incident readiness
Maturity reporting
```

---

## Audit Planning Questions

Before audit begins, answer:

```text
What is the audit scope?
Which AI use cases are included?
Which risk tiers are included?
Which AI patterns are included?
Which business units are included?
Which vendors are included?
Which controls are in scope?
Which evidence repositories are in scope?
What period is being audited?
```

---

## Audit Sampling

Audit samples should prioritize:

```text
Tier 3, Tier 4, and Tier 5 AI use cases
Customer-facing AI
Decision-supporting AI
Action-capable AI
Agentic AI
Vendor AI
AI using sensitive or regulated data
AI with open exceptions
AI with prior findings
AI involved in incidents or near misses
```

---

## Audit Evidence Requests

Audit may request:

```text
AI inventory
AI use case intake records
Risk assessments
Risk tiering records
Control assessments
Architecture decision records
Vendor assessments
Data boundary records
Identity/access records
Prompt/input control records
Output/decision control records
Tool/action control records
Human accountability records
Assurance test plans
Test results
Findings registers
Evidence packages
Exception records
Incident records
Maturity reports
Governance meeting records
```

---

# 9. Audit by Domain

## Governance Audit

Review whether:

```text
[ ] AI governance roles are defined.
[ ] Decision rights are documented.
[ ] Governance forums review high-risk AI.
[ ] AI intake process exists.
[ ] Risk-tiering process exists.
[ ] Exceptions are reviewed.
[ ] Metrics are reported.
```

---

## Inventory Audit

Review whether:

```text
[ ] AI use cases are inventoried.
[ ] Embedded vendor AI is tracked.
[ ] Business owners are assigned.
[ ] Lifecycle status is current.
[ ] Risk tier is assigned.
[ ] Inventory is reviewed periodically.
```

---

## Risk Management Audit

Review whether:

```text
[ ] Risk assessments are completed for high-risk AI.
[ ] Risk tiers are assigned consistently.
[ ] Risk drivers are documented.
[ ] Control requirements are mapped to risk tier.
[ ] Residual risk is accepted by appropriate owner.
```

---

## Vendor AI Audit

Review whether:

```text
[ ] Vendor AI features are identified.
[ ] Vendor processing is reviewed.
[ ] Retention and training/reuse are reviewed.
[ ] Vendor logs are assessed.
[ ] Vendor incident support is defined.
[ ] Contract gaps are documented.
```

---

## Data Boundary Audit

Review whether:

```text
[ ] Data sources are mapped.
[ ] Data classification is documented.
[ ] Data owner approval exists.
[ ] Retrieval boundaries are defined.
[ ] Sensitive data restrictions are implemented.
[ ] Retention and reuse are controlled.
```

---

## Identity and Access Audit

Review whether:

```text
[ ] AI identity model is defined.
[ ] Access approvals exist.
[ ] Least privilege is applied.
[ ] Privileged access is controlled.
[ ] Access reviews occur.
[ ] Revocation path is tested where required.
```

---

## Output and Decision Audit

Review whether:

```text
[ ] Output types are classified.
[ ] Decision impact is assessed.
[ ] Decision owner is assigned.
[ ] AI recommendation is separated from final decision.
[ ] Human review evidence exists.
[ ] Correction and override paths exist.
```

---

## Tool and Action Audit

Review whether:

```text
[ ] Tool inventory exists.
[ ] Tool access is approved.
[ ] Actions are classified.
[ ] High-risk actions require approval.
[ ] Tool and action logs exist.
[ ] Kill switch and rollback are tested where required.
```

---

## Evidence Audit

Review whether:

```text
[ ] Evidence requirements are defined.
[ ] Evidence packages exist for high-risk AI.
[ ] Evidence is retained.
[ ] Evidence is protected.
[ ] AI activity can be reconstructed.
[ ] Vendor evidence gaps are tracked.
```

---

## Incident Readiness Audit

Review whether:

```text
[ ] AI incident scenarios are defined.
[ ] Severity model exists.
[ ] Escalation path exists.
[ ] Containment mechanisms exist.
[ ] Evidence preservation is defined.
[ ] Recovery and restart criteria exist.
[ ] Tabletop exercises are performed where required.
```

---

# 10. Findings and Severity

Findings should be rated based on risk.

## Critical Finding

A critical finding exists when AI can create high-impact harm without effective control.

Examples:

```text
Tier 5 AI operates without assurance.
Agent can execute high-risk actions without approval.
AI can access regulated data without approved boundary.
AI incident cannot be contained.
AI activity cannot be reconstructed for high-risk use case.
```

---

## High Finding

A high finding exists when a significant control weakness affects sensitive data, decisions, actions, or evidence.

Examples:

```text
Decision owner missing for decision-supporting AI.
Prompt injection not tested for RAG or agent.
Vendor logs unavailable for high-risk vendor AI.
Privileged AI access not reviewed.
Kill switch untested for action-capable AI.
```

---

## Medium Finding

A medium finding exists when control weakness is limited or compensating controls exist.

Examples:

```text
Inventory record incomplete.
Evidence package partially complete.
Access review overdue but access is limited.
Output validation exists but evidence is inconsistent.
```

---

## Low Finding

A low finding exists when the issue is minor or improvement-oriented.

Examples:

```text
Template fields incomplete.
Review date missing.
Documentation wording unclear.
Metric owner not updated.
```

---

# 11. Remediation

Every finding should include:

```text
Finding ID
Finding description
Severity
Affected AI use case
Affected pillar
Risk impact
Required remediation
Owner
Due date
Evidence required
Retest requirement
Status
```

## Remediation Status

Use these statuses:

```text
Open
In progress
Remediated
Retest required
Closed
Risk accepted
Deferred
```

## Retest Rules

Retest is required when:

```text
The finding affects Tier 3, Tier 4, or Tier 5 AI.
The finding affects data boundary.
The finding affects decision control.
The finding affects tool/action control.
The finding affects logging or evidence.
The finding affects incident containment.
The finding was critical or high severity.
```

---

# 12. Assurance Report Structure

Use this structure for an assurance report.

```text
AI Assurance Report

1. Executive summary
2. AI use case scope
3. Risk tier and risk drivers
4. Controls tested
5. Test procedures
6. Test results
7. Evidence reviewed
8. Findings
9. Remediation actions
10. Residual risk
11. Exceptions
12. Readiness decision
13. Conditions for approval
14. Retest requirements
15. Sign-off
```

---

# 13. Audit Report Structure

Use this structure for an audit report.

```text
AI Control Audit Report

1. Executive summary
2. Audit scope
3. Audit period
4. AI use cases sampled
5. Control domains audited
6. Evidence reviewed
7. Design effectiveness assessment
8. Operating effectiveness assessment
9. Findings by severity
10. Findings by pillar
11. Management actions
12. Residual risk
13. Repeat findings
14. Maturity observations
15. Audit conclusion
```

---

# 14. Readiness Decisions

Assurance may result in one of the following decisions.

| Decision | Meaning |
|---|---|
| Ready for approved use | Controls are sufficient for intended use. |
| Ready for pilot only | Use is limited while controls are validated. |
| Ready with conditions | Use is allowed if conditions are completed. |
| Requires remediation | Control gaps must be remediated before approval. |
| Requires risk acceptance | Residual risk must be formally accepted. |
| Not ready | AI use should not proceed. |
| Requires additional testing | Assurance is incomplete. |

---

# 15. Audit and Assurance Anti-Patterns

## Anti-Pattern 1: Testing Only Accuracy

Testing output accuracy without testing data access, tool use, approval, evidence, or containment.

Why this fails:

```text
A useful AI system can still be uncontrolled.
```

---

## Anti-Pattern 2: Accepting Vendor Claims Without Evidence

Treating vendor documentation as proof of control.

Why this fails:

```text
Vendor claims may not prove enterprise configuration, retention, logging, or incident support.
```

---

## Anti-Pattern 3: No Reconstructability Test

Assuming logs are sufficient without testing whether an incident can be reconstructed.

Why this fails:

```text
Logs may exist but not answer the questions required during audit or incident response.
```

---

## Anti-Pattern 4: Human Review Without Testing

Assuming human-in-the-loop is effective without testing reviewer context, authority, and evidence.

Why this fails:

```text
Human review can become ceremonial.
```

---

## Anti-Pattern 5: Kill Switch on Paper Only

Documenting a kill switch but never testing it.

Why this fails:

```text
A containment control is not reliable until it has been tested.
```

---

## Anti-Pattern 6: Findings Without Remediation Discipline

Raising findings without owners, due dates, evidence, or retest.

Why this fails:

```text
Assurance becomes documentation rather than risk reduction.
```

---

# 16. Related Documents

```text
docs/17-implementation-checklists.md
docs/18-control-maturity-model.md
docs/19-common-ai-control-patterns.md
docs/20-common-failure-scenarios.md
docs/21-adoption-playbook.md
docs/22-governance-and-operating-model.md
docs/23-metrics-and-reporting.md
```

---

# 17. Related Templates

```text
templates/ai-assurance-test-plan-template.md
templates/ai-control-evidence-package-template.md
templates/ai-control-assessment-template.md
templates/ai-risk-assessment-template.md
templates/ai-vendor-assessment-template.md
templates/ai-exception-record-template.md
templates/ai-incident-record-template.md
templates/ai-incident-containment-recovery-template.md
```

---

# 18. Summary

AI assurance and audit must prove that AI is not only useful, but controlled.

The enterprise should be able to prove:

```text
AI is inventoried.
AI is owned.
AI is risk-tiered.
AI access is controlled.
AI data boundaries are enforced.
AI inputs are controlled.
AI outputs are validated.
AI decisions remain accountable.
AI tools and actions are bounded.
AI controls are tested.
AI evidence exists.
AI incidents can be contained.
AI failures improve the architecture.
```

The goal is not to create assurance paperwork.

The goal is to create confidence that AI can be adopted safely, responsibly, and recoverably.