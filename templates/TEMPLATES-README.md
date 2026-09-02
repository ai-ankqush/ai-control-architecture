# Templates

This folder contains reusable templates for applying and extending the AI Control Architecture.

The templates are grouped into three categories:

1. Core operational templates
2. Advanced control templates
3. Authoring templates

Use the core templates first. Use the advanced templates when deeper control design is required. Use the authoring templates when contributing new pillars, requirements, or risk scenarios to the architecture.

---

# 1. Core Operational Templates

Core operational templates are used to assess, approve, evidence, and manage AI use cases.

These are the primary templates most organizations should start with.

| Template | Purpose | When to Use |
|---|---|---|
| `ai-use-case-intake-template.md` | Captures basic information about an AI use case. | Use first for any proposed, existing, embedded, or discovered AI capability. |
| `ai-risk-assessment-template.md` | Assesses AI risk across data, decisions, outputs, tools, autonomy, vendor, and recoverability. | Use after intake to determine risk and required controls. |
| `ai-control-assessment-template.md` | Reviews control readiness across the ten AI Control Architecture pillars. | Use before pilot, production, scaling, or continued operation. |
| `ai-architecture-decision-record-template.md` | Documents architecture decisions and rationale. | Use when making design decisions about identity, data, prompts, outputs, tools, logging, or containment. |
| `ai-assurance-test-plan-template.md` | Defines assurance test cases, expected results, evidence, findings, and sign-off. | Use when testing an AI use case before deployment or after material change. |
| `ai-vendor-assessment-template.md` | Assesses vendor AI features, SaaS AI, model providers, and third-party AI services. | Use before enabling, purchasing, integrating, or scaling vendor AI. |
| `ai-exception-record-template.md` | Documents temporary deviations from required controls. | Use when a control requirement cannot be met and risk must be accepted temporarily. |
| `ai-incident-record-template.md` | Records AI incidents, containment, investigation, recovery, and lessons learned. | Use when AI fails, leaks data, produces unsafe output, misuses tools, or causes business impact. |

---

# 2. Advanced Control Templates

Advanced control templates are used when a use case requires deeper design, evidence, or assurance for a specific control area.

These templates are optional, but useful for higher-risk AI, agentic AI, vendor AI, regulated AI, customer-facing AI, or AI with sensitive data or action capability.

| Template | Purpose | When to Use |
|---|---|---|
| `ai-inventory-record-template.md` | Creates a detailed AI inventory record. | Use when the organization wants a structured inventory entry for each AI capability. |
| `ai-risk-tiering-template.md` | Assigns a consistent AI risk tier. | Use when risk tiering needs to be separated from the broader risk assessment. |
| `ai-control-requirements-mapping-template.md` | Maps use cases to applicable requirements and evidence. | Use when traceability is needed between risk, requirements, controls, evidence, and assurance. |
| `ai-control-review-checklist-template.md` | Provides a lightweight review checklist. | Use for quick reviews or early-stage assessments. |
| `ai-control-maturity-assessment-template.md` | Assesses maturity across the ten pillars. | Use at enterprise, business unit, platform, or portfolio level. |
| `ai-control-evidence-package-template.md` | Packages control evidence for review, audit, assurance, or incident response. | Use when evidence must be assembled and reviewed formally. |
| `ai-identity-and-access-control-template.md` | Defines AI identity, delegated authority, access scope, and revocation. | Use when AI has system, data, tool, API, agent, or vendor-managed access. |
| `ai-data-boundary-template.md` | Defines AI data access, retrieval, retention, reuse, and output boundaries. | Use when AI processes enterprise, sensitive, regulated, or vendor-processed data. |
| `ai-prompt-and-input-control-template.md` | Defines allowed inputs, prohibited inputs, prompt injection controls, and system prompt protection. | Use when AI accepts prompts, files, retrieved content, external content, or tool responses. |
| `ai-output-and-decision-control-template.md` | Defines output validation, decision separation, human review, and correction paths. | Use when AI output influences decisions, records, customer communication, or downstream workflows. |
| `ai-tool-and-action-control-template.md` | Defines tool access, action classification, approval gates, logging, kill switches, and rollback. | Use when AI can call tools, APIs, workflows, or perform actions. |
| `ai-agent-control-template.md` | Defines controls for agentic AI. | Use when AI can plan, use tools, act with autonomy, or execute multi-step workflows. |
| `ai-human-accountability-template.md` | Defines ownership, review, approval, escalation, override, and risk acceptance. | Use when AI influences decisions, actions, exceptions, incidents, or business outcomes. |
| `ai-monitoring-logging-evidence-template.md` | Defines AI event logging, monitoring, evidence retention, and reconstructability. | Use when AI activity must be monitored, audited, investigated, or reconstructed. |
| `ai-incident-containment-recovery-template.md` | Defines how an AI use case can be contained and recovered. | Use for high-risk, action-capable, customer-facing, vendor, or agentic AI. |

---

# 3. Authoring Templates

Authoring templates are used by contributors who want to extend the AI Control Architecture itself.

Use these when adding new architecture content to the repository.

| Template | Purpose | When to Use |
|---|---|---|
| `pillar-template.md` | Provides a standard structure for new control pillars. | Use when adding a new pillar or major control domain. |
| `requirement-template.md` | Provides a standard structure for new requirements. | Use when adding or changing functional, non-functional, evidence, assurance, vendor, or incident requirements. |
| `risk-scenario-template.md` | Provides a standard structure for reusable AI risk scenarios. | Use when adding new risk scenarios, failure modes, or control risk patterns. |

---

# Recommended Use Sequence

For most AI use cases, use the templates in this order:

```text
1. ai-use-case-intake-template.md
2. ai-risk-assessment-template.md
3. ai-control-assessment-template.md
4. ai-architecture-decision-record-template.md
5. ai-assurance-test-plan-template.md
6. ai-control-evidence-package-template.md
```

If the AI use case involves a vendor, add:

```text
ai-vendor-assessment-template.md
```

If the AI use case involves an exception, add:

```text
ai-exception-record-template.md
```

If the AI use case involves an incident, add:

```text
ai-incident-record-template.md
```

If the AI use case involves agentic AI or action capability, add:

```text
ai-agent-control-template.md
ai-tool-and-action-control-template.md
ai-incident-containment-recovery-template.md
```

If the AI use case involves sensitive data, retrieval, RAG, or vendor processing, add:

```text
ai-data-boundary-template.md
ai-prompt-and-input-control-template.md
ai-monitoring-logging-evidence-template.md
```

If the AI use case influences decisions or records, add:

```text
ai-output-and-decision-control-template.md
ai-human-accountability-template.md
```

---

# Minimum Template Set

For a lightweight implementation, start with only these:

```text
ai-use-case-intake-template.md
ai-risk-assessment-template.md
ai-control-assessment-template.md
ai-assurance-test-plan-template.md
ai-exception-record-template.md
ai-incident-record-template.md
ai-vendor-assessment-template.md
```

This gives enough structure to register AI use cases, assess risk, review controls, test assurance, manage exceptions, respond to incidents, and review vendors.

---

# Full Template Set

For a mature implementation, use the full template set.

The full set supports:

- AI inventory
- risk tiering
- requirements traceability
- architecture decisions
- control assessments
- vendor assessments
- data boundaries
- identity and access controls
- prompt and input controls
- output and decision controls
- tool and action controls
- agent controls
- human accountability
- monitoring and evidence
- incident containment and recovery
- assurance testing
- exceptions
- evidence packages
- maturity assessment
- authoring new architecture content

---

# Template Usage Principles

When using these templates:

1. Keep responses plain and practical.
2. Avoid vendor-specific assumptions unless documenting a vendor assessment.
3. Map every high-risk use case to clear ownership.
4. Map every risk tier to required controls.
5. Map every required control to evidence.
6. Test controls before trusting them.
7. Retain enough evidence to reconstruct important AI activity.
8. Treat exceptions as temporary and owned.
9. Treat incidents as opportunities to improve the architecture.
10. Keep the architecture reusable, vendor-neutral, and brownfield-compatible.

---

# Contribution Guidance

When contributing a new template:

- Use clear headings.
- Keep language vendor-neutral.
- Make requirements testable.
- Include evidence expectations.
- Include ownership fields.
- Include approval fields where risk decisions are involved.
- Include review triggers.
- Avoid product-specific configuration unless the template is explicitly vendor-specific.
- Keep the structure consistent with existing templates.

---

# Summary

The templates are designed to turn the AI Control Architecture from a reference model into something that can be applied.

Use the core templates to start.

Use the advanced templates when risk, complexity, autonomy, vendor dependency, data sensitivity, or assurance needs increase.

Use the authoring templates to extend the architecture in a consistent way.