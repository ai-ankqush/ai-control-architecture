# EU AI Act Crosswalk

This document maps the AI Control Architecture to selected control themes from the European Union Artificial Intelligence Act.

The purpose of this crosswalk is to show how the AI Control Architecture can help enterprises operationalize practical controls that may support EU AI Act readiness, especially for high-risk AI systems.

The AI Control Architecture is not a replacement for legal analysis, regulatory compliance, conformity assessment, or formal EU AI Act obligations.

This document is not legal advice.

---

# 1. Positioning

The EU AI Act establishes a risk-based regulatory framework for AI systems.

For high-risk AI systems, the Act includes requirements relating to:

```text
Risk management
Data and data governance
Technical documentation
Record-keeping
Transparency and provision of information to deployers
Human oversight
Accuracy, robustness, and cybersecurity
Quality management
Corrective actions
Logging
Documentation keeping
Registration and conformity processes where applicable
```

The AI Control Architecture helps answer:

```text
How do we operationalize these expectations inside enterprise systems, data, identity, workflows, vendors, assurance, evidence, and incident response?
```

A useful positioning is:

```text
EU AI Act = legal and regulatory obligation framework
AI Control Architecture = operational control and evidence implementation layer
```

---

# 2. Important Scope Note

The EU AI Act creates different obligations depending on the role of the organization and the type of AI system.

An organization may be acting as:

```text
Provider
Deployer
Importer
Distributor
Product manufacturer
Authorized representative
```

The AI Control Architecture does not determine legal role classification.

Organizations should obtain legal and regulatory advice to determine:

```text
Whether the AI system is in scope
Whether the AI system is high-risk
Which role the organization performs
Which obligations apply
Which conformity, registration, documentation, or notification requirements apply
```

This crosswalk focuses on practical control themes only.

---

# 3. AI Control Architecture Pillars

The AI Control Architecture uses ten pillars:

```text
1. AI inventory and classification
2. AI identity and access control
3. Data boundary control
4. Prompt and input control
5. Output and decision control
6. Tool and action control
7. Human accountability model
8. AI assurance and testing
9. Monitoring, logging, and evidence
10. Incident containment and recovery
```

These pillars can support operational readiness for AI governance, high-risk AI control, evidence, assurance, monitoring, and incident response.

---

# 4. High-Level Crosswalk

| EU AI Act Control Theme | AI Control Architecture Support |
|---|---|
| AI system classification | AI inventory and classification; risk tiering; AI pattern classification |
| Risk management | risk assessment; control assessment; failure scenarios; assurance testing; incident readiness |
| Data and data governance | data boundary control; data source mapping; classification; retention; reuse; retrieval boundaries |
| Technical documentation | architecture decision records; control assessments; requirements catalogue; evidence packages |
| Record-keeping and logging | monitoring, logging, evidence; event taxonomy; reconstructability |
| Transparency to deployers | output/decision control; user guidance; limitations; instructions; accountability |
| Human oversight | human accountability model; decision owner; meaningful review; contextual reconstructability |
| Accuracy, robustness, cybersecurity | assurance and testing; adversarial testing; output validation; security controls |
| Quality management | governance operating model; maturity model; metrics; continual improvement |
| Corrective action | incident containment and recovery; findings; remediation; exceptions; post-incident review |
| Vendor and supply chain AI | vendor assessment; subprocessor review; evidence; feature enablement controls |

---

# 5. AI System Classification Crosswalk

## EU AI Act Theme

The EU AI Act uses a risk-based approach. Organizations need to understand whether an AI system is in scope, whether it may be high-risk, and what role the organization plays.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture supports classification by requiring every AI capability to be inventoried, owned, pattern-classified, lifecycle-managed, and risk-tiered.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| AI inventory and classification | Captures AI use cases, pattern, lifecycle, risk tier, ownership, and status. |
| Human accountability model | Assigns owners responsible for classification and escalation. |
| Data boundary control | Identifies whether sensitive, regulated, personal, customer, or employee data is involved. |
| Output and decision control | Identifies whether AI influences high-impact decisions. |
| Tool and action control | Identifies whether AI can perform actions or affect systems. |

## Implementation Activities

```text
Create AI inventory.
Record intended purpose.
Record business owner.
Record technical owner.
Record AI pattern.
Record lifecycle status.
Identify vendor involvement.
Identify data categories.
Identify user population.
Identify external exposure.
Identify decision impact.
Identify tool/action capability.
Assign AI risk tier.
Flag possible high-risk or regulated AI for legal review.
```

## Example Evidence

```text
AI inventory record
AI use case intake
Risk tiering record
Risk assessment
Business purpose
Lifecycle status
Data classification
Decision impact assessment
Vendor assessment
Legal/regulatory review record where applicable
```

## Related Project Files

```text
QUICKSTART.md
docs/17-implementation-checklists.md
docs/19-common-ai-control-patterns.md
templates/ai-use-case-intake-template.md
templates/ai-risk-assessment-template.md
templates/ai-risk-tiering-template.md
templates/ai-inventory-record-template.md
```

---

# 6. Risk Management Crosswalk

## EU AI Act Theme

High-risk AI systems are associated with risk management expectations across lifecycle design, foreseeable risks, mitigation, testing, and monitoring.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture supports risk management by defining risk tiering, control objectives, control assessments, failure scenarios, assurance tests, findings, exceptions, and incident containment.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| AI inventory and classification | Enables portfolio visibility and risk-tier prioritization. |
| Data boundary control | Identifies data-related risks. |
| Prompt and input control | Identifies input manipulation and prompt injection risk. |
| Output and decision control | Identifies decision, record, and output risks. |
| Tool and action control | Identifies action, workflow, and autonomy risks. |
| AI assurance and testing | Tests control effectiveness and AI behavior. |
| Incident containment and recovery | Defines containment, correction, recovery, and restart. |

## Implementation Activities

```text
Assign risk tier.
Identify risk drivers.
Identify foreseeable misuse.
Identify failure scenarios.
Map required controls.
Assess control readiness.
Define assurance tests.
Track findings.
Define compensating controls.
Document exceptions.
Define incident scenarios.
Define containment and recovery paths.
Review residual risk.
```

## Example Evidence

```text
Risk assessment
Risk tiering record
Risk scenario record
Control assessment
Requirements mapping
Assurance test plan
Findings register
Exception record
Risk acceptance record
Incident containment plan
Maturity roadmap
```

## Related Project Files

```text
docs/06-requirements-catalogue.md
docs/17-implementation-checklists.md
docs/20-common-failure-scenarios.md
docs/21-adoption-playbook.md
docs/24-assurance-and-audit-guide.md
templates/ai-risk-assessment-template.md
templates/risk-scenario-template.md
templates/ai-control-assessment-template.md
templates/ai-assurance-test-plan-template.md
```

---

# 7. Data and Data Governance Crosswalk

## EU AI Act Theme

High-risk AI controls include data governance expectations. For enterprises, this requires practical control over data sources, data quality, data categories, access, retrieval, retention, reuse, and exposure.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture supports data governance through explicit data boundaries, data source mapping, owner approval, classification, retrieval controls, sensitive data restrictions, and vendor data processing review.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| Data boundary control | Defines approved data sources, classifications, retrieval rules, retention, and reuse. |
| AI identity and access control | Ensures AI data access is identity-bound and least privilege. |
| Prompt and input control | Defines prohibited inputs and sensitive data handling. |
| Monitoring, logging, and evidence | Provides evidence of data access and retrieval activity. |
| AI assurance and testing | Tests data leakage and retrieval boundaries. |

## Implementation Activities

```text
Map data sources.
Identify data owners.
Classify data.
Define allowed and prohibited data.
Define retrieval boundaries.
Define retention rules.
Define training and reuse restrictions.
Review vendor data processing.
Review subprocessor chain where applicable.
Test data leakage.
Test retrieval boundaries.
Log data access and retrieval events where required.
```

## Example Evidence

```text
Data source map
Data classification record
Data owner approval
Retrieval boundary configuration
Sensitive source exclusion
Retention settings
Training/reuse restrictions
Vendor data processing review
Subprocessor review
Data leakage test result
Retrieval boundary test result
Data access logs
```

## Related Project Files

```text
docs/09-pillar-data-boundary-control.md
docs/17-implementation-checklists.md
docs/19-common-ai-control-patterns.md
templates/ai-data-boundary-template.md
templates/ai-vendor-assessment-template.md
examples/rag-assistant-example.md
examples/vendor-ai-example.md
```

---

# 8. Technical Documentation Crosswalk

## EU AI Act Theme

High-risk AI systems require technical documentation sufficient to demonstrate design, intended purpose, operation, risk management, and compliance-related information.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture supports technical documentation by requiring architecture records, requirements mapping, control assessments, risk assessments, evidence packages, assurance test results, and lifecycle documentation.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| AI inventory and classification | Documents use case, purpose, pattern, owner, lifecycle, and risk tier. |
| AI identity and access control | Documents identity, access model, and delegated authority. |
| Data boundary control | Documents data sources and data controls. |
| Prompt and input control | Documents input surfaces and system prompt controls. |
| Output and decision control | Documents output use and decision impact. |
| Tool and action control | Documents tools, actions, approvals, and kill switch design. |
| AI assurance and testing | Documents tests, results, findings, and retesting. |
| Monitoring, logging, and evidence | Documents evidence sources and retention. |

## Implementation Activities

```text
Create architecture decision record.
Document intended purpose.
Document AI pattern.
Document data sources.
Document identity model.
Document prompt/input controls.
Document output/decision controls.
Document tool/action controls.
Document monitoring and logging.
Document assurance test results.
Document limitations.
Document incident containment path.
Maintain evidence package.
```

## Example Evidence

```text
AI inventory
Architecture decision record
Risk assessment
Control assessment
Requirements catalogue
Data boundary record
Identity/access record
Tool inventory
Assurance test report
Evidence package
Incident containment plan
Change history
```

## Related Project Files

```text
docs/05-reference-architecture.md
docs/06-requirements-catalogue.md
templates/ai-architecture-decision-record-template.md
templates/ai-control-assessment-template.md
templates/ai-control-evidence-package-template.md
```

---

# 9. Record-Keeping and Logging Crosswalk

## EU AI Act Theme

High-risk AI systems include record-keeping and logging expectations to support traceability, monitoring, oversight, and investigation.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture supports record-keeping through monitoring, logging, evidence retention, event taxonomy, evidence packages, and reconstructability testing.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| Monitoring, logging, and evidence | Defines log types, retention, protection, evidence packages, and reconstructability. |
| Tool and action control | Defines tool call and action logs. |
| Output and decision control | Defines output, generated record, and decision evidence. |
| AI identity and access control | Supports attribution of AI-mediated activity. |
| Incident containment and recovery | Defines evidence preservation during incidents. |

## Implementation Activities

```text
Define logging requirements by risk tier.
Define AI event taxonomy.
Log AI identity and user identity where required.
Log prompt/input metadata where required.
Log retrieval/context metadata where required.
Log output metadata where required.
Log decision evidence where required.
Log tool calls and actions where required.
Log approvals and exceptions.
Define retention.
Protect evidence.
Test evidence reconstruction.
```

## Example Evidence

```text
Logging requirements
AI event taxonomy
Prompt/input logs or metadata
Retrieval logs
Output logs
Decision records
Tool call logs
Action logs
Approval logs
Exception logs
Evidence package
Evidence reconstruction test
Incident evidence preservation record
```

## Related Project Files

```text
docs/23-metrics-and-reporting.md
docs/24-assurance-and-audit-guide.md
templates/ai-monitoring-logging-evidence-template.md
templates/ai-control-evidence-package-template.md
templates/ai-incident-record-template.md
```

---

# 10. Transparency and Information to Deployers Crosswalk

## EU AI Act Theme

High-risk AI systems include transparency and information expectations so deployers can understand intended purpose, capabilities, limitations, use conditions, and oversight requirements.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture supports transparency through documented intended use, limitations, output boundaries, user guidance, escalation paths, decision accountability, and vendor/instructions review.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| AI inventory and classification | Documents intended purpose, owner, pattern, and lifecycle. |
| Output and decision control | Defines output limitations, validation, decision separation, and correction paths. |
| Human accountability model | Defines who must review, approve, override, or escalate. |
| Data boundary control | Defines data limitations and prohibited data. |
| Prompt and input control | Defines allowed and prohibited inputs. |
| Vendor AI assessment | Reviews vendor instructions, limitations, admin controls, and feature behavior. |

## Implementation Activities

```text
Document intended purpose.
Document approved users.
Document approved use.
Document prohibited use.
Document data restrictions.
Document output limitations.
Document decision boundaries.
Document human review requirements.
Document escalation triggers.
Document correction process.
Document vendor instructions and limitations.
Publish user guidance.
```

## Example Evidence

```text
Use case intake
User guidance
Approved use statement
Prohibited use statement
Output limitations
Decision owner record
Human review criteria
Escalation path
Correction procedure
Vendor instructions for use
Training or awareness record
```

## Related Project Files

```text
QUICKSTART.md
docs/11-pillar-output-and-decision-control.md
docs/13-pillar-human-accountability.md
templates/ai-output-and-decision-control-template.md
templates/ai-human-accountability-template.md
templates/ai-vendor-assessment-template.md
```

---

# 11. Human Oversight Crosswalk

## EU AI Act Theme

High-risk AI systems include human oversight expectations to reduce risk and enable human intervention, interpretation, control, and override where needed.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture supports human oversight through accountable ownership, meaningful human review, decision separation, approval gates, contextual reconstructability, override rights, escalation, and incident ownership.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| Human accountability model | Assigns accountable owners, reviewers, approvers, and decision owners. |
| Output and decision control | Separates AI recommendation from final decision. |
| Tool and action control | Implements approval gates and action controls. |
| Monitoring, logging, and evidence | Provides review evidence and reconstructability. |
| Incident containment and recovery | Supports intervention, containment, correction, and restart approval. |

## Implementation Activities

```text
Assign decision owner.
Define meaningful human review.
Define reviewer authority.
Define what reviewer must see.
Provide source material or evidence to reviewer.
Define approval gates.
Define override and rejection paths.
Log review decisions.
Log approvals and denials.
Define escalation triggers.
Define incident ownership.
Define restart approval.
```

## Contextual Reconstructability Requirement

Human review should be treated as valid only when the reviewer receives enough context to make an informed decision.

The reviewer should be able to see:

```text
AI output or recommendation
Input or prompt context where appropriate
Relevant source material
Retrieved evidence or citations
Risk indicators
Confidence or uncertainty where available
Action impact
Required approval threshold
Alternatives or escalation path
```

## Example Evidence

```text
Decision owner record
Human review criteria
Reviewer record
Approval log
Rejection log
Override record
Escalation record
Source references
Decision evidence
Tool/action approval evidence
Incident restart approval
```

## Related Project Files

```text
docs/13-pillar-human-accountability.md
docs/11-pillar-output-and-decision-control.md
templates/ai-human-accountability-template.md
templates/ai-output-and-decision-control-template.md
templates/ai-tool-and-action-control-template.md
examples/agentic-ai-example.md
```

---

# 12. Accuracy, Robustness, and Cybersecurity Crosswalk

## EU AI Act Theme

High-risk AI systems include expectations around accuracy, robustness, and cybersecurity.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture supports these expectations through assurance testing, adversarial testing, prompt injection testing, data leakage testing, output validation, tool/action testing, monitoring, incident response, and rollback.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| AI assurance and testing | Defines testing for behavior and control effectiveness. |
| Prompt and input control | Addresses prompt injection, external input, and input manipulation. |
| Data boundary control | Addresses data leakage and retrieval boundary failures. |
| Output and decision control | Addresses output accuracy, validation, and correction. |
| Tool and action control | Addresses unsafe actions, excessive agency, and approval bypass. |
| Monitoring, logging, and evidence | Supports detection and investigation. |
| Incident containment and recovery | Supports containment and recovery from failures or attacks. |

## Implementation Activities

```text
Define assurance scope.
Test output accuracy and validation.
Test prompt injection.
Test retrieval boundaries.
Test data leakage.
Test unauthorized tool use.
Test approval bypass.
Test logging completeness.
Test evidence reconstruction.
Test kill switch.
Test rollback or compensation.
Monitor failures and anomalies.
Track findings and remediation.
```

## Example Evidence

```text
Assurance test plan
Output validation test
Prompt injection test
Retrieval boundary test
Data leakage test
Tool/action test
Approval bypass test
Security test result
Logging completeness test
Kill switch test
Rollback test
Findings register
Remediation evidence
Incident record
```

## Related Project Files

```text
docs/24-assurance-and-audit-guide.md
docs/20-common-failure-scenarios.md
templates/ai-assurance-test-plan-template.md
templates/ai-incident-containment-recovery-template.md
```

---

# 13. Quality Management Crosswalk

## EU AI Act Theme

The EU AI Act includes quality management expectations for providers of high-risk AI systems.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture supports quality management through governance roles, lifecycle processes, requirements, controls, assurance, evidence, incident learning, metrics, and continual improvement.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| AI inventory and classification | Supports lifecycle and portfolio management. |
| Human accountability model | Defines roles, responsibility, and decision rights. |
| AI assurance and testing | Provides quality assurance and validation. |
| Monitoring, logging, and evidence | Provides performance and control evidence. |
| Incident containment and recovery | Supports corrective action and lessons learned. |
| Metrics and reporting | Supports management review and improvement. |

## Implementation Activities

```text
Define AI lifecycle process.
Define ownership and governance.
Define control requirements.
Define assurance requirements.
Define documentation and evidence requirements.
Define vendor review process.
Define exception process.
Define incident process.
Define metrics.
Review maturity.
Update controls after findings and incidents.
```

## Example Evidence

```text
Governance operating model
Risk tiering process
Requirements catalogue
Control assessment process
Assurance process
Evidence package
Exception process
Incident process
Metrics dashboard
Maturity assessment
Post-incident review
Change history
```

## Related Project Files

```text
docs/21-adoption-playbook.md
docs/22-governance-and-operating-model.md
docs/23-metrics-and-reporting.md
docs/18-control-maturity-model.md
CHANGELOG.md
ROADMAP.md
```

---

# 14. Corrective Action and Incident Response Crosswalk

## EU AI Act Theme

High-risk AI obligations include corrective action and information duties when systems present risk, fail, or do not perform as intended.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture supports corrective action through incident containment, recovery, findings management, exception management, remediation, restart criteria, and post-incident control improvement.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| Incident containment and recovery | Defines detection, containment, recovery, correction, restart, and lessons learned. |
| Monitoring, logging, and evidence | Supports evidence preservation and investigation. |
| Tool and action control | Supports disabling tools, revoking access, rolling back actions. |
| Human accountability model | Assigns incident and recovery owners. |
| AI assurance and testing | Supports retesting after correction. |

## Implementation Activities

```text
Define AI incident scenarios.
Define severity criteria.
Define incident owner.
Define containment authority.
Preserve evidence.
Disable AI capability where required.
Revoke AI identity or tool access.
Quarantine outputs or generated records.
Correct affected records.
Notify stakeholders where required.
Track findings.
Define restart criteria.
Retest controls.
Conduct post-incident review.
Update requirements and tests.
```

## Example Evidence

```text
Incident record
Containment action log
Evidence preservation checklist
Access revocation record
Tool disablement record
Output quarantine record
Correction record
Stakeholder notification record
Recovery plan
Restart approval
Retest result
Post-incident review
Updated controls
```

## Related Project Files

```text
docs/20-common-failure-scenarios.md
docs/24-assurance-and-audit-guide.md
templates/ai-incident-record-template.md
templates/ai-incident-containment-recovery-template.md
templates/ai-exception-record-template.md
```

---

# 15. Vendor and Supply Chain AI Crosswalk

## EU AI Act Theme

The EU AI Act creates obligations across AI supply chains depending on role. Enterprises also need to understand vendors, subprocessors, model providers, deployers, and shared responsibility.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture supports vendor and supply chain control through vendor AI assessment, feature enablement control, subprocessor review, data processing review, logging review, incident support review, and vendor evidence requirements.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| AI inventory and classification | Identifies vendor AI and embedded SaaS AI. |
| Data boundary control | Reviews vendor data processing, retention, reuse, and subprocessor flows. |
| Output and decision control | Reviews vendor AI output use and decision impact. |
| Tool and action control | Reviews vendor AI actions and workflow capability. |
| Monitoring, logging, and evidence | Reviews vendor logs and evidence availability. |
| Incident containment and recovery | Reviews vendor incident support and disablement. |

## Vendor AI Default Principle

```text
No vendor AI feature should be enabled for enterprise data processing without explicit control-plane approval.
```

## Implementation Activities

```text
Identify vendor AI feature.
Confirm feature enablement status.
Review whether AI is enabled by default.
Review whether admin disablement is available.
Review vendor data processing.
Review prompt/output retention.
Review training and product improvement use.
Review third-party model providers.
Review subprocessors.
Review logs and evidence.
Review incident support.
Review contractual terms.
Define feature disablement path.
```

## Example Evidence

```text
Vendor assessment
Vendor AI feature inventory
Admin configuration record
Data processing terms
Retention terms
Training/reuse terms
Subprocessor list
Third-party model provider disclosure
Logging documentation
Evidence export test
Incident support path
Feature disablement test
Contract review record
```

## Related Project Files

```text
templates/ai-vendor-assessment-template.md
examples/vendor-ai-example.md
docs/19-common-ai-control-patterns.md
docs/22-governance-and-operating-model.md
```

---

# 16. EU AI Act Theme to Pillar Matrix

| EU AI Act Theme | Primary AI Control Architecture Pillars |
|---|---|
| Classification and scope | AI inventory and classification; human accountability |
| Risk management | AI inventory; data boundary; output/decision; tool/action; assurance; incident |
| Data and data governance | Data boundary; identity/access; prompt/input; evidence |
| Technical documentation | inventory; architecture decisions; control assessment; evidence |
| Record-keeping and logging | monitoring, logging, evidence; identity; tool/action |
| Transparency to deployers | output/decision; human accountability; prompt/input; vendor |
| Human oversight | human accountability; output/decision; tool/action; evidence |
| Accuracy, robustness, cybersecurity | assurance; prompt/input; data boundary; tool/action; incident |
| Quality management | governance; maturity; metrics; assurance; improvement |
| Corrective actions | incident containment; findings; remediation; exceptions |
| Vendor and supply chain AI | vendor assessment; data boundary; evidence; incident |

---

# 17. Example: High-Risk Decision-Supporting AI

## Use Case

```text
AI system that supports decisions affecting customers, employees, financial outcomes, legal obligations, security actions, or regulated processes.
```

## AI Control Architecture Implementation

| EU AI Act Theme | Implementation Activity |
|---|---|
| Classification | Flag use case for legal/regulatory high-risk review. |
| Risk management | Complete risk assessment and risk scenario analysis. |
| Data governance | Map data sources, classifications, quality constraints, and owner approvals. |
| Technical documentation | Maintain architecture decision records and control assessment. |
| Record-keeping | Define decision evidence and output logs. |
| Transparency | Document intended use, limitations, and user guidance. |
| Human oversight | Assign decision owner and define meaningful review criteria. |
| Robustness/cybersecurity | Test output validation, prompt injection, and evidence reconstruction. |
| Corrective action | Define correction, appeal/escalation, incident, and recovery path. |

## Example Evidence

```text
Risk assessment
Legal/regulatory review record
Data boundary record
Decision owner record
Output validation test
Human review evidence
Decision evidence
Assurance test result
Incident containment plan
```

---

# 18. Example: Agentic AI With Tool Access

## Use Case

```text
AI agent that can classify work, request actions, call tools, route tickets, or trigger workflows.
```

## AI Control Architecture Implementation

| EU AI Act Theme | Implementation Activity |
|---|---|
| Classification | Identify action capability and autonomy level. |
| Risk management | Assign Tier 4 or Tier 5 based on action impact and recoverability. |
| Data governance | Map data sources and tool responses available to agent. |
| Technical documentation | Document agent architecture, identity, tools, and action boundaries. |
| Record-keeping | Log goals, prompts, tool calls, approvals, actions, and outcomes. |
| Transparency | Inform operators of agent limits, escalation triggers, and approval requirements. |
| Human oversight | Require approval gates for high-risk actions. |
| Robustness/cybersecurity | Test prompt injection, tool misuse, approval bypass, kill switch, and rollback. |
| Corrective action | Define disablement, rollback, incident response, and restart criteria. |

## Example Evidence

```text
Agent control record
Tool inventory
Action classification
Approval gate configuration
Tool/action logs
Kill switch test
Rollback test
Evidence reconstruction test
Incident containment plan
```

Related example:

```text
examples/agentic-ai-example.md
```

---

# 19. How to Use This Crosswalk

Use this crosswalk when:

```text
An enterprise wants to understand how AI Control Architecture may support EU AI Act readiness.
A legal or compliance team asks how controls support high-risk AI governance themes.
A product, platform, or architecture team needs practical controls for high-risk AI themes.
An assurance team wants evidence examples for AI Act-related control themes.
A vendor AI review needs stronger documentation, logging, human oversight, or incident controls.
```

Suggested use:

```text
1. Determine whether the AI system is potentially in scope.
2. Determine organizational role with legal support.
3. Determine whether the system may be high-risk with legal support.
4. Complete AI use case intake.
5. Assign owners.
6. Assign risk tier.
7. Map relevant EU AI Act themes to AI Control Architecture pillars.
8. Identify required controls.
9. Identify evidence.
10. Define assurance tests.
11. Track findings, exceptions, incidents, and corrective actions.
```

---

# 20. Limitations

This crosswalk is intended to support implementation thinking.

It is not:

```text
Legal advice
A compliance guarantee
A conformity assessment
A CE marking assessment
A complete article-by-article legal mapping
A substitute for qualified EU AI Act legal counsel
A substitute for regulatory interpretation
A substitute for formal audit or certification work
```

Organizations should consult qualified legal, privacy, compliance, regulatory, and audit advisors when determining EU AI Act obligations.

---

# 21. Future Enhancements

Future versions may add:

```text
Article-by-article EU AI Act mapping
Provider obligation mapping
Deployer obligation mapping
High-risk AI documentation checklist
EU AI Act evidence catalogue
Conformity readiness checklist
AI Act incident and corrective action checklist
Machine-readable EU AI Act crosswalk
```

---

# 22. Summary

The EU AI Act creates legal and regulatory obligations for AI systems, especially high-risk AI systems.

The AI Control Architecture does not replace those obligations.

It helps enterprises operationalize practical controls around:

```text
Inventory
Risk management
Data governance
Documentation
Logging
Transparency
Human oversight
Assurance
Cybersecurity
Corrective action
Vendor AI
Incident containment
Evidence
```

The goal is to move from:

```text
Regulatory requirement awareness
```

to:

```text
Operational AI control readiness
```