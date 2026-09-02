# Architecture Principles

These are the design rules that govern every pillar, requirement, and template in this architecture. If a control contradicts a principle here, the principle wins. They exist so the architecture stays coherent as it grows and so contributors extend it in the same spirit.

---

## 1. Control, not policy

Every element of this architecture must be **applied, testable, and evidenced** in the running system. "We have a policy that says X" is not a control. A control constrains what an AI can see, decide, or do, and you can demonstrate that it holds. If a requirement cannot be tested and evidenced, it is guidance, and it is labelled as such.

## 2. Bound the actor, with least authority

An AI that can act is an actor, and actors get the **least authority** required for their purpose, no more. AI receives its own bounded identity, scoped access, and explicit action limits, never a human's standing credentials or blanket access. Default-deny; grant narrowly; justify every capability.

## 3. No standing authority, authority is granted, scoped, and revocable

Authority to see, decide, or act is **granted for a purpose, scoped to it, and revocable at any time**, not a permanent property of the AI. The enterprise must be able to reduce or revoke an AI's authority quickly and completely. Every consequential action should be traceable to the grant that permitted it.

## 4. Proportionate to risk, graduate by consequence and autonomy

Controls scale with the use case's **consequence** (what it can See, Decide, Do) and its **autonomy** (how little human oversight stands between it and effect). A read-only copilot and an action-capable agent do not carry the same burden. Risk-tier first; apply the control weight the tier demands; do not impose enterprise-grade controls on trivial use cases or trivial controls on high-impact ones.

## 5. See, Decide, Do are the control surfaces

Every AI use case is bounded along the same three surfaces, what it can **See**, what it can **Decide**, what it can **Do**. Controls are organized so that each surface is explicitly addressed. A use case with an unexamined surface is an incomplete assessment.

## 6. Evidence-first, grade every boundary by its source

A control is only as strong as the basis it rests on: **declared → evidenced → verified → enforced.** Every control records its boundary source, so the difference between claimed and proven control is always visible. Prefer verified and enforced boundaries for anything consequential; never let a declared boundary pass as a held one.

## 7. Accountability is non-delegable

A **named human owns every consequential outcome**, the decision, the approval, the exception, the risk acceptance, the recovery. AI informs judgment; it never becomes the accountable party. A use case that cannot name its accountable owner has a finding, not a gap to defer.

## 8. Assume failure, design for containment and recovery

Controls will be bypassed, misconfigured, or simply wrong. The architecture assumes this and requires that high-impact AI be **observable, stoppable, and recoverable**: you can see what it did, halt it quickly, and undo or compensate its effects. A corollary: **do not grant enforcement over an action you cannot contain or reverse.** Never enforce what you cannot undo.

## 9. Defense in depth across the lifecycle

No single control is trusted to hold alone. Controls are layered across the life of a use case, inventory, identity, data, input, output, action, accountability, assurance, monitoring, containment, so that the failure of one is caught by another. The pillars are deliberately overlapping, not a single gate.

## 10. Brownfield-compatible and vendor-neutral

The architecture assumes you already have identity systems, data platforms, SaaS, security tooling, and GRC, and it **extends** them rather than replacing them. It depends on no single model, vendor, cloud, or product, and it works whether the AI is a copilot, an internal application, a RAG assistant, an embedded vendor feature, an agent, or an API.

## 11. Interoperable, map to standards, don't compete with them

The architecture is the **common control language beneath** recognized frameworks, not a rival to them. Every control carries a conceptual crosswalk to the standards the enterprise is already held to (NIST AI RMF, ISO/IEC 42001, EU AI Act, SR 11-7, NYDFS, OWASP), so one assessment serves many obligations. Where possible, artifacts are expressed in open, machine-readable form.

## 12. Continuous, not point-in-time

An AI use case changes, new data sources, new tools, model updates, drift. A control that held at assessment can fail silently later. The architecture treats control as **ongoing**: monitored, re-verified, and re-tiered when the use case changes, not certified once and forgotten.

## 13. Usable, or it will be bypassed

Controls that are too heavy for their risk get routed around, and a bypassed control is worse than none because it hides the exposure. The architecture favors the **minimum control that genuinely holds** for a given tier, and provides triage paths so teams can start with the smallest safe set and graduate. Simplicity is a safety property.

---

## How the principles are used

The pillars (07–16) implement these principles for a specific control surface. The [Requirements Catalogue](06-requirements-catalogue.md) turns them into numbered, testable requirements. The [Reference Architecture](05-reference-architecture.md) shows how they compose. When you assess a use case, these principles are the lens: least authority, proportionate to risk, evidence-first, accountable, containable.

---

**Next:** [05 · Reference Architecture](05-reference-architecture.md)

*Version 0.1.0 · Licensed under the terms in [LICENSE.md](../LICENSE.md).*
