# US State AI Laws Crosswalk (Appendix)

This document maps the AI Control Architecture to the principal United States state artificial-intelligence laws as of mid-2026. It is a lighter, appendix-style companion to the framework crosswalks (NIST AI RMF, ISO/IEC 42001, EU AI Act) and the US financial-services crosswalks (SR 11-7, NYDFS Part 500).

The state landscape is unsettled. Laws are being enacted, narrowed, repealed, and replaced, and federal policy has signaled possible preemption of state AI regulation. Treat this crosswalk as a moving target and confirm current law before relying on it.

The AI Control Architecture does not determine legal obligations. It provides the controls and evidence that help an organization meet whatever obligations apply.

---

# 1. Positioning

Most enacted state AI laws converge on a small set of operational obligations:

```text
Notice and disclosure that AI or automated decision-making is in use.
Documentation of the AI system and how it works.
Human review or human decision-making for consequential outcomes.
Explanation or contestability for adverse decisions.
Testing for discrimination or bias, in some sectors.
Transparency of AI-generated content or training data, in some states.
```

Each maps cleanly to AI Control Architecture pillars, so one Neo assessment can produce evidence across several state laws at once.

---

# 2. AI Control Architecture Pillars

```text
1. AI inventory and classification
2. AI identity and access control
3. Data boundary control
4. Prompt and input control
5. Output and decision control
6. Tool and action control
7. Human accountability model
8. AI assurance and testing
9. Monitoring, logging, and evidence
10. Incident containment and recovery
```

---

# 3. State Law Crosswalk

## Colorado: SB 26-189 (ADMT)

Colorado repealed and replaced its earlier comprehensive AI Act (SB 24-205) with SB 26-189, a narrower law on automated decision-making technology that materially influences consequential decisions, effective January 1, 2027. Core obligations: pre-use consumer notice, adverse-outcome explanation within a defined window, meaningful human review rights, and developer documentation duties. The earlier risk-management-program and impact-assessment duties were removed.

| Obligation | Primary Pillar | Implementation Interpretation | Example Evidence |
|---|---|---|---|
| Pre-use consumer notice of ADMT | Output and decision control; human accountability | Record where AI materially influences a consequential decision and the notice given. | Decision-impact record; notice artifact |
| Adverse-outcome explanation | Output and decision control | Produce a plain-language explanation of the decision and factors. | Decision explanation record |
| Meaningful human review | Human accountability model | Enforce and evidence a human review path for consequential decisions. | Human-in-the-loop control evidence |
| Developer documentation | AI inventory and classification | Maintain system documentation, intended use, and limitations. | Model documentation package |

## Texas: TRAIGA (HB 149)

The Texas Responsible Artificial Intelligence Governance Act took effect January 1, 2026. It focuses on government-agency use of AI, takes an intent-based approach to private-sector liability, and prohibits certain uses (for example, manipulation and unlawful discrimination) and certain biometric practices. Government agencies face disclosure duties.

| Obligation | Primary Pillar | Implementation Interpretation | Example Evidence |
|---|---|---|---|
| Government AI disclosure | Output and decision control; human accountability | Record and disclose where a government service uses AI. | AI inventory; disclosure record |
| Prohibited-use avoidance | Output and decision control; tool and action control | Constrain AI to permitted purposes and bound actions. | Appropriate-use limits; action bounds |
| Intent and documentation | AI inventory and classification | Document intended purpose and controls to support an intent-based defense. | Purpose and control documentation |

## California: AB 2013 and SB 942

Effective January 1, 2026. AB 2013 requires transparency about the data used to train generative-AI systems. SB 942 (AI Transparency Act) requires disclosure of AI-generated content.

| Obligation | Primary Pillar | Implementation Interpretation | Example Evidence |
|---|---|---|---|
| Training-data transparency (AB 2013) | Data boundary control; AI inventory and classification | Record model provenance and training-data characteristics through the AI supply chain. | AI supply-chain / AI-BOM record |
| AI-generated content disclosure (SB 942) | Output and decision control | Mark or disclose AI-generated outputs. | Output disclosure control evidence |

## Utah: SB 149 (AI Policy Act)

Effective May 1, 2024. Requires businesses in regulated industries (including healthcare, legal, and financial services) to disclose, on request, when a consumer is interacting with a generative-AI system rather than a human. Establishes the Office of Artificial Intelligence Policy.

| Obligation | Primary Pillar | Implementation Interpretation | Example Evidence |
|---|---|---|---|
| GenAI interaction disclosure | Output and decision control; human accountability | Enforce and evidence a disclosure control for GenAI interactions in regulated contexts. | Disclosure control record |

## New York City: Local Law 144 (AEDT)

Requires a bias audit of automated employment decision tools and candidate notice.

| Obligation | Primary Pillar | Implementation Interpretation | Example Evidence |
|---|---|---|---|
| Bias audit of AEDT | AI assurance and testing | Test the tool for disparate impact and record results. | Bias / disparate-impact test results |
| Candidate notice | Output and decision control | Record notice given before use. | Notice record |

## Illinois: HB 3773 (AI in Employment)

Effective January 1, 2026. Amends the Illinois Human Rights Act to address AI use in employment decisions, including discrimination and notice.

| Obligation | Primary Pillar | Implementation Interpretation | Example Evidence |
|---|---|---|---|
| No AI discrimination in employment | AI assurance and testing; output and decision control | Test for discriminatory outcomes and constrain decision use. | Bias test results; decision controls |
| Employee notice | Human accountability model | Record notice of AI use. | Notice record |

---

# 4. One Assessment, Many Laws

Because the state obligations converge, a single Neo assessment tends to produce the evidence several laws require:

| Recurring obligation | Pillar that produces the evidence |
|---|---|
| Disclosure / notice of AI use | Output and decision control; human accountability |
| Human review of consequential decisions | Human accountability model |
| Explanation / contestability | Output and decision control |
| Bias / discrimination testing | AI assurance and testing |
| Training-data / provenance transparency | Data boundary control; AI inventory and classification |
| System documentation | AI inventory and classification |

---

# 5. How to Use This Crosswalk

```text
1. Identify which states and sectors the use case touches.
2. Confirm current law and effective dates for those states.
3. Inventory and classify the AI system.
4. Identify the recurring obligations that apply.
5. Map them to the pillars above.
6. Produce the shared evidence once and reuse it across states.
7. Re-check as state law changes.
```

---

# 6. Limitations and Volatility Note

This crosswalk is intended to support AI control and evidence, not to determine legal obligations.

It is not:

```text
Legal advice
A compliance guarantee
A complete list of every state or local AI law
A stable snapshot, state AI law is changing rapidly
```

Specific volatility to note as of mid-2026:

```text
Colorado replaced its comprehensive AI Act with a narrower ADMT law (SB 26-189).
Federal policy has signaled possible preemption of state AI regulation.
Several state laws take effect on staggered 2026 and 2027 dates.
```

Because of this volatility, organizations targeting durable obligations should anchor on the financial-services regimes (SR 11-7, NYDFS Part 500) and treat state consumer-AI laws as a fast-moving overlay. Confirm current law with qualified legal counsel before relying on any mapping here.

---

# 7. Summary

US state AI laws converge on a handful of operational obligations, disclosure, documentation, human review, explanation, and bias testing, even as the specifics shift.

The AI Control Architecture produces the controls and evidence behind those obligations, so an organization can meet several state laws from one assessment, and adapt as the landscape moves.
