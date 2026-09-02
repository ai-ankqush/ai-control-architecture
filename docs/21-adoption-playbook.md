# Adoption Playbook

This document provides a practical playbook for adopting the AI Control Architecture inside an enterprise.

The goal is not to slow down AI adoption.

The goal is to make AI adoption visible, controlled, accountable, evidenced, and recoverable.

Enterprises do not need another AI policy sitting on a shelf. They need a practical control architecture that can be applied to copilots, agents, RAG systems, vendor AI, AI-enabled SaaS, internal LLM applications, and AI-enabled workflows.

---

# 1. Purpose

This playbook explains how to move from:

```text
Uncontrolled AI adoption
```

to:

```text
AI adoption with control architecture
```

It provides a staged approach for:

- discovering AI use
- assigning ownership
- classifying risk
- mapping controls
- creating evidence
- testing AI control effectiveness
- managing vendor AI
- preparing for AI incidents
- improving maturity over time

---

# 2. Who Should Use This Playbook

This playbook is intended for:

- executive sponsors
- AI governance teams
- enterprise architects
- security architects
- risk teams
- compliance teams
- privacy teams
- legal teams
- vendor risk teams
- data governance teams
- application owners
- platform owners
- AI product teams
- internal audit teams
- incident response teams

AI control adoption is not owned by one function.

It requires shared ownership across business, technology, risk, security, data, legal, privacy, vendor management, and operations.

---

# 3. Adoption Principles

## Principle 1: Start With Visibility

AI cannot be controlled if it is not visible.

The first step is to identify:

```text
What AI exists?
Where is it used?
Who owns it?
What business process does it support?
What data does it touch?
```

---

## Principle 2: Risk-Tier Before You Over-Control

Not every AI use case needs the same level of control.

A low-risk drafting assistant does not require the same controls as an autonomous agent that can modify customer records.

Use risk tiering to decide the level of review, evidence, assurance, and monitoring required.

---

## Principle 3: Focus on What AI Can See, Decide, and Do

Every AI use case should be assessed through three control questions:

```text
What can AI see?
What can AI decide?
What can AI do?
```

Then ask:

```text
Who is accountable?
What evidence exists?
How is failure contained?
```

---

## Principle 4: Use Existing Enterprise Processes

AI control should integrate with existing processes wherever possible.

Do not create isolated AI governance if existing processes can be extended.

Integrate AI control with:

- enterprise architecture
- security architecture
- IAM/PAM
- data governance
- SDLC
- vendor risk management
- privacy review
- legal review
- GRC
- SIEM/SOC
- incident response
- audit

---

## Principle 5: Treat Vendor AI as Enterprise AI

Vendor AI is still enterprise AI if it processes, generates, retains, exposes, or acts on enterprise data.

Vendor AI must be inventoried, reviewed, configured, evidenced, and monitored.

---

## Principle 6: Evidence Is Part of the Control

A control that cannot be evidenced is difficult to trust.

For high-risk AI, the enterprise should be able to reconstruct:

```text
What prompt or input was submitted?
What data was retrieved?
What output was produced?
What decision was influenced?
What tool was called?
What action occurred?
Who approved it?
What evidence exists?
```

---

## Principle 7: Design for Failure

AI failure should be expected.

High-risk AI should have:

- incident scenarios
- containment mechanisms
- access revocation
- kill switches where required
- rollback or compensation
- evidence preservation
- recovery process
- restart criteria

---

# 4. Adoption Stages

The adoption journey has five stages:

```text
Stage 1: Establish visibility
Stage 2: Establish minimum control
Stage 3: Integrate control into enterprise processes
Stage 4: Measure and evidence control effectiveness
Stage 5: Adapt and improve continuously
```

---

# 5. Stage 1: Establish Visibility

## Objective

Create a reliable view of AI use across the enterprise.

The enterprise should know what AI capabilities exist, who owns them, what they are used for, and whether they present elevated risk.

## Key Activities

- create an AI inventory
- identify known AI use cases
- identify AI-enabled SaaS features
- identify embedded vendor AI
- identify copilots and productivity AI
- identify internal LLM applications
- identify RAG systems
- identify agents and automations
- identify developer AI tools
- identify customer-facing AI
- identify high-risk or regulated AI
- assign business owners
- record lifecycle status

## Minimum Outputs

```text
AI inventory
AI use case intake process
Initial owner mapping
Initial AI pattern classification
Initial lifecycle status
Initial list of high-risk AI use cases
```

## Questions to Answer

```text
What AI exists?
Who owns each AI use case?
Which business process does it support?
Is it internal, vendor, customer-facing, or agentic?
Does it use sensitive data?
Does it influence decisions?
Can it perform actions?
```

## Recommended Templates

```text
templates/ai-use-case-intake-template.md
templates/ai-inventory-record-template.md
```

## Common Mistakes

- only inventorying internally built AI
- ignoring AI-enabled SaaS
- ignoring embedded vendor AI
- assuming pilots do not need inventory
- failing to assign business owners
- tracking tools but not use cases

---

# 6. Stage 2: Establish Minimum Control

## Objective

Apply basic risk-tiered controls to known AI use cases.

The enterprise should move from simple visibility to minimum viable control.

## Key Activities

- assign risk tiers
- classify data sensitivity
- identify decision impact
- identify tool/action capability
- identify vendor involvement
- identify external exposure
- define required controls by tier
- document control gaps
- approve exceptions where required
- define minimum logging requirements
- define incident escalation path

## Minimum Outputs

```text
Risk tiering model
Risk assessments for high-risk AI
Control assessment for high-risk AI
Exception process
Minimum evidence requirements
AI incident escalation path
```

## Questions to Answer

```text
What risk tier applies?
What data does the AI process?
Does output influence decisions?
Can the AI trigger actions?
Does vendor AI process or retain data?
What controls are missing?
Who accepts residual risk?
```

## Recommended Templates

```text
templates/ai-risk-assessment-template.md
templates/ai-risk-tiering-template.md
templates/ai-control-assessment-template.md
templates/ai-exception-record-template.md
```

## Common Mistakes

- treating all AI as the same risk level
- over-controlling low-risk AI and under-controlling high-risk AI
- failing to document exceptions
- accepting risk without an accountable owner
- ignoring recoverability
- overlooking tool/action capability

---

# 7. Stage 3: Integrate Control Into Enterprise Processes

## Objective

Make AI control part of normal enterprise governance and technology delivery.

AI should not require a separate parallel bureaucracy. Existing processes should be extended to handle AI-specific risk.

## Key Activities

- integrate AI intake with enterprise architecture review
- integrate AI risk tiering with GRC
- integrate AI access review with IAM/PAM
- integrate AI data review with data governance
- integrate vendor AI review with vendor risk
- integrate AI assurance with SDLC and change management
- integrate AI events with monitoring where appropriate
- integrate AI incidents with incident response
- integrate AI evidence with audit processes

## Minimum Outputs

```text
AI governance workflow
Architecture review integration
Security review integration
Data governance integration
Vendor risk integration
IAM/PAM integration
Incident response integration
Audit evidence process
```

## Questions to Answer

```text
Where does AI review happen?
Who approves AI use?
Who approves data access?
Who reviews vendor AI?
Who reviews high-risk actions?
Who tests controls?
Where is evidence stored?
How are incidents handled?
```

## Recommended Templates

```text
templates/ai-architecture-decision-record-template.md
templates/ai-control-requirements-mapping-template.md
templates/ai-vendor-assessment-template.md
templates/ai-human-accountability-template.md
```

## Common Mistakes

- creating an AI board with no operational integration
- relying only on policy attestation
- leaving vendor AI outside AI governance
- failing to connect AI risk to IAM, data, SDLC, and incident response
- creating controls without evidence ownership

---

# 8. Stage 4: Measure and Evidence Control Effectiveness

## Objective

Prove that AI controls are not only designed, but operating.

The enterprise should be able to demonstrate control coverage, test results, findings, exceptions, and evidence completeness.

## Key Activities

- create assurance test plans
- perform control testing
- test prompt injection scenarios
- test data leakage scenarios
- test retrieval boundaries
- test tool/action controls
- test approval gates
- test logging completeness
- test evidence reconstruction
- test kill switches
- test rollback where required
- track findings
- create evidence packages
- report AI control metrics

## Minimum Outputs

```text
AI assurance test plans
Test results
Findings register
Remediation tracking
Evidence packages
Control metrics
Maturity reporting
```

## Questions to Answer

```text
Have controls been tested?
What failed?
What evidence exists?
Can we reconstruct AI activity?
Can we prove approval occurred?
Can we prove retrieval boundaries worked?
Can we prove tool actions were controlled?
Can we prove containment works?
```

## Recommended Templates

```text
templates/ai-assurance-test-plan-template.md
templates/ai-control-evidence-package-template.md
templates/ai-control-maturity-assessment-template.md
```

## Common Mistakes

- testing model output but not controls
- relying on vendor claims without evidence
- failing to test kill switches
- failing to test evidence reconstruction
- not tracking findings to closure
- accepting logs without checking usefulness

---

# 9. Stage 5: Adapt and Improve Continuously

## Objective

Create a feedback loop so the AI Control Architecture improves as AI adoption, incidents, vendors, models, and business use cases change.

## Key Activities

- review AI incidents and near misses
- review assurance findings
- review vendor AI changes
- review new AI patterns
- update requirements
- update templates
- update assurance test cases
- update incident playbooks
- update risk tiering criteria
- update maturity roadmap
- report trends to governance

## Minimum Outputs

```text
Control improvement backlog
Updated requirements
Updated assurance tests
Updated incident playbooks
Updated risk scenarios
Maturity roadmap
Governance reporting
```

## Questions to Answer

```text
What new failure patterns are emerging?
Which controls are failing?
Which vendors changed AI behavior?
Which exceptions are recurring?
Which incidents require architecture updates?
Which assurance tests should be added?
Which controls should be automated?
```

## Recommended Templates

```text
templates/risk-scenario-template.md
templates/requirement-template.md
templates/pillar-template.md
templates/ai-incident-record-template.md
```

## Common Mistakes

- treating AI control as a one-time project
- not updating controls after incidents
- not updating tests after new failure modes
- not reviewing vendor changes
- not retiring unused or unsafe AI use cases
- not using metrics to drive roadmap decisions

---

# 10. 30-Day Adoption Plan

The first 30 days should focus on visibility and minimum governance.

## Week 1: Establish Ownership and Scope

Actions:

```text
[ ] Identify executive sponsor.
[ ] Assign AI control architecture owner.
[ ] Define initial scope.
[ ] Confirm governance forum.
[ ] Agree on risk-tiering approach.
[ ] Agree on initial templates.
```

Outputs:

```text
Sponsor
Owner
Scope
Initial governance path
Initial risk-tiering model
```

---

## Week 2: Build Initial Inventory

Actions:

```text
[ ] Identify known AI use cases.
[ ] Identify copilots.
[ ] Identify AI-enabled SaaS.
[ ] Identify internal AI applications.
[ ] Identify RAG systems.
[ ] Identify agents or automations.
[ ] Identify developer AI tools.
[ ] Assign initial business owners.
```

Outputs:

```text
Initial AI inventory
Initial owner map
Initial pattern classification
```

---

## Week 3: Identify High-Risk AI

Actions:

```text
[ ] Review data sensitivity.
[ ] Review decision impact.
[ ] Review tool/action capability.
[ ] Review customer-facing exposure.
[ ] Review vendor processing.
[ ] Identify Tier 3, Tier 4, and Tier 5 candidates.
```

Outputs:

```text
High-risk AI list
Initial risk tiers
Priority review queue
```

---

## Week 4: Establish Minimum Controls

Actions:

```text
[ ] Define required controls by risk tier.
[ ] Start risk assessments for high-risk use cases.
[ ] Define exception process.
[ ] Define AI incident reporting path.
[ ] Define minimum evidence requirements.
[ ] Identify immediate control gaps.
```

Outputs:

```text
Minimum control baseline
Risk assessment backlog
Exception process
Incident escalation path
Evidence requirements
```

---

# 11. 60-Day Adoption Plan

The next 30 days should focus on control mapping and integration.

## Key Actions

```text
[ ] Complete risk assessments for priority AI use cases.
[ ] Complete vendor assessments for priority vendor AI.
[ ] Map data sources for high-risk AI.
[ ] Review identity and access for high-risk AI.
[ ] Define output and decision controls for decision-supporting AI.
[ ] Define tool and action controls for agentic or action-capable AI.
[ ] Define monitoring and evidence requirements.
[ ] Create evidence packages for high-risk AI.
[ ] Document exceptions and remediation plans.
[ ] Integrate AI review with architecture and security review.
```

## Outputs

```text
Risk assessments
Control assessments
Vendor assessments
Data boundary records
Identity/access reviews
Output/decision controls
Tool/action controls
Evidence packages
Exception register
Architecture review integration
```

---

# 12. 90-Day Adoption Plan

The next 30 days should focus on assurance, incident readiness, and reporting.

## Key Actions

```text
[ ] Create assurance test plans for high-risk AI.
[ ] Test retrieval boundaries.
[ ] Test prompt injection scenarios.
[ ] Test data leakage scenarios.
[ ] Test output validation.
[ ] Test tool/action controls.
[ ] Test approval gates.
[ ] Test logging completeness.
[ ] Test evidence reconstruction.
[ ] Test kill switches where required.
[ ] Conduct AI incident tabletop.
[ ] Report maturity and roadmap to governance.
```

## Outputs

```text
Assurance test results
Findings register
Remediation plan
Evidence reconstruction results
Kill switch test results
Incident tabletop results
Maturity assessment
Governance report
```

---

# 13. 6-Month Adoption Plan

By six months, AI control should be integrated into enterprise processes.

## Key Actions

```text
[ ] Integrate AI inventory with governance workflow.
[ ] Integrate AI control requirements with GRC.
[ ] Integrate AI access reviews with IAM/PAM.
[ ] Integrate AI data boundary review with data governance.
[ ] Integrate vendor AI review with vendor risk management.
[ ] Integrate AI assurance with SDLC and change management.
[ ] Integrate AI incident scenarios with incident response.
[ ] Define AI monitoring metrics.
[ ] Establish recurring exception review.
[ ] Establish recurring maturity reporting.
```

## Outputs

```text
Integrated AI governance process
GRC mapping
IAM/PAM integration
Data governance integration
Vendor risk integration
SDLC integration
Incident response integration
Monitoring metrics
Recurring reporting
```

---

# 14. 12-Month Adoption Plan

By twelve months, AI control should be measurable and improving.

## Key Actions

```text
[ ] Measure AI inventory completeness.
[ ] Measure control coverage by risk tier.
[ ] Measure assurance coverage.
[ ] Measure evidence completeness.
[ ] Measure open findings and remediation.
[ ] Measure open exceptions.
[ ] Measure AI incidents and near misses.
[ ] Review vendor AI changes.
[ ] Update risk scenarios.
[ ] Update assurance test catalogue.
[ ] Update control requirements.
[ ] Update maturity roadmap.
```

## Outputs

```text
AI control dashboard
Maturity assessment
Updated roadmap
Updated requirements
Updated assurance tests
Updated incident scenarios
Governance reporting
```

---

# 15. Operating Model

AI Control Architecture requires an operating model.

The operating model should define who does what.

## Key Roles

| Role | Responsibilities |
|---|---|
| Business owner | Owns business purpose, outcome, adoption, and business risk. |
| Technical owner | Owns implementation, integration, configuration, and technical remediation. |
| Data owner | Approves data access, classification, retention, and reuse. |
| Decision owner | Owns final decision where AI influences decisions. |
| Risk owner | Owns residual risk acceptance. |
| Security owner | Reviews security controls, identity, access, monitoring, and incident risks. |
| Privacy owner | Reviews personal data, retention, privacy rights, and legal obligations. |
| Legal owner | Reviews legal risk, privilege, contract, and regulated use. |
| Vendor owner | Owns vendor relationship, vendor evidence, and vendor risk actions. |
| Assurance owner | Owns test planning, findings, and assurance evidence. |
| Incident owner | Owns incident response, containment, recovery, and lessons learned. |
| Governance forum | Approves risk-tiering rules, exceptions, roadmap, and major decisions. |

---

# 16. Governance Forums

AI control does not always need a new committee.

It can be integrated into existing forums.

## Possible Forums

| Forum | AI Control Responsibilities |
|---|---|
| Enterprise architecture board | Reviews architecture decisions and control design. |
| Security architecture review | Reviews identity, access, data, tool, monitoring, and incident controls. |
| Data governance council | Reviews data sources, classification, retention, reuse, and retrieval boundaries. |
| Vendor risk committee | Reviews vendor AI processing, retention, logging, and incident support. |
| Privacy/legal review | Reviews personal data, regulated data, legal, and contractual impact. |
| Change advisory board | Reviews production changes, model changes, prompt changes, and high-risk deployments. |
| Risk committee | Reviews risk tiering, exceptions, residual risk, and control maturity. |
| Incident response forum | Reviews AI incidents, containment, recovery, and lessons learned. |
| Audit committee | Reviews evidence, maturity, findings, and assurance results. |

---

# 17. RACI Model

Use this starter RACI model and adapt it to the enterprise.

| Activity | Business | Tech | Data | Security | Legal/Privacy | Vendor | Risk/GRC | Assurance | Incident |
|---|---|---|---|---|---|---|---|---|---|
| AI use case intake | A | R | C | C | C | C | C | I | I |
| Risk tiering | A | C | C | C | C | C | R | I | I |
| Data boundary approval | C | C | A/R | C | C | C | I | I | I |
| Identity/access review | C | R | C | A/R | I | C | I | I | I |
| Vendor AI assessment | C | C | C | C | C | A/R | C | I | I |
| Control assessment | A | R | C | C | C | C | R | C | I |
| Assurance testing | C | R | C | C | C | C | I | A/R | I |
| Exception approval | A | C | C | C | C | C | R | I | I |
| Incident response | C | R | C | R | C | C | I | I | A/R |
| Post-incident review | C | C | C | C | C | C | R | C | A/R |

Legend:

```text
R = Responsible
A = Accountable
C = Consulted
I = Informed
```

---

# 18. Prioritization Model

Not every AI use case can be reviewed at the same depth immediately.

Prioritize based on risk.

## Highest Priority

Review first:

```text
[ ] Customer-facing AI
[ ] AI with regulated data
[ ] AI with customer or employee data
[ ] AI that influences decisions
[ ] AI that creates records
[ ] AI that can call tools or APIs
[ ] AI agents
[ ] AI that triggers workflows
[ ] AI with privileged access
[ ] Vendor AI with unclear data handling
[ ] AI in production
```

## Medium Priority

Review next:

```text
[ ] Internal productivity AI using enterprise data
[ ] RAG assistants using internal content
[ ] Developer AI tools
[ ] AI-enabled SaaS with limited impact
[ ] AI used for internal analysis
```

## Lower Priority

Review later, but still inventory:

```text
[ ] Public-data-only experimentation
[ ] Low-risk drafting
[ ] Low-risk summarization
[ ] Personal productivity AI with no enterprise data
```

---

# 19. Minimum Control Baseline by Tier

| Risk Tier | Minimum Control Baseline |
|---|---|
| Tier 1 | Inventory, owner, acceptable use guidance, basic data restriction. |
| Tier 2 | Tier 1 controls plus data source mapping, data classification, access boundary, vendor review where applicable. |
| Tier 3 | Tier 2 controls plus decision owner, output validation, human review, decision evidence, correction path, assurance testing. |
| Tier 4 | Tier 3 controls plus tool inventory, action classification, approval gates, tool/action logging, kill switch or revocation path, rollback assessment. |
| Tier 5 | Tier 4 controls plus enhanced assurance, full reconstructable evidence, incident tabletop, tested containment, risk acceptance, ongoing monitoring. |

---

# 20. Adoption Metrics

Track adoption using simple metrics.

## Inventory Metrics

- number of AI use cases inventoried
- percentage of AI use cases with business owner
- percentage of AI use cases risk-tiered
- number of embedded vendor AI features identified
- number of unreviewed AI use cases

## Control Metrics

- percentage of high-risk AI with completed risk assessment
- percentage of high-risk AI with completed control assessment
- percentage of AI use cases with data sources mapped
- percentage of AI use cases with identity model defined
- percentage of action-capable AI with tool inventory
- percentage of decision-supporting AI with decision owner

## Assurance Metrics

- percentage of high-risk AI with assurance testing completed
- number of open assurance findings
- percentage of findings closed on time
- number of failed or partial tests
- percentage of high-risk AI with evidence package

## Incident and Exception Metrics

- number of open AI exceptions
- number of expired AI exceptions
- number of AI incidents
- number of AI near misses
- percentage of high-risk AI with containment plan
- percentage of agents with tested kill switch

## Vendor Metrics

- number of vendor AI features assessed
- percentage of vendor AI with retention reviewed
- percentage of vendor AI with training/reuse reviewed
- percentage of vendor AI with logs reviewed
- number of vendor evidence gaps

---

# 21. Evidence Strategy

Evidence should be designed from the beginning.

For high-risk AI, evidence should answer:

```text
What was approved?
Who approved it?
What data was accessed?
What prompt or input was submitted?
What context was retrieved?
What output was produced?
What decision was influenced?
What tool was called?
What action occurred?
What exception existed?
What incident response occurred?
```

## Evidence Principles

- evidence should be mapped to risk tier
- evidence should have an owner
- evidence should have a retention period
- evidence should be protected
- evidence should support reconstruction
- evidence should be available for assurance, audit, and incident response

Related template:

```text
templates/ai-control-evidence-package-template.md
```

---

# 22. Incident Readiness Strategy

AI incident readiness should be built before incidents occur.

For high-risk AI, define:

```text
[ ] Incident scenarios
[ ] Severity model
[ ] Detection sources
[ ] Incident owner
[ ] Escalation path
[ ] Access revocation
[ ] Kill switch
[ ] Output containment
[ ] Workflow containment
[ ] Vendor escalation
[ ] Evidence preservation
[ ] Recovery path
[ ] Restart criteria
```

Related templates:

```text
templates/ai-incident-containment-recovery-template.md
templates/ai-incident-record-template.md
```

---

# 23. Common Adoption Anti-Patterns

## Anti-Pattern 1: Starting With Policy Only

A policy is useful, but policy alone does not control AI.

Policy must be translated into:

- requirements
- ownership
- evidence
- assurance
- incident response

---

## Anti-Pattern 2: Treating AI as a Security-Only Problem

AI control includes security, but it also includes:

- data governance
- legal
- privacy
- compliance
- business accountability
- vendor risk
- operational resilience
- decision governance
- audit evidence

---

## Anti-Pattern 3: Letting Vendors Define the Control Model

Vendors provide capabilities, but the enterprise remains accountable for use.

Vendor controls must be mapped into enterprise control requirements.

---

## Anti-Pattern 4: Over-Engineering Low-Risk AI

Low-risk AI should not be burdened with Tier 5 controls.

Use risk tiering to avoid unnecessary friction.

---

## Anti-Pattern 5: Under-Controlling Agents

Agents are different from passive AI.

If AI can act, it needs identity, boundaries, approval gates, logs, kill switches, and recovery paths.

---

## Anti-Pattern 6: Measuring Adoption Instead of Control

High AI usage does not mean high AI maturity.

Measure control coverage, evidence, assurance, exceptions, and incidents.

---

# 24. Success Criteria

The adoption program is working when the enterprise can say:

```text
We know what AI exists.
We know who owns it.
We know what risk tier applies.
We know what data it can access.
We know what decisions it influences.
We know what tools and actions it can use.
We know what controls apply.
We know what evidence exists.
We know how to test it.
We know how to stop it.
We know how to recover when it fails.
```

---

# 25. Summary

The adoption playbook turns the AI Control Architecture into an operating approach.

The recommended path is:

```text
Visibility
    ↓
Minimum control
    ↓
Enterprise integration
    ↓
Evidence and assurance
    ↓
Continuous adaptation
```

The enterprise should start small, prioritize high-risk AI, integrate with existing processes, and build evidence from the beginning.

The goal is simple:

```text
Adopt AI faster without losing control.
```