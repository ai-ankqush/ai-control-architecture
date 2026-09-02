# Common AI Control Patterns

This document describes common AI adoption patterns and how the AI Control Architecture should be applied to each pattern.

The purpose is to help teams understand that different AI patterns require different control emphasis.

A copilot, a RAG assistant, an embedded SaaS AI feature, a customer-facing chatbot, and an autonomous agent do not create the same control problem.

Each pattern must be assessed based on what AI can:

```text
See
Decide
Do
Remember
Trigger
Expose
```

---

# 1. How to Use This Document

Use this document when reviewing or designing AI use cases.

For each AI use case:

1. Identify the AI pattern.
2. Determine what AI can see.
3. Determine what AI can decide or influence.
4. Determine what AI can do or trigger.
5. Determine who owns the outcome.
6. Determine what evidence must exist.
7. Determine how failure can be contained.

Most AI use cases combine more than one pattern.

For example:

```text
A customer support AI may be:
- customer-facing AI
- RAG-based AI
- decision-supporting AI
- tool-using AI
- vendor AI
```

When patterns combine, apply the strongest relevant controls.

---

# 2. Pattern Overview

| Pattern | Primary Risk | Control Emphasis |
|---|---|---|
| Copilot | Overtrust, data exposure, weak output review | Data boundaries, input guidance, output review, user accountability |
| RAG / knowledge assistant | Unauthorized retrieval, source leakage, prompt injection in documents | Retrieval boundaries, data classification, source attribution, retrieval testing |
| Internal LLM application | Data exposure, weak ownership, unclear evidence | Inventory, ownership, data boundary, logging, assurance |
| AI-enabled SaaS | Vendor processing, feature enablement, limited logs | Vendor assessment, admin controls, data retention, evidence access |
| Embedded vendor AI | Hidden AI behavior, unclear shared responsibility | Inventory, vendor review, contract terms, monitoring |
| Customer-facing AI | Harmful output, incorrect commitments, privacy exposure | Output control, escalation, human review, customer remediation |
| Decision-supporting AI | AI recommendation becoming decision | Decision owner, validation, human review, decision evidence |
| Tool-using AI | Unauthorized tool use, unsafe actions | Tool inventory, action classification, approval gates, logging |
| Agentic AI | Autonomy, action chaining, containment failure | Identity, action boundaries, kill switches, rollback, monitoring |
| Developer AI | Source code leakage, insecure code, license risk | Data boundary, code review, secure SDLC, output validation |
| Security operations AI | Unsafe enforcement, missed detection, excessive authority | Human accountability, action control, logging, rollback |
| High-impact or regulated AI | Legal, compliance, rights, financial, security, or safety impact | Full control architecture, enhanced assurance, evidence, incident readiness |

---

# 3. Pattern 1: Enterprise Copilot

## Description

An enterprise copilot assists users with drafting, summarizing, searching, analyzing, or generating content.

Copilots are often deployed broadly across the enterprise and may inherit user permissions across email, documents, chats, meetings, tickets, or collaboration platforms.

## What AI Can See

Depending on configuration, a copilot may see:

- user prompts
- documents
- emails
- chats
- meetings
- calendar data
- tickets
- enterprise search results
- user-accessible files
- customer or employee records
- metadata
- conversation history

## What AI Can Decide

Usually, copilots should not make formal decisions.

However, they may influence:

- user judgment
- document summaries
- customer response drafts
- internal analysis
- prioritization
- recommendations
- management reporting

## What AI Can Do

Most copilots primarily generate output.

Some copilots may also:

- create drafts
- summarize records
- update tasks
- create documents
- trigger workflows
- call plugins or extensions

## Key Risks

- users enter sensitive data into prompts
- copilot retrieves excessive information
- permission inheritance exposes data unexpectedly
- users overtrust summaries
- AI-generated drafts become records without review
- vendor retention or training settings are unclear
- usage visibility is weak

## Required Controls

| Control Area | Required Control |
|---|---|
| Inventory | Register copilot deployment and enabled features. |
| Ownership | Assign business and technical owners. |
| Data boundary | Review permission inheritance and sensitive data exposure. |
| Prompt/input | Define prohibited inputs and user guidance. |
| Output/decision | Clarify that output is draft or advisory unless approved. |
| Accountability | Users remain accountable for use of output. |
| Monitoring/evidence | Define usage and evidence requirements by risk tier. |
| Vendor | Review data processing, retention, training/reuse, and logs. |
| Incident response | Define reporting and containment path. |

## Minimum Controls

At minimum:

```text
[ ] Copilot is inventoried.
[ ] Business owner is assigned.
[ ] User population is defined.
[ ] Permission model is understood.
[ ] Sensitive data guidance exists.
[ ] Output use restrictions are defined.
[ ] Vendor data processing is reviewed.
[ ] Incident reporting path exists.
```

## Stronger Controls

For higher-risk copilots:

```text
[ ] Usage logs are reviewed.
[ ] Sensitive data input monitoring exists.
[ ] High-risk output review is required.
[ ] Vendor retention and training settings are controlled.
[ ] Permission inheritance is tested.
[ ] Evidence package exists.
```

---

# 4. Pattern 2: RAG / Knowledge Assistant

## Description

A RAG or knowledge assistant retrieves enterprise content and uses it as context to answer user questions or generate outputs.

This pattern is common in enterprise search, knowledge management, policy assistants, support assistants, legal assistants, engineering assistants, and internal helpdesk assistants.

## What AI Can See

A RAG assistant may see:

- user prompts
- retrieved documents
- document metadata
- source excerpts
- embeddings
- vector index results
- knowledge base articles
- policies
- tickets
- case notes
- customer records
- source references

## What AI Can Decide

RAG systems may influence:

- interpretation of source material
- user understanding
- business decisions
- customer responses
- compliance judgments
- operational recommendations

## What AI Can Do

RAG systems usually generate grounded answers, but may also:

- summarize documents
- extract data
- recommend actions
- create records
- trigger workflows if connected to tools

## Key Risks

- unauthorized retrieval
- cross-user or cross-tenant data leakage
- sensitive document exposure
- stale or incorrect source material
- prompt injection inside retrieved documents
- missing source attribution
- output sensitivity not inherited from source material
- retrieval logs unavailable

## Required Controls

| Control Area | Required Control |
|---|---|
| Inventory | Register RAG use case and knowledge sources. |
| Data boundary | Map data sources, owners, classifications, and retrieval boundaries. |
| Identity/access | Enforce user, role, tenant, or attribute-based access. |
| Prompt/input | Treat retrieved documents as untrusted where appropriate. |
| Output/decision | Preserve source attribution and output sensitivity. |
| Assurance | Test retrieval boundaries and data leakage. |
| Monitoring/evidence | Capture retrieval evidence and source references. |
| Incident response | Define containment for retrieval leakage. |

## Minimum Controls

At minimum:

```text
[ ] Data sources are mapped.
[ ] Data owners are identified.
[ ] Data classification is recorded.
[ ] Retrieval boundaries are defined.
[ ] Permission inheritance is tested.
[ ] Source attribution is available where required.
[ ] Retrieval logs or references are retained where required.
```

## Stronger Controls

For higher-risk RAG:

```text
[ ] Cross-user retrieval testing is performed.
[ ] Cross-tenant retrieval testing is performed.
[ ] Sensitive source exclusion is tested.
[ ] Prompt injection in retrieved documents is tested.
[ ] Output sensitivity inherits from source context.
[ ] Evidence reconstruction is tested.
```

---

# 5. Pattern 3: Internal LLM Application

## Description

An internal LLM application is built by the enterprise to support a specific business process, team, workflow, or function.

It may use internal data, hosted models, open-source models, APIs, retrieval, tools, or workflow integrations.

## What AI Can See

Internal LLM applications may see:

- prompts
- uploaded files
- internal records
- business process data
- retrieved documents
- API responses
- workflow state
- user metadata
- logs
- tool outputs

## What AI Can Decide

They may influence:

- case handling
- triage
- recommendations
- internal operations
- summaries
- reports
- risk assessments
- compliance reviews

## What AI Can Do

Depending on design, they may:

- generate summaries
- classify records
- extract data
- prepare drafts
- create tickets
- update records
- call APIs
- trigger workflows

## Key Risks

- unclear business ownership
- unclear data boundaries
- excessive application permissions
- insufficient prompt/input controls
- weak output validation
- missing logging
- no assurance testing
- no containment path

## Required Controls

| Control Area | Required Control |
|---|---|
| Inventory | Register application and lifecycle status. |
| Ownership | Assign business and technical owners. |
| Risk tiering | Classify based on data, decision, output, action, and autonomy. |
| Data boundary | Map data sources and classifications. |
| Identity/access | Define application identity and delegated authority. |
| Prompt/input | Define input controls and prompt change process. |
| Output/decision | Define validation and downstream use controls. |
| Tool/action | Classify and approve any tool or workflow action. |
| Assurance | Test controls before deployment. |
| Evidence | Define logs and evidence retention. |
| Incident response | Define containment and recovery. |

## Minimum Controls

At minimum:

```text
[ ] Use case is inventoried.
[ ] Business and technical owners are assigned.
[ ] Risk tier is assigned.
[ ] Data sources are mapped.
[ ] Identity model is defined.
[ ] Output use is documented.
[ ] Logging requirements are defined.
[ ] Assurance review is completed before production.
```

---

# 6. Pattern 4: AI-Enabled SaaS

## Description

AI-enabled SaaS refers to AI features inside third-party software platforms.

These features may be embedded into CRM, HR, finance, productivity, security, collaboration, customer support, legal, development, or analytics tools.

## What AI Can See

Depending on vendor and configuration, SaaS AI may see:

- tenant data
- user data
- customer data
- employee data
- tickets
- records
- documents
- prompts
- outputs
- workflow data
- metadata
- logs

## What AI Can Decide

SaaS AI may influence:

- recommendations
- rankings
- lead scoring
- HR summaries
- customer responses
- security triage
- financial insights
- workflow routing

## What AI Can Do

SaaS AI may:

- summarize
- classify
- draft
- recommend
- score
- create records
- modify records
- send communications
- trigger workflows

## Key Risks

- AI feature enabled by default
- unclear vendor data processing
- unclear data retention
- vendor training or product improvement use
- limited admin controls
- limited logs
- unclear permission model
- weak incident support
- vendor changes behavior without clear enterprise review

## Required Controls

| Control Area | Required Control |
|---|---|
| Inventory | Identify and register SaaS AI feature. |
| Vendor | Review data processing, retention, training/reuse, and subprocessors. |
| Ownership | Assign business, technical, and vendor owners. |
| Data boundary | Identify data exposed to vendor AI. |
| Identity/access | Understand whether AI respects enterprise permissions. |
| Output/decision | Assess output and decision impact. |
| Tool/action | Review workflow or record modification capability. |
| Monitoring/evidence | Confirm log availability and export options. |
| Incident response | Define vendor escalation and feature disablement. |

## Minimum Controls

At minimum:

```text
[ ] Vendor AI feature is identified.
[ ] Enablement status is known.
[ ] Vendor owner is assigned.
[ ] Data processing is reviewed.
[ ] Retention and training/reuse are reviewed.
[ ] Admin controls are reviewed.
[ ] Logs and evidence availability are understood.
[ ] Feature disablement path is known.
```

---

# 7. Pattern 5: Embedded Vendor AI

## Description

Embedded vendor AI is AI functionality built into a third-party product, often as a feature rather than a separately procured AI system.

It may be easy to miss because it appears as a product enhancement.

## What AI Can See

Embedded vendor AI may see:

- data already inside the vendor platform
- user inputs
- records
- documents
- messages
- metadata
- workflow history
- customer or employee data

## What AI Can Decide

It may influence:

- prioritization
- recommendations
- summaries
- alerts
- classifications
- automated decisions
- workflow suggestions

## What AI Can Do

It may:

- generate content
- enrich records
- classify data
- suggest next actions
- trigger built-in workflows
- automate internal platform actions

## Key Risks

- AI not identified as AI
- feature enabled without governance
- vendor terms unclear
- user cannot distinguish AI-generated output
- logs unavailable
- control ownership unclear
- vendor changes feature behavior
- data used for training or improvement

## Required Controls

| Control Area | Required Control |
|---|---|
| Inventory | Track embedded vendor AI explicitly. |
| Vendor | Review AI terms, processing, retention, and feature controls. |
| Ownership | Assign internal owner for enterprise use of vendor AI. |
| Data boundary | Identify platform data exposed to AI feature. |
| Output/decision | Assess whether outputs influence decisions or records. |
| Monitoring/evidence | Determine available evidence and gaps. |
| Incident response | Define vendor escalation and disablement options. |

## Minimum Controls

At minimum:

```text
[ ] Embedded AI feature is identified.
[ ] Business and vendor owners are assigned.
[ ] Vendor terms are reviewed.
[ ] Data exposed to the feature is understood.
[ ] Feature enablement can be controlled where possible.
[ ] Evidence availability is understood.
[ ] Incident escalation path is defined.
```

---

# 8. Pattern 6: Customer-Facing AI

## Description

Customer-facing AI interacts directly with customers, suppliers, partners, or the public.

It may provide answers, support, recommendations, summaries, troubleshooting, sales guidance, onboarding support, or automated service.

## What AI Can See

Customer-facing AI may see:

- customer prompts
- account data
- service history
- tickets
- orders
- product data
- policies
- public content
- conversation history
- uploaded files
- customer personal data

## What AI Can Decide

It may influence:

- customer expectations
- customer actions
- issue resolution
- complaint handling
- eligibility guidance
- routing
- escalation
- recommendations

## What AI Can Do

It may:

- answer questions
- draft customer responses
- send customer communications
- create tickets
- update cases
- escalate issues
- recommend products or services
- trigger workflows

## Key Risks

- incorrect customer guidance
- unauthorized customer commitment
- privacy leakage
- harmful or inappropriate output
- inconsistent escalation
- failure to identify high-risk customer situations
- inability to correct or retract output
- reputational impact

## Required Controls

| Control Area | Required Control |
|---|---|
| Inventory | Register customer-facing AI. |
| Ownership | Assign business owner and customer impact owner. |
| Data boundary | Control customer data access and privacy exposure. |
| Prompt/input | Handle external and untrusted inputs. |
| Output/decision | Define output boundaries, prohibited commitments, and review rules. |
| Accountability | Assign owner for customer impact and escalation. |
| Monitoring/evidence | Retain conversation and output evidence where required. |
| Assurance | Test output quality, escalation, privacy, and safety. |
| Incident response | Define correction, customer notification, and containment. |

## Minimum Controls

At minimum:

```text
[ ] Customer-facing use is approved.
[ ] Customer data exposure is assessed.
[ ] Output boundaries are defined.
[ ] Prohibited outputs are defined.
[ ] Escalation path is defined.
[ ] Correction or retraction path exists.
[ ] Conversation evidence is retained where required.
[ ] Incident response path exists.
```

---

# 9. Pattern 7: Decision-Supporting AI

## Description

Decision-supporting AI provides analysis, recommendations, scores, classifications, rankings, summaries, or insights that influence human or business decisions.

The AI may not make the final decision, but it can materially shape it.

## What AI Can See

Decision-supporting AI may see:

- business records
- customer data
- employee data
- financial data
- case history
- operational data
- compliance data
- security data
- source documents
- scoring inputs

## What AI Can Decide

It may influence:

- prioritization
- approval decisions
- customer treatment
- employee decisions
- risk decisions
- financial decisions
- security decisions
- compliance judgments
- operational actions

## What AI Can Do

It may:

- generate recommendations
- assign scores
- classify cases
- rank options
- create decision summaries
- produce evidence packs
- recommend escalation

## Key Risks

- AI recommendation becomes final decision
- human review becomes ceremonial
- reviewer lacks context or authority
- decision evidence is missing
- bias or unfairness where relevant
- generated record becomes authoritative without review
- correction path is unclear

## Required Controls

| Control Area | Required Control |
|---|---|
| Inventory | Register decision-supporting use. |
| Risk tiering | Classify based on decision impact. |
| Output/decision | Separate AI recommendation from final decision. |
| Accountability | Assign decision owner. |
| Human review | Ensure meaningful review, not ceremonial approval. |
| Evidence | Capture recommendation, review, approval, and final decision. |
| Assurance | Test output validation and decision process. |
| Incident response | Define correction and remediation path. |

## Minimum Controls

At minimum:

```text
[ ] Decision impact is documented.
[ ] Decision owner is assigned.
[ ] AI recommendation is labeled.
[ ] Final decision is recorded separately.
[ ] Human reviewer can reject or override AI output.
[ ] Decision evidence is retained.
[ ] Correction path is defined.
```

---

# 10. Pattern 8: Tool-Using AI

## Description

Tool-using AI can call tools, APIs, functions, plugins, workflows, or integrations.

This pattern moves AI from generating content to interacting with systems.

## What AI Can See

Tool-using AI may see:

- user prompts
- tool descriptions
- API responses
- records
- workflow data
- system state
- retrieved context
- tool outputs
- error messages

## What AI Can Decide

It may decide or influence:

- which tool to call
- what parameters to send
- whether a workflow should start
- whether a record should be created
- whether an issue should be escalated
- what action to recommend or request

## What AI Can Do

It may:

- search
- retrieve
- create tickets
- update records
- call APIs
- send messages
- trigger workflows
- execute scripts
- perform bounded actions

## Key Risks

- unauthorized tool call
- tool used for unauthorized purpose
- incorrect parameters
- approval bypass
- excessive tool permissions
- unsafe action chaining
- incomplete tool logs
- no rollback or kill switch

## Required Controls

| Control Area | Required Control |
|---|---|
| Inventory | Inventory tools accessible to AI. |
| Identity/access | Define identity used for tool access. |
| Tool/action | Classify actions and define boundaries. |
| Approval | Require approval for high-risk actions. |
| Monitoring/evidence | Log tool calls, parameters, results, and approvals. |
| Assurance | Test unauthorized tool use and approval bypass. |
| Incident response | Define tool disablement, rollback, and evidence preservation. |

## Minimum Controls

At minimum:

```text
[ ] Tool inventory exists.
[ ] Tool owner is assigned.
[ ] Tool access is approved.
[ ] Actions are classified by risk.
[ ] High-risk actions require approval.
[ ] Tool calls are logged.
[ ] Tool access can be disabled.
[ ] Rollback or compensation is assessed.
```

---

# 11. Pattern 9: Agentic AI

## Description

Agentic AI can pursue goals, plan steps, use tools, retrieve context, call APIs, trigger workflows, and perform actions with some level of autonomy.

Agentic AI requires stronger controls because it can combine reasoning, planning, tool use, memory, and action.

## What AI Can See

An AI agent may see:

- goals
- user prompts
- system prompts
- planning context
- retrieved documents
- workflow state
- tool outputs
- API responses
- memory
- logs
- prior actions
- system state

## What AI Can Decide

An agent may decide:

- what steps to take
- what tools to use
- what data to retrieve
- what action to request
- whether to retry
- when to escalate
- how to complete a goal

## What AI Can Do

An agent may:

- call tools
- trigger workflows
- update records
- send communications
- perform multi-step tasks
- interact with multiple systems
- execute bounded actions
- request approvals
- continue until a goal is complete

## Key Risks

- unsafe autonomy
- action chaining
- tool misuse
- excessive delegated authority
- prompt injection causing actions
- approval bypass
- agent loops or excessive retries
- weak kill switch
- weak rollback
- unclear accountability
- incomplete evidence

## Required Controls

| Control Area | Required Control |
|---|---|
| Inventory | Register agent and purpose. |
| Ownership | Assign agent owner, business owner, technical owner, and incident contact. |
| Identity/access | Define agent identity and delegated authority. |
| Data boundary | Approve data sources accessible to agent. |
| Prompt/input | Test prompt injection to action path. |
| Tool/action | Inventory tools, classify actions, define approval gates and boundaries. |
| Accountability | Define human review, override, and escalation. |
| Monitoring/evidence | Log goals, plans or summaries, tool calls, actions, approvals, and outcomes. |
| Assurance | Test boundaries, approval gates, kill switch, rollback, and incident scenarios. |
| Incident response | Define kill switch, containment, recovery, and restart criteria. |

## Minimum Controls

At minimum:

```text
[ ] Agent purpose is defined.
[ ] Agent owner is assigned.
[ ] Autonomy level is defined.
[ ] Agent identity is defined.
[ ] Tool inventory exists.
[ ] Actions are classified.
[ ] High-risk actions require approval.
[ ] Boundaries and blast-radius limits are defined.
[ ] Tool/action logs are retained.
[ ] Kill switch is defined and tested.
[ ] Rollback or compensation is defined.
[ ] Incident scenarios are documented.
```

---

# 12. Pattern 10: Developer AI

## Description

Developer AI assists with code generation, debugging, code review, testing, documentation, infrastructure scripts, queries, and engineering workflows.

It may operate inside IDEs, repositories, CI/CD pipelines, ticketing systems, or code hosting platforms.

## What AI Can See

Developer AI may see:

- source code
- repository metadata
- tickets
- pull requests
- build logs
- secrets accidentally present in code
- infrastructure configuration
- documentation
- dependency files
- security findings

## What AI Can Decide

It may influence:

- code design
- dependency selection
- security fixes
- testing strategy
- infrastructure changes
- pull request review
- vulnerability triage

## What AI Can Do

It may:

- generate code
- suggest patches
- create pull requests
- write tests
- summarize vulnerabilities
- modify configuration
- trigger CI/CD workflows
- call developer tools

## Key Risks

- source code leakage
- secrets in prompts or logs
- insecure generated code
- vulnerable dependency suggestions
- license or IP concerns
- unreviewed code merged into production
- AI-generated infrastructure change
- weak audit trail

## Required Controls

| Control Area | Required Control |
|---|---|
| Inventory | Register developer AI tools and integrations. |
| Data boundary | Control source code, secrets, and confidential repositories. |
| Identity/access | Review repo, CI/CD, and developer tool permissions. |
| Prompt/input | Prohibit secrets and restricted code where required. |
| Output/decision | Require code review and secure SDLC controls. |
| Tool/action | Control PR creation, merge, CI/CD, and deployment actions. |
| Monitoring/evidence | Retain evidence for AI-generated code where required. |
| Assurance | Test generated code, security, and workflow controls. |

## Minimum Controls

At minimum:

```text
[ ] Developer AI tool is inventoried.
[ ] Repositories accessible to AI are understood.
[ ] Secret input restrictions are defined.
[ ] Generated code requires review.
[ ] AI cannot merge or deploy without approval.
[ ] Logs and evidence are defined where required.
[ ] Vendor processing and retention are reviewed.
```

---

# 13. Pattern 11: Security Operations AI

## Description

Security operations AI supports alert triage, investigation, detection engineering, incident response, threat analysis, vulnerability prioritization, or automated security actions.

This pattern is high-risk when AI can change security controls or take enforcement actions.

## What AI Can See

Security AI may see:

- alerts
- logs
- identities
- endpoints
- network data
- vulnerabilities
- threat intelligence
- incident records
- user behavior
- cloud resources
- privileged systems
- sensitive security telemetry

## What AI Can Decide

It may influence:

- alert priority
- incident severity
- containment recommendation
- vulnerability priority
- user risk score
- access risk
- enforcement actions
- escalation

## What AI Can Do

It may:

- summarize incidents
- classify alerts
- recommend containment
- open tickets
- block indicators
- disable accounts
- quarantine endpoints
- update rules
- trigger playbooks

## Key Risks

- false negative suppresses real incident
- false positive causes unnecessary disruption
- AI disables user or system incorrectly
- AI changes detection or enforcement controls
- excessive security tool authority
- incomplete evidence
- accountability gaps during incident response

## Required Controls

| Control Area | Required Control |
|---|---|
| Inventory | Register security AI capability. |
| Risk tiering | Treat enforcement or privileged actions as high risk. |
| Identity/access | Control privileged security tool access. |
| Output/decision | Separate recommendation from enforcement decision. |
| Tool/action | Require approval for high-impact security actions. |
| Accountability | Assign security decision owner. |
| Monitoring/evidence | Retain alert, recommendation, approval, and action evidence. |
| Assurance | Test false positive, false negative, approval, and rollback scenarios. |
| Incident response | Define containment and rollback for AI-triggered security action. |

## Minimum Controls

At minimum:

```text
[ ] Security AI is inventoried.
[ ] Security owner is assigned.
[ ] Privileged access is reviewed.
[ ] Enforcement actions are approval-gated.
[ ] AI recommendations are logged.
[ ] Security actions are logged.
[ ] Rollback path exists.
[ ] Incident evidence is retained.
```

---

# 14. Pattern 12: High-Impact or Regulated AI

## Description

High-impact or regulated AI affects important decisions, rights, access, money, employment, legal obligations, compliance, security, production systems, safety, or regulated processes.

This pattern requires the strongest controls.

## What AI Can See

High-impact AI may see:

- regulated data
- personal data
- customer data
- employee data
- financial data
- legal data
- health or safety data
- production data
- security-sensitive data
- privileged records

## What AI Can Decide

It may influence:

- eligibility
- access
- pricing
- employment
- financial outcomes
- legal positions
- compliance decisions
- safety decisions
- security enforcement
- production operations

## What AI Can Do

Depending on design, it may:

- score
- recommend
- classify
- approve
- deny
- escalate
- create records
- trigger actions
- perform workflows

## Key Risks

- unlawful or unfair decision support
- regulated data exposure
- inaccurate output causing material harm
- weak human review
- missing decision evidence
- vendor evidence gaps
- inability to explain or reconstruct decisions
- inadequate incident response
- irreversible impact

## Required Controls

| Control Area | Required Control |
|---|---|
| Inventory | Register and classify as high impact. |
| Risk tiering | Assign Tier 5 where applicable. |
| Ownership | Assign business, technical, data, decision, risk, and incident owners. |
| Data boundary | Strong data classification, access, retention, and reuse controls. |
| Identity/access | Least privilege and privileged access controls. |
| Output/decision | Strong validation, human review, decision evidence, and correction path. |
| Tool/action | Strict approval gates and action boundaries. |
| Accountability | Explicit decision ownership and risk acceptance. |
| Assurance | Enhanced or independent assurance. |
| Monitoring/evidence | Full reconstructable evidence. |
| Incident response | Tested containment, recovery, communication, and restart criteria. |
| Vendor | Strong vendor evidence and contractual controls where applicable. |

## Minimum Controls

At minimum:

```text
[ ] Tier 5 risk classification is reviewed.
[ ] Owners are assigned across business, technical, data, decision, risk, and incident roles.
[ ] Data boundary is approved.
[ ] Identity and access are reviewed.
[ ] Output validation is required.
[ ] Human review is meaningful and evidenced.
[ ] Decision evidence is retained.
[ ] Tool/action capability is strictly controlled.
[ ] Assurance testing is completed.
[ ] Evidence reconstruction is tested.
[ ] Incident containment is tested.
[ ] Residual risk is accepted by accountable owner.
```

---

# 15. Pattern Combination Rules

Many real-world AI use cases combine patterns.

Use these rules when patterns overlap.

## Rule 1: Apply the Highest-Risk Pattern

If an AI use case combines low-risk and high-risk patterns, apply the controls for the high-risk pattern.

Example:

```text
A copilot that can trigger workflows should also be treated as tool-using AI.
```

## Rule 2: Tool Use Raises Control Requirements

If AI can call tools, APIs, workflows, or actions, apply tool and action controls.

```text
No tool access should exist without inventory, approval, logging, and revocation.
```

## Rule 3: Decision Impact Raises Control Requirements

If AI output influences decisions, apply output and decision controls.

```text
No AI recommendation should silently become the final decision.
```

## Rule 4: Sensitive Data Raises Data Boundary Requirements

If AI can access sensitive, regulated, privileged, customer, employee, security, financial, or production data, apply data boundary controls.

```text
No AI data access should exist without classification, owner approval, and evidence.
```

## Rule 5: Vendor AI Requires Vendor Evidence

If AI behavior depends on a vendor, apply vendor assessment controls.

```text
No vendor AI should be trusted without understanding processing, retention, reuse, logging, and incident support.
```

## Rule 6: Agentic AI Requires Containment

If AI can pursue goals, plan, use tools, or act autonomously, apply agent controls and containment controls.

```text
No agent should operate without identity, boundaries, logs, kill switch, and recovery path.
```

## Rule 7: External Exposure Requires Strong Output Controls

If AI output reaches customers, suppliers, partners, regulators, or the public, apply customer-facing or external output controls.

```text
No external AI output should be uncontrolled, unreviewable, or uncorrectable.
```

---

# 16. Pattern-to-Pillar Mapping

| Pattern | Highest Priority Pillars |
|---|---|
| Copilot | Inventory, Data Boundary, Prompt/Input, Output/Decision, Accountability, Vendor |
| RAG | Data Boundary, Identity/Access, Prompt/Input, Output/Decision, Assurance, Evidence |
| Internal LLM App | Inventory, Identity/Access, Data Boundary, Output/Decision, Assurance, Evidence |
| AI-enabled SaaS | Inventory, Vendor, Data Boundary, Identity/Access, Evidence, Incident |
| Embedded Vendor AI | Inventory, Vendor, Data Boundary, Output/Decision, Evidence |
| Customer-Facing AI | Output/Decision, Prompt/Input, Accountability, Evidence, Incident |
| Decision-Supporting AI | Output/Decision, Accountability, Assurance, Evidence |
| Tool-Using AI | Identity/Access, Tool/Action, Accountability, Evidence, Incident |
| Agentic AI | Identity/Access, Tool/Action, Accountability, Assurance, Evidence, Incident |
| Developer AI | Data Boundary, Prompt/Input, Output/Decision, Tool/Action, Assurance |
| Security Operations AI | Identity/Access, Output/Decision, Tool/Action, Accountability, Evidence, Incident |
| High-Impact AI | All pillars |

---

# 17. Pattern-to-Template Mapping

| Pattern | Recommended Templates |
|---|---|
| Copilot | `ai-use-case-intake-template.md`, `ai-risk-assessment-template.md`, `ai-vendor-assessment-template.md` |
| RAG | `ai-data-boundary-template.md`, `ai-prompt-and-input-control-template.md`, `ai-assurance-test-plan-template.md` |
| Internal LLM App | `ai-risk-assessment-template.md`, `ai-control-assessment-template.md`, `ai-architecture-decision-record-template.md` |
| AI-enabled SaaS | `ai-vendor-assessment-template.md`, `ai-risk-assessment-template.md`, `ai-control-assessment-template.md` |
| Customer-Facing AI | `ai-output-and-decision-control-template.md`, `ai-human-accountability-template.md`, `ai-incident-record-template.md` |
| Decision-Supporting AI | `ai-output-and-decision-control-template.md`, `ai-human-accountability-template.md`, `ai-control-evidence-package-template.md` |
| Tool-Using AI | `ai-tool-and-action-control-template.md`, `ai-identity-and-access-control-template.md`, `ai-incident-containment-recovery-template.md` |
| Agentic AI | `ai-agent-control-template.md`, `ai-tool-and-action-control-template.md`, `ai-incident-containment-recovery-template.md` |
| High-Impact AI | Full template set |

---

# 18. Summary

AI control should be pattern-aware.

Different AI patterns create different control problems:

```text
Copilots need data and output discipline.
RAG needs retrieval boundaries.
SaaS AI needs vendor control.
Customer-facing AI needs output and escalation control.
Decision-supporting AI needs human accountability.
Tool-using AI needs action control.
Agentic AI needs containment.
High-impact AI needs the full architecture.
```

The enterprise should not ask only:

```text
Which AI product are we using?
```

It should ask:

```text
What pattern is this?
What can it see?
What can it decide?
What can it do?
What evidence exists?
How do we stop it if it fails?
```