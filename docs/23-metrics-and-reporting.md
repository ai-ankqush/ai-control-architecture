# Metrics and Reporting

This document defines the metrics and reporting model for the AI Control Architecture.

The purpose is to help organizations measure AI control coverage, control maturity, evidence completeness, assurance results, exceptions, incidents, and improvement over time.

AI control reporting should not measure AI adoption alone.

High AI usage does not mean high AI control maturity.

The enterprise should measure whether AI is:

```text
Visible
Owned
Risk-tiered
Controlled
Tested
Evidenced
Monitored
Containable
Improving
```

---

# 1. Purpose

The metrics and reporting model helps answer:

```text
What AI exists?
Who owns it?
Which AI use cases are high risk?
Which controls are implemented?
Which controls are missing?
Which AI use cases have been tested?
Which evidence exists?
Which exceptions are open?
Which incidents occurred?
Which vendors create evidence gaps?
Where should leadership invest next?
```

Metrics should support action.

A metric that does not drive ownership, remediation, prioritization, or governance decision-making should be reviewed.

---

# 2. Reporting Principles

## Principle 1: Measure Control, Not Just Adoption

Do not report only:

```text
Number of AI users
Number of prompts
Number of AI tools deployed
Number of copilots enabled
```

Also report:

```text
Number of AI use cases inventoried
Percentage with owners
Percentage risk-tiered
Percentage with required controls
Percentage with assurance completed
Percentage with evidence package
Percentage with containment path
```

---

## Principle 2: Report by Risk Tier

Metrics should distinguish low-risk AI from high-risk AI.

A missing control on a Tier 1 drafting assistant is not the same as a missing control on a Tier 5 autonomous or regulated AI use case.

Report separately for:

```text
Tier 1: Low-risk productivity or public-data use
Tier 2: Internal productivity with enterprise data
Tier 3: Decision-supporting AI
Tier 4: Action-capable AI
Tier 5: High-impact autonomous or regulated AI
```

---

## Principle 3: Report by Pattern

Different AI patterns create different control issues.

Report metrics by AI pattern where useful:

```text
Copilot
RAG system
Internal LLM application
AI-enabled SaaS
Embedded vendor AI
Agent
Customer-facing AI
Developer AI tool
Security operations AI
Decision-supporting AI
Action-capable AI
```

---

## Principle 4: Separate Design, Operation, and Evidence

A control may be:

```text
Designed
Implemented
Operating
Tested
Evidenced
Effective
```

Do not treat these as the same.

For example, a logging requirement may be designed but not yet producing useful evidence.

---

## Principle 5: Metrics Must Have Owners

Every reported metric should have:

```text
Metric owner
Data source
Reporting frequency
Target
Threshold
Action when outside threshold
```

---

# 3. Reporting Audiences

Different audiences need different reports.

| Audience | Reporting Focus |
|---|---|
| Executive leadership | Risk posture, high-risk AI, incidents, maturity, investment needs |
| AI governance forum | Intake, risk tiering, control gaps, exceptions, roadmap |
| Enterprise architecture | architecture decisions, pattern adoption, control design gaps |
| Security leadership | identity, access, tool/action risk, monitoring, incidents |
| Data governance | data sources, classification, retrieval boundaries, leakage findings |
| Privacy/legal | personal data, regulated data, vendor terms, customer-facing AI |
| Vendor risk | vendor AI features, retention, training/reuse, evidence gaps |
| Assurance/audit | control testing, evidence packages, findings, remediation |
| Incident response | AI incidents, containment readiness, kill switch tests, lessons learned |
| Business owners | use case readiness, open actions, residual risk, approvals |

---

# 4. Executive Dashboard

The executive dashboard should be short and risk-focused.

## Recommended Executive Metrics

| Metric | Purpose |
|---|---|
| Total AI use cases inventoried | Shows visibility. |
| Percentage of AI use cases with business owner | Shows accountability. |
| Percentage of AI use cases risk-tiered | Shows classification coverage. |
| Number of Tier 3, Tier 4, and Tier 5 AI use cases | Shows high-risk AI population. |
| Percentage of high-risk AI with completed control assessment | Shows control review coverage. |
| Percentage of high-risk AI with assurance completed | Shows testing coverage. |
| Percentage of high-risk AI with evidence package | Shows audit and incident readiness. |
| Number of open critical/high AI findings | Shows unresolved control weakness. |
| Number of open AI exceptions | Shows accepted control gaps. |
| Number of AI incidents and near misses | Shows operational risk. |
| AI control maturity level | Shows overall maturity. |
| Top five AI control risks | Shows where leadership attention is needed. |

## Executive Dashboard Format

```text
AI Control Executive Dashboard

Reporting period:
Prepared by:
Overall status:

1. AI visibility
2. High-risk AI exposure
3. Control readiness
4. Assurance and evidence
5. Exceptions and findings
6. Incidents and near misses
7. Vendor AI risk
8. Maturity trend
9. Key decisions required
10. Investment or resource needs
```

---

# 5. Governance Dashboard

The governance dashboard should support operational decision-making.

## Recommended Governance Metrics

| Metric | Purpose |
|---|---|
| New AI intake requests | Shows incoming demand. |
| AI use cases awaiting review | Shows backlog. |
| AI use cases approved this period | Shows throughput. |
| AI use cases rejected or deferred | Shows control decisions. |
| AI use cases approved with conditions | Shows conditional risk. |
| AI use cases by lifecycle stage | Shows maturity of adoption. |
| AI use cases by risk tier | Shows risk distribution. |
| AI use cases by pattern | Shows control pattern distribution. |
| Open AI exceptions by age | Shows unresolved risk. |
| Open findings by severity | Shows remediation priority. |
| Overdue remediation actions | Shows accountability issues. |
| Upcoming review dates | Shows review discipline. |

## Governance Reporting Questions

The governance report should answer:

```text
Which AI use cases need decisions?
Which high-risk use cases are blocked?
Which exceptions are overdue?
Which findings need escalation?
Which vendors create unresolved risk?
Which AI use cases should be suspended, restricted, or retired?
```

---

# 6. Inventory Metrics

Inventory metrics measure AI visibility.

## Core Inventory Metrics

| Metric | Definition | Target |
|---|---|---|
| AI use cases inventoried | Count of AI capabilities recorded in inventory. | Increasing until complete |
| AI use cases with business owner | Percentage with assigned business owner. | 100% |
| AI use cases with technical owner | Percentage with assigned technical owner where required. | 100% for technical AI |
| AI use cases with lifecycle status | Percentage with current lifecycle status. | 100% |
| AI use cases with pattern classification | Percentage classified by AI pattern. | 100% |
| Embedded vendor AI features identified | Count of known embedded vendor AI features. | Increasing during discovery |
| Unreviewed AI use cases | Count of known AI use cases not yet reviewed. | Decreasing |
| Retired AI use cases | Count retired from active use. | Tracked |

## Inventory Breakdown

Report inventory by:

```text
Business unit
Function
Owner
AI pattern
Risk tier
Lifecycle stage
Vendor involvement
Customer-facing status
Action capability
Decision impact
```

## Inventory Warning Indicators

Investigate when:

```text
AI use cases have no owner.
AI use cases have unknown lifecycle status.
AI-enabled SaaS is not recorded.
Vendor AI features are discovered outside review.
High-risk AI is missing from the inventory.
```

---

# 7. Risk Tier Metrics

Risk tier metrics measure whether AI use cases are classified consistently.

## Core Risk Metrics

| Metric | Definition | Target |
|---|---|---|
| Percentage of AI use cases risk-tiered | AI use cases with assigned risk tier. | 100% |
| Number of Tier 1 use cases | Low-risk productivity/public-data AI. | Tracked |
| Number of Tier 2 use cases | Internal productivity with enterprise data. | Tracked |
| Number of Tier 3 use cases | Decision-supporting AI. | Tracked |
| Number of Tier 4 use cases | Action-capable AI. | Tracked |
| Number of Tier 5 use cases | High-impact autonomous or regulated AI. | Tracked |
| AI use cases with unknown risk tier | Use cases without classification. | 0 |
| Risk tier changes this period | Count of risk tier upgrades/downgrades. | Tracked |
| High-risk AI awaiting review | Tier 3-5 use cases not yet fully reviewed. | Decreasing |

## Risk Distribution Report

```text
Tier 1:
Tier 2:
Tier 3:
Tier 4:
Tier 5:
Unknown:
```

## Risk Tier Warning Indicators

Investigate when:

```text
A use case has unknown risk tier.
A customer-facing use case is Tier 1 or Tier 2 without rationale.
An action-capable use case is below Tier 4.
A regulated or high-impact use case is below Tier 5.
Risk tier has not been reviewed after major change.
```

---

# 8. Control Coverage Metrics

Control coverage metrics measure whether required controls are defined and implemented.

## Pillar Coverage Metrics

| Pillar | Example Metric |
|---|---|
| AI inventory and classification | Percentage of use cases inventoried and risk-tiered. |
| AI identity and access control | Percentage with defined AI identity model. |
| Data boundary control | Percentage with data sources mapped and classified. |
| Prompt and input control | Percentage with allowed/prohibited inputs defined. |
| Output and decision control | Percentage with output classification and validation rule. |
| Tool and action control | Percentage with tool inventory and action classification. |
| Human accountability model | Percentage with accountable business owner and decision owner where required. |
| AI assurance and testing | Percentage with assurance completed where required. |
| Monitoring, logging, and evidence | Percentage with logging requirements and evidence location defined. |
| Incident containment and recovery | Percentage with containment path defined and tested where required. |

## Control Coverage by Tier

Report control coverage by risk tier.

```text
Tier 1 control coverage:
Tier 2 control coverage:
Tier 3 control coverage:
Tier 4 control coverage:
Tier 5 control coverage:
```

## Control Coverage Warning Indicators

Investigate when:

```text
Tier 3 AI lacks decision owner.
Tier 4 AI lacks tool/action control.
Tier 5 AI lacks evidence package.
Action-capable AI lacks kill switch.
Vendor AI lacks vendor assessment.
Sensitive data AI lacks data boundary.
```

---

# 9. Identity and Access Metrics

Identity metrics measure AI authority control.

## Core Identity Metrics

| Metric | Purpose |
|---|---|
| Percentage of AI use cases with identity model defined | Measures authority clarity. |
| Number of AI identities | Measures AI actor footprint. |
| Number of agent identities | Measures agentic AI authority. |
| Number of AI service accounts | Measures non-human access. |
| Percentage of AI identities reviewed | Measures access governance. |
| Number of AI identities with privileged access | Measures high-risk access. |
| Percentage with revocation path defined | Measures containment readiness. |
| Number of failed or blocked AI access attempts | Measures policy enforcement. |
| Number of AI access exceptions | Measures access control gaps. |

## Identity Warning Indicators

Investigate when:

```text
AI access uses shared accounts.
AI service accounts are over-permissioned.
AI has privileged access without approval.
Agent identity cannot be disabled quickly.
Vendor AI identity model is unknown.
AI activity cannot be distinguished from human activity.
```

---

# 10. Data Boundary Metrics

Data metrics measure whether AI data access is controlled.

## Core Data Metrics

| Metric | Purpose |
|---|---|
| Percentage of AI use cases with data sources mapped | Measures data visibility. |
| Percentage with highest data classification recorded | Measures sensitivity awareness. |
| Percentage with data owner approval | Measures accountability. |
| Number of AI use cases using sensitive data | Measures exposure. |
| Number of AI use cases using regulated data | Measures regulatory exposure. |
| Number of AI use cases using customer data | Measures customer exposure. |
| Number of AI use cases using employee data | Measures HR/privacy exposure. |
| Percentage with retention defined | Measures lifecycle control. |
| Percentage with training/reuse restrictions defined | Measures reuse control. |
| Number of data leakage findings | Measures control weakness. |

## RAG-Specific Data Metrics

| Metric | Purpose |
|---|---|
| Number of RAG systems | Measures retrieval footprint. |
| Percentage of RAG systems with retrieval boundary defined | Measures retrieval control. |
| Percentage of RAG systems with permission inheritance tested | Measures access enforcement. |
| Number of retrieval boundary failures | Measures leakage risk. |
| Number of sensitive sources indexed | Measures exposure. |
| Number of denied retrieval events | Measures policy enforcement. |

## Data Warning Indicators

Investigate when:

```text
Data classification is unknown.
Data owner approval is missing.
Sensitive data is used without boundary.
RAG system lacks retrieval testing.
Vendor retention is unknown.
Training/reuse setting is unknown.
```

---

# 11. Prompt and Input Metrics

Prompt and input metrics measure whether input risk is managed.

## Core Prompt/Input Metrics

| Metric | Purpose |
|---|---|
| Percentage with allowed inputs defined | Measures input control clarity. |
| Percentage with prohibited inputs defined | Measures sensitive input control. |
| Percentage with system prompt owner assigned | Measures prompt accountability. |
| Percentage with prompt change control | Measures configuration discipline. |
| Number of prompt injection tests performed | Measures assurance coverage. |
| Number of prompt injection findings | Measures vulnerability. |
| Number of blocked sensitive inputs | Measures policy enforcement. |
| Number of input policy violations | Measures user or system risk. |

## Prompt/Input Warning Indicators

Investigate when:

```text
System prompts are not versioned.
Prompt changes bypass review.
External content is processed without prompt injection testing.
Sensitive data inputs are not detected or blocked.
Tool responses are treated as trusted instructions.
```

---

# 12. Output and Decision Metrics

Output and decision metrics measure whether AI output is controlled before it becomes a decision, record, communication, or action.

## Core Output Metrics

| Metric | Purpose |
|---|---|
| Percentage with output classification | Measures output control coverage. |
| Percentage with validation rule | Measures output readiness control. |
| Number of customer-facing AI outputs | Measures external exposure. |
| Number of generated records | Measures record impact. |
| Output rejection rate | Measures quality and review effectiveness. |
| Output modification rate | Measures human review effectiveness. |
| Output correction rate | Measures downstream issue frequency. |
| Number of output quality findings | Measures AI behavior risk. |

## Decision Metrics

| Metric | Purpose |
|---|---|
| Number of decision-supporting AI use cases | Measures decision exposure. |
| Percentage with decision owner assigned | Measures accountability. |
| Percentage with final decision evidence retained | Measures auditability. |
| Number of AI-assisted decisions reviewed | Measures oversight. |
| Number of AI recommendations overridden | Measures review effectiveness. |
| Number of disputed AI-assisted decisions | Measures risk and quality. |

## Output/Decision Warning Indicators

Investigate when:

```text
AI recommendation becomes final decision.
Decision owner is missing.
Human review has near-zero rejection or modification rate.
Generated records lack provenance.
Customer-facing outputs lack correction path.
```

---

# 13. Tool and Action Metrics

Tool and action metrics measure whether AI can affect enterprise state safely.

## Core Tool/Action Metrics

| Metric | Purpose |
|---|---|
| Number of action-capable AI use cases | Measures AI actor footprint. |
| Percentage with tool inventory | Measures tool visibility. |
| Percentage with action classification | Measures action risk clarity. |
| Percentage with approval gates for high-risk actions | Measures action control. |
| Number of tool calls | Measures activity. |
| Number of denied tool calls | Measures enforcement. |
| Number of high-risk actions requested | Measures risk exposure. |
| Number of high-risk actions approved | Measures approval activity. |
| Number of high-risk actions denied | Measures control operation. |
| Number of approval bypass attempts | Measures control attack or weakness. |
| Number of abnormal tool-use alerts | Measures monitoring effectiveness. |

## Agent-Specific Metrics

| Metric | Purpose |
|---|---|
| Number of AI agents | Measures agent footprint. |
| Percentage with autonomy level defined | Measures autonomy visibility. |
| Percentage with kill switch defined | Measures containment readiness. |
| Percentage with kill switch tested | Measures operational readiness. |
| Percentage with rollback or compensation assessed | Measures recovery readiness. |
| Number of agent incidents or near misses | Measures operational risk. |

## Tool/Action Warning Indicators

Investigate when:

```text
Tool inventory is incomplete.
AI can perform actions without approval.
High-risk actions lack logs.
Kill switch is missing or untested.
Rollback is unknown.
Agent retries or tool calls spike unexpectedly.
```

---

# 14. Vendor AI Metrics

Vendor AI metrics measure third-party AI risk.

## Core Vendor Metrics

| Metric | Purpose |
|---|---|
| Number of vendor AI features identified | Measures vendor AI visibility. |
| Percentage assessed before enablement | Measures review discipline. |
| Percentage with data processing reviewed | Measures data control. |
| Percentage with retention reviewed | Measures persistence risk. |
| Percentage with training/reuse reviewed | Measures reuse risk. |
| Percentage with admin controls reviewed | Measures configuration control. |
| Percentage with logs reviewed | Measures evidence readiness. |
| Percentage with incident support path defined | Measures incident readiness. |
| Number of vendor evidence gaps | Measures third-party assurance weakness. |
| Number of vendor AI incidents | Measures operational vendor risk. |

## Vendor Warning Indicators

Investigate when:

```text
Vendor AI feature is enabled by default.
Training/reuse setting is unknown.
Vendor retains prompts or outputs without approval.
Logs are unavailable.
Vendor incident support path is unclear.
Vendor changed AI feature behavior without review.
```

---

# 15. Assurance Metrics

Assurance metrics measure whether AI behavior and controls have been tested.

## Core Assurance Metrics

| Metric | Purpose |
|---|---|
| Percentage of high-risk AI with assurance test plan | Measures assurance planning. |
| Percentage of high-risk AI with testing completed | Measures testing coverage. |
| Number of tests performed | Measures assurance activity. |
| Number of failed tests | Measures control weakness. |
| Number of partial tests | Measures uncertainty. |
| Number of open assurance findings | Measures unresolved risk. |
| Percentage of findings closed on time | Measures remediation discipline. |
| Number of retests required | Measures remediation validation. |
| Number of regression tests triggered | Measures change control. |
| Number of incident tabletop exercises | Measures incident readiness. |

## Assurance Warning Indicators

Investigate when:

```text
Tier 4 or Tier 5 AI has no assurance test plan.
Prompt injection testing is missing for RAG or agentic AI.
Tool/action testing is missing for action-capable AI.
Evidence reconstruction has not been tested.
Findings remain overdue.
Regression testing is not triggered after material change.
```

---

# 16. Evidence Metrics

Evidence metrics measure auditability and incident readiness.

## Core Evidence Metrics

| Metric | Purpose |
|---|---|
| Percentage of high-risk AI with evidence package | Measures evidence readiness. |
| Percentage with evidence owner assigned | Measures accountability. |
| Percentage with evidence retention defined | Measures lifecycle control. |
| Percentage with reconstructability tested | Measures investigation readiness. |
| Number of evidence gaps | Measures audit and incident weakness. |
| Number of vendor evidence gaps | Measures third-party evidence risk. |
| Number of missing approval records | Measures governance weakness. |
| Number of missing decision records | Measures accountability weakness. |
| Number of missing tool/action logs | Measures action investigation weakness. |

## Evidence Warning Indicators

Investigate when:

```text
High-risk AI lacks evidence package.
AI activity cannot be reconstructed.
Approval records are missing.
Vendor logs are unavailable.
Evidence retention is shorter than business, legal, or incident needs.
```

---

# 17. Exception Metrics

Exception metrics measure accepted control gaps.

## Core Exception Metrics

| Metric | Purpose |
|---|---|
| Number of open AI exceptions | Measures accepted control gaps. |
| Number of exceptions by severity | Measures risk concentration. |
| Number of expired exceptions | Measures governance weakness. |
| Number of exceptions without owner | Measures accountability gap. |
| Number of exceptions without remediation plan | Measures permanence risk. |
| Average exception age | Measures remediation discipline. |
| Percentage of exceptions reviewed on time | Measures review discipline. |
| Number of recurring exceptions | Measures systemic control weakness. |

## Exception Warning Indicators

Investigate when:

```text
Exception has no expiry date.
Exception has no owner.
Exception lacks compensating control.
Exception is repeatedly renewed.
Exception relates to Tier 4 or Tier 5 AI.
Exception contributed to incident.
```

---

# 18. Incident Metrics

Incident metrics measure AI operational risk and resilience.

## Core Incident Metrics

| Metric | Purpose |
|---|---|
| Number of AI incidents | Measures realized AI risk. |
| Number of AI near misses | Measures emerging risk. |
| Incidents by severity | Measures impact. |
| Incidents by AI pattern | Shows failure concentration. |
| Incidents by pillar failure | Shows control weakness. |
| Mean time to detect | Measures detection effectiveness. |
| Mean time to contain | Measures containment effectiveness. |
| Mean time to recover | Measures recovery effectiveness. |
| Number of incidents involving vendor AI | Measures third-party dependency. |
| Number of incidents involving tool/action use | Measures action risk. |
| Number of incidents involving data exposure | Measures data boundary weakness. |
| Number of incidents with complete evidence | Measures investigation readiness. |
| Number of post-incident control updates | Measures learning loop. |

## Incident Warning Indicators

Investigate when:

```text
Incident cannot be reconstructed.
Containment is delayed.
Kill switch fails.
Vendor evidence is unavailable.
Same failure pattern repeats.
Post-incident actions are not closed.
```

---

# 19. Maturity Metrics

Maturity metrics show progress across the architecture.

## Pillar Maturity Metrics

Report current and target maturity for each pillar:

| Pillar | Current Level | Target Level | Trend |
|---|---|---|---|
| AI inventory and classification | [1-5] | [1-5] | [Improving/Stable/Declining] |
| AI identity and access control | [1-5] | [1-5] | [Improving/Stable/Declining] |
| Data boundary control | [1-5] | [1-5] | [Improving/Stable/Declining] |
| Prompt and input control | [1-5] | [1-5] | [Improving/Stable/Declining] |
| Output and decision control | [1-5] | [1-5] | [Improving/Stable/Declining] |
| Tool and action control | [1-5] | [1-5] | [Improving/Stable/Declining] |
| Human accountability model | [1-5] | [1-5] | [Improving/Stable/Declining] |
| AI assurance and testing | [1-5] | [1-5] | [Improving/Stable/Declining] |
| Monitoring, logging, and evidence | [1-5] | [1-5] | [Improving/Stable/Declining] |
| Incident containment and recovery | [1-5] | [1-5] | [Improving/Stable/Declining] |

## Maturity Warning Indicators

Investigate when:

```text
High-risk adoption grows faster than control maturity.
Tool/action capability grows while incident containment remains low.
Vendor AI use grows while vendor evidence remains weak.
Decision-supporting AI grows while accountability remains low.
AI incidents increase without control improvements.
```

---

# 20. Reporting Cadence

A suggested reporting cadence is below.

| Report | Audience | Cadence |
|---|---|---|
| Executive AI control dashboard | Executives, risk committee | Monthly or quarterly |
| AI governance operating report | Governance forum | Biweekly or monthly |
| High-risk AI review report | Risk, architecture, security | Monthly |
| Vendor AI report | Vendor risk, legal, privacy, security | Monthly or quarterly |
| AI assurance report | Assurance, audit, governance | Monthly or quarterly |
| AI exception report | Governance, risk owners | Monthly |
| AI incident report | Incident response, governance, leadership | Event-driven and monthly summary |
| AI maturity report | Governance, leadership, audit | Quarterly or semi-annually |
| AI control roadmap report | Governance, leadership | Quarterly |

---

# 21. Sample Monthly Governance Report

Use this structure for a monthly governance report.

```text
AI Control Governance Report

Reporting period:
Prepared by:
Overall status:

1. Executive summary
2. New AI use cases
3. AI inventory status
4. Risk tier distribution
5. High-risk AI review status
6. Control coverage
7. Vendor AI status
8. Assurance testing status
9. Evidence package status
10. Open findings
11. Open exceptions
12. Incidents and near misses
13. Maturity changes
14. Decisions required
15. Escalations
16. Next-period priorities
```

---

# 22. Sample Executive Summary

Example:

```text
During this reporting period, the enterprise inventory increased from [X] to [Y] AI use cases. [Z]% of use cases now have assigned business owners, and [Z]% have assigned risk tiers.

There are currently [X] Tier 3, [Y] Tier 4, and [Z] Tier 5 AI use cases. [N] high-risk use cases still require control assessment.

The most significant control gaps are [gap 1], [gap 2], and [gap 3]. There are [N] open high-severity findings and [N] open exceptions, of which [N] are overdue.

There were [N] AI incidents and [N] near misses this period. The most important incident theme was [theme].

The recommended leadership actions are:
1. [Action]
2. [Action]
3. [Action]
```

---

# 23. Metric Data Quality

Metrics are only useful if the data is reliable.

For each metric, define:

```text
Metric name:
Metric owner:
Data source:
Calculation method:
Reporting frequency:
Target:
Threshold:
Known limitations:
Action when metric is outside threshold:
```

## Data Quality Warning Indicators

Investigate when:

```text
Metric source is manual and inconsistent.
Metric owner is unclear.
Definitions vary across teams.
Risk tier is not applied consistently.
Vendor evidence is self-reported but not validated.
Dashboard shows green despite incidents or exceptions.
```

---

# 24. Targets and Thresholds

Targets should be risk-tiered.

Example targets:

| Metric | Suggested Target |
|---|---|
| AI use cases with business owner | 100% |
| AI use cases risk-tiered | 100% |
| Tier 3-5 AI with control assessment | 100% |
| Tier 3-5 AI with assurance plan | 100% |
| Tier 4-5 AI with tool/action controls | 100% |
| Tier 4-5 AI with incident containment path | 100% |
| Tier 5 AI with evidence package | 100% |
| Open critical findings | 0 beyond approved remediation window |
| Expired exceptions | 0 |
| AI incidents without evidence package | 0 for Tier 4-5 |
| AI agents with tested kill switch | 100% |

Targets should be adapted to the organization’s maturity stage.

---

# 25. Using Metrics to Drive Action

Metrics should trigger action.

Examples:

| Metric Condition | Action |
|---|---|
| High-risk AI without owner | Escalate to governance and restrict approval. |
| Tier 4 AI without tool inventory | Block production deployment. |
| Tier 5 AI without evidence package | Require remediation before approval. |
| Expired exception | Escalate to risk owner and governance forum. |
| Vendor logs unavailable | Open vendor remediation or exception. |
| Kill switch untested | Block or restrict agentic deployment. |
| Repeated prompt injection findings | Update prompt/input controls and assurance tests. |
| AI incident cannot be reconstructed | Update logging and evidence requirements. |

---

# 26. Reporting Anti-Patterns

## Anti-Pattern 1: Adoption Theater

Reporting only adoption numbers.

Example:

```text
10,000 users enabled for AI
1 million prompts submitted
```

Why this fails:

```text
It does not show whether AI is controlled.
```

---

## Anti-Pattern 2: Green Dashboard With No Evidence

Showing controls as complete because a document exists.

Why this fails:

```text
A control is not effective until it is implemented, tested, and evidenced.
```

---

## Anti-Pattern 3: No Risk Tier Distinction

Combining low-risk drafting tools and high-risk autonomous agents in the same metric.

Why this fails:

```text
It hides serious risk concentration.
```

---

## Anti-Pattern 4: Vendor Blind Spots

Reporting vendor AI as approved without tracking logs, retention, training/reuse, and incident support.

Why this fails:

```text
Vendor AI can create enterprise risk even when internally built AI is controlled.
```

---

## Anti-Pattern 5: Ignoring Near Misses

Tracking only confirmed incidents.

Why this fails:

```text
Near misses reveal control weakness before major harm occurs.
```

---

# 27. Summary

AI control reporting should show whether the enterprise can safely adopt AI.

The best metrics answer:

```text
Do we know what AI exists?
Is it owned?
Is it risk-tiered?
Are required controls implemented?
Are controls tested?
Does evidence exist?
Are exceptions temporary?
Are incidents contained?
Are lessons improving the architecture?
```

The goal of reporting is not to create dashboards.

The goal is to create decisions, accountability, remediation, and safer AI adoption.