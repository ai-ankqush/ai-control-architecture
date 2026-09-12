# Where the Halves Meet: the Action Fabric

**Control question:** *Where does a control become an enforced decision?*
**Half:** The join.

---

## Purpose

The two halves of the architecture meet at the Action Fabric. The design-time half decides which controls a use case requires; the runtime half enforces them as the AI acts. The Action Fabric is the governed point in the path of an action where a control stops being a policy and becomes a decision: admit, withhold, throttle, hold for a human, or reverse.

This is the single canonical description of the Action Fabric in the architecture. The [Tool & Action Control](12-pillar-tool-and-action-control.md) pillar defines *what* an AI may do; this section defines *how* that decision is made and enforced at runtime. The [Disrupt](28-rcdm-five-functions.md) function acts here; the [adaptive engine](30-rcdm-adaptive-engine.md), where present, decides here; the [governance overlay](29-rcdm-governance-overlay.md) surrounds it.

---

## What it does

For every consequential action an AI attempts, the Action Fabric evaluates it against the governing policy before it takes effect, and returns a verdict:

- **Admit**, the action is within authority and reversible enough to proceed.
- **Withhold**, the action violates a hard limit and is refused outright.
- **Throttle**, the action is permitted but rate-limited, including across a fleet of agents, to catch coordinated behaviour that per-agent limits miss.
- **Escalate**, the action is consequential or irreversible and is held for a human on the loop.
- **Reverse**, where an action proves harmful after the fact and is reversible, it is rolled back through the recovery path.

Every verdict, taken or withheld, is written to a tamper-evident audit.

---

## Action class and reversibility

The Action Fabric decides by two properties of the action, not by trusting the actor: what kind of effect the action has, and whether that effect can be undone.

**Action class** is the taxonomy of effects an AI action can have. Every action an agent attempts is one of these, and the class is what determines the authority it requires:

| Class | What it does | Default reversibility |
|---|---|---|
| **Read** | Retrieves or views data; no change of state | Reversible (no effect to undo) |
| **Notify** | Sends an informational message or alert | Reversible in effect; the message itself persists |
| **Create** | Brings a new record or resource into being | Compensatable (can be removed) |
| **Update** | Modifies an existing record or resource | Compensatable (prior state can be restored) |
| **Execute** | Runs a tool, workflow, or command | Depends on what it triggers; treated as consequential |
| **Externalize** | Sends data or effect outside the trust boundary | Irreversible (cannot be recalled) |
| **Delete** | Destroys a record or resource | Irreversible (cannot be undone in place) |

**Reversibility** grades each action by whether its effect can be undone. Reversible actions (read, notify) may flow freely. Compensatable actions (create, update) may proceed with a recorded way back. Irreversible actions (externalize, delete, and any execute whose effect cannot be recalled) require a human on the loop. This grading is what lets the defense grant speed safely: an agent moves fast on the reversible many and stops for a person on the irreversible few. It ties directly to [Incident Containment & Recovery](16-pillar-containment-and-recovery.md), and the Action Fabric refuses to enforce autonomously any action it cannot contain or reverse.

The class-and-reversibility pairing is what makes the standard machine-readable and enforceable: a policy states which classes an agent may perform, up to which reversibility grade, under whose authority, and the Action Fabric evaluates every action against that before it takes effect.

---

## Why it is the join

The Action Fabric is where the standard stops being two documents and becomes one system. A control defined in the design-time half has no effect until something enforces it in the path of the action; a runtime defense has nothing to enforce until the design-time half tells it which controls apply. The Fabric is the seam. It is also the point that must be open: for the architecture to be a standard anyone can build on, the Action Fabric's contract, its action-class taxonomy, reversibility grades, authority format, and audit schema, are published so that any implementation can conform, and any engine can act through it under the same governance.
