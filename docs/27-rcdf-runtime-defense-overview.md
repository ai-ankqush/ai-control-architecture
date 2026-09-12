# Runtime Defense (RCDF)

**Control question:** *How do these controls defend at machine speed, under human authority?*
**Half:** Runtime.

---

## Purpose

The pillars establish *what* controls an AI use case requires. This half of the architecture establishes *how* those controls hold at runtime, when actions occur faster than a human can intervene. It is the enforcement counterpart to the design-time control pillars: the Runtime Defense model, RCDF. RCDF is documented in full as a standalone work; this half of the architecture is its integration into the standard.

The AI Control Architecture is therefore one standard with two halves. The design-time half answers what an AI can see, decide, and do, and which controls that demands. The runtime half answers how those controls are observed and, where warranted, enforced in the path of the AI's own actions, without removing human authority over what the defense does. The two halves meet at the [Action Fabric](31-action-fabric-where-halves-meet.md), the governed point where a control becomes an enforced decision.

---

## Why it matters

Two forces make human-paced defense insufficient for agentic AI. Attacks are increasingly automated and can complete a damaging action in milliseconds, well inside the time a human needs to perceive, decide, and respond. And the systems being defended now include AI agents that themselves act autonomously and at speed. A defense that can only recommend, alert, or wait for approval will always arrive after the consequential action has occurred.

RCDF names the boundary at the heart of this the **human-latency wall**: the point, on the order of a few hundred milliseconds, beyond which only an automated responder can interdict in time. The runtime half of the architecture allows defense to operate at and below that wall responsibly, under explicit policy, with human oversight retained, and with every autonomous action contained and accountable.

---

## The two requirements, reconciled

Governed machine-speed defense reconciles two requirements long held to be in tension:

- **Fast enough to matter**, able to act below the human-latency wall, in the path of the action, before the damaging step rather than after it.
- **Never beyond human authority**, every autonomous action bounded by policy, supervised, instantly revocable, and recorded.

The rest of this half describes how: [the five recursive functions](28-rcdf-five-functions.md) that organise the defense, [the governance overlay](29-rcdf-governance-overlay.md) that keeps autonomy safe, [the adaptive engine](30-rcdf-adaptive-engine.md) that may realise the forward-looking functions, and [the Action Fabric](31-action-fabric-where-halves-meet.md) where the two halves of the architecture meet.

---

## The runtime defense maturity ladder

Maturity here is not merely speed. It is earning the right to act faster by first demonstrating reliability and control. An organisation progresses through six levels:

- **L0, Unaware.** No continuous defense capability; response is reactive and after the fact.
- **L1, Instrumented.** Observation exists, but anticipation and response remain manual and human-paced.
- **L2, Coordinated.** The five functions are defined and connected; response is human-driven with limited automation.
- **L3, Adaptive (Shadow Mode).** The full loop runs continuously, but enforcement operates in *shadow*: the defense determines what it *would* do and records it, under human review, building an evidence trail and earning trust before it is permitted to act. This is the deliberate proving ground between recommendation and action.
- **L4, Predictive.** The defense acts autonomously within governed bounds, below the human-latency wall, with a human retained *on the loop*, supervising and able to override rather than approving each action. Reaching L4 is conditioned on having demonstrated reliability at L3.
- **L5, Recursive.** The defense continuously and self-referentially improves its own posture across cycles, adapting to a shifting adversary while remaining within the authority the Govern function defines.

Progression is governed: a capability earns the right to act more autonomously by demonstrating, at the level below, that it does so reliably and within bounds. This runtime maturity ladder complements the design-time [Control Maturity Model](18-control-maturity-model.md), which measures control coverage across the pillars; together they answer both *are the right controls in place* and *can they defend at speed*.
