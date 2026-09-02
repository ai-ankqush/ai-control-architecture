# Roadmap

This roadmap describes the planned direction for the AI Control Architecture project.

The project is currently in an initial public draft state.

The goal of the roadmap is to make the project easier to use, easier to adopt, and easier to operationalize over time.

---

# Current Version

```text
v0.1.0: Initial Public Draft
```

## Current Focus

The current version establishes the foundation:

- core thesis
- architecture principles
- reference architecture
- requirements catalogue
- ten control pillars
- implementation guidance
- maturity model
- common AI control patterns
- common AI failure scenarios
- adoption playbook
- governance and operating model
- metrics and reporting
- assurance and audit guide
- glossary
- templates
- filled examples
- quickstart guide
- contribution guide
- open license (CC BY 4.0)
- trademark and conformance note

---

# Roadmap Principles

Future versions should make the AI Control Architecture:

```text
More usable
More practical
More operational
More testable
More visual
More mapped to real enterprise processes
```

The project should avoid becoming documentation-heavy without improving usability.

Future work should prioritize:

- examples
- mappings
- checklists
- diagrams
- implementation aids
- assurance tests
- control mappings
- practical adoption guidance

---

# v0.1.0: Initial Public Draft

## Status

```text
Complete
```

## Purpose

Establish the first complete public version of the AI Control Architecture.

## Included

```text
README.md
QUICKSTART.md
WHY_THIS_EXISTS.md
CONTRIBUTING.md
CHANGELOG.md
LICENSE
docs/
templates/
examples/
```

## Main Outcome

The project now has a complete architecture foundation that explains:

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

# v0.2.0: Operationalization and Standards Mapping

## Goal

Make the AI Control Architecture easier to adopt inside real enterprises by connecting it to existing standards, reducing low-risk governance friction, and preparing the architecture for workflow and GRC integration.

The purpose of v0.2.0 is to move from:

```text
Architecture documentation
```

to:

```text
Operational adoption
```

This version should help enterprises understand how the AI Control Architecture supports existing governance, risk, security, compliance, audit, and engineering workflows.

---

## Priority 1: Standards Crosswalks

Large enterprises already operate against existing standards, regulations, and assurance expectations.

The AI Control Architecture should not compete with these frameworks.

It should help operationalize them.

Initial crosswalks should map the ten AI Control Architecture pillars and core requirements to:

```text
NIST AI Risk Management Architecture
ISO/IEC 42001
EU AI Act
OWASP Top 10 for LLM Applications
OWASP guidance for agentic AI, where applicable
```

## Positioning

The architecture should be positioned as:

```text
The technical and operational implementation layer for enterprise AI governance, risk, assurance, and control requirements.
```

It should not be positioned as a replacement for NIST, ISO, EU AI Act obligations, OWASP, internal GRC, privacy review, legal review, or audit programs.

## Potential Files

```text
mappings/MAPPINGS-README.md
mappings/nist-ai-rmf-crosswalk.md
mappings/iso-42001-crosswalk.md
mappings/eu-ai-act-crosswalk.md
mappings/owasp-llm-crosswalk.md
mappings/owasp-agentic-ai-crosswalk.md
```

---

## Priority 2: Triage and Minimum-Control Flow

The architecture must avoid becoming governance theater.

Not every AI use case should require a full documentation pack.

Low-risk AI should move quickly through lightweight review, while higher-risk AI should receive deeper control, evidence, and assurance.

## Triage Principle

```text
Control depth should scale with risk tier.
```

## Intended Direction

Define a strict triage flow:

```text
Tier 1: Minimal intake and acceptable use confirmation.
Tier 2: Data and vendor review where applicable.
Tier 3: Decision owner, output validation, human review, and evidence.
Tier 4: Tool/action control, approval gates, logging, kill switch, and rollback assessment.
Tier 5: Enhanced assurance, reconstructable evidence, incident tabletop, containment testing, and risk acceptance.
```

## Potential File

```text
docs/25-triage-and-minimum-controls.md
```

## Success Criteria

Users should be able to determine quickly:

```text
Can this AI use case be fast-tracked?
Does it require data review?
Does it require vendor review?
Does it require decision accountability?
Does it require tool/action controls?
Does it require full assurance and evidence?
```

---

## Priority 3: Machine-Readable Control Catalogue

The current version uses Markdown templates because they are easy to read, review, and adapt.

Future versions should begin converting core requirements and controls into machine-readable structures.

This will make it easier to integrate the architecture with:

```text
GRC platforms
ServiceNow
Jira
OneTrust
Archer
developer portals
CI/CD pipelines
internal control libraries
evidence repositories
audit workflows
```

## Initial Direction

Start simple before attempting complex control automation.

Potential early formats:

```text
YAML
JSON
CSV
```

Potential later formats:

```text
OSCAL
GRC import formats
control testing datasets
schema-based intake forms
```

## Potential Files

```text
controls/ai-control-pillars.yaml
controls/ai-risk-tiers.yaml
controls/ai-control-requirements.yaml
controls/ai-assurance-tests.yaml
schemas/ai-use-case.schema.json
schemas/ai-control-assessment.schema.json
```

## Success Criteria

The architecture should begin moving from:

```text
Documents humans read
```

to:

```text
Controls systems can ingest
```

---

## Priority 4: Threat Modeling and OWASP Alignment

The architecture should explicitly connect AI control design to recognized AI security threat categories.

This includes mapping relevant controls to:

```text
OWASP Top 10 for LLM Applications
OWASP Agentic AI guidance where applicable
```

## Focus Areas

```text
Prompt injection
Sensitive information disclosure
Insecure output handling
Excessive agency
Tool misuse
Insecure plugin or tool design
Supply chain risk
Model or prompt manipulation
Logging and monitoring gaps
Incident response gaps
```

## Intended Enhancements

Strengthen assurance and testing guidance for:

```text
Adversarial prompt testing
Retrieval boundary testing
Execution boundary testing
Tool/action misuse testing
Approval bypass testing
Evidence reconstruction testing
Agent containment testing
```

## Success Criteria

Security, AppSec, SOC, and red-team teams should be able to map the architecture to known AI threat categories and convert controls into tests.

---

## Priority 5: Human Review and Contextual Reconstructability

The architecture already warns against ceremonial human review.

v0.2.0 should make this more operational.

Human review should not be treated as a checkbox.

A human reviewer must receive enough context to make a valid approval, rejection, escalation, or override decision.

## New Concept

```text
Contextual Reconstructability
```

## Definition

```text
A human reviewer or approver must be shown enough evidence, context, source material, AI reasoning summary, risk indicators, and action impact to understand what they are approving and why.
```

## Intended Enhancements

Human review controls should define:

```text
What the reviewer must see
What evidence must be available
What source material must be linked
What risk indicators must be shown
What alternatives or uncertainty must be disclosed
What authority the reviewer has
How rejection, override, or escalation is recorded
```

## Success Criteria

The architecture should distinguish between:

```text
A human clicking approve
```

and:

```text
A human making an informed, evidenced, accountable decision
```

---

## Priority 6: Vendor AI Hardening

Most enterprise AI adoption will enter through vendor platforms and SaaS updates, not only through internally built AI systems.

v0.2.0 should strengthen vendor AI control expectations.

## Vendor AI Principle

```text
No vendor AI feature should be enabled for enterprise data processing without explicit control-plane approval.
```

## Intended Enhancements

Vendor AI review should explicitly address:

```text
Whether AI features are enabled by default
Whether admins can disable AI features centrally
Whether the vendor uses third-party model providers
Which subprocessors process prompts, outputs, embeddings, files, or telemetry
Whether prompts and outputs are retained
Whether customer data is used for training or product improvement
Whether AI feature changes are announced before activation
Whether logs can be exported during incident response
Whether vendor evidence is sufficient for audit and incident reconstruction
```

## Success Criteria

The architecture should help enterprises control AI features introduced through routine vendor updates, not only AI systems they intentionally build.

---

## v0.2.0 Success Criteria

v0.2.0 should be considered successful when the project includes:

```text
[ ] Standards mapping starter
[ ] OWASP mapping starter
[ ] Triage and minimum-control flow
[ ] Updated roadmap for machine-readable controls
[ ] Stronger vendor AI default-off principle
[ ] Human review contextual reconstructability concept
[ ] Clearer positioning as an implementation layer for existing standards
```

---

## v0.2.0 Outcome

The project should become easier for enterprises to adopt because it will answer:

```text
How does this map to standards we already care about?
How do we avoid heavy paperwork for low-risk AI?
How do we plug this into GRC and engineering workflows?
How do security teams map this to AI threat models?
How do we make human review meaningful?
How do we control vendor AI features before they are enabled?
```

# v0.3.0: Control Mapping and Traceability

## Goal

Improve traceability between risks, pillars, requirements, controls, evidence, and assurance tests.

## Potential Additions

- risk-to-control mapping
- pillar-to-requirement mapping
- requirement-to-evidence mapping
- requirement-to-assurance mapping
- template-to-use-case mapping
- risk tier to minimum control baseline mapping

## Possible Files

```text
docs/control-mapping-guide.md
docs/risk-to-control-mapping.md
docs/requirement-to-evidence-mapping.md
docs/risk-tier-control-baseline.md
```

## Success Criteria

Users should be able to trace:

```text
Risk scenario
    ↓
Control objective
    ↓
Requirement
    ↓
Evidence
    ↓
Assurance test
    ↓
Incident containment
```

---

# v0.4.0: Diagrams and Visual Architecture

## Goal

Add visual diagrams that explain the architecture quickly.

## Potential Diagrams

- AI Control Architecture overview
- ten-pillar model
- AI use case lifecycle
- AI control review flow
- AI risk tiering flow
- AI evidence flow
- AI incident containment flow
- AI agent control model
- RAG control model
- vendor AI review model

## Possible Files

```text
diagrams/
diagrams/ai-control-architecture-overview.md
diagrams/ai-use-case-lifecycle.md
diagrams/ai-agent-control-model.md
diagrams/rag-control-model.md
diagrams/vendor-ai-control-model.md
```

## Success Criteria

Users should be able to understand the architecture visually without reading every document.

---

# v0.5.0: More Filled Examples

## Goal

Add more completed examples for common enterprise AI use cases.

## Potential Examples

```text
examples/customer-facing-ai-example.md
examples/developer-ai-example.md
examples/security-operations-ai-example.md
examples/high-impact-ai-example.md
examples/ai-enabled-hr-use-case-example.md
examples/ai-enabled-finance-use-case-example.md
examples/ai-generated-record-example.md
```

## Success Criteria

Users should be able to find an example close to their real-world AI use case.

---

# v0.6.0: Assurance Test Catalogue

## Goal

Create reusable assurance tests for common AI control risks.

## Potential Test Categories

- AI inventory tests
- risk tiering tests
- identity and access tests
- data boundary tests
- retrieval boundary tests
- prompt injection tests
- output validation tests
- decision accountability tests
- tool/action tests
- approval gate tests
- logging completeness tests
- evidence reconstruction tests
- kill switch tests
- rollback tests
- vendor evidence tests

## Possible Files

```text
docs/assurance-test-catalogue.md
templates/assurance-test-case-template.md
examples/assurance-test-results-example.md
```

## Success Criteria

Users should be able to convert architecture requirements into practical tests.

---

# v0.7.0: Enterprise Adoption Toolkit

## Goal

Create practical materials that help teams introduce the architecture inside an organization.

## Potential Additions

- executive briefing outline
- workshop agenda
- AI control assessment workshop guide
- 30/60/90-day implementation pack
- stakeholder interview questions
- AI control maturity questionnaire
- AI governance operating cadence example

## Possible Files

```text
toolkit/executive-briefing-outline.md
toolkit/workshop-agenda.md
toolkit/stakeholder-interview-guide.md
toolkit/30-60-90-implementation-pack.md
toolkit/maturity-questionnaire.md
```

## Success Criteria

Users should be able to use the architecture in an enterprise workshop or assessment.

---

# v0.8.0: Vendor AI Review Expansion

## Goal

Strengthen vendor AI review guidance.

## Potential Additions

- vendor AI due diligence checklist
- vendor AI contract questions
- vendor AI evidence request list
- vendor AI feature enablement checklist
- vendor AI logging and incident support checklist
- vendor AI shared responsibility model

## Possible Files

```text
docs/vendor-ai-review-guide.md
templates/vendor-ai-evidence-request-template.md
templates/vendor-ai-contract-review-template.md
examples/vendor-ai-assessment-example.md
```

## Success Criteria

Users should be able to evaluate SaaS AI and vendor AI before enablement or renewal.

---

# v0.9.0: Agent and Tool Control Expansion

## Goal

Strengthen agentic AI and tool/action control content.

## Potential Additions

- agent identity patterns
- tool access patterns
- approval gate patterns
- blast-radius design patterns
- kill switch patterns
- rollback and compensation models
- agent incident scenarios
- tool misuse test cases

## Possible Files

```text
docs/agent-control-patterns.md
docs/tool-action-control-patterns.md
docs/agent-incident-scenarios.md
templates/agent-readiness-review-template.md
```

## Success Criteria

Users should be able to design and review agentic AI controls before deployment.

---

# v1.0.0: Stable Reference Release

## Goal

Publish a stable version of the AI Control Architecture.

## Criteria for v1.0.0

Before v1.0.0, the project should have:

```text
[ ] stable README
[ ] stable quickstart
[ ] stable ten-pillar model
[ ] stable requirements catalogue
[ ] stable templates
[ ] stable examples
[ ] complete cross-linking
[ ] reduced duplication
[ ] completed roadmap review
[ ] clear version history
[ ] reviewed license language
[ ] reviewed contribution model
```

## v1.0.0 Outcome

The project should be ready to serve as a stable reference model for:

- enterprise AI governance
- AI security architecture
- AI risk management
- AI assurance
- vendor AI review
- agent control design
- audit preparation
- AI incident readiness

---

# Future Ideas

The following ideas may be considered after v1.0.0.

## Control Mappings

Potential mappings to:

```text
NIST AI RMF
ISO/IEC AI management standards
ISO 27001 control domains
SOC 2 trust service criteria
COBIT
ITIL
privacy impact assessment processes
vendor risk management processes
enterprise architecture review processes
```

These should be added carefully and only where useful.

---

## Machine-Readable Controls

Potential future formats:

```text
YAML control catalogue
JSON requirements catalogue
CSV risk-control mapping
GRC import format
control testing dataset
```

---

## Assessment Workbook

Potential workbook formats:

```text
spreadsheet-based maturity assessment
control assessment tracker
AI inventory tracker
risk tiering workbook
vendor AI review tracker
```

---

## Diagrams

Potential diagram formats:

```text
Mermaid diagrams
architecture flow diagrams
control lifecycle diagrams
agent control diagrams
RAG boundary diagrams
incident containment diagrams
```

---

# Contribution Priorities

The most useful contributions are:

```text
Filled examples
Practical assurance tests
Risk-to-control mappings
Evidence examples
Implementation checklists
Control diagrams
Vendor AI review improvements
Agent control improvements
Glossary improvements
```

Lower priority contributions:

```text
More abstract theory
More policy language
More generic AI commentary
Vendor-specific marketing
Model benchmark comparisons
```

---

# Versioning Approach

This project uses simple semantic-style versioning:

```text
0.1.0 = Initial public draft
0.2.0 = Significant additions or usability improvements
0.x.0 = Major pre-1.0 content expansion
1.0.0 = Stable reference release
```

Small corrections may be tracked in the changelog without changing the overall direction of the roadmap.

---

# Current Priority

The immediate priority after v0.1.0 is not more long-form documentation.

The immediate priority is:

```text
Usability
Examples
Mappings
Diagrams
Assurance tests
Operational adoption aids
```

The architecture should become easier to apply, not just larger.

---

# Summary

The AI Control Architecture roadmap moves from:

```text
Architecture foundation
    ↓
Usability
    ↓
Traceability
    ↓
Visual models
    ↓
Examples
    ↓
Assurance tests
    ↓
Adoption toolkit
    ↓
Stable reference release
```

The goal is to help enterprises adopt AI faster without losing control.