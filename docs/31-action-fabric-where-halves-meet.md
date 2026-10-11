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

## The refusal contract

A verdict that only says "no" teaches an agent to look for another way. When the Action Fabric withholds or escalates an action, it returns to the agent ([ACA-12-06](12-pillar-tool-and-action-control.md)):

- **The reason**: which rule stopped the action and why, in terms the agent can act on.
- **Whether it is negotiable**: some refusals the agent may resolve itself (a claim with no source); others are a person's call (who the organization may speak to, a sensitive topic, an authority limit) and are marked as such.
- **The responses open to it**: cite evidence for an evidence hold, revise the action, or withdraw it.
- **A retry budget**: a small, fixed number of revisions per action. When it is spent, a person decides.
- **A repeat stop**: resubmitting content that was already refused, unchanged, is stopped outright.

Evidence the agent cites is checked by the Fabric, never taken on the agent's word. Every exchange is recorded with the verdict, so the audit shows not just what was refused but what the agent did next.

---

## Three kinds of check

Every rule the Fabric applies is one of three kinds. Placing a rule in the wrong kind is what makes governance brittle.

| Kind | Decides | Examples | How it must behave |
|---|---|---|---|
| **Code** | Facts about the action | identity, tool, target, caps, credentials in content, disclosure, scope | Deterministic, exact, cheap. Carries most of the protection. |
| **Model** | Meaning | is this claim supported by the approved facts, is this topic sensitive, is this content hostile | Pinned, tested against known-bad cases before adoption, fails closed, may relax only the specific hold it was built for, never overrides a block ([ACA-14-04](14-pillar-assurance-and-testing.md)). |
| **Person** | Authority and trade-offs | speaking to someone who never engaged, accepting a risk, restarting after a stop | Named, recorded, time-bound ([ACA-13-04](13-pillar-human-accountability.md)). |

A rule that keeps needing word-level tuning is a model-kind check written as code: move it rather than tune it. A model check should earn its place: replay real held actions and known-bad cases through it and adopt it only if it materially reduces what reaches a person without letting anything through that should be stopped. Human rulings are recorded with their reasons and become the labelled data that model checks are re-tested against.

---

## Who sets the policy

The policy the Fabric enforces is itself governed ([ACA-12-05](12-pillar-tool-and-action-control.md)). It is versioned and machine-readable, and the business owner and security both approve each version before it is enforced. Approval expires. Any change, including a different model in an acting role ([ACA-07-05](07-pillar-ai-inventory-and-classification.md)), is a new version. Until a version is approved, the Fabric admits only non-consequential actions such as reading and drafting.

---

## Why it is the join

The Action Fabric is where the standard stops being two documents and becomes one system. A control defined in the design-time half has no effect until something enforces it in the path of the action; a runtime defense has nothing to enforce until the design-time half tells it which controls apply. The Fabric is the seam. It is also the point that must be open: for the architecture to be a standard anyone can build on, the Action Fabric's contract, its action-class taxonomy, reversibility grades, authority format, and audit schema, are published so that any implementation can conform, and any engine can act through it under the same governance.
