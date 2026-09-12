# NIST CSF Crosswalk

This crosswalk maps the Runtime Defense model (RCDF), the runtime half of the AI Control Architecture, to the NIST Cybersecurity Framework (CSF) functions. RCDF organises runtime defense into five functions: Govern, Observe, Anticipate, Disrupt, and Adapt. CSF organises cybersecurity outcomes into Govern, Identify, Protect, Detect, Respond, and Recover. The two align closely, which is deliberate: RCDF extends the established CSF outcomes for machine-speed operation and for AI agents as first-class actors.

Status: Planned. This document states the intended mapping; the detailed control-level crosswalk is a work in progress.

---

## Function mapping

| RCDF function | NIST CSF function(s) | How they relate |
|---|---|---|
| **Govern** | Govern, Identify | RCDF Govern sets the policy, authority, and rules of engagement that bound every other function, and identifies what is being defended and under whose authority. It is the runtime expression of the controls the ten pillars require. |
| **Observe** | Detect, Identify | RCDF Observe is continuous, behavioural detection: real-time awareness of what is happening, by which actors, in what sequence, reasoning about what an action does rather than matching known signatures. |
| **Anticipate** | Detect, Respond | RCDF Anticipate adds forward reasoning ahead of a completed attack: predicting the adversary's next move and the earliest point at which intervention prevents the objective. CSF has no explicit forward-prediction function; Anticipate extends Detect toward Respond. |
| **Disrupt** | Protect, Respond | RCDF Disrupt is graduated interdiction in the path of the action, at machine speed where policy permits, strictly within the authority Govern grants. It realises Protect and Respond as an enforced runtime decision at the Action Fabric. |
| **Adapt** | Recover, Improve | RCDF Adapt closes the loop: it learns from each cycle and feeds improvement back into every function, and it carries the recovery and reversal path. Each loop returns to Govern so improvement never escapes oversight. |

---

## Notes

- The mapping is not one-to-one because RCDF is built for defense that must act below the human-latency wall while remaining under human authority. Anticipate (forward prediction) and the graduated, reversibility-aware enforcement of Disrupt have no direct single-function equivalent in CSF; they extend the CSF outcomes rather than restate them.
- CSF's Govern function and RCDF's Govern function are aligned in intent: both make policy and authority the spine that bounds all other activity.
- Recovery in CSF maps to RCDF Adapt together with the reversal path defined in [Incident Containment & Recovery](../docs/16-pillar-containment-and-recovery.md) and enforced through the [Action Fabric](../docs/31-action-fabric-where-halves-meet.md).

For the full runtime half, see the [Runtime Defense Overview](../docs/27-rcdf-runtime-defense-overview.md) and [The Five Functions](../docs/28-rcdf-five-functions.md).
