# Glossary

Shared definitions for the AI Control Architecture. Terms are as used in this architecture; where a term also has a broader industry meaning, the definition here is the operative one for these documents.

---

**AI Control Architecture (ACA)**: a vendor-neutral reference model for governing, securing, assuring, and containing enterprise AI, organized around six control questions and ten control pillars.

**AI use case**: a specific deployment of AI in a business context (a particular copilot, RAG assistant, or agent). The unit the architecture assesses, tiers, and controls. Not the model, not the vendor, the *use*.

**Action broker / mediation point**: a control point that intercepts an AI's intended action and decides *allow / deny / constrain / step-up* before it executes. The enforcement surface for [pillar 12](12-pillar-tool-and-action-control.md).

**Action class**: a category of action (Notify, Draft, Create, Update, Delete, Execute, Externalize, Privilege) used to set a default control treatment. See [pillar 12](12-pillar-tool-and-action-control.md).

**Agent**: an AI system that plans and chains multiple steps, reasoning, retrieval, and tool/action calls, toward a goal, often with limited per-step human oversight. Elevated risk by autonomy regardless of any single action.

**Assurance**: testing that a use case's controls actually hold, before go-live and on change. The pillar ([14](14-pillar-assurance-and-testing.md)) that produces *verified* boundaries.

**Autonomy**: how little human oversight stands between an AI's output and its effect. One of the two axes (with consequence) that set risk tier.

**Boundary source**: the strength of the basis a control rests on, graded *Declared → Evidenced → Verified → Enforced*. Recorded per control so claimed and proven control are always distinguishable. See [Core Thesis](03-core-thesis.md).

- **Declared**: asserted in the assessment; self-attested.
- **Evidenced**: backed by configuration, documentation, or a public registry.
- **Verified**: confirmed by a live check against the running system.
- **Enforced**: an active control point blocks the disallowed behavior inline.

**Brownfield**: an environment with existing identity, data, security, and GRC systems. The architecture extends these rather than replacing them.

**Consequence**: what an AI use case can touch, across See/Decide/Do. One of the two axes (with autonomy) that set risk tier.

**Containment**: the ability to halt an AI use case in place, stop further actions, freeze an agent, quarantine outputs, without waiting for full shutdown. See [pillar 16](16-pillar-containment-and-recovery.md).

**Control**: an applied, testable measure that constrains what an AI can see, decide, or do. Distinct from a *policy*, which states intent. If it cannot be tested and evidenced, it is guidance, not a control.

**Control point**: a place in the running system where a boundary is declared, evidenced, verified, or enforced (e.g., an identity check, a retrieval scope, an action broker, a log store).

**Compensation**: a counter-action that offsets the effect of an action that already executed, where a clean rollback is not possible. See *reversibility classes*.

**Decision (AI-influenced)**: a consequential outcome (about people, money, rights, safety, or operations) that an AI's output shapes. Governed by [pillar 11](11-pillar-output-and-decision-control.md).

**Kill switch**: a tested, fast, complete means to disable an AI capability or revoke its authority. See [pillar 16](16-pillar-containment-and-recovery.md).

**Least authority / least privilege**: granting an AI only the access and actions its use case requires, default-deny. See [principle 2](04-architecture-principles.md).

**No standing authority**: the principle that authority to see, decide, or act is granted for a purpose and revocable, not a permanent property of the AI. See [principle 3](04-architecture-principles.md).

**Pillar**: one of the ten control domains (07–16). The first seven bound what an AI *is and can do*; the last three make that boundedness provable, observable, and reversible.

**PDP / PEP**: Policy Decision Point (the component that returns a verdict on an action) and Policy Enforcement Point (the component that honors it). A common pattern for action mediation ([pillar 12](12-pillar-tool-and-action-control.md)).

**Prompt injection**: an attack in which instructions hidden in user input or retrieved/tool-returned content override the AI's intended behavior. Governed by [pillar 10](10-pillar-input-control.md).

**RAG (retrieval-augmented generation)**: supplying an AI with retrieved documents/context at query time. A primary data-boundary concern ([pillar 09](09-pillar-data-boundary-control.md)) because retrieval can cross entitlement boundaries.

**Requirement**: a numbered, normative control statement (`ACA-<pillar>-<n>`) with a tier and expected boundary source. See the [Requirements Catalogue](06-requirements-catalogue.md).

**Reversibility classes**: a classification of actions by whether their effects can be undone: *Reversible* (cleanly undone), *Compensatable* (offset by a counter-action), *Irreversible* (cannot be undone). Dictates what may be enforced. See [pillar 16](16-pillar-containment-and-recovery.md).

**Risk tier**: the level of scrutiny a use case attracts (T1 low-risk/public-data, T2 internal productivity with enterprise data or vendor AI, T3 decision-supporting, T4 action-capable, T5 high-impact autonomous or regulated), set from consequence and autonomy by the highest material risk driver. Controls are graduated by tier. See [pillar 07](07-pillar-ai-inventory-and-classification.md).

**See / Decide / Do**: the three surfaces through which an AI touches the enterprise: what it can access, what it can influence, and what it can act on. The organizing axes of the pillars.

**Shadow AI**: AI in use without being inventoried, owned, or governed, the default state the [inventory pillar](07-pillar-ai-inventory-and-classification.md) exists to eliminate.

**Step-up**: requiring elevated authorization or human approval before a high-impact action or decision proceeds.

**Vendor / embedded AI**: AI capabilities shipped inside third-party SaaS or products. In scope for inventory, data-boundary, and vendor-review controls even though the enterprise did not build them.

---

*Version 0.1.0 · Licensed under the terms in [LICENSE.md](../LICENSE.md).*
