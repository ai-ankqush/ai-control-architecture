# Pillar 12: Tool & Action Control

**Control question:** *What can the AI do?*
**Surface:** Do.

---

## Purpose

This is the pillar that governs AI **as an actor.** Once an AI can call APIs, trigger workflows, update records, send communications, or move money, it is no longer producing suggestions, it is taking actions with real, often irreversible, effect. This pillar bounds what those actions can be, requires human authority for the consequential ones, and refuses to enforce any action it cannot contain or undo.

---

## Why it matters

Everything before this pillar is about what the AI knows and recommends. This pillar is about what it *does*, and doing is where probabilistic behavior meets deterministic consequence. An agent that can call a tool it should not, at machine speed, thousands of times, is a categorically different risk from a copilot that drafts text. The blast radius of a single mistaken or injected action can exceed anything a human operator could cause, and it can happen faster than a human could intervene. This is the surface the [Core Thesis](03-core-thesis.md) is ultimately about: deterministic authority handed to a probabilistic actor.

---

## Control objectives

- **Allow-list** the tools and actions an AI may invoke, default-deny.
- Require **approval or step-up** for high-impact actions before execution.
- Never enforce an action class **without a defined containment or compensation path**.
- **Log every action** with the requesting identity, inputs, and outcome.

---

## Requirements

From the [Requirements Catalogue](06-requirements-catalogue.md):

| ID | Requirement | From | Boundary |
|----|-------------|------|----------|
| ACA-12-01 | The tools and actions an AI may invoke are explicitly allow-listed. | T4 | Verified |
| ACA-12-02 | High-impact actions require approval or step-up before execution. | T4 | Enforced |
| ACA-12-03 | No action class is enforced live without a defined containment or compensation path. | T4 | Enforced |
| ACA-12-04 | Every action is logged with the requesting identity, inputs, and outcome. | T4 | Verified |

---

## Action classes

Classify every action before deciding how to control it; the class sets the default treatment:

```text
Class Examples Default
────────────────────────────────────────────────────────────
Notify post message, send alert allow / step-up by audience
Draft draft email, draft ticket allow
Create create ticket, create task allow / step-up
Update update CRM, IAM, config step-up
Delete delete record, remove access deny / step-up
Execute run command, trigger workflow step-up / deny
Externalize send outside org, expose data step-up / deny
Privilege change access, modify role deny unless explicitly approved
```

Risk tier and [boundary source](03-core-thesis.md) move these defaults; the class also drives which containment or compensation path must exist before the action can be enforced live.

---

## Key controls

- **Action broker / mediation point**: route the AI's actions through a control point that decides allow / deny / constrain / step-up *before* execution (an API gateway, an action broker, or a governed tool proxy). This is the enforcement surface.
- **Allow-listing & least action**: the AI may invoke only the tools and action classes its use case needs; everything else is denied.
- **Approval & step-up gates**: high-impact actions pause for a human, or require elevated authorization, before they run.
- **Containment precondition**: do not turn on live enforcement for an action class that has no rollback, compensation, or containment path ([pillar 16](16-pillar-containment-and-recovery.md)). Never enforce what you cannot undo.
- **Agent-specific controls**: for agents that chain actions, bound the loop: step budgets, scope per task, and human gates on high-impact steps (see the [AI Agent Control template](../templates/ai-agent-control-template.md)).
- **Full action logging**: every attempted and executed action recorded for [monitoring](15-pillar-monitoring-and-evidence.md) and reconstruction.

---

## Tier guidance

| | T1 | T2 | T3 | T4 | T5 |
|---|----|----|----|----|----|
| Action allow-list | - | - | - | Required (verified) | Required (verified) |
| Approval / step-up on high-impact | - | - | - | Required (enforced) | Required (enforced) |
| Containment path before enforcement | - | - | - | Required | Required |
| Full action logging | - | - | - | Required | Required |

---

## Evidence

The [AI Tool & Action Control template](../templates/ai-tool-and-action-control-template.md) and [AI Agent Control template](../templates/ai-agent-control-template.md) capture the allow-list, the action classes, the mediation/approval design, and the containment preconditions. Boundary source reaches *Enforced* when an active mediation point blocks or gates disallowed actions inline, the strongest control in the architecture, and the one that most requires [pillar 16](16-pillar-containment-and-recovery.md) behind it.

---

## Standards crosswalk

Maps to NIST AI RMF **Manage**, ISO/IEC 42001 operational controls, EU AI Act (human oversight and robustness for high-risk systems), and directly to OWASP LLM (excessive agency, insecure plugin/tool design) and the OWASP Agentic Top 10. See [`mappings/`](../mappings/MAPPINGS-README.md).

---

## Failure modes

- An agent invokes a tool or action outside any allow-list.
- A high-impact action executes with no approval and no way to stop it.
- Live enforcement enabled on an irreversible action with no compensation path.
- Actions that cannot be attributed or reconstructed after the fact.

---

**Next:** [13 · Human Accountability Model](13-pillar-human-accountability.md)

*Version 0.1.0 · Licensed under the terms in [LICENSE.md](../LICENSE.md).*
