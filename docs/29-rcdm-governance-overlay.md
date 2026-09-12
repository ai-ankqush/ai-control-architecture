# Human-on-the-Loop and the Governance Overlay

Autonomy below the human-latency wall is only safe if it is surrounded by governance. This section defines the overlay that makes machine-speed defense accountable, and the distinction that makes it possible.

---

## In the loop versus on the loop

The model distinguishes **human-in-the-loop**, where a human approves each action, from **human-on-the-loop**, where a human supervises an autonomous process and can intervene or halt it at any time.

Below the human-latency wall, in-the-loop approval is impossible by definition: the action completes before a human could respond. The answer is on-the-loop governance, autonomy that remains continuously supervised and instantly revocable. A human does not approve each action; a human supervises the acting capability, sees what it is doing, and can override or stop it at once.

This is the same principle the [Human Accountability Model](13-pillar-human-accountability.md) pillar defines at design time, carried into runtime: accountability is retained by a person even when the action is autonomous.

---

## The governance overlay

Any acting capability is surrounded by four requirements:

- **Policy-as-code**, the rules of engagement expressed in enforceable form, not documentation. This is the runtime expression of the controls the pillars require.
- **Validation gates**, checks that constrain what the defense may do before it does it: authority, action class, reversibility, and rate.
- **Human-on-the-loop oversight**, continuous supervision with override and a kill switch that halts autonomous action immediately.
- **Tamper-evident audit**, a complete, immutable record of what was decided and done, and why, consistent with [Monitoring, Logging & Evidence](15-pillar-monitoring-and-evidence.md).

---

## Containment

A core safety principle is **containment**: any autonomous or adversarial capability is isolated, its only outward path is a governed gateway exposing sanctioned functions, and the capability itself cannot escape that boundary. Speed is granted only within containment.

Containment is what makes it responsible to let a capability act at machine speed at all. The capability may be fast, but it can only reach the world through the [Action Fabric](31-action-fabric-where-halves-meet.md), which enforces policy on every action and can withhold, throttle, or hold for a human any action that exceeds its authority. This connects directly to [Incident Containment & Recovery](16-pillar-containment-and-recovery.md): an action the defense cannot contain or reverse is not permitted autonomously.

---

## Earning autonomy

The overlay is also how autonomy is *earned*. A capability begins in Shadow Mode (recording what it would do, under review), and is granted the right to act only after demonstrating reliability within the overlay. Autonomy is never assumed; it is a privilege the runtime maturity ladder grants and the overlay can revoke.
