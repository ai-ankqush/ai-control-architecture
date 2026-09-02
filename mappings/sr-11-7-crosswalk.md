# SR 11-7 Model Risk Management Crosswalk

This document maps the AI Control Architecture to the Federal Reserve and OCC supervisory guidance on model risk management, commonly referred to as SR 11-7 (Board of Governors SR Letter 11-7; OCC Bulletin 2011-12).

The purpose of this crosswalk is to show how the AI Control Architecture can help financial institutions operationalize SR 11-7 for AI and machine-learning models through practical controls, evidence, independent challenge, and ongoing monitoring.

The AI Control Architecture is not a replacement for SR 11-7.

It is an implementation layer that helps translate model risk management expectations into enterprise control activities for AI, machine-learning, generative-AI, and agentic systems.

---

# 1. Positioning

SR 11-7 defines the supervisory expectations for managing model risk, the potential for adverse consequences from decisions based on incorrect or misused model outputs.

The AI Control Architecture helps answer:

```text
How do we implement model risk expectations for AI and machine-learning models inside enterprise systems, data, access, decisions, actions, assurance, monitoring, and incident response?
```

SR 11-7 focuses on managing model risk.

AI Control Architecture focuses on operational control.

Together, they can be used as:

```text
SR 11-7 = Model risk management expectations
AI Control Architecture = Control implementation layer for AI and ML models
```

Scope note: SR 11-7 applies to quantitative methods that turn inputs into outputs used in decisions. Supervisory practice in 2025-2026 treats machine-learning, generative-AI, LLM, and agentic systems that inform or execute business decisions as models within scope. This crosswalk is written for that reading.

---

# 2. SR 11-7 Elements of a Sound Framework

SR 11-7 organizes a sound model risk management framework around three elements:

```text
1. Model development, implementation, and use
2. Model validation (including effective challenge)
3. Governance, policies, and controls
```

Two supervisory expectations run across all three:

```text
Effective challenge: critical, independent review by parties with the competence, authority, and incentive to challenge.
Model inventory: a complete, maintained record of models, their risk rating, owners, and status.
```

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

These pillars provide the operational control structure that can support SR 11-7 outcomes for AI and ML models.

---

# 4. High-Level Crosswalk

| SR 11-7 Element | Primary AI Control Architecture Support |
|---|---|
| Model development, implementation, and use | AI inventory and classification; data boundary control; prompt and input control; output and decision control; tool and action control |
| Model validation and effective challenge | AI assurance and testing; output and decision control; monitoring, logging, and evidence |
| Governance, policies, and controls | AI inventory and classification; human accountability model; monitoring, logging, and evidence; incident containment and recovery |

Two cross-cutting SR 11-7 expectations map directly:

```text
Effective challenge  = AI assurance and testing (independent validation), including adversarial red-team challenge of model behavior.
Model inventory      = AI inventory and classification (the AI/model inventory, risk rating, owners, and lifecycle status).
Model risk rating    = AI risk tiering.
Ongoing monitoring   = Monitoring, logging, and evidence.
```

---

# 5. Model Development, Implementation, and Use

## SR 11-7 Intent

Models should be developed on sound theory and logic, use appropriate and quality-checked data, be tested for fitness of purpose, be well documented, and be used only for the purposes for which they are appropriate. Controls should surround implementation and ongoing use.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture operationalizes this by requiring that each model is inventoried and classified, that its data sources and boundaries are defined and appropriate, that inputs are controlled, that outputs and decisions are validated and used only within their intended purpose, and that any tools or actions the model can trigger are bounded.

## Relevant AI Control Architecture Pillars

| Pillar | Contribution to Development, Implementation, and Use |
|---|---|
| AI inventory and classification | Records the model, its pattern, intended use, lifecycle status, and risk tier. |
| Data boundary control | Defines the data sources, quality boundaries, retrieval scope, retention, and reuse limits. |
| Prompt and input control | Controls input surfaces and external content that shape model behavior. |
| Output and decision control | Validates outputs and constrains use to the intended purpose. |
| Tool and action control | Bounds any action a model-driven or agentic system can take. |

## Implementation Activities

```text
Inventory the model and its intended purpose.
Classify the model pattern and autonomy level.
Assign a model risk tier.
Map and quality-check data sources.
Define data and retrieval boundaries.
Control input surfaces and external content.
Define appropriate-use limits for outputs and decisions.
Validate outputs against intended purpose.
Bound tools and actions the model can trigger.
Document development, data, assumptions, and limitations.
```

## Example Evidence

```text
Model inventory record
Model purpose and scope statement
Data source map and data-quality record
Retrieval boundary record
Input control record
Output validation evidence
Appropriate-use limits
Tool and action inventory
Model documentation package
```

---

# 6. Model Validation and Effective Challenge

## SR 11-7 Intent

Model validation is the set of processes and activities that verify models are performing as expected and are conceptually sound. It requires effective challenge, critical, independent review by parties with competence, authority, and incentive to challenge. Validation covers evaluation of conceptual soundness, ongoing monitoring (process verification and benchmarking), and outcomes analysis (including back-testing). Validation should cover all model components: inputs, processing, and reports.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture operationalizes validation and effective challenge through independent assurance and testing of model behavior and control effectiveness, adversarial red-team challenge of the model on its real authority path, output and decision validation, and ongoing monitoring for drift and performance. Independence is enforced through the human accountability model (a validator role distinct from the model owner).

## Relevant AI Control Architecture Pillars

| Pillar | Contribution to Validation and Effective Challenge |
|---|---|
| AI assurance and testing | Provides the independent test of conceptual soundness, control effectiveness, and adversarial (red-team) challenge, the operational form of effective challenge. |
| Output and decision control | Provides output validation, decision evidence, and appropriate-use checks. |
| Monitoring, logging, and evidence | Provides ongoing monitoring, benchmarking, drift detection, and outcomes evidence. |
| Human accountability model | Assigns an independent validator role with authority and incentive to challenge, distinct from the model owner. |
| Prompt and input control | Supports testing of prompt-injection and input-manipulation exposure. |
| Data boundary control | Supports data-leakage and retrieval-boundary testing. |

## Implementation Activities

```text
Assign an independent validator distinct from the model owner.
Evaluate conceptual soundness and assumptions.
Test the model on its real authority path (red-team / effective challenge).
Test explainability sufficient to support challenge.
Test output validation and decision evidence.
Test prompt injection and input manipulation.
Test data and retrieval boundaries.
Establish ongoing monitoring, benchmarking, and drift detection.
Perform outcomes analysis and back-testing where applicable.
Record findings, severity, and required remediation.
Re-validate on material change or on a defined cadence.
```

## Example Evidence

```text
Independent validation report
Effective-challenge / red-team findings
Conceptual soundness assessment
Explainability assessment
Output validation results
Prompt injection and input test results
Data and retrieval boundary test results
Ongoing monitoring and benchmarking results
Outcomes analysis / back-test results
Findings register and remediation plan
Re-validation record
```

---

# 7. Governance, Policies, and Controls

## SR 11-7 Intent

Model risk should be governed by a framework with board and senior management oversight, policies and procedures, clear roles and responsibilities, a maintained model inventory, documentation standards, model risk tiering by materiality, internal audit review, and controls over model use and change.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture operationalizes governance through a maintained AI/model inventory with risk tiering, an accountability model that assigns owners and independent validators and defines oversight and decision rights, evidence and documentation for audit, and defined incident containment for model failure.

## Relevant AI Control Architecture Pillars

| Pillar | Contribution to Governance, Policies, and Controls |
|---|---|
| AI inventory and classification | Maintains the model inventory, risk rating, lifecycle status, and change tracking. |
| Human accountability model | Assigns model owners, independent validators, risk owners, and defines oversight and decision rights. |
| Monitoring, logging, and evidence | Provides documentation, audit evidence, and reporting. |
| Incident containment and recovery | Defines containment, correction, and recovery for model failure. |
| AI assurance and testing | Provides validation evidence that supports internal audit and governance confidence. |

## Implementation Activities

```text
Maintain a complete model inventory.
Assign a model risk rating to every model.
Assign model owners and independent validators.
Define oversight, decision rights, and approval authority.
Define policies for development, validation, use, and change.
Define documentation standards.
Enable internal audit review of the framework.
Define exception and risk-acceptance processes.
Define incident containment for model failure.
Report model risk metrics to senior management and the board.
```

## Example Evidence

```text
Model inventory
Model risk rating record
Ownership and validator assignment
Governance policy and decision-rights record
Documentation standard
Internal audit record
Exception and risk-acceptance record
Model change record
Incident containment record
Model risk reporting to senior management and the board
```

---

# 8. Pillar-to-SR 11-7 Element Matrix

| AI Control Architecture Pillar | Development / Use | Validation & Effective Challenge | Governance & Controls |
|---|---:|---:|---:|
| AI inventory and classification | Primary | Supporting | Primary |
| AI identity and access control | Supporting | Supporting | Supporting |
| Data boundary control | Primary | Primary | Supporting |
| Prompt and input control | Primary | Primary | Supporting |
| Output and decision control | Primary | Primary | Supporting |
| Tool and action control | Primary | Supporting | Supporting |
| Human accountability model | Supporting | Primary | Primary |
| AI assurance and testing | Supporting | Primary | Primary |
| Monitoring, logging, and evidence | Supporting | Primary | Primary |
| Incident containment and recovery | Supporting | Supporting | Primary |

---

# 9. SR 11-7 Concept to AI Control Architecture Equivalent

| SR 11-7 Concept | AI Control Architecture Equivalent |
|---|---|
| Model inventory | AI inventory and classification (the AI/model inventory) |
| Model risk rating (materiality and complexity) | AI risk tiering |
| Effective challenge | Independent AI assurance and testing, including adversarial red-team challenge |
| Conceptual soundness review | Assurance evaluation of model logic, assumptions, and limitations |
| Ongoing monitoring | Monitoring, logging, and evidence (drift, performance, benchmarking) |
| Outcomes analysis / back-testing | Outcomes evidence and validation results |
| Model documentation | Evidence and documentation package |
| Roles and independence | Human accountability model (owner vs independent validator) |
| Model change control | Inventory change tracking and re-validation trigger |
| Model failure response | Incident containment and recovery |

---

# 10. Example: Mapping a Credit Decision Model (ML)

## Use Case

```text
Machine-learning model that supports consumer credit decisions.
```

## SR 11-7 Element Mapping

| SR 11-7 Element | AI Control Architecture Implementation |
|---|---|
| Development, implementation, and use | Inventory the model, classify it, tier its risk, map and quality-check data, define appropriate-use limits, and validate outputs. |
| Validation and effective challenge | Assign an independent validator, evaluate conceptual soundness, red-team the model, test for bias and data leakage, and establish ongoing monitoring and back-testing. |
| Governance, policies, and controls | Record the model in inventory with a risk rating, assign owner and validator, enforce change control and re-validation, and report model risk to senior management. |

## Example Evidence

```text
Model inventory record
Model risk rating
Data-quality and data source map
Independent validation report
Effective-challenge / red-team findings
Bias and data-leakage test results
Ongoing monitoring and back-test results
Model change and re-validation record
```

---

# 11. Example: Mapping an Agentic AI Assistant

## Use Case

```text
Agentic assistant that can take actions in banking workflows.
```

## SR 11-7 Element Mapping

| SR 11-7 Element | AI Control Architecture Implementation |
|---|---|
| Development, implementation, and use | Inventory the agent, classify its autonomy, bound its tools and actions, and define appropriate use. |
| Validation and effective challenge | Independently challenge the agent on its real authority path (tool misuse, approval bypass, unsafe action), test explainability sufficient to challenge, and monitor for drift. |
| Governance, policies, and controls | Assign owner and independent validator, enforce approval gates and change control, and define containment for unsafe action. |

Note: SR 11-7 was written for traditional models and strains on agentic systems, where a model can also take actions. The AI Control Architecture closes that gap through tool and action control, approval gates, and incident containment, controls that a purely quantitative model-risk framework does not describe.

---

# 12. How to Use This Crosswalk

Use this crosswalk when:

```text
A bank or financial institution wants to bring AI and ML models under its SR 11-7 model risk management framework.
A model risk management or validation team asks how AI control work maps to SR 11-7.
An independent validation function wants to operationalize effective challenge for AI models.
An internal audit or examination team wants AI model evidence aligned to SR 11-7 expectations.
A governance team wants to avoid creating a competing framework alongside model risk management.
```

Suggested use:

```text
1. Confirm the AI/ML system is in scope as a model.
2. Add it to the model inventory and assign a model risk rating.
3. Map it to the three SR 11-7 elements.
4. Identify which AI Control Architecture pillars apply.
5. Assign an independent validator distinct from the model owner.
6. Run effective challenge, including adversarial red-team testing.
7. Establish ongoing monitoring and outcomes analysis.
8. Record findings, re-validation triggers, and reporting.
```

---

# 13. Limitations

This crosswalk is intended to support model risk management and AI control implementation.

It is not:

```text
A supervisory approval or examination outcome
A compliance guarantee
A legal opinion
An audit or validation opinion
A complete mapping to every SR 11-7 expectation
```

Organizations should tailor this crosswalk to their own model risk policy, validation standards, internal audit, legal, and supervisory expectations. Where a model also takes actions, controls beyond traditional model risk management (tool/action control, approval gates, incident containment) apply.

---

# 14. Summary

SR 11-7 sets the expectation that models are developed soundly, independently validated through effective challenge, and governed with a maintained inventory and clear ownership.

The AI Control Architecture helps financial institutions implement those expectations for AI and machine-learning models through practical controls, independent and adversarial assurance, ongoing monitoring, and incident containment.

Together, they support a movement from:

```text
Model risk management intention
```

to:

```text
Operational AI model control and effective challenge
```
