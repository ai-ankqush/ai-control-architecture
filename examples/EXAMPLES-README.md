# Examples

This folder contains filled examples showing how to apply the AI Control Architecture to common enterprise AI patterns.

These examples are not blank templates.

They are sample completed records that demonstrate how to think through:

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

# Available Examples

| Example | AI Pattern | Use This When |
|---|---|---|
| `copilot-use-case-example.md` | Enterprise copilot / AI-enabled SaaS / employee-facing AI | Reviewing broad productivity AI, copilots, or embedded workplace AI features. |
| `rag-assistant-example.md` | RAG system / internal LLM application / knowledge assistant | Reviewing AI that retrieves enterprise documents, policies, knowledge, or records. |
| `agentic-ai-example.md` | Agent / tool-using AI / workflow automation | Reviewing AI that can plan, use tools, request actions, route work, or affect workflows. |
| `vendor-ai-example.md` | AI-enabled SaaS / embedded vendor AI / decision-supporting AI | Reviewing AI features provided by SaaS vendors or third-party platforms. |

---

# How to Use These Examples

Use these examples to understand how the architecture is applied in practice.

Recommended approach:

```text
1. Pick the example closest to your AI use case.
2. Compare your use case against the example.
3. Identify what AI can see, decide, and do.
4. Assign the likely risk tier.
5. Identify required controls.
6. Identify missing evidence.
7. Decide whether the use case is ready, conditionally approved, or not ready.
```

---

# Example 1: Copilot Use Case

File:

```text
examples/copilot-use-case-example.md
```

Use this for:

```text
Enterprise copilots
Productivity assistants
AI-enabled workplace SaaS
Employee-facing AI assistants
Meeting, email, chat, or document copilots
```

Key control focus:

```text
User permission inheritance
Sensitive data guidance
Vendor processing
Prompt/input restrictions
Output review
Human accountability
Incident escalation
```

Typical risk tier:

```text
Tier 2, unless the copilot influences decisions or performs actions.
```

Risk may increase when:

```text
The copilot uses sensitive data.
The copilot generates official records.
The copilot influences decisions.
The copilot can call tools or trigger workflows.
The copilot is customer-facing.
```

---

# Example 2: RAG Assistant

File:

```text
examples/rag-assistant-example.md
```

Use this for:

```text
Knowledge assistants
Policy assistants
Enterprise search AI
Document-grounded AI
RAG systems
Internal helpdesk assistants
Legal or compliance knowledge assistants
```

Key control focus:

```text
Data source mapping
Retrieval boundaries
Data owner approval
Source attribution
Prompt injection through retrieved content
Output grounding
Retrieval logging
Evidence reconstruction
```

Typical risk tier:

```text
Tier 2 or Tier 3, depending on whether the assistant influences decisions.
```

Risk may increase when:

```text
The RAG system retrieves sensitive data.
The system supports compliance, legal, HR, security, or financial decisions.
The system lacks source attribution.
The system can call tools or trigger workflows.
```

---

# Example 3: Agentic AI

File:

```text
examples/agentic-ai-example.md
```

Use this for:

```text
AI agents
Tool-using AI
Workflow automation
Ticket routing agents
IT operations agents
Multi-step task automation
AI systems that can request or perform actions
```

Key control focus:

```text
Agent identity
Autonomy level
Delegated authority
Tool inventory
Action classification
Approval gates
Blast-radius limits
Tool/action logs
Kill switch
Rollback or compensation
Incident containment
```

Typical risk tier:

```text
Tier 4, because the AI can use tools or affect workflow state.
```

Risk may increase to Tier 5 when:

```text
The agent can perform privileged actions.
The agent can affect production systems.
The agent can make regulated or high-impact decisions.
The agent can perform financial, access, security, HR, legal, or customer-impacting actions.
The agent is difficult to stop or recover from.
```

---

# Example 4: Vendor AI

File:

```text
examples/vendor-ai-example.md
```

Use this for:

```text
AI-enabled SaaS
Embedded vendor AI
Vendor copilots
Customer support AI features
Third-party AI summaries
Vendor-provided recommendation features
Hosted model or platform AI
```

Key control focus:

```text
Vendor data processing
Prompt and output retention
Training and product improvement use
Subprocessors
Admin controls
Logging and evidence
Incident support
Feature disablement
Contractual terms
```

Typical risk tier:

```text
Tier 2 or Tier 3, depending on data and decision impact.
```

Risk may increase when:

```text
Vendor AI processes sensitive or regulated data.
Vendor AI influences customer, employee, financial, legal, security, or compliance decisions.
Vendor AI can perform actions inside the SaaS platform.
Vendor logs are unavailable.
Vendor retains or reuses enterprise data.
```

---

# Examples vs Templates

Use examples when you want to see a completed version.

Use templates when you want to create your own record.

| Need | Use |
|---|---|
| See a filled example | `examples/` |
| Create a new use case record | `templates/ai-use-case-intake-template.md` |
| Assess risk | `templates/ai-risk-assessment-template.md` |
| Assess controls | `templates/ai-control-assessment-template.md` |
| Review vendor AI | `templates/ai-vendor-assessment-template.md` |
| Plan assurance testing | `templates/ai-assurance-test-plan-template.md` |
| Package evidence | `templates/ai-control-evidence-package-template.md` |
| Record an incident | `templates/ai-incident-record-template.md` |
| Record an exception | `templates/ai-exception-record-template.md` |

---

# Recommended Use

For a new AI use case:

```text
1. Read the closest example.
2. Complete the AI use case intake template.
3. Complete the risk assessment template.
4. Complete the control assessment template.
5. Use specialist templates if the use case involves sensitive data, vendor AI, decisions, tools, or agents.
6. Create an evidence package for high-risk AI.
7. Complete assurance testing before approval.
```

---

# Pattern Mapping

| If Your AI Looks Like This | Start With |
|---|---|
| Employee copilot | `copilot-use-case-example.md` |
| Policy assistant or knowledge bot | `rag-assistant-example.md` |
| Service desk agent or workflow agent | `agentic-ai-example.md` |
| SaaS AI feature | `vendor-ai-example.md` |
| Customer-facing AI | `vendor-ai-example.md` and `copilot-use-case-example.md` |
| Tool-using AI | `agentic-ai-example.md` |
| Decision-supporting AI | `rag-assistant-example.md` or `vendor-ai-example.md` |
| High-impact AI | Use the closest example, then apply the full control assessment. |

---

# Summary

The examples show how the AI Control Architecture moves from theory to practice.

They demonstrate how to:

```text
Classify the AI pattern
Assign ownership
Assign a risk tier
Identify data boundaries
Define decision boundaries
Control tools and actions
Assign human accountability
Define evidence
Plan assurance tests
Prepare incident containment
Make an approval decision
```

Use them as starting points, not final answers.

Every enterprise should adapt the examples to its own systems, data, vendors, risk appetite, and governance model.