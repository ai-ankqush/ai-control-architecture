# Quickstart

This quickstart helps you apply the AI Control Architecture without reading the full repository first.

Use it when you need to review, approve, assess, or control an AI use case quickly.

---

# 1. What This Architecture Helps You Do

The AI Control Architecture helps answer six practical questions:

```text
What AI exists?
What can AI see?
What can AI decide?
What can AI do?
Who is accountable?
How is failure evidenced and contained?
```

Use it for:

- copilots
- AI-enabled SaaS
- embedded vendor AI
- RAG systems
- internal LLM applications
- agents
- workflow automation
- customer-facing AI
- decision-supporting AI
- developer AI tools
- security operations AI

---

# 2. Fastest Way to Start

For any AI use case, follow this sequence:

```text
1. Record the AI use case.
2. Assign a business owner.
3. Identify the AI pattern.
4. Assign a risk tier.
5. Apply the minimum controls for that tier.
6. Test required controls.
7. Keep evidence.
8. Define how to contain failure.
```

---

# 3. Step 1: Record the AI Use Case

Start by documenting the AI capability.

Ask:

```text
What is the AI use case?
Who wants to use it?
What business process does it support?
Is it already in use?
Is it internal, vendor-provided, customer-facing, or agentic?
```

Use:

```text
templates/ai-use-case-intake-template.md
```

Minimum information to capture:

```text
Use case name:
Business purpose:
Business owner:
Technical owner:
AI pattern:
Users:
Vendor involved:
Data used:
Decision impact:
Tool/action capability:
Lifecycle status:
```

---

# 4. Step 2: Assign Ownership

Every AI use case needs accountable human ownership.

At minimum, assign:

```text
Business owner:
Technical owner:
Data owner, if sensitive or enterprise data is used:
Decision owner, if AI influences decisions:
Vendor owner, if vendor AI is involved:
Incident contact:
```

Remember:

```text
AI can assist.
AI can recommend.
AI can generate.
AI can act within limits.

But AI cannot own the outcome.
```

---

# 5. Step 3: Identify the AI Pattern

Classify the AI use case.

Select one or more:

```text
[ ] Copilot
[ ] RAG system
[ ] Internal LLM application
[ ] AI-enabled SaaS
[ ] Embedded vendor AI
[ ] Agent
[ ] AI-enabled workflow automation
[ ] Customer-facing AI
[ ] Developer AI tool
[ ] Security operations AI
[ ] Decision-supporting AI
[ ] Action-capable AI
[ ] High-impact or regulated AI
```

Use:

```text
docs/19-common-ai-control-patterns.md
```

---

# 6. Step 4: Assign a Risk Tier

Use risk tiering to decide how much control is required.

| Tier | Description | Typical Use |
|---|---|---|
| Tier 1 | Low-risk productivity or public-data use | Drafting, brainstorming, public content |
| Tier 2 | Internal productivity with enterprise data | Internal summarization, internal knowledge assistant |
| Tier 3 | Decision-supporting AI | Recommendations, scoring, prioritization, generated records |
| Tier 4 | Action-capable AI | Tool calls, workflow triggers, record updates, communications |
| Tier 5 | High-impact autonomous or regulated AI | Regulated, privileged, production, financial, legal, HR, security, or autonomous AI |

Use:

```text
templates/ai-risk-assessment-template.md
templates/ai-risk-tiering-template.md
```

Simple rule:

```text
If AI influences decisions, start at Tier 3.
If AI can perform actions, start at Tier 4.
If AI is regulated, autonomous, privileged, production-critical, or hard to reverse, start at Tier 5.
```

---

# 7. Step 5: Apply Minimum Controls

Use the risk tier to select minimum controls.

| Risk Tier | Minimum Controls |
|---|---|
| Tier 1 | Inventory, owner, acceptable use guidance, basic data restriction |
| Tier 2 | Tier 1 controls plus data source mapping, data classification, access boundary, vendor review where applicable |
| Tier 3 | Tier 2 controls plus decision owner, output validation, human review, decision evidence, correction path, assurance testing |
| Tier 4 | Tier 3 controls plus tool inventory, action classification, approval gates, tool/action logging, kill switch or revocation path, rollback assessment |
| Tier 5 | Tier 4 controls plus enhanced assurance, full reconstructable evidence, incident tabletop, tested containment, risk acceptance, ongoing monitoring |

Use:

```text
templates/ai-control-assessment-template.md
docs/17-implementation-checklists.md
```

---

# 8. Step 6: Ask the Three Control Questions

For every AI use case, ask:

## What can AI see?

Check:

```text
Data sources
Documents
Emails
Chats
Tickets
Customer records
Employee records
Source code
Logs
Vendor data access
Retrieved context
```

Controls:

```text
Data classification
Data owner approval
Retrieval boundary
Permission inheritance
Retention and reuse rules
Vendor processing review
```

---

## What can AI decide?

Check whether AI output influences:

```text
Customer decisions
Employee decisions
Financial decisions
Legal or compliance decisions
Security decisions
Access decisions
Operational decisions
Generated records
Workflow routing
```

Controls:

```text
Decision owner
Output validation
Human review
Recommendation vs final decision separation
Decision evidence
Correction path
```

---

## What can AI do?

Check whether AI can:

```text
Call tools
Call APIs
Trigger workflows
Create records
Modify records
Send communications
Change access
Execute code
Perform security actions
Affect production systems
```

Controls:

```text
Tool inventory
Action classification
Least privilege
Approval gates
Tool/action logging
Kill switch
Rollback or compensation
Incident containment
```

---

# 9. Step 7: Test Before Trust

For low-risk AI, basic review may be enough.

For higher-risk AI, test the controls.

Important tests include:

```text
[ ] Data leakage test
[ ] Retrieval boundary test
[ ] Prompt injection test
[ ] Output validation test
[ ] Decision evidence test
[ ] Tool/action test
[ ] Approval gate test
[ ] Logging completeness test
[ ] Evidence reconstruction test
[ ] Kill switch test
[ ] Rollback test
```

Use:

```text
templates/ai-assurance-test-plan-template.md
docs/24-assurance-and-audit-guide.md
```

---

# 10. Step 8: Keep Evidence

For high-risk AI, evidence should show:

```text
What was approved?
Who approved it?
What risk tier applies?
What data can AI access?
What output can AI produce?
What decision can AI influence?
What tool or action can AI use?
What tests were performed?
What findings exist?
What exceptions exist?
What incident path exists?
```

Use:

```text
templates/ai-control-evidence-package-template.md
```

---

# 11. Step 9: Prepare for Failure

Before approving high-risk AI, answer:

```text
How do we disable it?
How do we revoke access?
How do we stop tool use?
How do we quarantine bad output?
How do we roll back or correct actions?
How do we preserve evidence?
Who owns the incident?
Who approves restart?
```

Use:

```text
templates/ai-incident-containment-recovery-template.md
templates/ai-incident-record-template.md
```

---

# 12. Quick Review Checklist

Use this for any AI use case.

| Question | Answer |
|---|---|
| Is the AI use case inventoried? |  |
| Is a business owner assigned? |  |
| Is the AI pattern identified? |  |
| Is the risk tier assigned? |  |
| Are data sources mapped? |  |
| Is sensitive data involved? |  |
| Is vendor AI involved? |  |
| Does AI influence decisions? |  |
| Can AI call tools or perform actions? |  |
| Is human accountability defined? |  |
| Are required controls mapped? |  |
| Has assurance testing been completed where required? |  |
| Does evidence exist? |  |
| Are exceptions documented? |  |
| Can the AI capability be contained if it fails? |  |

---

# 13. Common Starting Paths

## If you are reviewing a new AI use case

Use:

```text
templates/ai-use-case-intake-template.md
templates/ai-risk-assessment-template.md
templates/ai-control-assessment-template.md
```

---

## If you are reviewing vendor AI

Use:

```text
templates/ai-vendor-assessment-template.md
docs/19-common-ai-control-patterns.md
```

Focus on:

```text
Data processing
Retention
Training/reuse
Admin controls
Logs and evidence
Incident support
Feature disablement
```

---

## If you are reviewing RAG

Use:

```text
templates/ai-data-boundary-template.md
docs/19-common-ai-control-patterns.md
```

Focus on:

```text
Data sources
Retrieval boundaries
Permission inheritance
Sensitive source exclusion
Prompt injection in retrieved content
Retrieval logs
Source attribution
```

---

## If you are reviewing an agent

Use:

```text
templates/ai-agent-control-template.md
templates/ai-tool-and-action-control-template.md
templates/ai-incident-containment-recovery-template.md
```

Focus on:

```text
Agent identity
Autonomy level
Delegated authority
Tool inventory
Action classification
Approval gates
Blast-radius limits
Kill switch
Rollback
Monitoring
```

---

## If you are auditing AI controls

Use:

```text
docs/24-assurance-and-audit-guide.md
templates/ai-control-evidence-package-template.md
templates/ai-assurance-test-plan-template.md
```

Focus on:

```text
Control design
Control operation
Evidence completeness
Findings
Exceptions
Reconstructability
Incident readiness
```

---

# 14. Minimum First Implementation

For an organization starting from zero:

```text
1. Create AI inventory.
2. Identify known AI use cases.
3. Identify embedded vendor AI.
4. Assign business owners.
5. Risk-tier each use case.
6. Prioritize Tier 3, Tier 4, and Tier 5.
7. Complete risk and control assessments for high-risk AI.
8. Review vendor AI.
9. Define evidence requirements.
10. Define incident containment paths.
```

---

# 15. What to Read Next

## For the architecture

```text
docs/01-executive-summary.md
docs/02-introduction.md
docs/03-core-thesis.md
docs/04-architecture-principles.md
docs/05-reference-architecture.md
```

## For implementation

```text
docs/17-implementation-checklists.md
docs/21-adoption-playbook.md
docs/22-governance-and-operating-model.md
```

## For controls by pattern

```text
docs/19-common-ai-control-patterns.md
```

## For common failures

```text
docs/20-common-failure-scenarios.md
```

## For maturity and reporting

```text
docs/18-control-maturity-model.md
docs/23-metrics-and-reporting.md
```

## For assurance and audit

```text
docs/24-assurance-and-audit-guide.md
```

## For vocabulary

```text
docs/26-glossary.md
```

---

# 16. Core Message

The fastest way to apply the AI Control Architecture is to ask:

```text
What AI exists?
What can it see?
What can it decide?
What can it do?
Who is accountable?
What evidence exists?
How do we contain failure?
```

Then apply risk-tiered controls.

The goal is simple:

```text
Adopt AI faster without losing control.
```