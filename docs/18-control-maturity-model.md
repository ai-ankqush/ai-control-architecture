# Control Maturity Model

This document defines the maturity model for the AI Control Architecture.

The purpose of the maturity model is to help organizations assess how well they control AI across the ten architecture pillars, identify gaps, prioritize improvement, and build a practical roadmap from ad hoc AI use to adaptive AI control.

AI control maturity is not measured by how many AI products an enterprise has purchased.

It is measured by whether the enterprise can answer:

```text
What AI exists?
What can AI see?
What can AI decide?
What can AI do?
Who is accountable?
What evidence exists?
How is failure contained?
```

---

# 1. Maturity Levels

The AI Control Architecture uses five maturity levels.

| Level | Name | Summary |
|---|---|---|
| Level 1 | Ad Hoc | AI use is fragmented, informal, reactive, and inconsistently controlled. |
| Level 2 | Visible | AI use is becoming visible, but controls are still partial, manual, or uneven. |
| Level 3 | Integrated | AI controls are embedded into enterprise processes and ownership is defined. |
| Level 4 | Measurable | AI controls are tested, evidenced, measured, monitored, and reported. |
| Level 5 | Adaptive | AI controls continuously improve based on monitoring, incidents, assurance, and change. |

---

# 2. Level 1: Ad Hoc

At Level 1, AI adoption is happening faster than AI control.

AI use may be useful, innovative, and business-driven, but the enterprise does not yet have a consistent way to see, classify, govern, test, evidence, or contain AI.

## Characteristics

- AI use cases are not consistently inventoried.
- Business ownership is unclear.
- AI-enabled SaaS features may be enabled without review.
- Sensitive data exposure is not consistently assessed.
- AI identity and access models are not clearly defined.
- Prompt and input risks are handled informally.
- AI outputs may be used without validation.
- Tool or action capability may not be controlled.
- Human accountability is assumed but not assigned.
- Assurance testing is limited or absent.
- Logging and evidence are inconsistent.
- AI incident response is not defined.

## Typical Symptoms

- Teams use AI before governance knows about it.
- Vendor AI features are enabled by default.
- Users copy sensitive data into AI tools without clear rules.
- AI output is copied into reports, emails, tickets, or records without review.
- Agents or automations are piloted without kill switches.
- No one can reconstruct what AI saw, produced, or triggered.
- Incidents are handled as general technology issues rather than AI control failures.

## Level 1 Goal

The goal at Level 1 is to establish minimum visibility.

The enterprise should first identify what AI exists and who owns it.

---

# 3. Level 2: Visible

At Level 2, AI use is becoming visible.

The enterprise has started to identify AI use cases, assign owners, classify risk, and define basic controls. However, implementation is still inconsistent and often manual.

## Characteristics

- AI inventory exists or is being established.
- High-risk AI use cases are identified.
- Business owners are assigned for known AI use cases.
- Risk tiering model exists.
- Basic vendor AI review is performed.
- Data sensitivity is assessed for some use cases.
- Output and decision impact are considered.
- Tool/action capability is identified where obvious.
- Basic logging expectations are defined.
- Exceptions are documented for known gaps.
- Incident escalation path exists for high-risk AI.

## Typical Symptoms

- Known AI use cases are tracked, but shadow AI remains.
- Risk tiering exists but is not yet consistently applied.
- Control reviews occur for major AI initiatives but not all AI-enabled SaaS.
- Some teams use templates while others use informal review.
- Evidence exists but is scattered.
- Incident response is known for high-risk use cases but not tested.

## Level 2 Goal

The goal at Level 2 is to move from unknown AI use to known AI use.

The enterprise should be able to identify AI use cases, owners, risk tiers, and major control gaps.

---

# 4. Level 3: Integrated

At Level 3, AI controls are integrated into enterprise processes.

AI review is no longer a standalone activity. It becomes part of architecture, security, data governance, vendor risk, SDLC, GRC, monitoring, and incident response processes.

## Characteristics

- AI inventory is maintained as part of governance.
- Risk tiering drives required controls.
- AI intake is integrated with architecture and security review.
- AI identity and access are reviewed through IAM or PAM processes.
- Data boundaries are reviewed through data governance.
- Vendor AI is reviewed through vendor risk and contract processes.
- Output and decision controls are defined for decision-supporting AI.
- Tool and action controls are defined for agents and action-capable AI.
- Human accountability is documented.
- Assurance testing is performed for higher-risk AI.
- Monitoring and evidence requirements are defined by risk tier.
- AI incident response is integrated with existing incident processes.

## Typical Symptoms

- Teams know how to submit AI use cases for review.
- Required controls are linked to risk tier.
- Review forums understand AI-specific risks.
- Vendor AI features are not enabled without review.
- Architecture decisions are documented.
- Exceptions are time-bound and owned.
- High-risk AI use cases have evidence packages.

## Level 3 Goal

The goal at Level 3 is to make AI control part of normal enterprise control operation.

The enterprise should not need a special process every time AI appears. Existing processes should know how to handle AI.

---

# 5. Level 4: Measurable

At Level 4, AI controls are measured, tested, evidenced, and reported.

The enterprise can prove that controls exist and operate. It can measure coverage, identify gaps, test control effectiveness, and report maturity to governance, risk, audit, and leadership.

## Characteristics

- AI inventory completeness is measured.
- AI use cases are risk-tiered and reviewed.
- Control coverage is measured by pillar and risk tier.
- Assurance testing is performed and evidenced.
- Findings are tracked to remediation or risk acceptance.
- Logging completeness is tested.
- Evidence reconstruction is tested for high-risk AI.
- Kill switches and rollback paths are tested where required.
- Metrics are reported to governance forums.
- Vendor AI evidence gaps are tracked.
- Exceptions are monitored for expiry and remediation.
- Incident metrics and near misses inform control improvement.

## Typical Symptoms

- Dashboards show AI inventory, risk tiers, exceptions, findings, and incidents.
- Assurance testing produces repeatable evidence.
- Audit can review AI control operation.
- Control gaps have owners and due dates.
- High-risk AI use cases have reconstructable evidence.
- Leadership can see maturity trends over time.

## Level 4 Goal

The goal at Level 4 is to prove control effectiveness.

The enterprise should be able to demonstrate not only that controls are designed, but that they operate.

---

# 6. Level 5: Adaptive

At Level 5, AI control is adaptive.

The enterprise continuously improves AI controls based on changes in AI use, incidents, assurance findings, vendor changes, regulatory expectations, business adoption, and emerging failure modes.

## Characteristics

- AI control architecture is continuously improved.
- Monitoring signals update control priorities.
- Incident lessons update requirements, tests, and playbooks.
- Assurance findings update control design.
- Vendor changes trigger review automatically.
- High-risk AI use cases are continuously monitored.
- Regression testing is triggered by material AI changes.
- Evidence collection is automated where appropriate.
- AI control metrics inform strategic roadmap decisions.
- Risk-tiering and control requirements evolve with enterprise AI adoption.
- Governance can respond quickly to new AI patterns.

## Typical Symptoms

- The enterprise detects new AI risk patterns early.
- Control requirements are updated after incidents and near misses.
- AI assurance testing evolves with new attack and failure patterns.
- Monitoring and evidence collection improve over time.
- Governance decisions are based on current risk and control data.
- AI architecture remains vendor-neutral while adapting to new technologies.

## Level 5 Goal

The goal at Level 5 is continuous adaptation.

The enterprise should be able to control current AI use while adapting to future AI patterns.

---

# 7. Maturity by Pillar

The following sections describe maturity expectations across the ten AI Control Architecture pillars.

---

# 8. Pillar 1: AI Inventory and Classification

## Level 1: Ad Hoc

- AI use cases are not consistently recorded.
- Embedded vendor AI is unknown.
- Business ownership is unclear.
- Risk tiering is not applied.

## Level 2: Visible

- AI inventory exists for known use cases.
- High-risk use cases are identified.
- Owners are assigned for major AI capabilities.
- Basic risk classification is performed.

## Level 3: Integrated

- AI inventory is part of governance.
- AI intake is integrated with architecture, security, vendor, and data review.
- Risk tier drives required controls.
- Lifecycle status is tracked.

## Level 4: Measurable

- Inventory completeness is measured.
- Unreviewed AI use is tracked.
- Risk-tier distribution is reported.
- Inventory review cadence is defined.

## Level 5: Adaptive

- Inventory updates are triggered by vendor, platform, procurement, and usage signals.
- Shadow AI discovery improves over time.
- Inventory data informs governance, assurance, and roadmap decisions.

---

# 9. Pillar 2: AI Identity and Access Control

## Level 1: Ad Hoc

- AI identity is not clearly defined.
- AI may inherit user or service access without review.
- Delegated authority is unclear.
- Revocation path is not documented.

## Level 2: Visible

- AI identity models are identified for major use cases.
- Access scope is reviewed for high-risk AI.
- Service accounts or vendor identities are documented where known.
- Basic access approval exists.

## Level 3: Integrated

- AI access review is integrated with IAM/PAM.
- Delegated authority is documented.
- Least privilege is applied.
- Revocation paths are defined.

## Level 4: Measurable

- AI access reviews are evidenced.
- Privileged AI access is tracked.
- Access violations are monitored.
- Revocation tests are performed where required.

## Level 5: Adaptive

- AI access adapts based on risk, usage, incidents, and lifecycle status.
- Access anomalies trigger review.
- Identity and authority models evolve with agentic AI and tool use.

---

# 10. Pillar 3: Data Boundary Control

## Level 1: Ad Hoc

- AI data sources are not consistently mapped.
- Sensitive data exposure is not systematically assessed.
- Retrieval boundaries are unclear.
- Retention and reuse are unknown.

## Level 2: Visible

- Data sources are documented for high-risk AI.
- Data classification is considered.
- Vendor data processing is reviewed for major use cases.
- Basic sensitive data restrictions exist.

## Level 3: Integrated

- Data governance reviews AI data access.
- Retrieval boundaries are defined.
- Training, reuse, and retention restrictions are documented.
- Data owner approvals are captured.

## Level 4: Measurable

- Data boundary tests are performed.
- Retrieval leakage tests are evidenced.
- Data access logs are reviewed.
- Sensitive data exposure findings are tracked.

## Level 5: Adaptive

- Data boundaries adjust based on classification, usage, incidents, and policy changes.
- Sensitive data exposure monitoring improves over time.
- AI data control is integrated with enterprise data governance.

---

# 11. Pillar 4: Prompt and Input Control

## Level 1: Ad Hoc

- Users decide what to enter into AI tools.
- Prohibited inputs are not clearly defined.
- Prompt injection risk is not assessed.
- System prompts are not controlled.

## Level 2: Visible

- Basic acceptable use guidance exists.
- Sensitive input restrictions are defined for known use cases.
- Prompt injection is recognized as a risk.
- System prompts are owned for some systems.

## Level 3: Integrated

- Input controls are designed by risk tier.
- System prompts are versioned and reviewed.
- External and untrusted inputs are treated as risk surfaces.
- Prompt changes are controlled.

## Level 4: Measurable

- Prompt injection testing is performed.
- Input policy violations are monitored.
- Prompt changes are evidenced.
- Context isolation is tested where required.

## Level 5: Adaptive

- Input controls evolve based on incidents, attack patterns, and assurance findings.
- Prompt injection tests are updated regularly.
- Prompt and context controls are integrated into SDLC and monitoring.

---

# 12. Pillar 5: Output and Decision Control

## Level 1: Ad Hoc

- AI output is used based on user judgment.
- Output validation is informal.
- AI recommendations may become decisions.
- Generated records may lack provenance.

## Level 2: Visible

- Output types are identified.
- Decision impact is assessed for major use cases.
- Human review is required for some high-risk outputs.
- Customer-facing outputs receive additional attention.

## Level 3: Integrated

- Output validation rules are defined.
- AI recommendation is separated from final decision.
- Decision owners are assigned.
- Generated records have provenance and correction paths.

## Level 4: Measurable

- Output validation is tested.
- Decision evidence is retained.
- Output quality metrics are tracked.
- Reviewer override and rejection rates are monitored.

## Level 5: Adaptive

- Output controls adapt based on quality trends, incidents, and business impact.
- Decision controls improve based on assurance and feedback.
- Generated record governance is continuously refined.

---

# 13. Pillar 6: Tool and Action Control

## Level 1: Ad Hoc

- AI tool access is not consistently inventoried.
- Action risk is not classified.
- Approval gates are informal.
- Kill switches may not exist.

## Level 2: Visible

- AI-accessible tools are identified for high-risk use cases.
- High-risk actions are recognized.
- Basic approval requirements exist.
- Some tool/action logs are available.

## Level 3: Integrated

- Tool access is approved and least privilege.
- Actions are classified by risk.
- Approval gates are enforced.
- Kill switches and rollback paths are defined.

## Level 4: Measurable

- Tool/action tests are performed.
- Approval bypass testing is evidenced.
- Tool call logs are monitored.
- Kill switches and rollback paths are tested.

## Level 5: Adaptive

- Tool and action boundaries adjust based on risk, usage, incidents, and behavior.
- Abnormal tool use triggers automated containment where appropriate.
- Agentic action control improves continuously.

---

# 14. Pillar 7: Human Accountability Model

## Level 1: Ad Hoc

- Accountability is assumed.
- Owners are unclear.
- Human review may be ceremonial.
- Exceptions and incidents lack clear ownership.

## Level 2: Visible

- Business owners are assigned for known AI use cases.
- Review roles are documented for high-risk outputs.
- Decision owners are identified where obvious.
- Escalation paths exist for major use cases.

## Level 3: Integrated

- Accountability model is documented.
- Decision owners, approvers, reviewers, and risk owners are assigned.
- RACI is defined for high-risk AI.
- Exceptions are owned and time-bound.

## Level 4: Measurable

- Accountability evidence is retained.
- Review and approval records are tested.
- Exceptions and risk acceptances are tracked.
- Ownership gaps are reported.

## Level 5: Adaptive

- Accountability models update as AI autonomy, vendor dependency, and decision impact change.
- Human review effectiveness is assessed and improved.
- Accountability lessons from incidents update governance.

---

# 15. Pillar 8: AI Assurance and Testing

## Level 1: Ad Hoc

- AI testing is informal.
- Vendor claims may be accepted without evidence.
- Control effectiveness is not tested.
- Regression testing is not defined.

## Level 2: Visible

- High-risk AI use cases are reviewed.
- Some pre-deployment testing occurs.
- Prompt injection and data leakage are recognized.
- Findings are documented informally.

## Level 3: Integrated

- Assurance requirements are defined by risk tier.
- Testing is integrated into deployment and change processes.
- Findings are tracked.
- Vendor assurance is reviewed.

## Level 4: Measurable

- Test coverage is measured.
- Findings are tracked to closure or acceptance.
- Regression testing is performed after material changes.
- Assurance evidence is retained.

## Level 5: Adaptive

- Test catalogues evolve based on incidents, emerging risks, and new AI patterns.
- Assurance results update requirements and controls.
- High-risk AI receives continuous or periodic assurance.

---

# 16. Pillar 9: Monitoring, Logging, and Evidence

## Level 1: Ad Hoc

- AI logs are inconsistent or unavailable.
- Evidence is scattered.
- Activity cannot be reconstructed.
- Vendor logs may be unknown.

## Level 2: Visible

- Logging needs are identified for high-risk AI.
- Basic usage evidence exists.
- Evidence owners are known for some use cases.
- Incident evidence needs are understood.

## Level 3: Integrated

- Logging requirements are defined by risk tier.
- AI events integrate with monitoring or GRC where appropriate.
- Evidence retention is defined.
- Approval and exception evidence is retained.

## Level 4: Measurable

- Logging completeness is tested.
- Evidence packages are produced.
- Reconstructability is tested for high-risk AI.
- Monitoring alerts are tracked.

## Level 5: Adaptive

- Evidence collection improves based on incidents, audits, and assurance findings.
- Monitoring rules adapt to new AI risk patterns.
- AI events correlate with identity, data, tool, and workflow events.

---

# 17. Pillar 10: Incident Containment and Recovery

## Level 1: Ad Hoc

- AI incidents are not clearly defined.
- Containment paths are unclear.
- Evidence may be lost.
- Recovery is improvised.

## Level 2: Visible

- AI incident scenarios are identified.
- Escalation paths exist for high-risk AI.
- Basic containment options are documented.
- Vendor escalation paths are known.

## Level 3: Integrated

- AI incident response integrates with enterprise incident response.
- Kill switches are defined for agents and action-capable AI.
- Evidence preservation is defined.
- Recovery and correction paths are documented.

## Level 4: Measurable

- Containment tests are performed.
- Kill switches are tested.
- Incident tabletop exercises are conducted.
- Recovery and evidence preservation are validated.

## Level 5: Adaptive

- Incident lessons update controls, tests, monitoring, and playbooks.
- Containment becomes faster and more automated where appropriate.
- Incident patterns inform architecture roadmap.

---

# 18. Maturity Assessment Method

A maturity assessment should evaluate each pillar independently.

Do not average maturity too quickly.

A high score in one pillar does not compensate for a critical weakness in another.

For example:

- strong AI inventory does not compensate for weak tool/action control
- strong vendor review does not compensate for missing evidence
- strong output validation does not compensate for no incident containment
- strong assurance testing does not compensate for unclear accountability

## Recommended Assessment Steps

1. Define assessment scope.
2. Identify AI use cases in scope.
3. Review evidence for each pillar.
4. Assign current maturity level per pillar.
5. Define target maturity level per pillar.
6. Identify gaps.
7. Prioritize gaps based on risk.
8. Define roadmap actions.
9. Assign owners and due dates.
10. Review maturity periodically.

Related template:

```text
templates/ai-control-maturity-assessment-template.md
```

---

# 19. Maturity Targets by Organization Stage

Different organizations may need different target maturity levels.

| Organization Stage | Suggested Target |
|---|---|
| Early AI adoption | Level 2 for all pillars, Level 3 for high-risk AI |
| Scaling AI adoption | Level 3 for all pillars, Level 4 for high-risk AI |
| Regulated enterprise | Level 3 minimum, Level 4 for sensitive or regulated AI |
| Heavy agentic AI adoption | Level 4 for tool/action, logging, assurance, and incident containment |
| High-impact autonomous AI | Level 4 to Level 5 for all relevant pillars |

---

# 20. Minimum Target State

At minimum, an enterprise should aim for:

```text
Level 2 across all pillars
Level 3 for high-risk AI use cases
Level 4 for agentic, regulated, or action-capable AI
```

This means the enterprise should at least have:

- AI inventory
- assigned owners
- risk tiering
- data source mapping
- identity model
- output and decision classification
- tool/action classification
- accountability model
- assurance process
- logging requirements
- incident containment path

---

# 21. Maturity Metrics

Useful maturity metrics include:

| Metric | Purpose |
|---|---|
| Number of AI use cases inventoried | Measures AI visibility. |
| Percentage of AI use cases with business owners | Measures accountability coverage. |
| Percentage of AI use cases risk-tiered | Measures classification coverage. |
| Percentage of high-risk AI use cases reviewed | Measures governance coverage. |
| Percentage of AI use cases with data sources mapped | Measures data boundary coverage. |
| Percentage of AI use cases with identity model defined | Measures identity control coverage. |
| Percentage of decision-supporting AI with decision owner assigned | Measures decision accountability. |
| Percentage of action-capable AI with tool/action controls | Measures action control coverage. |
| Percentage of high-risk AI with assurance completed | Measures testing coverage. |
| Percentage of high-risk AI with logging implemented | Measures evidence coverage. |
| Percentage of high-risk AI with incident containment defined | Measures readiness. |
| Number of open AI exceptions | Measures unresolved control gaps. |
| Number of AI incidents or near misses | Measures operational risk. |
| Percentage of AI findings closed on time | Measures remediation discipline. |

---

# 22. Maturity Roadmap

A practical maturity roadmap may look like this.

## Phase 1: Establish Visibility

- create AI inventory
- identify known AI use cases
- identify embedded vendor AI
- assign business owners
- define AI risk tiers
- identify high-risk use cases

## Phase 2: Establish Control Baseline

- define minimum controls by risk tier
- map data sources
- define identity model
- define output and decision controls
- identify tool/action capability
- define accountability model
- create exception process

## Phase 3: Establish Evidence and Assurance

- define logging requirements
- create evidence package format
- test high-risk AI controls
- review vendor evidence
- track findings
- define incident scenarios

## Phase 4: Integrate Enterprise Processes

- integrate with architecture review
- integrate with IAM/PAM
- integrate with data governance
- integrate with SDLC
- integrate with vendor risk
- integrate with GRC
- integrate with incident response
- integrate with audit

## Phase 5: Measure and Adapt

- report AI control metrics
- monitor policy violations
- conduct periodic assurance
- review exceptions
- learn from incidents
- update requirements and controls
- update roadmap based on risk

---

# 23. Maturity Anti-Patterns

Avoid these maturity anti-patterns.

## Anti-Pattern 1: Product-Led Control

The organization assumes buying an AI security product equals AI control maturity.

Why this fails:

- products do not define accountability
- products do not classify business decision impact
- products do not automatically create evidence
- products do not replace architecture

## Anti-Pattern 2: Policy-Only Governance

The organization publishes an AI policy but does not implement controls.

Why this fails:

- users may not follow policy
- vendors may behave differently
- agents may act outside policy
- evidence may not exist

## Anti-Pattern 3: Inventory Without Control

The organization tracks AI use cases but does not map controls to risk.

Why this fails:

- visibility does not equal control
- high-risk AI may remain under-controlled
- gaps may not be remediated

## Anti-Pattern 4: Human-in-the-Loop Theater

The organization requires human review but reviewers lack time, context, authority, or accountability.

Why this fails:

- review becomes ceremonial
- AI recommendations become decisions
- accountability remains unclear

## Anti-Pattern 5: Logging Without Reconstructability

The organization collects logs but cannot reconstruct what happened.

Why this fails:

- incident response is weak
- audit evidence is incomplete
- control operation cannot be proven

## Anti-Pattern 6: Vendor Trust Without Evidence

The organization trusts vendor AI claims without evidence, configuration review, or contract clarity.

Why this fails:

- vendor retention may be unclear
- logs may be unavailable
- AI features may change
- incident support may be limited

---

# 24. Summary

AI control maturity is the enterprise’s ability to make AI visible, bounded, accountable, testable, observable, and containable.

The maturity journey moves through five stages:

```text
Ad Hoc
    ↓
Visible
    ↓
Integrated
    ↓
Measurable
    ↓
Adaptive
```

The goal is not to slow AI adoption.

The goal is to make AI adoption safe, explainable, controllable, and resilient.