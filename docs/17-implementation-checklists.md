# Implementation Checklists

This document provides practical checklists for applying the AI Control Architecture.

The purpose of these checklists is to help teams move from architecture theory to implementation.

Use these checklists when reviewing AI use cases, preparing pilots, approving production deployment, assessing vendor AI, designing agents, or improving AI control maturity.

---

# 1. How to Use These Checklists

These checklists are designed for:

- business owners
- enterprise architects
- security architects
- risk teams
- privacy teams
- legal teams
- compliance teams
- vendor risk teams
- data governance teams
- platform teams
- AI product teams
- audit teams
- incident response teams

Use them to answer four practical questions:

```text
What AI exists?
What can it see?
What can it decide?
What can it do?
```

Then answer:

```text
Who owns it?
What controls apply?
What evidence exists?
How is failure contained?
```

---

# 2. Minimum Implementation Checklist

Use this checklist when starting from zero.

The goal is to establish minimum viable AI control.

| Area | Minimum Check |
|---|---|
| Inventory | Is the AI use case recorded? |
| Ownership | Is a business owner assigned? |
| Risk tier | Has the AI use case been risk-tiered? |
| Data | Are data sources and classifications known? |
| Identity | Is the AI identity or authority model understood? |
| Inputs | Are allowed and prohibited inputs defined? |
| Outputs | Is output use understood? |
| Decisions | Does AI influence decisions? |
| Tools/actions | Can AI call tools, APIs, workflows, or perform actions? |
| Human accountability | Is a human accountable for outcomes? |
| Logging | Is required evidence defined? |
| Assurance | Has the AI use case been reviewed or tested? |
| Incident response | Can the AI capability be disabled or contained? |
| Vendor | Is vendor AI involvement understood? |
| Exceptions | Are control gaps documented and approved? |

Minimum implementation is not the target state.

It is the starting point.

---

# 3. AI Use Case Intake Checklist

Use this checklist before approving any AI use case.

| Check | Yes / No / NA | Notes |
|---|---|---|
| Use case name is documented. | | |
| Business purpose is documented. | | |
| Business owner is assigned. | | |
| Technical owner is assigned where required. | | |
| Data owner is assigned where required. | | |
| Vendor owner is assigned where required. | | |
| AI pattern is identified. | | |
| Lifecycle status is recorded. | | |
| Intended users are identified. | | |
| External exposure is understood. | | |
| Business process impact is documented. | | |
| Decision impact is assessed. | | |
| Tool or action capability is assessed. | | |
| Initial risk tier is proposed. | | |
| Required reviews are identified. | | |

Related template:

```text
templates/ai-use-case-intake-template.md
```

---

# 4. Risk Tiering Checklist

Use this checklist to assign a risk tier.

| Risk Driver | Low | Medium | High | Critical |
|---|---|---|---|---|
| Data sensitivity | Public only | Internal data | Sensitive data | Regulated, privileged, secret, or highly sensitive data |
| Decision impact | No decision impact | Informal support | Business decision support | Regulated or high-impact decision |
| Output impact | Draft or summary | Internal operational output | Customer, record, or workflow output | Legal, financial, HR, security, or regulated output |
| Tool/action capability | None | Read-only or draft | Record, workflow, customer, or system action | Financial, privileged, production, or hard-to-reverse action |
| Autonomy | Human fully controls | AI recommends | AI requests or performs bounded actions | AI performs high-impact or multi-step autonomous actions |
| External exposure | Internal only | Vendor processing | Customer, supplier, or partner-facing | Public, regulator-facing, or high-impact external |
| Vendor dependency | None | Known vendor controls | Vendor processes sensitive data | Vendor controls critical AI behavior or retains/trains on data |
| Recoverability | Easy to discard | Manual correction | Difficult recovery | Irreversible or unclear recovery |

Risk tier guidance:

| Tier | Use When |
|---|---|
| Tier 1 | Low-risk productivity or public-data use. |
| Tier 2 | Internal productivity with enterprise data. |
| Tier 3 | AI influences decisions or records. |
| Tier 4 | AI can call tools, trigger workflows, or perform actions. |
| Tier 5 | AI is high-impact, regulated, autonomous, privileged, production-critical, or hard to recover from. |

Related templates:

```text
templates/ai-risk-assessment-template.md
templates/ai-risk-tiering-template.md
```

---

# 5. Control Readiness Checklist

Use this checklist before pilot, production deployment, scaling, or continued operation.

| Pillar | Key Question | Ready? |
|---|---|---|
| AI inventory and classification | Is the AI use case visible, owned, classified, and risk-tiered? | |
| AI identity and access control | Is AI authority identifiable, limited, approved, and revocable? | |
| Data boundary control | Are data sources, classifications, retrieval boundaries, retention, and reuse controlled? | |
| Prompt and input control | Are inputs controlled as a risk surface? | |
| Output and decision control | Are AI outputs validated before they become decisions, records, or actions? | |
| Tool and action control | Are tools and actions inventoried, approved, bounded, logged, and containable? | |
| Human accountability model | Is human ownership assigned for outcomes, decisions, exceptions, and incidents? | |
| AI assurance and testing | Has the AI use case been tested based on risk? | |
| Monitoring, logging, and evidence | Can AI activity be monitored and reconstructed? | |
| Incident containment and recovery | Can AI failure be contained, investigated, corrected, and learned from? | |

Related template:

```text
templates/ai-control-assessment-template.md
```

---

# 6. Copilot Implementation Checklist

Use this checklist for enterprise copilots and productivity assistants.

| Check | Yes / No / NA | Notes |
|---|---|---|
| Copilot use case is recorded in inventory. | | |
| Business owner is assigned. | | |
| User population is defined. | | |
| Copilot access model is understood. | | |
| Permission inheritance is reviewed. | | |
| Sensitive data exposure is assessed. | | |
| User guidance is provided. | | |
| Prohibited prompt/input rules are defined. | | |
| Output use restrictions are defined. | | |
| Human remains responsible for use of output. | | |
| Logging approach is defined. | | |
| Vendor processing and retention are reviewed. | | |
| Incident reporting path is defined. | | |

Common copilot risks:

- users overtrusting generated output
- excessive permission inheritance
- sensitive data appearing in prompts
- output copied into records without review
- weak visibility into usage
- vendor retention or reuse uncertainty

---

# 7. RAG Implementation Checklist

Use this checklist for retrieval-augmented generation, enterprise search, knowledge assistants, and document-grounded AI.

| Check | Yes / No / NA | Notes |
|---|---|---|
| RAG use case is recorded in inventory. | | |
| Data sources are mapped. | | |
| Data owners are identified. | | |
| Data classifications are documented. | | |
| Retrieval boundaries are defined. | | |
| User permission inheritance is tested. | | |
| Cross-user or cross-tenant retrieval is tested. | | |
| Sensitive sources are excluded or controlled. | | |
| Source attribution is enabled where required. | | |
| Prompt injection in retrieved content is tested. | | |
| Output sensitivity inheritance is defined. | | |
| Retrieval logs are captured where required. | | |
| Data leakage testing is completed where required. | | |

Common RAG risks:

- unauthorized retrieval
- sensitive source exposure
- stale or incorrect source material
- prompt injection embedded in documents
- weak source attribution
- cross-user or cross-tenant leakage

---

# 8. Agentic AI Implementation Checklist

Use this checklist for AI agents and action-capable AI.

| Check | Yes / No / NA | Notes |
|---|---|---|
| Agent is recorded in inventory. | | |
| Agent owner is assigned. | | |
| Agent purpose is clearly defined. | | |
| Approved and prohibited uses are documented. | | |
| Autonomy level is defined. | | |
| Agent identity is defined. | | |
| Delegated authority is documented. | | |
| Data sources accessible to the agent are approved. | | |
| Tools available to the agent are inventoried. | | |
| Actions are classified by risk. | | |
| High-risk actions require approval. | | |
| Action boundaries are enforced. | | |
| Blast-radius limits are defined. | | |
| Tool calls and actions are logged. | | |
| Kill switch is defined and tested. | | |
| Rollback or compensation is assessed. | | |
| Incident scenarios are defined. | | |
| Agent assurance testing is completed. | | |

Related template:

```text
templates/ai-agent-control-template.md
```

Common agent risks:

- unauthorized tool use
- approval bypass
- excessive autonomy
- unsafe action chaining
- prompt injection causing tool misuse
- weak kill switch
- incomplete tool/action logs
- unclear accountability for agent actions

---

# 9. Vendor AI Implementation Checklist

Use this checklist before enabling, purchasing, integrating, or scaling vendor AI.

| Check | Yes / No / NA | Notes |
|---|---|---|
| Vendor AI feature is identified. | | |
| Vendor AI feature enablement status is known. | | |
| Business owner is assigned. | | |
| Vendor owner is assigned. | | |
| Vendor data processing is understood. | | |
| Prompt and output retention is understood. | | |
| Training and product improvement use is understood. | | |
| Opt-out settings are reviewed where available. | | |
| Subprocessors are reviewed where required. | | |
| Processing location is understood. | | |
| Admin controls are reviewed. | | |
| Identity and permission model is understood. | | |
| Logs and evidence availability are reviewed. | | |
| Incident support path is defined. | | |
| Contract terms are reviewed where required. | | |
| Vendor risk decision is recorded. | | |

Related template:

```text
templates/ai-vendor-assessment-template.md
```

Common vendor AI risks:

- AI features enabled by default
- unclear data retention
- vendor use of prompts or outputs for training
- weak admin controls
- limited audit logs
- poor evidence export
- unclear incident support
- shared responsibility gaps

---

# 10. Customer-Facing AI Implementation Checklist

Use this checklist for AI that interacts with customers, suppliers, partners, or the public.

| Check | Yes / No / NA | Notes |
|---|---|---|
| Customer-facing use is recorded in inventory. | | |
| Business owner is assigned. | | |
| Customer impact is assessed. | | |
| Output boundaries are defined. | | |
| Prohibited outputs are defined. | | |
| Escalation triggers are defined. | | |
| Human review is required where appropriate. | | |
| Customer commitments are controlled. | | |
| Sensitive data handling is defined. | | |
| Complaint handling process is defined. | | |
| Correction or retraction process is defined. | | |
| Conversation logs are retained where required. | | |
| Legal/privacy review is completed where required. | | |
| Incident response path is defined. | | |

Common customer-facing AI risks:

- incorrect customer guidance
- unauthorized commitments
- harmful or inappropriate output
- privacy leakage
- inconsistent escalation
- poor correction process
- reputational impact

---

# 11. Decision-Supporting AI Implementation Checklist

Use this checklist when AI output influences a decision.

| Check | Yes / No / NA | Notes |
|---|---|---|
| Decision impact is documented. | | |
| Decision owner is assigned. | | |
| AI recommendation is separated from final decision. | | |
| Human review model is defined. | | |
| Reviewer has access to source material. | | |
| Reviewer can reject or override AI output. | | |
| Validation rules are defined. | | |
| Decision evidence is retained. | | |
| Output uncertainty is communicated where required. | | |
| Generated records are controlled. | | |
| Correction or override path is defined. | | |
| Output quality is monitored. | | |
| Assurance testing is completed. | | |

Related templates:

```text
templates/ai-output-and-decision-control-template.md
templates/ai-human-accountability-template.md
```

Common decision-supporting AI risks:

- AI recommendation treated as final decision
- weak reviewer context
- ceremonial human review
- missing decision evidence
- uncorrected generated records
- unclear accountability

---

# 12. Tool and Action Implementation Checklist

Use this checklist when AI can call tools, APIs, workflows, or perform actions.

| Check | Yes / No / NA | Notes |
|---|---|---|
| Tool inventory is complete. | | |
| Tool owners are assigned. | | |
| Tool permissions are approved. | | |
| Tool permissions are least privilege. | | |
| Actions are classified by risk. | | |
| High-risk actions require approval. | | |
| Approval gates cannot be bypassed. | | |
| Action boundaries are enforced. | | |
| Blast-radius limits are defined. | | |
| Tool calls are logged. | | |
| Actions are logged. | | |
| Abnormal tool use is monitored. | | |
| Kill switch is defined. | | |
| Rollback or compensation is defined. | | |
| Tool/action tests are completed. | | |

Related template:

```text
templates/ai-tool-and-action-control-template.md
```

---

# 13. Monitoring and Evidence Checklist

Use this checklist to confirm that AI activity is observable and reconstructable.

| Check | Yes / No / NA | Notes |
|---|---|---|
| Logging requirements are defined by risk tier. | | |
| AI event taxonomy is defined. | | |
| Prompt/input logging approach is defined. | | |
| Retrieval/context logging is defined where required. | | |
| Output logging is defined. | | |
| Decision evidence is retained where required. | | |
| Tool/action logs are captured where required. | | |
| Approval and exception logs are captured. | | |
| Policy violations are monitored. | | |
| Logs are protected. | | |
| Retention requirements are defined. | | |
| Evidence can be retrieved for review. | | |
| AI activity can be reconstructed where required. | | |
| Vendor logs are available where required. | | |

Related templates:

```text
templates/ai-monitoring-logging-evidence-template.md
templates/ai-control-evidence-package-template.md
```

---

# 14. Assurance Checklist

Use this checklist before deployment, after material change, or during periodic review.

| Check | Yes / No / NA | Notes |
|---|---|---|
| Assurance scope is defined. | | |
| Test plan is created. | | |
| Test cases are mapped to risk tier. | | |
| Identity and access controls are tested. | | |
| Data boundaries are tested. | | |
| Prompt injection is tested where required. | | |
| Data leakage is tested where required. | | |
| Retrieval boundaries are tested where required. | | |
| Output validation is tested where required. | | |
| Tool/action controls are tested where required. | | |
| Logging completeness is tested. | | |
| Evidence reconstruction is tested where required. | | |
| Kill switch is tested where required. | | |
| Rollback is tested where required. | | |
| Findings are tracked to closure. | | |
| Residual risk is accepted where required. | | |

Related template:

```text
templates/ai-assurance-test-plan-template.md
```

---

# 15. Incident Readiness Checklist

Use this checklist to confirm that AI failure can be contained.

| Check | Yes / No / NA | Notes |
|---|---|---|
| AI incident scenarios are defined. | | |
| Severity criteria are defined. | | |
| Incident owner is assigned. | | |
| Escalation path is defined. | | |
| Access revocation path is defined. | | |
| Agent/tool kill switch is defined where required. | | |
| Vendor feature disablement path is defined where required. | | |
| Output quarantine path is defined where required. | | |
| Workflow stop path is defined where required. | | |
| Evidence preservation checklist exists. | | |
| Recovery or correction path is defined. | | |
| Communication path is defined. | | |
| Restart criteria are defined. | | |
| Post-incident review process is defined. | | |

Related templates:

```text
templates/ai-incident-containment-recovery-template.md
templates/ai-incident-record-template.md
```

---

# 16. Exception Management Checklist

Use this checklist when a required control cannot be met.

| Check | Yes / No / NA | Notes |
|---|---|---|
| Exception requirement is identified. | | |
| Affected control objective is documented. | | |
| Business justification is documented. | | |
| Risk created by exception is assessed. | | |
| Compensating controls are defined. | | |
| Residual risk is documented. | | |
| Exception owner is assigned. | | |
| Risk acceptance owner is assigned. | | |
| Expiry date is defined. | | |
| Review date is defined. | | |
| Remediation plan is documented. | | |
| Approval is recorded. | | |
| Evidence is retained. | | |

Related template:

```text
templates/ai-exception-record-template.md
```

---

# 17. 30-Day Implementation Checklist

Use this checklist to start implementing AI control quickly.

| Action | Complete? | Owner |
|---|---|---|
| Establish an AI inventory. | | |
| Define AI use case intake process. | | |
| Define initial AI risk tiering model. | | |
| Identify existing AI use cases. | | |
| Identify embedded vendor AI features. | | |
| Assign business owners for known AI use cases. | | |
| Identify high-risk AI use cases. | | |
| Define minimum controls for Tier 1 to Tier 5. | | |
| Create exception process. | | |
| Define AI incident reporting path. | | |

---

# 18. 60-Day Implementation Checklist

Use this checklist after the basic inventory and intake process exist.

| Action | Complete? | Owner |
|---|---|---|
| Complete risk assessment for high-risk AI use cases. | | |
| Review identity and access for high-risk AI. | | |
| Map data sources for high-risk AI. | | |
| Review vendor AI processing and retention. | | |
| Define output and decision controls for decision-supporting AI. | | |
| Define tool/action controls for agentic AI. | | |
| Define logging requirements by risk tier. | | |
| Start assurance testing for high-risk AI. | | |
| Document control gaps and exceptions. | | |
| Create initial evidence packages for high-risk AI. | | |

---

# 19. 90-Day Implementation Checklist

Use this checklist to mature the operating model.

| Action | Complete? | Owner |
|---|---|---|
| Integrate AI intake with architecture review. | | |
| Integrate AI control assessment with security review. | | |
| Integrate AI risk decisions with GRC. | | |
| Integrate AI event logs with monitoring where appropriate. | | |
| Define AI assurance test catalogue. | | |
| Test kill switches for high-risk AI and agents. | | |
| Conduct tabletop exercise for AI incident scenarios. | | |
| Review open exceptions. | | |
| Define metrics for AI control maturity. | | |
| Report maturity and roadmap to governance forum. | | |

---

# 20. Ongoing Review Checklist

Use this checklist periodically.

| Check | Frequency | Owner |
|---|---|---|
| Review AI inventory. | Quarterly | |
| Review high-risk AI use cases. | Quarterly | |
| Review AI access. | Quarterly / semi-annually | |
| Review vendor AI features. | At renewal or material change | |
| Review open exceptions. | Monthly / quarterly | |
| Review assurance findings. | Monthly / quarterly | |
| Review AI incidents and near misses. | Monthly / quarterly | |
| Review logging and evidence gaps. | Quarterly | |
| Review kill switch and recovery tests. | Semi-annually / annually | |
| Review maturity roadmap. | Quarterly / annually | |

---

# 21. Definition of Done

An AI use case should not be considered control-ready until the following are true:

```text
[ ] AI use case is inventoried.
[ ] Business owner is assigned.
[ ] Risk tier is assigned.
[ ] Data sources are mapped.
[ ] Identity and authority model is defined.
[ ] Required controls are mapped.
[ ] Output and decision use is understood.
[ ] Tool and action capability is controlled.
[ ] Human accountability is assigned.
[ ] Logging and evidence requirements are defined.
[ ] Assurance testing is completed where required.
[ ] Exceptions are documented and approved.
[ ] Incident containment path exists.
[ ] Evidence is retained.
```

---

# Summary

Implementation should start small but become systematic.

The first goal is visibility.

The second goal is risk-tiering.

The third goal is control mapping.

The fourth goal is evidence.

The fifth goal is assurance.

The final goal is operational control: the ability to know what AI can see, decide, and do, and to contain it when it fails.