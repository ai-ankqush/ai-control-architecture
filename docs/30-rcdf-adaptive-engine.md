# The Adaptive Engine

The forward-looking functions, Anticipate and Disrupt, may be realised by an adaptive engine: a component that reasons over behaviour to predict an adversary's next move and apply a graduated verdict in the path of the action. This section defines that engine's *role* in the architecture. It is deliberately engine-neutral.

---

## A role, not a product

Within the architecture, the adaptive engine's role is defined at the standard level: under the authority of Govern, it provides behavioural anticipation and graduated interdiction, advancing through the runtime maturity ladder from Shadow Mode upward. The standard specifies what the engine must do and the boundaries it must respect. It does not specify how the engine works inside.

A conformant implementation may realise this role with a rule set, a learned model, a hybrid, or any other mechanism, provided it operates within the [governance overlay](29-rcdf-governance-overlay.md) and containment: bounded by policy-as-code, constrained by validation gates, supervised on the loop, recorded in a tamper-evident audit, and reaching the world only through the [Action Fabric](31-action-fabric-where-halves-meet.md). The architecture governs the engine; it does not require any particular one, and it could govern more than one.

---

## Engine-neutral by design

Keeping the engine's internal mechanism out of the standard is deliberate and load-bearing. It means:

- **The standard is implementation-neutral.** Anyone can build a conformant engine, or bring their own, and be certified against the same requirements. The standard is the contract, not the code.
- **Conformance is about behaviour, not internals.** An engine conforms if it respects Govern's authority, stays within containment, produces the required audit, and earns autonomy through the maturity ladder, whatever it is made of.
- **Advanced engines remain optional.** Some implementations of the adaptive engine are sophisticated learned systems whose internal mechanism is proprietary and, in some cases, separately patented. The architecture references only the engine's role and does not disclose or depend on any such mechanism. The model stands independently of any particular engine.

---

## What the standard requires of any engine

Whatever realises Anticipate and Disrupt must:

1. Act only within the authority Govern grants, and never exceed it.
2. Operate inside containment, reaching the world only through the governed [Action Fabric](31-action-fabric-where-halves-meet.md).
3. Grade its own actions by reversibility, and hold irreversible or out-of-authority actions for a human.
4. Begin in Shadow Mode and earn autonomy by demonstrated reliability, per the runtime maturity ladder.
5. Write every decision, taken or withheld, to a tamper-evident audit.
6. Remain supervised on the loop, with override and a kill switch that halt it immediately.

An engine that meets these requirements is conformant, regardless of what it is built from. That is what lets the standard be open while the best engines remain a matter of implementation.
