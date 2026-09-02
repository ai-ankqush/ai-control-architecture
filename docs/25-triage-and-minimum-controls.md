# Triage and Minimum Controls

This document defines a lightweight triage and minimum-control model for the AI Control Architecture.

The purpose is to prevent the architecture from becoming governance theater.

Not every AI use case should require the same level of review, documentation, evidence, and assurance.

Control depth should scale with risk.

---

# 1. Purpose

The AI Control Architecture includes detailed templates and control guidance.

Those artifacts are useful for high-risk AI, regulated AI, vendor AI, RAG systems, decision-supporting AI, and agentic AI.

However, applying the full control pack to every low-risk AI use case would create unnecessary friction.

This document defines a triage model that helps teams quickly decide:

```text
Can this AI use case be fast-tracked?
Does it require data review?
Does it require vendor review?
Does it require decision accountability?
Does it require tool/action controls?
Does it require full assurance and evidence?
```

The goal is:

```text
Low-risk AI moves quickly.
High-risk AI receives deeper control.
```

---

# 2. Core Principle

The core principle is:

```text
Control depth should scale with risk tier.
```

A low-risk drafting assistant should not go through the same review process as an autonomous agent that can update records, trigger workflows, or affect customers.

A practical control architecture must avoid two failures:

```text
Over-controlling low-risk AI
Under-controlling high-risk AI
```

Both are harmful.

Over-controlling low-risk AI creates bureaucracy and avoidance.

Under-controlling high-risk AI creates unmanaged enterprise risk.

---

# 3. Triage Outcomes

AI triage should result in one of the following outcomes.

| Outcome | Meaning |
|---|---|
| Fast-track | Low-risk AI can proceed with minimal documentation and acceptable use confirmation. |
| Standard review | AI requires data, vendor, ownership, and control review before approval. |
| Enhanced review | AI affects decisions, records, customers, sensitive data, or regulated processes. |
| Action-capable review | AI can use tools, trigger workflows, modify records, or perform actions. |
| High-impact review | AI is autonomous, regulated, privileged, production-critical, difficult to reverse, or high-impact. |
| Not approved | AI should not proceed until major control gaps are resolved. |

---

# 4. Fast Triage Questions

Start with these questions.

```text
1. Does the AI use enterprise, customer, employee, regulated, confidential, or sensitive data?
2. Does the AI influence decisions, records, customer communication, legal/compliance outcomes, financial outcomes, HR outcomes, security actions, or operational processes?
3. Can the AI call tools, trigger workflows, modify records, send communications, execute code, change access, or perform actions?
4. Is vendor AI involved?
5. Is the AI customer-facing, employee-impacting, regulated, privileged, production-critical, or difficult to reverse?
```

## Triage Rule

```text
If all answers are No, the use case may be Tier 1 and eligible for fast-track review.
```

```text
If data or vendor AI is involved, the use case is at least Tier 2.
```

```text
If AI influences decisions or records, the use case is at least Tier 3.
```

```text
If AI can perform actions or call tools, the use case is at least Tier 4.
```

```text
If AI is high-impact, autonomous, regulated, privileged, production-critical, or difficult to reverse, the use case may be Tier 5.
```

---

# 5. Risk Tier Summary

| Tier | Description | Review Depth |
|---|---|---|
| Tier 1 | Low-risk productivity or public-data use | Minimal |
| Tier 2 | Internal productivity with enterprise data or vendor AI | Standard |
| Tier 3 | Decision-supporting AI | Enhanced |
| Tier 4 | Action-capable AI | Action-capable review |
| Tier 5 | High-impact autonomous or regulated AI | Full review |

---

# 6. Tier 1: Fast-Track AI

## Description

Tier 1 AI is low-risk AI used for personal productivity, drafting, brainstorming, or public-data-only work.

Typical examples:

```text
Brainstorming ideas
Rewriting non-sensitive text
Summarizing public information
Drafting generic internal wording
Generating low-risk outlines
Creating non-sensitive productivity content
```

## Tier 1 Must Not Include

Tier 1 should not include AI that:

```text
Uses confidential enterprise data
Uses customer data
Uses employee data
Uses regulated data
Uses legal privileged content
Influences formal decisions
Creates official records
Sends customer communications
Calls tools or APIs
Triggers workflows
Modifies records
Uses embedded vendor AI with unclear processing
Affects production systems
Affects access, security, finance, HR, legal, or compliance outcomes
```

## Minimum Intake

Tier 1 can use a lightweight intake.

```text
Use case name:
Business owner or user group:
Purpose:
Data used:
Confirmation that no sensitive, confidential, customer, employee, or regulated data is used:
Confirmation that no decisions or actions are affected:
Confirmation that no tools or workflows are used:
```

## Minimum Controls

```text
[ ] Use case recorded.
[ ] Owner or user group identified.
[ ] Acceptable use guidance acknowledged.
[ ] Sensitive data use prohibited.
[ ] No decision impact confirmed.
[ ] No tool/action capability confirmed.
```

## Required Templates

Usually not required beyond a short intake record.

Optional:

```text
templates/ai-use-case-intake-template.md
```

## Approval Path

```text
Fast-track approval by business owner or AI intake owner.
```

## Evidence

```text
Lightweight intake record
Acceptable use acknowledgement
Owner record
```

## Reassessment Triggers

Reassess Tier 1 if:

```text
Enterprise data is introduced.
Vendor AI processing changes.
Outputs are used in decisions.
Outputs become official records.
Tool/action capability is enabled.
The use case becomes customer-facing.
Sensitive data is used.
```

---

# 7. Tier 2: Standard Review

## Description

Tier 2 AI uses internal enterprise data or vendor AI but does not materially influence decisions and cannot perform actions.

Typical examples:

```text
Internal productivity copilot with enterprise data
Internal document summarization
Internal knowledge assistant
AI-enabled SaaS feature with limited impact
Non-sensitive internal RAG assistant
Meeting summarization for internal use
```

## Tier 2 Risk Drivers

```text
Enterprise data
Vendor processing
Internal confidential information
Broad user population
Document or message summarization
Basic retrieval
Internal productivity usage
```

## Minimum Intake

```text
Use case name:
Business purpose:
Business owner:
Technical owner:
Vendor owner, if applicable:
Data sources:
Highest data classification:
Vendor involvement:
Retention and training/reuse status:
User population:
Lifecycle status:
```

## Minimum Controls

```text
[ ] Use case inventoried.
[ ] Business owner assigned.
[ ] Technical owner assigned where applicable.
[ ] Data sources mapped.
[ ] Highest data classification recorded.
[ ] Sensitive data restrictions defined.
[ ] Vendor AI reviewed where applicable.
[ ] Retention and training/reuse reviewed where applicable.
[ ] User guidance provided.
[ ] Logging approach defined.
[ ] Incident escalation path defined.
```

## Required Templates

Use as needed:

```text
templates/ai-use-case-intake-template.md
templates/ai-risk-assessment-template.md
templates/ai-data-boundary-template.md
templates/ai-vendor-assessment-template.md
```

## Approval Path

```text
Business owner approval
Data owner approval where sensitive or confidential enterprise data is involved
Vendor owner approval where vendor AI is involved
Security/privacy/legal review where required by data or vendor risk
```

## Evidence

```text
Inventory record
Risk assessment
Data source map
Data classification
Vendor assessment where applicable
Retention/training/reuse review
User guidance
Configuration record
```

## Reassessment Triggers

Reassess Tier 2 if:

```text
AI begins influencing decisions.
AI output becomes an official record.
AI becomes customer-facing.
Sensitive or regulated data is introduced.
Tool/action capability is enabled.
Vendor processing changes.
Prompt/output retention changes.
```

---

# 8. Tier 3: Enhanced Decision Review

## Description

Tier 3 AI supports or influences decisions, generated records, customer communications, compliance interpretation, prioritization, scoring, classification, or business judgment.

Typical examples:

```text
AI-generated case summaries used by support agents
Policy assistant used for compliance guidance
AI recommendation for ticket priority
AI scoring or ranking
AI-generated customer response drafts
AI-assisted investigation summaries
AI-assisted financial, legal, HR, or security analysis
```

## Tier 3 Risk Drivers

```text
Decision support
Generated records
Customer communication drafts
Policy interpretation
Prioritization
Scoring or ranking
Human review required
Potential overreliance
Correction path required
```

## Minimum Intake

Tier 3 requires the Tier 2 intake plus:

```text
Decision or output type:
Decision owner:
Reviewer role:
Human review model:
Output validation rule:
Source evidence required:
Correction or override path:
Decision evidence requirement:
```

## Minimum Controls

```text
[ ] Tier 2 controls completed.
[ ] Decision impact assessed.
[ ] Decision owner assigned.
[ ] Output types classified.
[ ] Output validation rules defined.
[ ] Human review requirements defined.
[ ] Reviewer authority defined.
[ ] Source evidence or grounding required where appropriate.
[ ] AI recommendation separated from final decision.
[ ] Decision evidence retained where required.
[ ] Correction and override path defined.
[ ] Assurance testing completed before production use.
```

## Human Review Requirement

Human review must be meaningful.

A human reviewer should receive enough context to make an informed decision.

The reviewer should be able to see:

```text
AI output or recommendation
Relevant input or prompt context where appropriate
Source material or citations
Retrieved evidence where applicable
Risk indicators
Known limitations or uncertainty
Decision impact
Escalation path
Override or rejection option
```

## Minimum Templates

```text
templates/ai-risk-assessment-template.md
templates/ai-control-assessment-template.md
templates/ai-output-and-decision-control-template.md
templates/ai-human-accountability-template.md
templates/ai-assurance-test-plan-template.md
```

## Approval Path

```text
Business owner approval
Decision owner approval
Data owner approval where required
Risk/security/privacy/legal review depending on impact
Assurance approval before production where required
```

## Evidence

```text
Risk assessment
Control assessment
Decision impact assessment
Decision owner record
Output validation criteria
Human review evidence
Decision evidence
Correction or override record
Assurance test results
Evidence package for high-risk decision use
```

## Reassessment Triggers

Reassess Tier 3 if:

```text
AI begins performing actions.
AI recommendations become automated decisions.
AI output becomes customer-facing without review.
AI affects regulated or high-impact decisions.
Human review is removed or weakened.
Tool or workflow capability is enabled.
```

---

# 9. Tier 4: Action-Capable Review

## Description

Tier 4 AI can call tools, trigger workflows, update records, send communications, route work, execute commands, or otherwise affect enterprise state.

Typical examples:

```text
IT ticket triage agent
Workflow routing agent
AI that updates CRM records
AI that drafts and submits system changes
AI that sends messages after approval
AI that calls APIs
AI that opens, modifies, or closes tickets
AI that triggers business workflows
```

## Tier 4 Risk Drivers

```text
Tool access
API access
Workflow impact
Record modification
Action execution
Approval gates required
Blast-radius limits required
Kill switch required
Rollback or compensation required
```

## Minimum Intake

Tier 4 requires Tier 3 intake plus:

```text
Agent or system identity:
Autonomy level:
Tool inventory:
Action classification:
High-risk actions:
Approval gates:
Blast-radius limits:
Tool/action logs:
Kill switch:
Rollback or compensation path:
Incident owner:
```

## Minimum Controls

```text
[ ] Tier 3 controls completed where decision impact exists.
[ ] AI identity or agent identity defined.
[ ] Delegated authority defined.
[ ] Tool inventory completed.
[ ] Tool owners assigned.
[ ] Tool access approved.
[ ] Actions classified by risk.
[ ] High-risk actions require approval gates.
[ ] Least privilege applied.
[ ] Tool parameters validated where required.
[ ] Tool/action logs enabled.
[ ] Denied action attempts logged.
[ ] Blast-radius limits defined.
[ ] Kill switch or revocation path defined.
[ ] Rollback or compensation assessed.
[ ] Evidence reconstruction tested.
[ ] Incident containment path defined.
```

## Minimum Templates

```text
templates/ai-agent-control-template.md
templates/ai-tool-and-action-control-template.md
templates/ai-identity-and-access-control-template.md
templates/ai-incident-containment-recovery-template.md
templates/ai-assurance-test-plan-template.md
templates/ai-control-evidence-package-template.md
```

## Approval Path

```text
Business owner approval
Technical owner approval
Security/IAM approval
Tool owner approval
Risk owner approval where required
Incident owner review
Assurance approval before production
```

## Evidence

```text
Agent identity record
Access approval
Delegated authority record
Tool inventory
Action classification
Approval gate configuration
Tool/action logs
Denied action logs
Kill switch test
Rollback or compensation assessment
Evidence reconstruction test
Incident containment plan
Assurance test results
```

## Reassessment Triggers

Reassess Tier 4 if:

```text
New tools are added.
Tool permissions change.
Autonomy level increases.
Approval gates are removed or weakened.
AI can affect customers, money, access, security, HR, legal, or production systems.
Rollback becomes difficult or impossible.
Incidents or near misses occur.
```

---

# 10. Tier 5: High-Impact Full Review

## Description

Tier 5 AI is high-impact, autonomous, regulated, privileged, production-critical, externally exposed, difficult to reverse, or capable of causing material harm.

Typical examples:

```text
Autonomous agent with privileged tool access
AI affecting customer eligibility or entitlement
AI affecting employment decisions
AI affecting financial decisions
AI affecting legal or compliance outcomes
AI affecting security enforcement
AI affecting production systems
AI used in regulated processes
AI that is difficult to stop, reverse, or investigate
```

## Tier 5 Risk Drivers

```text
Regulated use
High-impact decisioning
Autonomous action
Privileged access
Production impact
Customer impact
Employee impact
Financial impact
Legal/compliance impact
Security impact
Low reversibility
High blast radius
```

## Minimum Intake

Tier 5 requires all Tier 4 intake plus:

```text
High-impact rationale:
Legal/regulatory review:
Residual risk owner:
Formal risk acceptance:
Enhanced assurance scope:
Evidence package owner:
Incident tabletop requirement:
Containment test requirement:
Restart approval authority:
Ongoing monitoring requirement:
```

## Minimum Controls

```text
[ ] Tier 4 controls completed.
[ ] Legal/regulatory review completed where applicable.
[ ] Formal high-impact risk assessment completed.
[ ] Full control assessment completed.
[ ] Residual risk owner assigned.
[ ] Formal risk acceptance completed where required.
[ ] Enhanced assurance testing completed.
[ ] Adversarial testing completed where required.
[ ] Evidence package completed.
[ ] Evidence reconstruction tested.
[ ] Incident tabletop completed.
[ ] Kill switch tested.
[ ] Rollback or compensation tested where possible.
[ ] Ongoing monitoring defined.
[ ] Restart criteria defined.
[ ] Governance approval obtained.
```

## Minimum Templates

```text
templates/ai-risk-assessment-template.md
templates/ai-control-assessment-template.md
templates/ai-assurance-test-plan-template.md
templates/ai-control-evidence-package-template.md
templates/ai-exception-record-template.md
templates/ai-incident-containment-recovery-template.md
templates/ai-incident-record-template.md
```

Additional templates may apply depending on the pattern:

```text
templates/ai-agent-control-template.md
templates/ai-data-boundary-template.md
templates/ai-output-and-decision-control-template.md
templates/ai-tool-and-action-control-template.md
templates/ai-vendor-assessment-template.md
```

## Approval Path

```text
Business owner approval
Technical owner approval
Data owner approval
Decision owner approval
Security approval
Privacy/legal approval where applicable
Risk owner approval
Assurance approval
Incident owner approval
Governance forum approval
Formal risk acceptance where residual risk remains
```

## Evidence

```text
Complete evidence package
Risk assessment
Control assessment
Legal/regulatory review record
Data owner approval
Decision owner record
Tool/action approval
Vendor assessment where applicable
Assurance test results
Adversarial test results
Evidence reconstruction test
Kill switch test
Rollback test
Incident tabletop result
Risk acceptance record
Governance approval
Ongoing monitoring record
```

## Reassessment Triggers

Reassess Tier 5 if:

```text
Model changes.
Vendor changes.
Data sources change.
Autonomy level changes.
Tool permissions change.
User population changes.
External exposure changes.
Regulatory environment changes.
Incidents occur.
Assurance findings occur.
Evidence gaps are discovered.
Control failures occur.
```

---

# 11. Minimum Control Baseline by Tier

| Control Area | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Tier 5 |
|---|---|---|---|---|---|
| Inventory | Required | Required | Required | Required | Required |
| Business owner | Required | Required | Required | Required | Required |
| Technical owner | Optional | Required where applicable | Required | Required | Required |
| Data source map | Not required if public/non-sensitive only | Required | Required | Required | Required |
| Vendor review | Not required unless vendor AI involved | Required if vendor AI involved | Required if vendor AI involved | Required if vendor AI involved | Required if vendor AI involved |
| Decision owner | Not required | Not required | Required | Required if decision/action impact | Required |
| Output validation | Basic user review | Basic | Required | Required where output drives action | Required |
| Human review | User responsibility | User responsibility | Required | Required for high-risk actions | Required and evidenced |
| Tool inventory | Not applicable | Not applicable | Required if tools exist | Required | Required |
| Approval gates | Not applicable | Not applicable | Required where decision impact exists | Required | Required |
| Logging | Minimal | Defined | Required | Required | Required |
| Evidence package | Not required | Optional | Required for high-risk decisions | Required | Required |
| Assurance testing | Not required | Targeted | Required | Required | Enhanced |
| Kill switch | Not required | Feature disablement where applicable | Required where operational impact exists | Required | Required and tested |
| Incident path | Basic escalation | Required | Required | Required | Required and tested |
| Risk acceptance | Not required | Not usually required | Required for material residual risk | Required for material residual risk | Required |

---

# 12. Template Use by Tier

| Template | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Tier 5 |
|---|---:|---:|---:|---:|---:|
| AI use case intake | Optional short form | Required | Required | Required | Required |
| AI risk assessment | Optional | Required | Required | Required | Required |
| AI control assessment | Not usually | Optional/targeted | Required | Required | Required |
| AI data boundary | Not usually | Required if enterprise data | Required | Required | Required |
| AI vendor assessment | Required if vendor AI | Required if vendor AI | Required if vendor AI | Required if vendor AI | Required if vendor AI |
| AI output and decision control | Not usually | Not usually | Required | Required where applicable | Required |
| AI human accountability | Lightweight | Lightweight | Required | Required | Required |
| AI agent control | Not applicable | Not applicable | Not applicable unless agent | Required if agent | Required if agent |
| AI tool and action control | Not applicable | Not applicable | Required if tools exist | Required | Required |
| AI assurance test plan | Not required | Targeted | Required | Required | Enhanced |
| AI evidence package | Not required | Optional | Required for high-risk | Required | Required |
| AI incident containment | Basic | Required | Required | Required | Required and tested |
| AI exception record | If exception exists | If exception exists | If exception exists | If exception exists | If exception exists |

---

# 13. Fast-Track Rules

A use case may be fast-tracked only when all of the following are true:

```text
[ ] No sensitive data.
[ ] No customer data.
[ ] No employee data.
[ ] No regulated data.
[ ] No confidential enterprise data.
[ ] No vendor AI processing beyond approved public/general tool use.
[ ] No decision impact.
[ ] No generated official records.
[ ] No customer-facing output.
[ ] No tool or API access.
[ ] No workflow action.
[ ] No production, security, finance, HR, legal, compliance, or access impact.
[ ] No persistent memory using enterprise data.
[ ] No material business risk if output is wrong.
```

If any of these are false, the use case should not be fast-tracked.

---

# 14. Escalation Rules

Escalate to deeper review when any of the following are true:

```text
AI uses confidential or sensitive data.
AI uses customer or employee data.
AI uses regulated data.
AI is embedded in vendor SaaS.
AI retrieves from enterprise repositories.
AI output influences decisions.
AI output becomes a record.
AI output is customer-facing.
AI can call tools.
AI can trigger workflows.
AI can update records.
AI can send communications.
AI can affect access.
AI can affect security actions.
AI can affect production systems.
AI has persistent memory.
AI is difficult to disable.
AI has unclear logging.
AI has unclear vendor retention or training/reuse.
```

---

# 15. Approval Decision Types

Triage may result in one of these decisions.

| Decision | Meaning |
|---|---|
| Approved | Use case may proceed as described. |
| Fast-track approved | Low-risk use may proceed with minimal controls. |
| Approved with conditions | Use may proceed only if listed conditions are met. |
| Pilot only | Use is approved only for limited pilot scope. |
| Requires remediation | Control gaps must be fixed before approval. |
| Requires enhanced review | Higher-risk review is required before decision. |
| Requires risk acceptance | Residual risk must be accepted by accountable owner. |
| Not approved | Use case should not proceed. |
| Suspended | Existing use must pause until review or remediation. |
| Retired | Use case should be removed from active use. |

---

# 16. Conditional Approval

Conditional approval should be used when risk is manageable but controls are incomplete.

A conditional approval should include:

```text
Condition:
Owner:
Due date:
Evidence required:
Review date:
Consequence if not completed:
```

Example:

```text
Condition: Vendor must confirm prompt/output retention and training/reuse settings before pilot expansion.
Owner: Vendor owner
Due date: 30 days
Evidence required: Vendor written confirmation or contract documentation
Review date: Before production rollout
Consequence: Pilot cannot expand
```

---

# 17. Exception Handling

An exception is required when a required control is not implemented but the use case is allowed to proceed.

Exceptions should not be used for convenience.

Exceptions should include:

```text
Requirement not met:
Risk created:
Business justification:
Compensating control:
Exception owner:
Risk acceptance owner:
Approval date:
Expiry date:
Remediation plan:
Review cadence:
Closure evidence:
```

Use:

```text
templates/ai-exception-record-template.md
```

---

# 18. Reassessment Triggers

Every AI use case should be reassessed when a material change occurs.

Material changes include:

```text
New data source
Higher data classification
New vendor processing
Vendor retention change
Vendor training/reuse change
New user population
New customer-facing use
New decision impact
New output type
New generated record
New tool or API access
New workflow action
New autonomy level
New persistent memory
New model
New system prompt
New retrieval source
New integration
New regulatory impact
Assurance finding
Incident or near miss
Control failure
Evidence gap
```

---

# 19. Anti-Bureaucracy Principles

The triage model should prevent governance theater.

## Principle 1: Ask fewer questions first

Start with the five fast triage questions.

Ask more only when risk drivers appear.

---

## Principle 2: Do not make Tier 1 feel like Tier 5

Low-risk AI should not require full evidence packages, incident tabletops, kill switch tests, or lengthy control assessments.

---

## Principle 3: Do not let Tier 4 hide inside Tier 2

If AI can act, call tools, trigger workflows, or modify records, it is not simple productivity AI.

---

## Principle 4: Templates should be conditional

Templates should be used when risk requires them.

They should not become mandatory paperwork for every use case.

---

## Principle 5: Automate intake where possible

Triage should eventually be implemented in workflow tools, GRC platforms, developer portals, or service management systems.

Markdown templates are starting points, not the final operating model.

---

# 20. Example Triage Outcomes

## Example 1: Public-Data Drafting Assistant

```text
Use case: Employee uses AI to rewrite public marketing text.
Data: Public only
Decision impact: None
Tool/action capability: None
Vendor AI: General approved tool
Tier: Tier 1
Outcome: Fast-track approved
Minimum controls: Acceptable use guidance and sensitive data prohibition
```

---

## Example 2: Internal Meeting Summarization Copilot

```text
Use case: Copilot summarizes internal meetings.
Data: Internal meeting content
Decision impact: Low
Tool/action capability: None
Vendor AI: Yes
Tier: Tier 2
Outcome: Standard review
Minimum controls: Vendor review, retention/training review, user guidance, incident path
```

---

## Example 3: Policy RAG Assistant

```text
Use case: RAG assistant answers employee policy questions.
Data: Approved policy repository
Decision impact: Guidance may influence compliance behavior
Tool/action capability: Read-only retrieval
Vendor AI: Possible
Tier: Tier 3
Outcome: Enhanced review
Minimum controls: Data boundary, source attribution, decision boundary, output validation, prompt injection testing
```

---

## Example 4: IT Ticket Triage Agent

```text
Use case: Agent classifies tickets and requests routing changes.
Data: ITSM tickets and knowledge base
Decision impact: Operational prioritization
Tool/action capability: Routing request and internal note draft
Vendor AI: Possible
Tier: Tier 4
Outcome: Action-capable review
Minimum controls: Agent identity, tool inventory, action classification, approval gates, logs, kill switch, rollback
```

---

## Example 5: AI System Supporting Employee Decisions

```text
Use case: AI supports employee performance or hiring decisions.
Data: Employee data
Decision impact: High-impact employee decision
Tool/action capability: Possible workflow influence
Vendor AI: Possible
Tier: Tier 5
Outcome: Full review
Minimum controls: Legal/privacy review, decision owner, enhanced assurance, evidence package, risk acceptance, incident readiness
```

---

# 21. Triage Checklist

Use this checklist during initial AI intake.

```text
[ ] Use case name recorded.
[ ] Business purpose recorded.
[ ] Business owner assigned.
[ ] AI pattern identified.
[ ] Vendor AI involvement identified.
[ ] Data sources identified.
[ ] Highest data classification identified.
[ ] Customer data identified.
[ ] Employee data identified.
[ ] Regulated data identified.
[ ] Decision impact identified.
[ ] Output type identified.
[ ] Generated record impact identified.
[ ] Tool/action capability identified.
[ ] Autonomy level identified where applicable.
[ ] Customer-facing exposure identified.
[ ] Reversibility assessed.
[ ] Initial risk tier assigned.
[ ] Minimum controls identified.
[ ] Required templates identified.
[ ] Approval path identified.
[ ] Reassessment triggers documented.
```

---

# 22. Relationship to Templates

The templates in this repository are reusable tools.

They should be applied based on risk.

Do not require every template for every use case.

Use the triage outcome to decide which templates are necessary.

For low-risk use cases, a lightweight intake may be sufficient.

For high-risk use cases, multiple templates may be required because ownership, evidence, assurance, and incident response matter.

---

# 23. Relationship to Machine-Readable Controls

This triage model should eventually be converted into machine-readable workflow logic.

Possible future formats:

```text
YAML risk-tier rules
JSON intake schema
GRC workflow fields
ServiceNow intake workflow
Jira issue template
Developer portal form
Control catalogue
Evidence checklist
```

The long-term goal is not to make teams fill out Markdown files manually.

The long-term goal is to convert AI control requirements into workflow, evidence, and automation.

---

# 24. Related Documents

```text
QUICKSTART.md
ROADMAP.md
docs/06-requirements-catalogue.md
docs/06-requirements-catalogue.md
docs/17-implementation-checklists.md
docs/18-control-maturity-model.md
docs/19-common-ai-control-patterns.md
docs/20-common-failure-scenarios.md
docs/21-adoption-playbook.md
docs/22-governance-and-operating-model.md
docs/23-metrics-and-reporting.md
docs/24-assurance-and-audit-guide.md
```

---

# 25. Related Templates

```text
templates/ai-use-case-intake-template.md
templates/ai-risk-assessment-template.md
templates/ai-risk-tiering-template.md
templates/ai-control-assessment-template.md
templates/ai-data-boundary-template.md
templates/ai-vendor-assessment-template.md
templates/ai-output-and-decision-control-template.md
templates/ai-tool-and-action-control-template.md
templates/ai-agent-control-template.md
templates/ai-assurance-test-plan-template.md
templates/ai-control-evidence-package-template.md
templates/ai-exception-record-template.md
templates/ai-incident-containment-recovery-template.md
```

---

# 26. Summary

The AI Control Architecture should be practical.

It should help enterprises move quickly where risk is low and apply deeper control where risk is high.

The triage model ensures that:

```text
Tier 1 AI is not overburdened.
Tier 2 AI gets data and vendor review.
Tier 3 AI gets decision accountability and output validation.
Tier 4 AI gets tool/action controls and containment.
Tier 5 AI gets full assurance, evidence, governance, and recovery planning.
```

The goal is not more paperwork.

The goal is:

```text
The right control depth for the right AI risk.
```