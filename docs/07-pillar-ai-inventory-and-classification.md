# Pillar 07: AI Inventory & Classification

**Control question:** *What AI exists?*
**Surface:** the precondition for all three, you cannot control what you cannot see.

---

## Purpose

The enterprise cannot control AI it does not know about. This pillar makes every AI use case **visible, owned, and risk-tiered** before any other control is chosen. It is the entry point of the architecture: intake, ownership, classification, and lifecycle tracking. Every other pillar depends on the tier this one assigns.

---

## Why it matters

Shadow AI is the default state. Copilots get switched on, SaaS vendors ship AI features into tools already in use, teams build internal LLM apps, and agents appear inside automation platforms, none of it routed through a register. The failure mode is quiet: you cannot assess, control, or contain a use case you never recorded, and you cannot size your exposure if you cannot count it. Inventory is unglamorous and it is the control that makes every other control possible.

---

## Control objectives

- Maintain a complete, current inventory of AI use cases, including embedded and vendor AI.
- Assign a named accountable owner to each use case at intake.
- Classify each use case into a risk tier from its consequence (See/Decide/Do) and autonomy.
- Keep the inventory reconciled as use cases change, appear, and are retired.

---

## Requirements

From the [Requirements Catalogue](06-requirements-catalogue.md):

| ID | Requirement | From | Boundary |
|----|-------------|------|----------|
| ACA-07-01 | Maintain an inventory of all AI use cases, including embedded and vendor AI. | T1 | Evidenced |
| ACA-07-02 | Each use case has a named accountable owner recorded at intake. | T1 | Declared |
| ACA-07-03 | Each use case is assigned a risk tier before controls are selected. | T1 | Evidenced |
| ACA-07-04 | The inventory is reconciled on a defined cadence and on material change. | T2 | Evidenced |

---

## How to classify: consequence × autonomy

Tier is a function of two axes, not a single score:

```text
CONSEQUENCE (what it can touch) AUTONOMY (how little oversight)
 See only, low-sensitivity human reviews every output
 Sees sensitive data human approves actions
 Influences decisions acts within bounds, human on exceptions
 Takes consequential actions acts unsupervised (agentic)
```

```text
T1 Low-risk productivity or public-data use     public or non-sensitive data; no decision impact; no tools or actions
T2 Internal productivity with enterprise        internal enterprise data or vendor AI for productivity; no decision
   data or vendor AI                             influence and no actions
T3 Decision-supporting AI                        influences human decisions, judgments, or records
T4 Action-capable AI                             can call tools, trigger workflows, or perform actions in enterprise systems
T5 High-impact autonomous or regulated AI        affects employment, credit, legal, safety, healthcare, regulated, or
                                                 difficult-to-reverse outcomes
```

Tier from the highest material risk driver, not an average. Tier up when either axis is high: an agent that only reads is still action-capable by its autonomy; a read-only assistant over regulated data is elevated by its consequence. When in doubt, tier higher and revisit.

---

## Key controls

- **Intake gate**: a lightweight registration for any new AI use case, capturing purpose, owner, data touched, decisions influenced, and actions taken. Make it easier to register than to route around.
- **Discovery**: actively find shadow AI: vendor-AI feature flags in existing SaaS, model API usage, agent frameworks, and financial and identity signals that reveal AI in use.
- **Classification**: apply the consequence × autonomy tiering at intake and on change.
- **Lifecycle**: track state from proposed → live → retired; reconcile on cadence.

---

## Tier guidance

| | T1 | T2 | T3 | T4 | T5 |
|---|----|----|----|----|----|
| Inventory record | Required | Required | Required | Required | Required |
| Named owner | Required | Required | Required | Required | Required |
| Risk tier assigned | Required | Required | Required | Required | Required |
| Reconciliation cadence | Periodic | Regular | Regular | Continuous / on change | Continuous / on change |

All ten pillars apply at every tier; the tier sets the *depth* of control, not which pillars are in scope. A "-" in any pillar's tier-guidance table means there is no distinct required control at that tier, not that the pillar is absent, the same pillar simply applies at lighter depth. See [Tiers and pillars](06-requirements-catalogue.md) in the catalogue.

---

## Evidence

The [AI Inventory Record template](../templates/ai-inventory-record-template.md) and [AI Risk Tiering template](../templates/ai-risk-tiering-template.md) capture the evidence for this pillar: the register entry, the owner, and the tiering rationale. Boundary source is *Evidenced* when the record exists and the tiering rationale is documented and reconciled against reality.

---

## Standards crosswalk

Inventory and classification underpin nearly every architecture's "map/identify" function: NIST AI RMF **Map**, ISO/IEC 42001 (AI system inventory and impact assessment), the EU AI Act (risk categorisation and record-keeping), and SR 11-7 (model inventory). See [`mappings/`](../mappings/MAPPINGS-README.md).

---

## Failure modes

- Shadow AI that never enters the register, the exposure you cannot see.
- A use case with no named owner, no one to make it right.
- Under-tiering an action-capable or autonomous use case as if it were read-only.
- A stale inventory that reflects last quarter, not the running estate.

See [Common Failure Scenarios](DOCS-README.md) for worked examples.

---

**Next:** [08 · AI Identity & Access Control](08-pillar-ai-identity-and-access-control.md)

*Version 0.1.0 · Licensed under the terms in [LICENSE.md](../LICENSE.md).*
