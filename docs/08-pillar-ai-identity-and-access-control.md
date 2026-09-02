# Pillar 08: AI Identity & Access Control

**Control question:** *Under what identity, and with what access, does the AI act?*
**Surface:** See (and the foundation of Do).

---

## Purpose

When an AI accesses systems or takes actions, it does so under some identity with some access. This pillar ensures that identity is **distinct, bounded, least-privileged, and revocable**, not a human user's standing credentials, and not a broad service account inherited by convenience. It is the difference between an actor you can attribute and constrain, and one you cannot.

---

## Why it matters

The most common, and most dangerous, shortcut in enterprise AI is letting the AI act *as the user*, with the user's full access. It feels natural (the copilot helps *me*, so it uses *my* permissions) and it is a control failure: a probabilistic system now wields a human's entire standing authority, across everything that human can reach, with none of the human's judgment. Agents make it worse: they run continuously, at machine speed, often with credentials broad enough to "just work." Identity is where you decide whether the AI is a bounded actor or an unbounded one.

---

## Control objectives

- Give each AI use case a **distinct non-human identity**, separate from the users it serves.
- Grant that identity **least-privilege** access scoped to the use case's actual need.
- Make access **promptly and completely revocable**.
- Make every consequential action **attributable** to the identity and the grant that authorized it.

---

## Requirements

From the [Requirements Catalogue](06-requirements-catalogue.md):

| ID | Requirement | From | Boundary |
|----|-------------|------|----------|
| ACA-08-01 | AI acts under a distinct non-human identity, not a user's standing credentials. | T4 | Verified |
| ACA-08-02 | AI identities are granted least-privilege access scoped to the use case. | T4 | Verified |
| ACA-08-03 | AI access is revocable promptly and completely. | T4 | Verified |
| ACA-08-04 | Consequential actions are attributable to the identity and grant that authorized them. | T4 | Enforced |

---

## Key controls

- **Dedicated AI identity**: a service/workload identity per use case (or per agent), issued and governed like any other privileged identity, never a shared human login.
- **Scoped, least-privilege access**: permissions derived from what the use case actually needs to See and Do, default-deny, reviewed as scope changes.
- **On-behalf-of with constraint**: where the AI must act for a user, it does so through a delegation that is *narrower* than the user's full rights and carries the user's context for attribution, not the user's blanket authority.
- **Short-lived credentials & revocation**: prefer short-lived, rotatable credentials; ensure a fast, complete kill path (ties to [pillar 16](16-pillar-containment-and-recovery.md)).
- **Attribution**: every action carries the AI identity and, where relevant, the human and grant behind it, so [monitoring](15-pillar-monitoring-and-evidence.md) can reconstruct who authorized what.

---

## No standing authority

Per [principle 3](04-architecture-principles.md), authority is granted for a purpose and revocable, not a permanent property of the AI. In practice: prefer just-in-time, scoped grants over broad standing access; treat every high-impact action as exercising a specific grant that can be withdrawn. This is what makes an AI's authority *reversible* at the identity layer.

---

## Tier guidance

| | T1 | T2 | T3 | T4 | T5 |
|---|----|----|----|----|----|
| Distinct AI identity | - | - | Recommended | Required | Required |
| Least-privilege scope | - | Recommended | Recommended | Required (verified) | Required (verified) |
| Prompt revocation | - | - | - | Required (tested) | Required (tested) |
| Per-action attribution | - | - | - | Required (enforced) | Required (enforced) |

---

## Evidence

The [AI Identity & Access Control template](../templates/ai-identity-and-access-control-template.md) captures the identity, its scope, the grant model, and the revocation path. Boundary source reaches *Verified* when access scope is confirmed against the live system, and *Enforced* when a control point actually blocks out-of-scope access.

---

## Standards crosswalk

Maps to NIST AI RMF **Manage**, ISO/IEC 42001 access and operational controls, EU AI Act (access governance for high-risk systems), NYDFS Part 500 (access controls, least privilege), and OWASP LLM (excessive agency / insecure access). See [`mappings/`](../mappings/MAPPINGS-README.md).

---

## Failure modes

- The AI runs as the user, with the user's full access.
- A broad service account shared across many use cases, no scoping, no attribution.
- Long-lived static credentials with no revocation path.
- An agent whose actions cannot be traced to an identity or a grant.

---

**Next:** [09 · Data Boundary Control](09-pillar-data-boundary-control.md)

*Version 0.1.0 · Licensed under the terms in [LICENSE.md](../LICENSE.md).*
