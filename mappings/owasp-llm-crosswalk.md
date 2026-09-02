# OWASP LLM Top 10 Crosswalk

This document maps the AI Control Architecture to the OWASP Top 10 for Large Language Model Applications.

The purpose of this crosswalk is to show how the AI Control Architecture can help enterprises translate LLM application security risks into practical controls, assurance tests, evidence, monitoring, and incident response.

The AI Control Architecture is not a replacement for OWASP guidance.

It is an enterprise control implementation layer that can help operationalize LLM application security expectations.

---

# 1. Positioning

OWASP provides security guidance for common risks in LLM applications.

The AI Control Architecture helps answer:

```text
How do we turn LLM application security risks into enterprise controls across identity, data, prompts, outputs, tools, evidence, assurance, and containment?
```

A useful positioning is:

```text
OWASP LLM Top 10 = LLM application security risk taxonomy
AI Control Architecture = enterprise control architecture and implementation layer
```

This crosswalk helps security, AppSec, red-team, platform, architecture, and governance teams connect LLM risks to operational control requirements.

---

# 2. OWASP LLM Top 10 Categories

The OWASP Top 10 for LLM Applications 2025 includes the following categories:

```text
LLM01: Prompt Injection
LLM02: Sensitive Information Disclosure
LLM03: Supply Chain
LLM04: Data and Model Poisoning
LLM05: Improper Output Handling
LLM06: Excessive Agency
LLM07: System Prompt Leakage
LLM08: Vector and Embedding Weaknesses
LLM09: Misinformation
LLM10: Unbounded Consumption
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

These pillars help enterprises turn OWASP risk categories into controls that are owned, tested, evidenced, monitored, and containable.

---

# 4. High-Level Crosswalk

| OWASP LLM Category | Primary AI Control Architecture Pillars |
|---|---|
| LLM01: Prompt Injection | Prompt and input control; tool and action control; AI assurance and testing |
| LLM02: Sensitive Information Disclosure | Data boundary control; prompt and input control; monitoring, logging, and evidence |
| LLM03: Supply Chain | AI inventory and classification; vendor AI review; data boundary control; evidence |
| LLM04: Data and Model Poisoning | Data boundary control; AI assurance and testing; monitoring, logging, and evidence |
| LLM05: Improper Output Handling | Output and decision control; human accountability; assurance and testing |
| LLM06: Excessive Agency | Tool and action control; AI identity and access control; incident containment |
| LLM07: System Prompt Leakage | Prompt and input control; monitoring, logging, and evidence; assurance and testing |
| LLM08: Vector and Embedding Weaknesses | Data boundary control; prompt and input control; assurance and testing |
| LLM09: Misinformation | Output and decision control; human accountability; assurance and testing |
| LLM10: Unbounded Consumption | Tool and action control; monitoring; incident containment; architecture controls |

---

# 5. LLM01: Prompt Injection

## OWASP Risk Theme

Prompt injection occurs when malicious or untrusted input manipulates the LLM into ignoring instructions, revealing information, producing unsafe output, or causing unintended behavior.

Prompt injection may be direct or indirect.

Indirect prompt injection can occur through:

```text
Retrieved documents
Uploaded files
Web pages
Emails
Tickets
Tool responses
Code comments
Logs
External content
```

## AI Control Architecture Implementation Interpretation

The AI Control Architecture treats prompts, retrieved content, uploaded files, external content, and tool responses as control surfaces.

The key control idea is:

```text
Untrusted content must be treated as data, not instruction.
```

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| Prompt and input control | Defines allowed inputs, prohibited inputs, prompt injection controls, system prompt protection, and context isolation. |
| Data boundary control | Controls retrieved content and external data sources. |
| Tool and action control | Prevents injected content from triggering unauthorized actions. |
| AI assurance and testing | Tests direct and indirect prompt injection. |
| Monitoring, logging, and evidence | Captures prompt injection attempts and policy violations. |
| Incident containment and recovery | Defines containment when injection succeeds. |

## Required Controls

```text
Classify trusted and untrusted inputs.
Define prohibited inputs.
Protect system prompts and policy prompts.
Separate instruction hierarchy from retrieved content.
Treat retrieved documents as untrusted context.
Treat uploaded files as untrusted context.
Treat tool responses as untrusted context.
Block or safely handle prompt injection attempts.
Require approval gates for high-risk tool actions.
Log prompt injection attempts where required.
Test direct and indirect prompt injection.
```

## Example Assurance Tests

```text
Test malicious user prompt asking model to ignore system instructions.
Test uploaded file containing hidden instructions.
Test retrieved document containing instruction to reveal secrets.
Test ticket text instructing agent to close ticket without approval.
Test tool response containing malicious instruction.
Test system prompt extraction attempt.
Test prompt injection to unauthorized tool use.
```

## Example Evidence

```text
Prompt/input control record
System prompt version history
Allowed/prohibited input rules
Context isolation design
Prompt injection test results
Blocked injection logs
Policy violation logs
Tool/action approval logs
Incident record if injection succeeds
```

## Related Project Files

```text
docs/10-pillar-input-control.md
docs/20-common-failure-scenarios.md
docs/24-assurance-and-audit-guide.md
templates/ai-prompt-and-input-control-template.md
templates/ai-assurance-test-plan-template.md
examples/rag-assistant-example.md
examples/agentic-ai-example.md
```

---

# 6. LLM02: Sensitive Information Disclosure

## OWASP Risk Theme

Sensitive information disclosure occurs when an LLM application exposes confidential, regulated, personal, privileged, security-sensitive, or proprietary information through prompts, retrieved context, outputs, logs, memory, or vendor processing.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture treats sensitive information disclosure as a data boundary, input, output, logging, and vendor control problem.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| Data boundary control | Defines approved data sources, classifications, retention, reuse, and retrieval boundaries. |
| Prompt and input control | Restricts sensitive data entry into prompts and uploads. |
| Output and decision control | Prevents sensitive data from appearing in uncontrolled outputs. |
| Monitoring, logging, and evidence | Protects prompt/output logs and monitors violations. |
| Vendor AI assessment | Reviews vendor data processing, retention, training/reuse, and subprocessors. |
| Incident containment and recovery | Defines response to data exposure. |

## Required Controls

```text
Map AI data sources.
Classify data.
Define prohibited data.
Define sensitive input restrictions.
Define retrieval boundaries.
Enforce user, role, tenant, or attribute boundaries.
Review vendor processing.
Review retention and training/reuse settings.
Protect prompt and output logs.
Test sensitive data leakage.
Define incident escalation for data exposure.
```

## Example Assurance Tests

```text
Test whether restricted documents can be retrieved.
Test whether sensitive prompts are blocked or warned.
Test whether secrets appear in outputs.
Test whether customer data appears for unauthorized user.
Test whether prompt/output logs store sensitive content.
Test whether vendor retention settings are configured correctly.
```

## Example Evidence

```text
Data source map
Data classification record
Data owner approval
Sensitive data restrictions
DLP or detection configuration
Retrieval boundary test
Data leakage test
Vendor assessment
Retention settings
Training/reuse settings
Incident record
```

## Related Project Files

```text
docs/09-pillar-data-boundary-control.md
templates/ai-data-boundary-template.md
templates/ai-vendor-assessment-template.md
examples/vendor-ai-example.md
```

---

# 7. LLM03: Supply Chain

## OWASP Risk Theme

Supply chain risk in LLM applications includes risks from models, datasets, plugins, tools, APIs, packages, vendors, hosted services, integrations, and dependencies.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture treats LLM supply chain risk as an inventory, vendor, data boundary, tool/action, evidence, and assurance issue.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| AI inventory and classification | Identifies AI systems, vendors, models, tools, and lifecycle status. |
| Data boundary control | Reviews vendor data processing, retention, reuse, and subprocessors. |
| Tool and action control | Reviews plugin, tool, API, and integration risk. |
| AI assurance and testing | Tests vendor/tool assumptions and control effectiveness. |
| Monitoring, logging, and evidence | Tracks vendor evidence and dependency-related logs. |
| Incident containment and recovery | Defines vendor escalation and disablement. |

## Required Controls

```text
Inventory AI vendors, models, plugins, tools, and integrations.
Review vendor AI feature enablement.
Review third-party model providers.
Review subprocessors.
Review model/API dependency.
Review tool/plugin permissions.
Review evidence availability.
Review vendor incident support.
Define vendor disablement path.
Track vendor changes.
```

## Example Assurance Tests

```text
Verify vendor AI feature enablement status.
Verify admin disablement path.
Verify tool/plugin permissions.
Request vendor evidence.
Test log export.
Test vendor incident contact path.
Review dependency changes.
```

## Example Evidence

```text
AI inventory
Vendor assessment
Subprocessor review
Third-party model provider disclosure
Tool inventory
Plugin review
Admin configuration record
Vendor evidence
Log export test
Vendor incident support path
```

## Related Project Files

```text
templates/ai-vendor-assessment-template.md
examples/vendor-ai-example.md
mappings/eu-ai-act-crosswalk.md
```

---

# 8. LLM04: Data and Model Poisoning

## OWASP Risk Theme

Data and model poisoning occurs when training data, fine-tuning data, retrieval data, embeddings, or model behavior are manipulated to produce biased, unsafe, incorrect, or attacker-controlled outputs.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture treats poisoning as a data governance, retrieval boundary, change control, monitoring, and assurance issue.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| Data boundary control | Defines approved data sources and prevents untrusted data from entering trusted context. |
| Prompt and input control | Treats external inputs as untrusted. |
| AI assurance and testing | Tests output behavior, retrieval integrity, and regression after changes. |
| Monitoring, logging, and evidence | Detects unexpected behavior and supports investigation. |
| Incident containment and recovery | Defines rollback, retraining, source removal, and recovery. |

## Required Controls

```text
Approve training, fine-tuning, and retrieval data sources.
Classify trusted and untrusted sources.
Control document ingestion into RAG indexes.
Control embedding/index lifecycle.
Review data update process.
Version prompts, retrieval logic, and data sources.
Test model or retrieval behavior after material changes.
Monitor unexpected output shifts.
Define rollback or source removal process.
```

## Example Assurance Tests

```text
Introduce malicious content into test retrieval source.
Test whether unapproved documents enter index.
Test output behavior before and after source update.
Test whether poisoned knowledge article influences output.
Test source removal and index rebuild.
Test regression after retrieval changes.
```

## Example Evidence

```text
Approved data source list
Data ingestion record
Embedding/index configuration
Source change record
Prompt/model/retrieval version history
Poisoning test result
Regression test result
Monitoring alert
Rollback evidence
Incident record
```

## Related Project Files

```text
docs/09-pillar-data-boundary-control.md
docs/24-assurance-and-audit-guide.md
examples/rag-assistant-example.md
```

---

# 9. LLM05: Improper Output Handling

## OWASP Risk Theme

Improper output handling occurs when LLM output is trusted or passed downstream without validation, escaping, review, authorization, or appropriate controls.

This can lead to unsafe decisions, code execution, injections, incorrect records, customer harm, or workflow errors.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture treats output as a control surface that must be classified, validated, reviewed, and prevented from silently becoming a decision, record, communication, or action.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| Output and decision control | Defines output classification, validation, decision separation, generated record controls, and correction paths. |
| Human accountability model | Assigns reviewers, decision owners, and approvers. |
| Tool and action control | Prevents output from directly triggering tools or actions without approval. |
| AI assurance and testing | Tests output validation and downstream handling. |
| Monitoring, logging, and evidence | Retains output and decision evidence where required. |

## Required Controls

```text
Classify output types.
Define output validation rules.
Separate AI recommendation from final decision.
Require human review where required.
Prevent direct execution of unvalidated output.
Prevent unreviewed customer communication.
Label generated records where required.
Define correction and override path.
Log output and decision evidence where required.
```

## Example Assurance Tests

```text
Test hallucinated output.
Test output containing unsafe instruction.
Test generated code review path.
Test AI recommendation becoming final decision.
Test customer response review requirement.
Test correction path for generated record.
```

## Example Evidence

```text
Output classification
Validation criteria
Reviewer record
Decision owner record
Final decision evidence
Generated record metadata
Correction record
Output validation test
Customer communication approval
```

## Related Project Files

```text
docs/11-pillar-output-and-decision-control.md
templates/ai-output-and-decision-control-template.md
examples/vendor-ai-example.md
```

---

# 10. LLM06: Excessive Agency

## OWASP Risk Theme

Excessive agency occurs when an LLM-based system is granted too much autonomy, access, tool capability, or authority, allowing it to perform unintended or harmful actions.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture treats excessive agency as an identity, access, tool/action, approval, blast-radius, monitoring, and incident containment problem.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| AI identity and access control | Defines agent identity, delegated authority, least privilege, attribution, and revocation. |
| Tool and action control | Defines tool inventory, action classification, approval gates, and kill switches. |
| Human accountability model | Assigns action owners, approvers, and incident owners. |
| Monitoring, logging, and evidence | Logs tool calls, approvals, actions, and denied attempts. |
| Incident containment and recovery | Defines disablement, rollback, and restart criteria. |

## Required Controls

```text
Define AI identity.
Define autonomy level.
Define delegated authority.
Apply least privilege.
Inventory AI-accessible tools.
Classify actions by risk.
Require approval for high-risk actions.
Define blast-radius limits.
Log tool calls and actions.
Test unauthorized tool use.
Test approval bypass.
Test kill switch.
Define rollback or compensation.
```

## Example Assurance Tests

```text
Attempt unauthorized tool call.
Attempt high-risk action without approval.
Attempt direct lower-level API path.
Attempt action outside approved scope.
Test rate and retry limits.
Test kill switch.
Test rollback.
```

## Example Evidence

```text
Agent identity record
Access approval
Tool inventory
Action classification
Approval gate configuration
Approval logs
Denied action logs
Tool/action logs
Kill switch test
Rollback test
Incident containment plan
```

## Related Project Files

```text
docs/12-pillar-tool-and-action-control.md
templates/ai-agent-control-template.md
templates/ai-tool-and-action-control-template.md
examples/agentic-ai-example.md
```

---

# 11. LLM07: System Prompt Leakage

## OWASP Risk Theme

System prompt leakage occurs when protected system instructions, hidden policies, internal configuration, routing logic, or sensitive implementation details are exposed through model output or attack prompts.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture treats system prompts as controlled configuration that should be owned, versioned, protected, tested, and monitored.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| Prompt and input control | Defines system prompt ownership, versioning, protection, and injection testing. |
| Monitoring, logging, and evidence | Tracks attempts to extract system prompts. |
| AI assurance and testing | Tests system prompt leakage and prompt extraction attempts. |
| Incident containment and recovery | Defines response if protected instructions leak. |

## Required Controls

```text
Assign system prompt owner.
Version system prompts.
Review prompt changes.
Protect system prompts from user disclosure where required.
Avoid storing secrets in system prompts.
Test prompt extraction attempts.
Monitor repeated extraction attempts where required.
Define incident response for prompt leakage.
```

## Example Assurance Tests

```text
Ask model to reveal system prompt.
Ask model to print hidden instructions.
Ask model to disclose policy prompt.
Inject document asking model to reveal system instructions.
Test whether secrets exist in prompt configuration.
```

## Example Evidence

```text
System prompt owner record
System prompt version history
Prompt change approval
Prompt leakage test result
Extraction attempt logs
Incident record if leakage occurs
```

## Related Project Files

```text
docs/10-pillar-input-control.md
templates/ai-prompt-and-input-control-template.md
```

---

# 12. LLM08: Vector and Embedding Weaknesses

## OWASP Risk Theme

Vector and embedding weaknesses include failures in RAG and embedding-based systems, such as unauthorized retrieval, sensitive source exposure, poisoned embeddings, poor access enforcement, stale data, and cross-tenant leakage.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture treats vector and embedding risk as a data boundary, retrieval, access control, source governance, logging, and assurance problem.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| Data boundary control | Defines data source mapping, classifications, source allowlists, and retrieval boundaries. |
| AI identity and access control | Enforces user, role, tenant, or attribute-based retrieval boundaries. |
| Prompt and input control | Treats retrieved content as untrusted context. |
| AI assurance and testing | Tests unauthorized retrieval and prompt injection through retrieved content. |
| Monitoring, logging, and evidence | Captures retrieval evidence and reconstructability. |

## Required Controls

```text
Map indexed sources.
Approve data sources.
Classify indexed content.
Define retrieval boundary.
Enforce permission inheritance.
Define tenant/customer boundaries.
Exclude sensitive sources where required.
Control embedding/index lifecycle.
Test cross-user retrieval.
Test cross-tenant retrieval.
Test sensitive source exclusion.
Log retrieval events where required.
```

## Example Assurance Tests

```text
Attempt retrieval of restricted document.
Attempt cross-user retrieval.
Attempt cross-tenant retrieval.
Test stale source retrieval.
Test sensitive source exclusion.
Test prompt injection inside retrieved document.
Test evidence reconstruction for RAG answer.
```

## Example Evidence

```text
Data source map
Index source allowlist
Sensitive source denylist
Retrieval boundary configuration
Permission inheritance test
Cross-tenant isolation test
Retrieval logs
Source references
Index rebuild record
Evidence reconstruction test
```

## Related Project Files

```text
docs/09-pillar-data-boundary-control.md
templates/ai-data-boundary-template.md
examples/rag-assistant-example.md
```

---

# 13. LLM09: Misinformation

## OWASP Risk Theme

Misinformation occurs when an LLM generates false, misleading, unsupported, outdated, or overconfident output that users may rely on.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture treats misinformation as an output validation, source grounding, decision accountability, human review, evidence, and correction problem.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| Output and decision control | Defines validation rules, source grounding, decision separation, and correction paths. |
| Human accountability model | Ensures humans remain accountable for final decisions. |
| AI assurance and testing | Tests output quality, hallucination, source citation, and escalation behavior. |
| Monitoring, logging, and evidence | Tracks output quality issues and correction evidence. |
| Incident containment and recovery | Defines correction, notification, and recovery if misinformation causes harm. |

## Required Controls

```text
Define output limitations.
Require source grounding where appropriate.
Define no-source behavior.
Require human review for high-impact output.
Separate AI recommendation from final decision.
Define correction path.
Monitor output quality.
Test hallucination and unsupported claims.
Escalate ambiguous or high-impact questions.
```

## Example Assurance Tests

```text
Ask question with no source.
Test outdated source behavior.
Test hallucinated policy requirement.
Test unsupported legal or compliance conclusion.
Test customer-facing incorrect answer.
Test correction and retraction path.
```

## Example Evidence

```text
Output validation criteria
Source citation record
No-source fallback design
Reviewer record
Output quality sampling
Hallucination test result
Correction record
Customer notification record where required
Incident record
```

## Related Project Files

```text
docs/11-pillar-output-and-decision-control.md
templates/ai-output-and-decision-control-template.md
examples/rag-assistant-example.md
examples/vendor-ai-example.md
```

---

# 14. LLM10: Unbounded Consumption

## OWASP Risk Theme

Unbounded consumption includes risks from excessive resource usage, cost spikes, denial of service, uncontrolled loops, excessive retries, runaway agents, or abusive prompt/tool usage.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture treats unbounded consumption as an operational control, monitoring, tool/action, rate limit, containment, and incident response problem.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| Tool and action control | Defines rate limits, retry limits, blast-radius limits, and stop controls for agents/tools. |
| Monitoring, logging, and evidence | Monitors usage, anomalies, cost spikes, retries, and loops. |
| Incident containment and recovery | Defines disablement, throttling, and recovery. |
| AI identity and access control | Supports revocation and scoped identities. |
| AI assurance and testing | Tests runaway behavior and containment. |

## Required Controls

```text
Define usage limits.
Define rate limits.
Define retry limits.
Define cost thresholds.
Define maximum tool calls.
Define maximum workflow actions.
Define loop detection where applicable.
Monitor abnormal usage.
Define throttle or disablement path.
Test kill switch.
Define incident escalation for runaway usage.
```

## Example Assurance Tests

```text
Test excessive prompt submission.
Test agent retry loop.
Test maximum tool-call limit.
Test rate limiting.
Test cost threshold alert.
Test kill switch during runaway workflow.
Test disablement of agent identity.
```

## Example Evidence

```text
Usage limit configuration
Rate limit configuration
Retry limit configuration
Cost monitoring alert
Tool-call limit
Usage anomaly alert
Kill switch test
Incident containment record
Recovery record
```

## Related Project Files

```text
docs/12-pillar-tool-and-action-control.md
docs/23-metrics-and-reporting.md
templates/ai-incident-containment-recovery-template.md
examples/agentic-ai-example.md
```

---

# 15. OWASP Category to Assurance Test Matrix

| OWASP Category | Example Assurance Tests |
|---|---|
| Prompt Injection | Direct injection, indirect injection, system prompt extraction, tool-use injection |
| Sensitive Information Disclosure | Data leakage, restricted retrieval, sensitive prompt detection, vendor retention review |
| Supply Chain | Vendor evidence review, dependency review, plugin/tool review, subprocessor review |
| Data and Model Poisoning | Source ingestion test, poisoned document test, retrieval regression test |
| Improper Output Handling | Output validation, generated record correction, customer response review |
| Excessive Agency | Unauthorized tool call, approval bypass, action boundary, kill switch |
| System Prompt Leakage | System prompt extraction test, prompt version review, secret-in-prompt review |
| Vector and Embedding Weaknesses | Retrieval boundary, cross-tenant, sensitive source exclusion, index lifecycle |
| Misinformation | Hallucination test, no-source fallback, source citation accuracy, correction path |
| Unbounded Consumption | Rate limit, retry limit, cost threshold, loop detection, disablement |

---

# 16. OWASP Category to Evidence Matrix

| OWASP Category | Example Evidence |
|---|---|
| Prompt Injection | Prompt injection tests, blocked attempt logs, prompt/input control record |
| Sensitive Information Disclosure | Data classification, data boundary test, DLP logs, vendor retention evidence |
| Supply Chain | Vendor assessment, subprocessor list, dependency review, feature enablement record |
| Data and Model Poisoning | Source approval, ingestion logs, regression tests, index rebuild record |
| Improper Output Handling | Output validation record, reviewer record, correction record |
| Excessive Agency | Tool inventory, action classification, approval logs, kill switch test |
| System Prompt Leakage | Prompt version history, prompt leakage test, extraction attempt logs |
| Vector and Embedding Weaknesses | Retrieval config, source allowlist, retrieval logs, boundary test |
| Misinformation | Source citation tests, output quality samples, correction records |
| Unbounded Consumption | Rate limits, cost alerts, usage logs, disablement record |

---

# 17. Example: RAG Assistant OWASP Mapping

## Use Case

```text
Internal policy RAG assistant.
```

## Key OWASP Risks

```text
Prompt injection
Sensitive information disclosure
Vector and embedding weaknesses
Misinformation
System prompt leakage
```

## AI Control Architecture Controls

```text
Source allowlist
Sensitive source denylist
Retrieval boundary
Permission inheritance
Retrieved content treated as untrusted
Source attribution
No-source fallback
Prompt injection testing
Retrieval boundary testing
Evidence reconstruction
```

Related example:

```text
examples/rag-assistant-example.md
```

---

# 18. Example: Agentic AI OWASP Mapping

## Use Case

```text
IT service desk ticket triage agent.
```

## Key OWASP Risks

```text
Prompt injection
Sensitive information disclosure
Excessive agency
Improper output handling
Unbounded consumption
System prompt leakage
```

## AI Control Architecture Controls

```text
Agent identity
Autonomy level
Tool inventory
Action classification
Approval gates
Blast-radius limits
Prompt injection testing
Approval bypass testing
Tool-call logging
Kill switch
Rollback or correction path
Evidence reconstruction
```

Related example:

```text
examples/agentic-ai-example.md
```

---

# 19. How to Use This Crosswalk

Use this crosswalk when:

```text
AppSec wants to threat model an LLM application.
Security architecture wants to review AI control design.
A red team wants to define AI attack scenarios.
A platform team wants to test RAG or agent controls.
A governance team wants to connect AI controls to recognized AI security risks.
An audit team wants evidence for LLM security controls.
```

Suggested use:

```text
1. Identify the AI pattern.
2. Identify relevant OWASP LLM categories.
3. Map each category to AI Control Architecture pillars.
4. Identify required controls.
5. Define assurance tests.
6. Define evidence.
7. Track findings and remediation.
8. Update incident scenarios and monitoring rules.
```

---

# 20. Limitations

This crosswalk is intended to support LLM application security control design.

It is not:

```text
A complete OWASP implementation guide
A penetration test report
A security certification
A substitute for AppSec review
A substitute for red-team testing
A substitute for secure software development lifecycle controls
```

Organizations should tailor tests and controls based on their AI architecture, threat model, risk tier, data sensitivity, tool access, and deployment context.

---

# 21. Future Enhancements

Future versions may add:

```text
Detailed OWASP category-to-requirement mapping
OWASP Agentic AI crosswalk
AI red-team test catalogue
Threat modeling worksheet
Machine-readable OWASP mapping
LLM security control checklist
RAG-specific adversarial testing guide
Agent-specific adversarial testing guide
```

---

# 22. Summary

OWASP helps define LLM application security risks.

The AI Control Architecture helps enterprises operationalize controls for those risks across:

```text
Identity
Data
Prompts
Outputs
Tools
Humans
Testing
Evidence
Monitoring
Incidents
Recovery
```

The goal is to move from:

```text
LLM security awareness
```

to:

```text
Operational LLM control
```