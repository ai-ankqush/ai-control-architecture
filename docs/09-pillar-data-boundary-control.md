# Pillar 09: Data Boundary Control

**Control question:** *What can the AI see?*
**Surface:** See.

---

## Purpose

This pillar defines and enforces the **boundary around the data an AI can reach**, what it may retrieve, what it may not, and what must never leave a controlled space. It is the confidentiality and data-protection core of the architecture: the difference between an AI that operates on the data it should, and one that quietly surfaces, combines, or exposes data it should not.

---

## Why it matters

AI accesses data differently from traditional software. It does not just read a record it was granted, it *retrieves* context (RAG), *infers* across sources, and *composes* information in ways no access-control list anticipated. A retrieval index built from "all of SharePoint" will happily surface a document the asker was never entitled to. A copilot summarizing a thread can carry confidential context into a reply that leaves the boundary. A vendor feature may retain prompts the enterprise assumed were transient. The classic failure is not a breached database; it is an AI that had *legitimate* access to too much, and moved data across a line no one drew.

---

## Control objectives

- Explicitly define and approve the **data sources** an AI may access.
- Scope **retrieval** so the AI cannot surface data the requester is not entitled to.
- **Exclude or mask** sensitive data classes unless explicitly permitted for the use case.
- Know and bound **third-party processing and retention** of data the AI touches.

---

## Requirements

From the [Requirements Catalogue](06-requirements-catalogue.md):

| ID | Requirement | From | Boundary |
|----|-------------|------|----------|
| ACA-09-01 | The data sources an AI may access are explicitly defined and approved. | T2 | Evidenced |
| ACA-09-02 | Retrieval is scoped so AI cannot surface data the requester is not entitled to. | T2 | Verified |
| ACA-09-03 | Sensitive data classes are excluded or masked unless explicitly permitted. | T2 | Verified |
| ACA-09-04 | Third-party processing and retention of data are known and bounded. | T2 | Evidenced |

---

## Key controls

- **Source allow-listing**: the AI's data sources are declared and approved, not "whatever the index happened to ingest."
- **Entitlement-aware retrieval**: RAG and search respect the requester's permissions at query time (permission-trimmed retrieval), so the AI cannot become a permission-bypass.
- **Sensitive-class handling**: classification-aware exclusion, redaction, or masking of regulated or confidential data unless the use case is explicitly approved for it.
- **Egress and context boundaries**: prevent confidential context from being carried into outputs or destinations outside the approved space; constrain what the AI can *expose*, not only what it can *read*.
- **Vendor data terms**: for embedded/vendor AI, know what is sent, where it is processed, whether it is retained, and whether it trains the vendor's models; bound it contractually and technically.

---

## Tier guidance

| | T1 | T2 | T3 | T4 | T5 |
|---|----|----|----|----|----|
| Approved source list | - | Required | Required | Required | Required |
| Entitlement-aware retrieval | - | Required (verified) | Required (verified) | Required (verified) | Required (verified) |
| Sensitive-class masking | - | Required | Required | Required | Required |
| Vendor retention bounded | - | Required | Required | Required | Required |

---

## Evidence

The [AI Data Boundary template](../templates/ai-data-boundary-template.md) captures the approved sources, the retrieval scoping, the sensitive-class handling, and the vendor data terms. Boundary source reaches *Verified* when entitlement-aware retrieval is confirmed against the live system (e.g., a user cannot retrieve what they can't otherwise access), and *Enforced* when a control point blocks out-of-boundary retrieval or egress.

---

## Standards crosswalk

Maps to NIST AI RMF **Map/Manage**, ISO/IEC 42001 (data governance for AI), EU AI Act (data governance, Art. 10), NYDFS Part 500 (data protection), GDPR/privacy obligations, and OWASP LLM (sensitive information disclosure). See [`mappings/`](../mappings/MAPPINGS-README.md).

---

## Failure modes

- A retrieval index that surfaces documents the asker was never entitled to.
- Confidential context summarized into an output that leaves the boundary.
- Sensitive data classes flowing to a use case never approved for them.
- Vendor AI retaining or training on prompts the enterprise assumed were transient.

---

**Next:** [10 · Prompt & Input Control](10-pillar-input-control.md)

*Version 0.1.0 · Licensed under the terms in [LICENSE.md](../LICENSE.md).*
