# Governance and Operating Model

This document defines the governance and operating model for the AI Control Architecture.

The purpose is to clarify who owns AI control, who makes decisions, who approves risk, who provides evidence, who tests controls, who manages exceptions, and who responds when AI fails.

AI control cannot operate through policy alone.

It requires clear roles, decision rights, operating processes, escalation paths, evidence ownership, and accountability.

---

# 1. Purpose

The governance and operating model answers the following questions:

```text
Who owns AI use?
Who owns AI risk?
Who owns AI controls?
Who approves AI use?
Who approves exceptions?
Who reviews vendor AI?
Who tests AI controls?
Who monitors AI activity?
Who responds to AI incidents?
Who decides whether AI can continue operating?
```

The goal is to make AI adoption:

- visible
- owned
- risk-tiered
- controlled
- evidenced
- tested
- monitored
- recoverable

---

# 2. Core Governance Principle

The core governance principle is:

> AI may be automated, but accountability must remain human.

AI systems can assist, recommend, summarize, classify, retrieve, generate, or act.

But AI must not become the accountable owner of:

- business outcomes
- decisions
- access
- data exposure
- customer impact
- employee impact
- regulatory impact
- vendor risk
- exceptions
- incidents
- recovery

Every AI use case must have accountable human ownership.

---

# 3. Operating Model Overview

The AI Control Architecture operating model has seven layers:

```text
1. Business ownership
2. Technical ownership
3. Risk and control ownership
4. Data and privacy ownership
5. Vendor ownership
6. Assurance and evidence ownership
7. Incident and recovery ownership
```

Each layer answers a different control question.

| Layer | Core Question |
|---|---|
| Business ownership | Why does this AI exist, and who owns the business outcome? |
| Technical ownership | Who owns the system, configuration, integration, and remediation? |
| Risk and control ownership | What risk tier applies, and what controls are required? |
| Data and privacy ownership | What data can AI access, process, retain, or expose? |
| Vendor ownership | What vendor AI is involved, and what evidence exists? |
| Assurance and evidence ownership | How do we prove controls operate? |
| Incident and recovery ownership | How do we contain and recover from AI failure? |

---

# 4. Key Roles

## 4.1 Business Owner

The business owner is accountable for the business purpose, business outcome, and business risk of the AI use case.

Responsibilities include:

- define the business purpose
- approve intended use
- own business outcome
- ensure the AI use case remains aligned to business need
- accept business risk where appropriate
- support risk tiering
- approve production use where required
- participate in incident response where business impact exists
- review continued use periodically

The business owner must not delegate accountability to the AI system or vendor.

---

## 4.2 Technical Owner

The technical owner is accountable for technical implementation and operation.

Responsibilities include:

- own system configuration
- own integrations
- own model or service configuration where applicable
- own prompt, retrieval, or workflow configuration where applicable
- implement identity and access controls
- implement logging and monitoring controls
- support assurance testing
- remediate technical findings
- support incident containment and recovery

The technical owner may be an application owner, platform owner, engineering owner, or product technology owner.

---

## 4.3 Data Owner

The data owner is accountable for approval and control of data used by AI.

Responsibilities include:

- approve data source use
- confirm data classification
- define sensitive data restrictions
- approve retrieval boundaries
- define retention requirements
- define training and reuse restrictions
- review cross-boundary data movement
- support data leakage investigations
- approve data-related exceptions where required

AI must not be granted access to sensitive or regulated data without appropriate data ownership and approval.

---

## 4.4 Decision Owner

The decision owner is accountable where AI output influences a decision.

Responsibilities include:

- own final decision authority
- ensure AI recommendation is separate from final decision
- define validation expectations
- define human review requirements
- ensure decision evidence is retained
- approve decision workflow where required
- support correction or override where AI output is wrong

The decision owner is especially important for:

- customer-impacting decisions
- employee-impacting decisions
- financial decisions
- legal or compliance decisions
- security decisions
- access decisions
- production or operational decisions
- regulated or high-impact decisions

---

## 4.5 AI Control Owner

The AI control owner is responsible for maintaining the AI Control Architecture requirements, templates, control expectations, and maturity roadmap.

Responsibilities include:

- maintain AI control requirements
- maintain templates and guidance
- define minimum controls by risk tier
- coordinate control assessments
- track control gaps
- support governance forums
- update the architecture based on incidents, assurance findings, and emerging risks

This role may sit in enterprise architecture, security architecture, risk, governance, or a dedicated AI governance function.

---

## 4.6 Security Owner

The security owner is accountable for security-related AI controls.

Responsibilities include:

- review AI identity and access
- review privileged access
- review tool and action security
- review prompt injection risk
- review data leakage risk
- review monitoring and alerting
- review incident response readiness
- support security assurance testing
- support AI security incidents

Security ownership is critical where AI can access sensitive data, use tools, trigger workflows, or affect production/security systems.

---

## 4.7 Privacy Owner

The privacy owner is accountable for privacy-related AI risk.

Responsibilities include:

- review personal data processing
- review customer and employee data use
- assess privacy rights impact
- review retention and deletion requirements
- review vendor data processing
- review cross-border transfer implications
- support privacy incident response
- advise on notification obligations where required

---

## 4.8 Legal Owner

The legal owner is accountable for legal and contractual AI risk.

Responsibilities include:

- review legal exposure
- review privileged material use
- review customer or public commitments
- review regulated use
- review vendor contractual terms
- review liability, indemnity, and audit rights where required
- support incident communications and regulatory response where required

---

## 4.9 Vendor Owner

The vendor owner is accountable for the enterprise relationship with any vendor providing AI capability.

Responsibilities include:

- identify vendor AI features
- coordinate vendor AI assessment
- obtain vendor documentation
- review feature enablement status
- track vendor remediation
- confirm vendor incident support path
- support contract updates where required
- monitor vendor changes

Vendor AI does not remove internal accountability.

---

## 4.10 Assurance Owner

The assurance owner is accountable for AI testing and control validation.

Responsibilities include:

- define assurance scope
- create assurance test plans
- coordinate testing
- document test evidence
- track findings
- confirm remediation
- define retesting requirements
- support readiness decisions
- report assurance results to governance

Assurance must test both:

```text
AI behavior
AI control effectiveness
```

---

## 4.11 Evidence Owner

The evidence owner is accountable for ensuring required AI control evidence exists, is retained, and can be retrieved.

Responsibilities include:

- define evidence requirements
- maintain evidence packages
- confirm evidence completeness
- manage evidence retention
- protect sensitive evidence
- support audit and incident response
- support reconstructability testing

For high-risk AI, evidence must support reconstruction of what AI saw, produced, decided, triggered, or exposed.

---

## 4.12 Incident Owner

The incident owner is accountable for AI incident coordination, containment, recovery, and lessons learned.

Responsibilities include:

- define AI incident scenarios
- own AI incident escalation
- coordinate containment
- preserve evidence
- coordinate investigation
- support recovery and correction
- coordinate communications where required
- approve or support restart criteria
- ensure lessons learned update the control architecture

---

# 5. Governance Forums

AI control decisions can be handled through existing enterprise forums.

A separate AI committee may be useful, but it is not always required.

The important point is that AI-specific control questions must be embedded into decision forums.

## 5.1 Enterprise Architecture Review

Responsibilities:

- review AI architecture decisions
- review control design
- review system integration
- review target-state alignment
- approve architecture decision records
- ensure brownfield compatibility

Relevant templates:

```text
templates/ai-architecture-decision-record-template.md
templates/ai-control-assessment-template.md
```

---

## 5.2 Security Architecture Review

Responsibilities:

- review identity and access
- review privileged access
- review tool and action controls
- review monitoring and logging
- review incident containment
- review prompt injection and data leakage controls

Relevant templates:

```text
templates/ai-identity-and-access-control-template.md
templates/ai-tool-and-action-control-template.md
templates/ai-incident-containment-recovery-template.md
```

---

## 5.3 Data Governance Forum

Responsibilities:

- approve data sources
- review data classification
- review retrieval boundaries
- review retention and reuse
- review training and fine-tuning use
- review cross-boundary data movement
- review data leakage findings

Relevant templates:

```text
templates/ai-data-boundary-template.md
templates/ai-risk-assessment-template.md
```

---

## 5.4 Privacy and Legal Review

Responsibilities:

- review personal data use
- review regulated data use
- review privileged material
- review customer-facing or external output
- review vendor data processing terms
- review incident notification requirements
- review legal or contractual risk

Relevant templates:

```text
templates/ai-vendor-assessment-template.md
templates/ai-output-and-decision-control-template.md
```

---

## 5.5 Vendor Risk Forum

Responsibilities:

- review AI-enabled SaaS
- review embedded vendor AI
- review hosted model providers
- review data processing
- review retention and training/reuse
- review subprocessors
- review vendor logs and evidence
- review vendor incident support

Relevant template:

```text
templates/ai-vendor-assessment-template.md
```

---

## 5.6 Risk and Governance Forum

Responsibilities:

- approve risk-tiering model
- review high-risk AI use cases
- approve risk acceptance
- review exceptions
- review open findings
- review maturity reporting
- review AI control roadmap

Relevant templates:

```text
templates/ai-risk-assessment-template.md
templates/ai-risk-tiering-template.md
templates/ai-exception-record-template.md
templates/ai-control-maturity-assessment-template.md
```

---

## 5.7 Change Advisory or SDLC Forum

Responsibilities:

- review model changes
- review prompt changes
- review retrieval changes
- review tool/API changes
- review workflow changes
- review production deployment
- trigger regression testing

Relevant templates:

```text
templates/ai-assurance-test-plan-template.md
templates/ai-architecture-decision-record-template.md
```

---

## 5.8 Incident Response Forum

Responsibilities:

- review AI incident scenarios
- coordinate AI incident response
- approve containment and recovery actions
- review incident evidence
- conduct post-incident review
- update controls after incidents

Relevant templates:

```text
templates/ai-incident-containment-recovery-template.md
templates/ai-incident-record-template.md
```

---

## 5.9 Audit or Assurance Forum

Responsibilities:

- review control evidence
- review assurance results
- review findings and remediation
- review evidence packages
- review maturity assessments
- validate reconstructability

Relevant templates:

```text
templates/ai-control-evidence-package-template.md
templates/ai-assurance-test-plan-template.md
```

---

# 6. Decision Rights

Decision rights should be explicit.

The following model can be adapted by each enterprise.

| Decision | Accountable Owner | Consulted Functions |
|---|---|---|
| Approve AI use case | Business owner | Architecture, security, risk, data, privacy, legal |
| Assign risk tier | Risk/governance owner | Business, technical, security, data, privacy, legal |
| Approve data source use | Data owner | Business, technical, privacy, security |
| Approve AI identity/access | Security/IAM owner | Technical owner, business owner, data owner |
| Approve vendor AI | Vendor owner / vendor risk forum | Security, privacy, legal, data, business |
| Approve customer-facing AI | Business owner | Legal, privacy, compliance, security |
| Approve decision-supporting AI | Decision owner | Risk, legal, compliance, assurance |
| Approve tool/action capability | Business and technical owners | Security, risk, IAM, incident response |
| Approve high-risk action | Designated approver | Business, security, risk |
| Approve exception | Risk owner / governance forum | Business, technical, control owner |
| Accept residual risk | Risk acceptance owner | Governance, legal, security, business |
| Approve production deployment | Business and technical owners | Architecture, security, risk, assurance |
| Approve restart after incident | Incident owner and business owner | Security, legal, privacy, technical, risk |

---

# 7. RACI Model

Use this starter RACI model and adapt it to local governance.

Legend:

```text
R = Responsible
A = Accountable
C = Consulted
I = Informed
```

| Activity | Business | Technical | Data | Security | Privacy/Legal | Vendor | Risk/GRC | Assurance | Incident |
|---|---|---|---|---|---|---|---|---|---|
| AI use case intake | A | R | C | C | C | C | C | I | I |
| AI inventory update | A | R | C | C | I | C | C | I | I |
| Risk tiering | A | C | C | C | C | C | R | I | I |
| Data boundary approval | C | C | A/R | C | C | C | I | I | I |
| Identity/access review | C | R | C | A/R | I | C | I | I | I |
| Vendor AI assessment | C | C | C | C | C | A/R | C | I | I |
| Output/decision control | A | R | C | C | C | I | C | C | I |
| Tool/action control | A | R | C | A/R | C | C | C | C | I |
| Human accountability model | A | C | C | C | C | C | R | I | I |
| Assurance testing | C | R | C | C | C | C | I | A/R | I |
| Evidence package | C | R | C | C | C | C | C | A/R | I |
| Exception approval | A | C | C | C | C | C | R | I | I |
| Incident response | C | R | C | R | C | C | I | I | A/R |
| Post-incident review | C | C | C | C | C | C | R | C | A/R |
| Maturity reporting | I | C | C | C | C | C | A/R | C | I |

---

# 8. Core Operating Processes

## 8.1 AI Use Case Intake

Purpose:

```text
Capture proposed, existing, embedded, or discovered AI use cases.
```

Minimum steps:

1. Submit use case intake.
2. Assign business owner.
3. Identify AI pattern.
4. Identify data sources.
5. Identify vendor involvement.
6. Identify decision impact.
7. Identify tool/action capability.
8. Assign initial risk tier.
9. Determine required reviews.

Related template:

```text
templates/ai-use-case-intake-template.md
```

---

## 8.2 AI Risk Tiering

Purpose:

```text
Determine required controls, assurance, evidence, and review depth.
```

Minimum steps:

1. Assess data risk.
2. Assess decision risk.
3. Assess output risk.
4. Assess tool/action risk.
5. Assess autonomy risk.
6. Assess external exposure.
7. Assess vendor risk.
8. Assess recoverability.
9. Assign risk tier.
10. Document rationale.

Related templates:

```text
templates/ai-risk-assessment-template.md
templates/ai-risk-tiering-template.md
```

---

## 8.3 AI Control Assessment

Purpose:

```text
Determine whether required controls exist and operate.
```

Minimum steps:

1. Review inventory and ownership.
2. Review identity and access.
3. Review data boundary.
4. Review prompt and input controls.
5. Review output and decision controls.
6. Review tool and action controls.
7. Review human accountability.
8. Review assurance requirements.
9. Review logging and evidence.
10. Review incident containment and recovery.
11. Document gaps.
12. Record approval, conditions, or exceptions.

Related template:

```text
templates/ai-control-assessment-template.md
```

---

## 8.4 Vendor AI Assessment

Purpose:

```text
Review vendor AI before enablement, purchase, integration, scaling, or continued use.
```

Minimum steps:

1. Identify vendor AI feature.
2. Confirm enablement status.
3. Review data processed.
4. Review retention.
5. Review training/reuse.
6. Review identity and permissions.
7. Review admin controls.
8. Review logs and evidence.
9. Review incident support.
10. Review contractual requirements.
11. Record vendor AI risk decision.

Related template:

```text
templates/ai-vendor-assessment-template.md
```

---

## 8.5 AI Architecture Decision

Purpose:

```text
Record key architecture decisions and their control implications.
```

Use an architecture decision record when deciding:

- AI pattern
- model or vendor
- identity model
- data boundary
- retrieval design
- prompt control
- output control
- tool/action control
- logging approach
- containment design

Related template:

```text
templates/ai-architecture-decision-record-template.md
```

---

## 8.6 AI Assurance Testing

Purpose:

```text
Validate AI behavior and control effectiveness before trust.
```

Minimum steps:

1. Define assurance scope.
2. Define test cases.
3. Test identity and access.
4. Test data boundaries.
5. Test prompt injection where required.
6. Test output validation where required.
7. Test tool/action controls where required.
8. Test logging completeness.
9. Test evidence reconstruction.
10. Test containment and recovery where required.
11. Document findings.
12. Approve, conditionally approve, or reject.

Related template:

```text
templates/ai-assurance-test-plan-template.md
```

---

## 8.7 AI Exception Management

Purpose:

```text
Document temporary deviations from required controls.
```

Minimum steps:

1. Identify unmet requirement.
2. Document business justification.
3. Assess risk.
4. Define compensating controls.
5. Assign exception owner.
6. Assign risk acceptance owner.
7. Define expiry date.
8. Define remediation plan.
9. Approve exception.
10. Review until closed.

Related template:

```text
templates/ai-exception-record-template.md
```

---

## 8.8 AI Incident Management

Purpose:

```text
Contain, investigate, recover, and learn from AI failure.
```

Minimum steps:

1. Detect incident or near miss.
2. Assign incident owner.
3. Preserve evidence.
4. Contain AI capability.
5. Revoke access or disable tools where needed.
6. Quarantine outputs or records where needed.
7. Investigate root cause.
8. Recover or correct impact.
9. Communicate where required.
10. Approve restart.
11. Conduct post-incident review.
12. Update controls and tests.

Related templates:

```text
templates/ai-incident-containment-recovery-template.md
templates/ai-incident-record-template.md
```

---

# 9. Risk Tier Governance

Risk tier determines control depth.

| Tier | Governance Expectation |
|---|---|
| Tier 1 | Lightweight inventory, owner, acceptable use, basic data restriction. |
| Tier 2 | Data source mapping, classification, access boundary, vendor review where applicable. |
| Tier 3 | Decision owner, output validation, human review, decision evidence, correction path. |
| Tier 4 | Tool inventory, action classification, approval gates, action logs, kill switch or revocation path. |
| Tier 5 | Enhanced assurance, full reconstructable evidence, tested containment, risk acceptance, ongoing monitoring. |

Risk tier should be reviewed when:

- data source changes
- user population changes
- external exposure changes
- output use changes
- decision impact changes
- tool/action capability changes
- autonomy level changes
- vendor processing changes
- incident occurs
- assurance finding occurs
- regulatory or legal requirement changes

---

# 10. Exception Governance

Exceptions must be temporary, owned, approved, and reviewed.

An AI exception should include:

```text
Affected requirement
Business justification
Risk created
Compensating control
Exception owner
Risk acceptance owner
Approval date
Expiry date
Remediation plan
Review cadence
Closure evidence
```

Exceptions should not be used to normalize weak control.

## Exception Escalation

Escalate exceptions when:

- expiry date is missed
- compensating control fails
- risk tier increases
- incident occurs
- assurance finding relates to exception
- remediation is not progressing
- exception becomes recurring

---

# 11. Evidence Governance

Evidence must be treated as part of the control.

For high-risk AI, evidence should allow the enterprise to reconstruct:

```text
What AI use case was involved?
Who initiated the interaction?
What identity did AI use?
What data was accessed?
What prompt or input was submitted?
What context was retrieved?
What output was generated?
What decision was influenced?
What tool was called?
What action was executed?
Was approval required?
Was approval obtained?
What exception existed?
What incident response occurred?
```

Evidence governance should define:

- evidence owner
- evidence location
- retention period
- access restrictions
- sensitivity handling
- legal hold process
- audit access
- deletion process
- vendor evidence dependencies

Related template:

```text
templates/ai-control-evidence-package-template.md
```

---

# 12. Incident Governance

AI incident governance should define:

- what qualifies as an AI incident
- severity criteria
- detection sources
- escalation path
- incident owner
- containment authority
- evidence preservation
- vendor escalation
- communication approval
- recovery owner
- restart approval
- post-incident review

## AI Incident Examples

AI incidents may include:

- sensitive data exposed through AI
- unauthorized retrieval
- prompt injection success
- unsafe customer-facing output
- incorrect AI-assisted decision
- unauthorized tool use
- approval bypass
- agent malfunction
- vendor AI data handling issue
- missing evidence during investigation
- AI-generated record error
- production or security impact caused by AI

---

# 13. Governance Metrics

Governance should monitor metrics that show control coverage and risk.

## Inventory Metrics

- number of AI use cases inventoried
- percentage of AI use cases with business owner
- percentage of AI use cases risk-tiered
- number of embedded vendor AI features identified
- number of unreviewed AI use cases

## Risk Metrics

- number of Tier 3, Tier 4, and Tier 5 AI use cases
- percentage of high-risk AI with completed risk assessment
- percentage of high-risk AI with completed control assessment
- number of use cases with unknown risk tier
- number of risk acceptances

## Control Metrics

- percentage of AI use cases with data sources mapped
- percentage with identity model defined
- percentage with output and decision control defined
- percentage of action-capable AI with tool/action controls
- percentage of high-risk AI with containment plan

## Assurance Metrics

- percentage of high-risk AI with assurance testing completed
- number of open assurance findings
- number of failed tests
- percentage of findings closed on time
- number of retests required

## Evidence Metrics

- percentage of high-risk AI with evidence package
- percentage of high-risk AI with reconstructability tested
- number of evidence gaps
- number of vendor evidence gaps

## Exception and Incident Metrics

- number of open AI exceptions
- number of expired AI exceptions
- number of AI incidents
- number of AI near misses
- number of incidents requiring vendor escalation
- number of incidents leading to control updates

---

# 14. Operating Cadence

A suggested operating cadence is below.

| Cadence | Activity |
|---|---|
| Weekly | Review new AI intake requests and urgent exceptions. |
| Biweekly | Review high-risk AI assessments and vendor AI requests. |
| Monthly | Review open findings, exceptions, and incidents. |
| Quarterly | Review AI inventory, maturity metrics, and roadmap. |
| Semi-annually | Test incident containment for high-risk AI and agents. |
| Annually | Review maturity model, requirements, templates, and governance model. |
| Event-driven | Review after model changes, vendor changes, incidents, or risk tier changes. |

---

# 15. Minimum Operating Model

A minimum operating model should include:

```text
[ ] AI inventory owner
[ ] AI use case intake process
[ ] Business owner assignment
[ ] Risk tiering model
[ ] Control assessment process
[ ] Vendor AI review process
[ ] Exception process
[ ] Assurance process for high-risk AI
[ ] Evidence owner or repository
[ ] AI incident escalation path
[ ] Governance forum for high-risk decisions
```

This is the minimum foundation.

Without these elements, AI control will remain informal.

---

# 16. Mature Operating Model

A mature operating model should include:

```text
[ ] Integrated AI intake workflow
[ ] Automated or semi-automated AI inventory updates
[ ] Risk-tier-driven control requirements
[ ] Integrated IAM/PAM review for AI identities
[ ] Integrated data governance review for AI data sources
[ ] Integrated vendor risk workflow for vendor AI
[ ] Assurance test catalogue
[ ] Evidence packages for high-risk AI
[ ] SIEM/SOC or monitoring integration for AI events
[ ] GRC integration for requirements, exceptions, and findings
[ ] AI incident playbooks
[ ] Periodic maturity assessment
[ ] AI control dashboard
[ ] Continuous improvement backlog
```

---

# 17. Common Governance Anti-Patterns

## Anti-Pattern 1: AI Governance Without Owners

A committee exists, but no one owns each AI use case.

Result:

```text
AI use remains unaccountable.
```

## Anti-Pattern 2: Security-Only AI Governance

AI is treated only as a cybersecurity issue.

Result:

```text
Decision risk, legal risk, data risk, vendor risk, and business accountability are missed.
```

## Anti-Pattern 3: Vendor-Led Governance

The enterprise relies on vendor claims and product settings as the control model.

Result:

```text
Internal accountability and evidence gaps remain unresolved.
```

## Anti-Pattern 4: Policy Without Operating Process

The organization publishes an AI policy but does not define intake, assessment, evidence, assurance, or incident response.

Result:

```text
Policy exists, but control does not.
```

## Anti-Pattern 5: Risk Acceptance Without Expiry

Control gaps are accepted without time limits or remediation.

Result:

```text
Exceptions become permanent weaknesses.
```

## Anti-Pattern 6: Human Review Without Authority

Human review is required, but reviewers cannot meaningfully challenge AI output.

Result:

```text
Human-in-the-loop becomes theater.
```

---

# 18. Success Criteria

The governance and operating model is working when the enterprise can say:

```text
We know what AI exists.
Every AI use case has a business owner.
High-risk AI is risk-tiered.
Required controls are mapped.
Exceptions are owned and temporary.
Vendor AI is reviewed before enablement.
AI controls are tested where required.
Evidence exists for high-risk AI.
AI incidents have a containment path.
Governance metrics are reported.
Lessons learned improve the architecture.
```

---

# 19. Related Documents

```text
docs/17-implementation-checklists.md
docs/18-control-maturity-model.md
docs/19-common-ai-control-patterns.md
docs/20-common-failure-scenarios.md
docs/21-adoption-playbook.md
```

---

# 20. Related Templates

```text
templates/ai-use-case-intake-template.md
templates/ai-risk-assessment-template.md
templates/ai-control-assessment-template.md
templates/ai-architecture-decision-record-template.md
templates/ai-assurance-test-plan-template.md
templates/ai-vendor-assessment-template.md
templates/ai-exception-record-template.md
templates/ai-incident-record-template.md
templates/ai-control-evidence-package-template.md
templates/ai-control-maturity-assessment-template.md
```

---

# 21. Summary

AI governance must become an operating model.

The enterprise must define:

```text
Who owns AI.
Who approves AI.
Who reviews risk.
Who owns data.
Who reviews vendors.
Who tests controls.
Who owns evidence.
Who approves exceptions.
Who responds to incidents.
Who improves the architecture.
```

The operating model should be practical, risk-tiered, and integrated into existing enterprise processes.

The goal is not governance for its own sake.

The goal is controlled AI adoption.