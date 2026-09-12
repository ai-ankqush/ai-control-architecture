# The Five Functions

RCDF expresses runtime defense as five functions arranged in a continuous, recursive loop. They are not phases performed once but capacities maintained always; the output of each cycle refines the next.

The loop is: **Govern to Observe to Anticipate to Disrupt to Adapt, and back to Govern.**

---

## Govern, the spine

Govern establishes the policy, authority, accountability, and rules of engagement that bound every other function. It defines what the defense is permitted to do, under whose authority, within what limits, and with what human oversight. Govern is expressed as enforceable policy rather than documentation, and it is the function to which all others remain subordinate. No other function may exceed the authority Govern grants it.

In the architecture, Govern is where the design-time control decisions become runtime authority: the controls a use case requires, expressed as the policy the runtime enforces.

---

## Observe, continuous behavioural awareness

Observe maintains real-time, behavioural awareness of the protected environment: what is happening, by which actors, in what sequence. RCDF emphasises behaviour over signatures. Defense reasons about *what an action does*, not merely whether it matches a known pattern, so that it remains effective against techniques never seen before. Observe is the runtime extension of the [Monitoring, Logging & Evidence](15-pillar-monitoring-and-evidence.md) pillar: the same evidence, read continuously and in time to act.

---

## Anticipate, forward defense

Anticipate looks ahead. Rather than waiting to detect a completed attack, it reasons over the unfolding sequence to predict an adversary's next move and identify the earliest point at which intervention prevents the objective. Anticipation is what allows defense to act *before* the damaging step rather than after it. It is the difference between reading the wreckage and interrupting the plan.

---

## Disrupt, governed interdiction

Disrupt is the function that acts. It interrupts the adversary's progress, at machine speed where necessary, strictly within the bounds set by Govern. Disruption is graduated: from observing and flagging, to requiring human approval, to acting autonomously. The conditions under which each is permitted are defined by policy, not left to the moment. Disrupt is realised in the path of the action at the [Action Fabric](31-action-fabric-where-halves-meet.md), and it refuses any action it cannot contain or reverse, consistent with the [Tool & Action Control](12-pillar-tool-and-action-control.md) pillar and [Incident Containment & Recovery](16-pillar-containment-and-recovery.md).

---

## Adapt, the recursion

Adapt closes the loop. It learns from each cycle, what was observed, anticipated, and disrupted, and how well, and feeds that learning back into Govern, Observe, Anticipate, and Disrupt. Adaptation is what makes the model *recursive*: the defense continually re-derives and improves its own posture, and each loop returns to Govern so that improvement never escapes oversight.

---

## Mapping to established functions

The five functions align with the widely used Identify, Protect, Detect, Respond, Recover model, extended for machine-speed and for AI agents as first-class actors: Govern spans Identify and the authority to Protect; Observe is continuous Detect; Anticipate adds forward reasoning ahead of Respond; Disrupt is Respond in the path of the action; Adapt carries Recover and improvement back into governance. The full crosswalk is in [Standards Crosswalks](../mappings/MAPPINGS-README.md).
