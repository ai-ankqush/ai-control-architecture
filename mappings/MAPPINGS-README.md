# Standards and Framework Mappings

This folder contains mappings between the AI Control Architecture and external standards, regulations, and security guidance.

The purpose of these mappings is to show how the AI Control Architecture can help enterprises operationalize existing AI governance, risk, compliance, security, privacy, and assurance expectations.

The AI Control Architecture is not intended to replace external standards.

It is intended to help implement them.

---

# Positioning

The AI Control Architecture should be understood as:

```text
A technical and operational implementation layer for enterprise AI governance, risk, assurance, and control requirements.
```

It helps translate high-level governance expectations into practical enterprise controls around:

```text
AI inventory
AI ownership
AI risk tiering
AI identity and access
Data boundaries
Prompt and input controls
Output and decision controls
Tool and action controls
Human accountability
Assurance and testing
Monitoring, logging, and evidence
Incident containment and recovery
```

---

# Why Mappings Matter

Large enterprises rarely adopt AI governance from a blank page.

They already operate against standards, regulations, frameworks, and internal control systems.

These may include:

```text
NIST AI Risk Management Framework
ISO/IEC 42001
EU AI Act
OWASP Top 10 for LLM Applications
Internal GRC control libraries
Privacy impact assessment processes
Vendor risk management processes
Security architecture review processes
Audit and assurance programs
```

Without mappings, the AI Control Architecture may appear to be a competing framework.

With mappings, it becomes an accelerator.

---

# Core Mapping Principle

External standards often define:

```text
What outcomes should be achieved.
```

The AI Control Architecture helps define:

```text
How those outcomes can be operationalized inside enterprise systems, data, identity, workflows, vendors, assurance, and incident response.
```

Example:

```text
External standard expectation:
AI systems should be governed, risk-managed, monitored, transparent, and subject to human oversight.

AI Control Architecture implementation layer:
Inventory AI use cases, assign owners, classify risk, define identity and access, control data boundaries, validate outputs, restrict tools/actions, retain evidence, test controls, and define containment paths.
```

---

# Initial Mapping Targets

The initial mapping targets are:

```text
NIST AI Risk Management Framework
ISO/IEC 42001
EU AI Act
OWASP Top 10 for LLM Applications
OWASP guidance for agentic AI, where applicable
```

These were selected because they represent common enterprise concerns across:

```text
AI governance
AI risk management
AI management systems
AI regulatory obligations
AI application security
AI assurance
AI incident readiness
```

---

# Mapping Files

Planned mapping files include:

```text
mappings/nist-ai-rmf-crosswalk.md
mappings/iso-42001-crosswalk.md
mappings/eu-ai-act-crosswalk.md
mappings/owasp-llm-crosswalk.md
mappings/owasp-agentic-ai-crosswalk.md
mappings/sr-11-7-crosswalk.md
mappings/nydfs-part-500-crosswalk.md
mappings/us-state-ai-laws-crosswalk.md
```

---

# Mapping Status

| Mapping | Status | Purpose |
|---|---|---|
| NIST AI RMF | Planned | Map AI Control Architecture pillars to Govern, Map, Measure, and Manage functions. |
| ISO/IEC 42001 | Planned | Map AI Control Architecture controls to AI management system expectations. |
| EU AI Act | Planned | Map AI Control Architecture controls to high-risk AI governance, documentation, logging, transparency, oversight, robustness, and incident expectations. |
| OWASP LLM Top 10 | Planned | Map AI security controls to LLM application threat categories. |
| OWASP Agentic AI | Planned | Map agent controls to agentic AI risks such as excessive agency, tool misuse, and containment failure. |
| SR 11-7 (Model Risk Management) | Available | Map pillars to model development/use, validation and effective challenge, and governance/controls for AI and ML models (US banking). |
| NYDFS 23 NYCRR Part 500 | Available | Map pillars to the New York DFS cybersecurity program through the NYDFS AI-cyber lens (US financial services). |
| US State AI Laws (appendix) | Available | Map pillars to the recurring obligations across state AI laws (Colorado, Texas, California, Utah, NYC, Illinois). Volatile; confirm current law. |

---

# AI Control Architecture Pillars

Mappings should use the ten AI Control Architecture pillars as the primary internal structure.

| Pillar | Control Focus |
|---|---|
| AI inventory and classification | Visibility, ownership, lifecycle, and risk tiering |
| AI identity and access control | AI identities, delegated authority, least privilege, revocation, attribution |
| Data boundary control | Data sources, classification, retrieval, retention, reuse, exposure |
| Prompt and input control | Prompts, files, external inputs, retrieved context, prompt injection |
| Output and decision control | Output validation, decision separation, generated records, correction |
| Tool and action control | Tools, APIs, workflows, actions, approval gates, kill switches, rollback |
| Human accountability model | Business ownership, decision ownership, review, approval, escalation |
| AI assurance and testing | Control testing, adversarial testing, regression testing, findings |
| Monitoring, logging, and evidence | Logs, event taxonomy, evidence packages, reconstructability |
| Incident containment and recovery | Incident scenarios, containment, recovery, restart criteria, lessons learned |

---

# How to Read the Mappings

Each mapping should answer:

```text
Which external requirement or concept is relevant?
Which AI Control Architecture pillar supports it?
Which control objectives or requirements help operationalize it?
What evidence would prove implementation?
What assurance tests could validate it?
```

A useful mapping should not only say:

```text
This maps to that.
```

It should also explain:

```text
What enterprise control activity should happen because of this mapping?
```

---

# Mapping Format

Recommended mapping table format:

| External Framework Area | AI Control Architecture Pillar | Implementation Interpretation | Example Evidence |
|---|---|---|---|
| [External requirement or concept] | [Relevant pillar] | [How the architecture operationalizes it] | [Evidence] |

Where useful, add:

```text
Example controls
Example assurance tests
Related templates
Related documents
```

---

# Important Disclaimer

These mappings are intended to support enterprise governance, risk, compliance, security, and assurance work.

They are not legal advice.

They do not guarantee compliance with any regulation, certification, standard, contract, procurement requirement, or audit expectation.

Organizations should consult qualified legal, compliance, privacy, audit, and regulatory advisors when determining formal obligations.

---

# Sources and References

The NIST AI Risk Management Framework Core is organized around four functions: Govern, Map, Measure, and Manage. These functions are intended to help organizations manage AI risks and responsibly develop trustworthy AI systems.

ISO/IEC 42001 is an AI management system standard intended for organizations that provide or use AI-based products or services.

The EU AI Act includes requirements for high-risk AI systems relating to risk management, data governance, technical documentation, record-keeping, transparency, human oversight, accuracy, robustness, and cybersecurity.

OWASP publishes security guidance for LLM applications, including risks specific to LLM application design and operation.

---

# Related Project Files

```text
README.md
QUICKSTART.md
ROADMAP.md
docs/06-requirements-catalogue.md
docs/17-implementation-checklists.md
docs/19-common-ai-control-patterns.md
docs/20-common-failure-scenarios.md
docs/24-assurance-and-audit-guide.md
templates/ai-control-assessment-template.md
templates/ai-assurance-test-plan-template.md
templates/ai-control-evidence-package-template.md
```

---

# Summary

The mappings folder exists to make the AI Control Architecture easier to adopt in real enterprises.

The goal is to connect the architecture to the standards and frameworks organizations already care about, while preserving the project’s core purpose:

```text
Adopt AI faster without losing control.