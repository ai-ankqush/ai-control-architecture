# Sovereign AI

*Sovereignty over AI is not only where it runs. It is who controls what it is allowed to do.*

Sovereign AI has moved to the centre of the conversation. Governments, regulated enterprises and critical-infrastructure operators increasingly ask not just whether they can use AI, but whether they remain in control of it. The AI Control Architecture treats that question as a design requirement, not a slogan.

Most of the sovereign-AI debate is framed around two questions. Where does the model run? Where does the data reside? Both matter. Neither, on its own, answers the most consequential question: **who decides what the AI is allowed to do?**

## The three dimensions of AI sovereignty

AI sovereignty has three distinct dimensions, and they are not interchangeable.

**Model sovereignty** determines *what you run* — which models, trained by whom, on what terms, and whether you can operate them without depending on a single external provider.

**Data sovereignty** determines *where your information resides* — the jurisdiction, residency and access boundaries around the data an AI system reads and produces.

**Control sovereignty** determines *who holds authority over AI actions* — who governs what an agent may see, decide and do at the moment it attempts to act, and who holds the evidence of those decisions.

The first two are now widely understood. The third is the one most organisations have not yet named, and it is the one that decides whether the other two mean anything in practice.

## The missing dimension

An organisation can operate a model inside its preferred jurisdiction and keep every byte of data within the required geographic boundary, and still not control its AI.

If every consequential action an agent takes must pass through an external vendor's proprietary enforcement engine, then the rules that govern the AI, the logic that decides what is allowed, and the evidence of what happened all sit outside the organisation's control. Its infrastructure may be sovereign. Its authority is not.

Control sovereignty is decisive because AI agents do not behave like traditional software. Traditional access control authorises the actor: an identity receives a role, the role receives permissions, and those permissions follow the actor into everything that comes next. That is adequate for software with a stable, predictable function. An agent, by contrast, interprets changing context, chains tools together, chooses its next step and acts on information nobody anticipated when its permissions were assigned. Every identity control can work exactly as designed while the resulting action is still wrong.

The control point that matters, therefore, is not the login. It is the execution path — the moment the agent attempts to act. Whoever governs that point governs the AI.

## How the AI Control Architecture delivers control sovereignty

ACA is built so that this control point belongs to the organisation running the AI, not to a vendor.

**The architecture is open.** ACA gives organisations a shared, public language for classifying AI, determining its risk tier, selecting proportionate controls and defining the evidence needed to prove them. It grades every control boundary by how strongly it actually holds — its *boundary source* — across four states: Declared, Evidenced, Verified and Enforced. Nobody has to adopt a private, vendor-defined compliance standard to describe how their AI is controlled.

**The runtime is open.** The [AI Action Fabric](/blog/2026-09-20-open-source-ai-control-runtime/), the layer that enforces those controls at runtime, is released as open source under AGPL-3.0. It sits inside the execution path and authorises the action, not only the actor: every consequential request becomes a fresh, scoped and revocable delegation, evaluated against its purpose, blast radius and reversibility, and every verdict carries its own evidence.

**The authority stays with you.** The Action Fabric runs inside your environment, on your own infrastructure, using your own model account and key. Your policies, your evidence and your execution path remain under your control. The code can be inspected, forked and extended. No vendor-controlled policy engine needs to sit between your agents and your systems.

This is what closes the gap. Model sovereignty and data sovereignty decide what you run and where your data lives. Control sovereignty decides who holds authority over what the AI does — and an open architecture with an open enforcement runtime is how an organisation actually holds it.

## What control sovereignty looks like in practice

An organisation that has control sovereignty over its AI can answer yes to each of these:

- The enforcement layer between our agents and our systems runs on infrastructure we control.
- The policies that decide what an agent may do are ours to read, change and own.
- The logic that grants, conditions, holds or blocks an action is inspectable, not a black box.
- The evidence of every decision is produced as part of the decision and stays with us.
- We could remove any single vendor and still enforce our controls.

Where any of these is answered by an external provider's proprietary system, sovereignty is incomplete, however well the model and data questions have been handled.

## The next question

Sovereign AI will not be settled by model choice and data residency alone. As AI shifts from answering questions to taking actions, the sovereignty that matters most is authority over those actions.

The architecture is open.
The runtime is open.
Sovereign AI requires sovereign control.
The authority remains yours.

---

See the launch announcement: [Neo's AI Control Runtime is now open source](/blog/2026-09-20-open-source-ai-control-runtime/). The open runtime, repository and quickstart: [github.com/ai-ankqush/neo-community-edition](https://github.com/ai-ankqush/neo-community-edition).
