# RFC-001: The AI Control Architecture Ecosystem

**Status:** Draft / Request for Comments
**Version:** 0.1
**Targets:** ACA spec v0.1
**How to comment:** open an issue on the ACA repository, or email the stewards. This is a proposal, not a final decision, the shape below is meant to be changed by the people who will build on it.

---

## 1. Summary

We propose an open, extensible ecosystem around the AI Control Architecture. ACA already gives the industry a shared way to *describe* AI control and a shared way to *represent proof* (the evidence schema). This RFC proposes the extension points, contracts, and distribution model that let anyone build on ACA, connectors, control packs, test packs and renderers, and share or sell what they build.

We are publishing this as an RFC because a standard is not something one vendor declares. If ACA is going to be shared infrastructure, its ecosystem has to be designed with the people who will implement it, including our competitors.

---

## 2. Motivation

Every AI-control product today invents its own control language, its own evidence format, and its own integrations. Nothing travels. An organisation re-implements the same control for each vendor, each auditor, and each regulator.

ACA fixes the language (the control model) and the proof (the evidence schema). This RFC fixes the last piece: **how the field extends what ACA can see, test and prove, without any single vendor owning the extension surface.**

Design constraint, above all else: *ACA must be usable, and extendable, without Neo.* Neo intends to be the strongest implementation, not the gatekeeper.

---

## 2.1 The core you build against

The ecosystem is a small **core** plus a fixed set of extension **slots**, the same shape every add-on plugs into.

**Object model:** `Use Case → Control → Evidence → Assessment → Finding → Tier`. Every add-on reads and writes these objects, and nothing else. Evidence is validated against the ACA Evidence Schema, the contract that makes proof portable across tools.

**Lifecycle + hooks:** `describe → classify → select controls → collect → assess → report`. An add-on subscribes to the stage it extends; the core invokes it at the right moment. That is the whole extension mechanism.

The reference implementation of this core is open (Apache-2.0). Notably, **the stewards' own product is built on the same public core**, first-party connectors, frameworks and reports are add-ons in these slots, not privileged internal code. If our own product can't ship without the public extension API, then that API is real, and nothing you build is blocked by a missing one.

---

## 3. Extension types

Four extension types, each targeting a defined contract. (Renderers absorb themes and report templates; we deliberately keep the initial surface small.)

### 3.1 Connectors
**Purpose:** read a system, read-only, and emit evidence.
**Contract:** given a scope + credentials the operator supplies, produce `aca-evidence[]` objects (see the Evidence Schema) mapped to one or more `controlId`s.
**Never:** write to the target system, or exceed declared permissions.
**Example:** an Okta connector emits `configuration` evidence for identity/access controls; a GitHub connector emits `scan` evidence for the presence of an AI-BOM.

### 3.2 Control packs
**Purpose:** add requirements and crosswalks for a domain, industry, or external framework.
**Contract:** contribute additional controls and/or crosswalks in the catalogue format.
**Rule:** **core `ACA-*` controls are immutable.** A pack may *supplement* (add namespaced controls) or *crosswalk* (map to external frameworks). It may never redefine a normative ACA control.
**Example:** a `healthcare.example/*` pack; a `SOC 2` or `ISO 27001` crosswalk pack.

### 3.3 Test packs
**Purpose:** add assurance and adversarial tests.
**Contract:** define tests bound to `controlId`s; a run emits `aca-evidence` with `evidenceType: test-result`.
**Example:** a prompt-injection scenario set; a retrieval-boundary assurance test.

### 3.4 Renderers
**Purpose:** transform ACA data (assessments, evidence, findings) into reports, exports, or branded/white-label output.
**Contract:** consume ACA objects, produce a document/export; no privileged access.

---

## 4. The add-on manifest

Every add-on ships an `aca-plugin.json`. No manifest, no install.

```json
{
  "name": "aca.core/okta-connector",
  "type": "connector",
  "version": "1.2.0",
  "acaVersion": ">=0.1 <1.0",
  "description": "Read-only evidence for identity & access controls from Okta.",
  "author": "Neo Control",
  "license": "Apache-2.0",
  "pricing": "free",
  "entry": "./index.mjs",
  "permissions": {
    "network": ["okta.com"],
    "reads": ["identity.policies", "identity.factors"],
    "writes": [],
    "dataScopes": ["confidential"]
  },
  "controls": ["ACA-08-01", "ACA-08-03"]
}
```

- `acaVersion` is a compatibility range against the spec.
- `permissions` are declared, surfaced at install, and enforced at runtime.
- `pricing` is `free` or `paid`; `license` is the author's choice for community add-ons.

---

## 5. Namespacing

- `ACA-*`, reserved for normative ACA controls. Immutable.
- `<domain>/*`, external modules, e.g. `healthcare.example/*`, `vendor.example/*`.
- Add-on identities are namespaced too (`org/name`) so two authors never collide.

Core controls can only be supplemented or crosswalked, never modified.

---

## 6. The shared output: evidence

Connectors and test packs emit objects in the **ACA Evidence Schema**. That is the whole point: a connector written by one vendor produces evidence a different vendor's monitoring tool, or an auditor, can consume without a translation layer. The schema is versioned in the ACA Specification; add-ons declare the schema version they emit.

---

## 7. Distribution: build it, share it, or sell it

Any author chooses their model:
- **Private**, build for your own organisation, never publish.
- **Free**, publish openly under the licence you choose.
- **Commercial**, charge for it, if it's hard enough to be worth it.

And two tracks (detailed in the Marketplace design):
- **Open track**, permissionless, unvetted, always sandboxed. Velocity and the long tail.
- **Curated track**, only security-reviewed, conformance-tested add-ons. Enterprise-safe.

---

## 8. Security model (connectors)

Read-only is not the same as safe, a read-only connector can still exfiltrate. Any add-on that touches a real system runs under: sandboxing, secret isolation, network-egress restrictions, declared data scopes, signed packages, dependency + provenance checks, revocation / kill switches, tenant isolation, and a security-update obligation. The security model is part of ACA's credibility, and comment on it is explicitly invited.

---

## 9. Certification & support tiers

**Certification** (what an add-on *is*):
- `ACA-Compatible`, valid manifest, schemas, interfaces (automated).
- `ACA-Verified`, plus security + behavioural testing.
- `ACA-Certified`, demonstrated conformance to an ACA profile via an approved assurance process.

**Support** (who *maintains* it): `Community` → `Verified` → `Certified` → `Neo-supported`.

These marks are ACA marks, kept separate from any single vendor's product claims.

---

## 10. Governance & versioning

ACA is stewarded today by Neo Control, moving toward multi-stakeholder governance: a public contribution and decision process, published and versioned conformance tests, transparent deprecation, an appeals path for rejected extensions, and an external technical advisory group. The spec follows semantic versioning; add-ons declare compatibility ranges. This RFC process is the first instance of that public process.

---

## 11. How to get involved

We're looking for design partners to shape this before it sets, specifically:
- an **auditor / assurance firm** (does the evidence schema carry what you need?),
- an **AI-security or monitoring vendor** (will you emit/consume ACA evidence?),
- a **systems integrator** (will you build connectors?),
- and **two enterprises** running real AI (does this reduce your control + audit burden?).

If ACA becomes portable across your tools, it's a standard. If it only produces plugins for one product, it's just another platform, and design-partner feedback is how we stay on the right side of that line.

**To comment:** open an issue, or reach the stewards. Everything here is a proposal.

---

## 12. Open questions (we want your input)

- Evidence **package** format for exchange with auditors (many objects + signed manifest).
- A standard, reproducible **query encoding** so a check can be re-run by a different tool.
- **Revocation** semantics for previously emitted evidence.
- **Per-tier evidence profiles** (minimum evidence sets for T1…T5) so "enough proof" is objective.
- Whether renderers should be sandboxed at the same level as connectors.
- The right first three **first-party connectors** to seed the ecosystem.
