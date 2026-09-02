# NYDFS Part 500 (23 NYCRR 500) Crosswalk

This document maps the AI Control Architecture to the New York Department of Financial Services Cybersecurity Regulation, 23 NYCRR Part 500, as it applies to artificial intelligence.

The purpose of this crosswalk is to show how the AI Control Architecture can help covered entities fold AI-related risk into the Part 500 cybersecurity program they already run, through practical controls, evidence, assurance, and incident readiness.

The AI Control Architecture is not a replacement for 23 NYCRR Part 500.

It is an implementation layer that helps translate Part 500 cybersecurity requirements, and NYDFS AI guidance, into enterprise control activities for AI systems.

---

# 1. Positioning

NYDFS regulates AI through a cybersecurity lens, not as a separate AI-model-governance regime. Its October 2024 guidance on AI-related cybersecurity risk, and subsequent advisories, direct covered entities to read AI-related threats into the Part 500 risk assessment and controls already on the books. The amended Part 500 requirements, including written asset-inventory procedures, took full effect on November 1, 2025.

The AI Control Architecture helps answer:

```text
How do we bring AI systems, their data, their access, their third-party dependencies, and their failure modes inside our existing Part 500 cybersecurity program with evidence?
```

Part 500 focuses on the cybersecurity program.

AI Control Architecture focuses on operational AI control.

Together, they can be used as:

```text
23 NYCRR Part 500 = Cybersecurity program requirements
AI Control Architecture = AI control implementation layer inside that program
```

---

# 2. NYDFS AI Risk Areas

NYDFS calls out four AI-related risk areas that covered entities must read into their existing program:

```text
1. AI-enabled social engineering and deepfakes
2. AI-enhanced cyberattacks
3. Theft of nonpublic information used to train AI models
4. Third-party, vendor, and supply-chain AI risk
```

These are new threat scenarios, not new control families. The Part 500 risk assessment, access controls, third-party policy, monitoring, and training programs are expected to address them.

---

# 3. AI Control Architecture Pillars

The AI Control Architecture uses ten pillars:

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

These pillars provide the operational control structure that can support Part 500 outcomes for AI systems.

---

# 4. High-Level Crosswalk

| 23 NYCRR Part 500 Requirement | Primary AI Control Architecture Support |
|---|---|
| 500.2 / 500.3 Cybersecurity program and policy | AI inventory and classification; human accountability model |
| 500.4 CISO oversight and governance | Human accountability model; monitoring, logging, and evidence |
| 500.5 Vulnerability assessment and penetration testing | AI assurance and testing |
| 500.7 Access privileges and management | AI identity and access control |
| 500.9 Risk assessment | AI inventory and classification; data boundary; prompt and input control |
| 500.11 Third-party service provider security | AI inventory and classification (vendor AI review and AI supply chain) |
| 500.12 Multi-factor authentication | AI identity and access control |
| 500.13 Asset management and data retention (asset inventory) | AI inventory and classification; data boundary control |
| 500.14 Monitoring and cybersecurity awareness training | Monitoring, logging, and evidence; prompt and input control |
| 500.16 / 500.17 Incident response, BCDR, and notification | Incident containment and recovery |

---

# 5. Risk Assessment (500.9) with AI

## Part 500 Intent

Covered entities must conduct and periodically update a risk assessment that informs the design of the cybersecurity program. NYDFS expects AI-related risks to be included.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture operationalizes this by requiring that AI systems are inventoried and classified, that the data they can reach is mapped and bounded, that their input surfaces (including deepfake and social-engineering exposure) are understood, and that their risk is tiered, feeding the Part 500 risk assessment with AI-specific findings.

## Relevant AI Control Architecture Pillars

| Pillar | Contribution |
|---|---|
| AI inventory and classification | Identifies AI systems, their pattern, owners, and risk tier for inclusion in the risk assessment. |
| Data boundary control | Maps data the AI can reach, including nonpublic information used in prompts, retrieval, or training. |
| Prompt and input control | Identifies input surfaces exposed to AI-enabled social engineering and deepfake content. |
| AI identity and access control | Identifies AI identities and their authority for the risk assessment. |

## Implementation Activities

```text
Inventory AI systems in use.
Classify each AI system and assign a risk tier.
Map data the AI can access, including nonpublic information.
Identify input surfaces exposed to deepfakes and social engineering.
Identify vendor and third-party AI dependencies.
Feed AI findings into the Part 500 risk assessment.
Update on material change.
```

## Example Evidence

```text
AI inventory record
AI risk tier record
AI data source map
Input surface record
Vendor AI dependency record
Updated Part 500 risk assessment with AI findings
```

---

# 6. Asset Inventory and Access (500.13, 500.7, 500.12)

## Part 500 Intent

Covered entities must maintain written policies and procedures for asset inventory (500.13), manage access privileges with least privilege and periodic review (500.7), and apply multi-factor authentication (500.12).

## AI Control Architecture Implementation Interpretation

The AI Control Architecture operationalizes this by treating AI systems and their identities as first-class assets: inventoried, owned, access-scoped, and access-reviewed, so AI does not sit outside the asset and access program.

## Relevant AI Control Architecture Pillars

| Pillar | Contribution |
|---|---|
| AI inventory and classification | Provides the AI portion of the asset inventory. |
| AI identity and access control | Maps AI identities, delegated authority, least-privilege scoping, review, and revocation. |
| Data boundary control | Bounds the data an AI identity can reach. |

## Implementation Activities

```text
Add AI systems and AI identities to the asset inventory.
Assign owners.
Scope AI access to least privilege.
Apply and verify authentication controls for AI access paths.
Review and revoke AI access on a defined cadence.
```

## Example Evidence

```text
AI asset inventory entries
AI identity and access record
Least-privilege scoping record
Access review record
Revocation record
```

---

# 7. Third-Party and Vendor AI (500.11)

## Part 500 Intent

Covered entities must maintain policies and procedures to ensure the security of information systems and nonpublic information accessible to, or held by, third-party service providers.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture operationalizes this through vendor AI review and AI supply-chain visibility: identifying vendor AI in the estate, the data it can reach, its provenance, and its residual risk, one of the four AI risk areas NYDFS names.

## Relevant AI Control Architecture Pillars

| Pillar | Contribution |
|---|---|
| AI inventory and classification | Records vendor AI use cases and the AI supply chain behind them. |
| Data boundary control | Maps nonpublic information a vendor AI can reach. |
| Human accountability model | Assigns vendor owners and review responsibility. |
| AI assurance and testing | Supports validation of vendor AI claims and commitments. |

## Implementation Activities

```text
Identify vendor AI in the estate.
Map data each vendor AI can access.
Record provenance and training-data commitments where applicable.
Assess residual risk and record decisions.
Assign vendor owners and review cadence.
```

## Example Evidence

```text
Vendor AI review record
AI supply-chain / dependency record
Vendor data-access map
Vendor commitment record
Vendor risk decision
```

---

# 8. Testing, Monitoring, and Awareness (500.5, 500.14)

## Part 500 Intent

Covered entities must perform vulnerability assessments and penetration testing (500.5), monitor systems, and run cybersecurity awareness training including social-engineering exercises (500.14).

## AI Control Architecture Implementation Interpretation

The AI Control Architecture operationalizes this through adversarial assurance of AI systems (including prompt-injection and AI-specific attack testing), continuous monitoring and evidence, and input controls that reduce exposure to AI-enabled social engineering and deepfakes.

## Relevant AI Control Architecture Pillars

| Pillar | Contribution |
|---|---|
| AI assurance and testing | Provides AI penetration and red-team testing (prompt injection, data exfiltration, tool misuse). |
| Monitoring, logging, and evidence | Provides monitoring, logs, and evidence for AI systems. |
| Prompt and input control | Reduces exposure to deepfake and social-engineering inputs. |
| Output and decision control | Validates AI outputs used in workflows. |

## Implementation Activities

```text
Include AI systems in penetration testing and vulnerability assessment.
Run AI-specific adversarial testing (prompt injection, exfiltration, tool misuse).
Monitor AI systems and retain logs and evidence.
Include AI-enabled social engineering and deepfakes in awareness training.
```

## Example Evidence

```text
AI penetration / red-team test results
Vulnerability assessment record
AI monitoring and log evidence
Awareness training record covering AI threats
```

---

# 9. Incident Response and Notification (500.16, 500.17)

## Part 500 Intent

Covered entities must maintain an incident response plan and business continuity and disaster recovery plans (500.16), and notify the superintendent of qualifying cybersecurity events within 72 hours (500.17).

## AI Control Architecture Implementation Interpretation

The AI Control Architecture operationalizes this by defining containment, correction, and recovery for AI-specific incidents, including the ability to disable AI capabilities, revoke AI identities and tool access, and correct AI-generated records, and by producing the evidence needed for timely notification.

## Relevant AI Control Architecture Pillars

| Pillar | Contribution |
|---|---|
| Incident containment and recovery | Defines AI containment, kill switch, recovery, and restart criteria. |
| Tool and action control | Enables disabling of AI actions during an incident. |
| AI identity and access control | Enables revocation of AI identities and access. |
| Monitoring, logging, and evidence | Provides the evidence needed for notification and reconstruction. |

## Implementation Activities

```text
Extend the incident response plan to AI-specific incidents.
Define containment: disable AI, revoke identities, block tools.
Define correction of AI-generated records and outputs.
Preserve logs and evidence for reconstruction.
Produce notification evidence within required timelines.
```

## Example Evidence

```text
AI incident response procedure
AI containment evidence
AI identity revocation record
Corrected records evidence
Notification evidence
Post-incident review
```

---

# 10. Pillar-to-Part 500 Matrix

| AI Control Architecture Pillar | Risk Assessment | Asset & Access | Third-Party | Testing & Monitoring | Incident |
|---|---:|---:|---:|---:|---:|
| AI inventory and classification | Primary | Primary | Primary | Supporting | Supporting |
| AI identity and access control | Supporting | Primary | Supporting | Supporting | Primary |
| Data boundary control | Primary | Primary | Primary | Supporting | Supporting |
| Prompt and input control | Primary | Supporting | Supporting | Primary | Supporting |
| Output and decision control | Supporting | Supporting | Supporting | Primary | Supporting |
| Tool and action control | Supporting | Supporting | Supporting | Supporting | Primary |
| Human accountability model | Supporting | Primary | Primary | Supporting | Primary |
| AI assurance and testing | Supporting | Supporting | Supporting | Primary | Supporting |
| Monitoring, logging, and evidence | Supporting | Supporting | Supporting | Primary | Primary |
| Incident containment and recovery | Supporting | Supporting | Supporting | Supporting | Primary |

---

# 11. Example: Mapping a Customer-Facing AI Assistant at a NY-Regulated Insurer

## Use Case

```text
Generative-AI assistant that answers policyholder questions and can reach nonpublic information.
```

## Part 500 Mapping

| Part 500 Area | AI Control Architecture Implementation |
|---|---|
| Risk assessment (500.9) | Inventory and tier the assistant; map nonpublic information it can reach; note deepfake and social-engineering exposure. |
| Asset and access (500.13, 500.7) | Add it to the asset inventory; scope its identity to least privilege; review access. |
| Third-party (500.11) | Record the model vendor and its data commitments in the AI supply chain. |
| Testing and monitoring (500.5, 500.14) | Red-team for prompt injection and data exfiltration; monitor and log. |
| Incident (500.16, 500.17) | Define containment and produce notification evidence. |

## Example Evidence

```text
AI inventory and risk tier
NPI data-access map
Vendor AI review record
Prompt injection and exfiltration test results
Monitoring and log evidence
Incident containment and notification evidence
```

---

# 12. How to Use This Crosswalk

Use this crosswalk when:

```text
A NYDFS-covered entity wants to bring AI systems inside its Part 500 program.
A CISO or risk team asks how AI control work maps to 23 NYCRR Part 500.
An examination or audit team wants AI evidence aligned to Part 500 requirements.
A third-party risk team wants to address vendor AI under 500.11.
A governance team wants to fold AI risk into the existing cybersecurity program rather than build a separate one.
```

Suggested use:

```text
1. Inventory AI systems and add them to the asset inventory.
2. Tier AI risk and feed the Part 500 risk assessment.
3. Scope AI identities and access.
4. Review vendor AI under the third-party policy.
5. Red-team and monitor AI systems.
6. Extend incident response to AI incidents.
7. Retain evidence for examination and notification.
```

---

# 13. Limitations

This crosswalk is intended to support cybersecurity program implementation and AI control.

It is not:

```text
A NYDFS approval or examination outcome
A compliance guarantee
A legal opinion
An audit opinion
A complete mapping to every Part 500 section
```

NYDFS guidance treats AI risk through the existing cybersecurity program; this crosswalk follows that reading. Organizations should tailor it to their own legal, compliance, and examination requirements, and confirm current Part 500 requirements and effective dates.

---

# 14. Summary

NYDFS expects covered entities to fold AI risk into the Part 500 cybersecurity program, the risk assessment, asset inventory, access controls, third-party policy, testing, monitoring, training, and incident response they already run.

The AI Control Architecture helps them do that with AI-specific controls and evidence, so AI systems do not sit outside the program.

Together, they support a movement from:

```text
AI risk noticed
```

to:

```text
AI risk controlled inside the cybersecurity program
```
