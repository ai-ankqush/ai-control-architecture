# Pillar 10: Prompt & Input Control

**Control question:** *What is shaping the AI's behavior?*
**Surface:** See (the input path into inference).

---

## Purpose

An AI's behavior is shaped by what enters its context, the user's prompt, the system instructions, and, critically, the **retrieved and third-party content** the AI reads along the way. This pillar treats that input path as an attack surface. It governs prompt injection, instruction override, and manipulation, so that untrusted content cannot silently redirect what the AI sees, decides, or does.

---

## Why it matters

In traditional software, code and data are separate. In an LLM, **instructions and data share one channel**, the model reads its system prompt, the user's message, and retrieved documents as one stream of text, and any of them can contain instructions. That is the root of prompt injection: a malicious instruction hidden in a web page, a document, an email, or a tool result can override the system's intent and turn the AI against its own controls, exfiltrating data, invoking tools, or ignoring its guardrails. As AI gains retrieval and tools, the input path becomes the primary way an attacker reaches the actions in [pillar 12](12-pillar-tool-and-action-control.md). You cannot bound what an AI does without bounding what shapes it.

---

## Control objectives

- Treat **all untrusted input**, including retrieved and tool-returned content, as potentially adversarial.
- **Mitigate prompt injection and manipulation** proportionate to the use case's tier and reach.
- **Protect system instructions** from override by user input or retrieved content.

---

## Requirements

From the [Requirements Catalogue](06-requirements-catalogue.md):

| ID | Requirement | From | Boundary |
|----|-------------|------|----------|
| ACA-10-01 | Untrusted input, including retrieved content, is treated as potentially adversarial. | T3 | Evidenced |
| ACA-10-02 | Prompt-injection and manipulation are mitigated proportionate to tier. | T3 | Verified |
| ACA-10-03 | System instructions are protected from override by user or retrieved content. | T4 | Enforced |

---

## Key controls

- **Trust separation**: distinguish trusted instructions from untrusted content in how the context is assembled; do not let retrieved or tool-returned text be interpreted as authoritative instruction.
- **Injection detection & filtering**: screen inputs and retrieved content for known injection and manipulation patterns proportionate to tier (a gateway or "prompt firewall").
- **Instruction integrity**: structure prompts and system messages so user or retrieved content cannot override policy, and so the model's guardrails are not addressable by input.
- **Reach-limiting**: the strongest mitigation is downstream: even a successful injection should hit a bounded data boundary ([09](09-pillar-data-boundary-control.md)) and an allow-listed, approval-gated action set ([12](12-pillar-tool-and-action-control.md)). Input control and action control are defense-in-depth for each other.
- **Content provenance**: where feasible, track and weight the trustworthiness of the sources feeding the context.

---

## Tier guidance

| | T1 | T2 | T3 | T4 | T5 |
|---|----|----|----|----|----|
| Untrusted input treated as adversarial | - | Recommended | Required | Required | Required |
| Injection mitigation | - | Recommended | Required (verified) | Required (verified + tested) | Required (verified + tested) |
| System-instruction protection | - | - | Recommended | Required (enforced) | Required (enforced) |
| Adversarial input testing | - | - | Recommended | Required | Required (see [14](14-pillar-assurance-and-testing.md)) |

---

## Evidence

The [AI Prompt & Input Control template](../templates/ai-prompt-and-input-control-template.md) captures the trust-separation design, the mitigations in place, and the test results. Boundary source reaches *Verified* when injection mitigations are tested against known techniques, and *Enforced* when a control point actively blocks or neutralizes injected instructions inline.

---

## Standards crosswalk

Maps to NIST AI RMF **Measure/Manage**, ISO/IEC 42001 operational controls, EU AI Act (accuracy, robustness, cybersecurity, Art. 15), and directly to OWASP LLM (prompt injection, insecure output handling) and the OWASP Agentic Top 10. See [`mappings/`](../mappings/MAPPINGS-README.md).

---

## Failure modes

- A document, web page, or email carrying a hidden instruction the AI obeys.
- Retrieved content that overrides the system prompt and disables guardrails.
- A tool result that injects instructions the agent then acts on.
- Treating input control as the *only* defense, with no downstream action limits behind it.

---

**Next:** [11 · Output & Decision Control](11-pillar-output-and-decision-control.md)

*Version 0.1.0 · Licensed under the terms in [LICENSE.md](../LICENSE.md).*
