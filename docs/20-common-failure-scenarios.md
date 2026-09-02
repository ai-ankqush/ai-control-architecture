# Common AI Failure Scenarios

This document describes common AI control failure scenarios.

The purpose is to make AI risk concrete.

AI failures do not usually happen because a model becomes malicious.

They happen because enterprises give probabilistic systems access, authority, data, tools, workflows, decisions, or customer interaction without a control architecture.

The next major AI security, privacy, operational, or governance failure is likely to come from one of these patterns:

```text
AI could see something it should not see.
AI could decide something it should not decide.
AI could do something it should not do.
AI could remember something it should not remember.
AI could trigger something it should not trigger.
AI could expose something it should not expose.
AI could fail in a way the enterprise cannot reconstruct or contain.
```

---

# 1. How to Use This Document

Use this document to:

- educate stakeholders
- test AI control designs
- define risk scenarios
- build assurance test cases
- create incident tabletop exercises
- improve templates and requirements
- prioritize control investments

Each scenario includes:

```text
What happens
Why it happens
Affected patterns
Affected pillars
Control failures
Potential impact
Required controls
Evidence needed
Assurance tests
Containment actions
```

These scenarios should be adapted to the organization’s actual AI use cases.

---

# 2. Scenario Overview

| Scenario | Primary Control Failure | Highest Priority Pillars |
|---|---|---|
| Unknown AI use | AI not inventoried or owned | Inventory, Accountability |
| Embedded vendor AI enabled silently | Vendor AI not reviewed | Inventory, Vendor, Data Boundary |
| Excessive AI data access | AI can see too much | Identity, Data Boundary |
| Unauthorized RAG retrieval | Retrieval boundary fails | Data Boundary, Identity, Evidence |
| Prompt injection through retrieved content | Untrusted content controls AI behavior | Prompt/Input, Tool/Action |
| Sensitive data entered into prompts | Input control missing | Prompt/Input, Data Boundary |
| AI recommendation becomes final decision | Decision control missing | Output/Decision, Accountability |
| Ceremonial human review | Accountability model weak | Accountability, Output/Decision |
| AI-generated record becomes authoritative | Provenance and correction missing | Output/Decision, Evidence |
| Unauthorized tool use | Tool boundary missing | Tool/Action, Identity |
| Approval bypass | Approval gate ineffective | Tool/Action, Accountability |
| Agent cannot be stopped | Kill switch missing | Tool/Action, Incident |
| Vendor logs unavailable during incident | Evidence gap | Vendor, Evidence, Incident |
| AI incident cannot be reconstructed | Logging insufficient | Evidence, Incident |
| Exception becomes permanent | Exception governance weak | Accountability, Evidence |
| AI output reaches customer incorrectly | External output controls weak | Output/Decision, Incident |
| AI changes production or security state | Action control weak | Tool/Action, Identity, Incident |
| Model or prompt change breaks control | Regression testing missing | Assurance, Prompt/Input |
| Data retained or reused unexpectedly | Vendor/data controls weak | Data Boundary, Vendor |
| AI failure has no recovery path | Recovery not designed | Incident, Tool/Action |

---

# 3. Failure Scenario 1: Unknown AI Use

## What Happens

A team adopts an AI tool, SaaS AI feature, internal model, automation, or agent without registering it in the AI inventory.

The AI capability becomes operational before the enterprise knows it exists.

## Why It Happens

- AI is easy to adopt at team level.
- SaaS products add AI features without formal procurement.
- AI pilots start as experiments and become operational.
- Teams assume AI use is covered by existing technology review.
- No intake process exists.
- No one owns AI discovery.

## Affected AI Patterns

- Copilots
- AI-enabled SaaS
- Embedded vendor AI
- Internal LLM applications
- Agents
- Developer AI tools
- Shadow AI

## Affected Pillars

- AI inventory and classification
- Human accountability model
- Monitoring, logging, and evidence
- Incident containment and recovery

## Control Failures

- No inventory record
- No business owner
- No risk tier
- No data boundary
- No vendor review
- No logging expectations
- No incident path

## Potential Impact

- Sensitive data exposure
- Uncontrolled vendor processing
- Unreviewed decision support
- Unauthorized tool use
- Missing evidence
- Audit failure
- Incident response delay

## Required Controls

- AI inventory
- AI use case intake
- embedded vendor AI discovery
- shadow AI discovery
- business owner assignment
- risk tiering
- lifecycle tracking

## Evidence Needed

- inventory record
- intake record
- owner record
- risk tier record
- approval status
- lifecycle status
- vendor review where applicable

## Assurance Tests

- sample procurement and SaaS portfolio for AI features
- review expense data for AI tools
- review browser/plugin usage where appropriate
- review developer tools for AI assistants
- compare known AI use with inventory

## Containment Actions

- suspend unreviewed AI use
- restrict access
- disable vendor AI feature
- require intake submission
- assign owner
- complete risk assessment

---

# 4. Failure Scenario 2: Embedded Vendor AI Enabled Silently

## What Happens

A vendor adds an AI feature to an existing SaaS platform.

The feature is enabled by default or enabled by an administrator without AI-specific review.

Enterprise data becomes available to vendor AI processing before governance, security, privacy, legal, or risk teams understand the impact.

## Why It Happens

- Vendor AI is marketed as a product enhancement.
- Procurement already approved the SaaS product before AI was added.
- Admins enable features without AI review.
- AI feature flags are not monitored.
- Vendor documentation is unclear.
- Existing vendor risk review does not cover AI behavior.

## Affected AI Patterns

- AI-enabled SaaS
- Embedded vendor AI
- Copilot
- Customer-facing AI
- Workflow automation

## Affected Pillars

- AI inventory and classification
- Data boundary control
- Output and decision control
- Monitoring, logging, and evidence
- Incident containment and recovery

## Control Failures

- AI feature not inventoried
- vendor processing not reviewed
- retention and training settings unknown
- admin controls not assessed
- logs unavailable or unknown
- incident support path undefined

## Potential Impact

- vendor retention of prompts or outputs
- data used for product improvement or training
- sensitive data exposure
- unreviewed AI output influencing decisions
- lack of audit evidence
- inability to disable feature quickly

## Required Controls

- vendor AI assessment
- feature enablement review
- admin control review
- data processing review
- retention and training/reuse review
- vendor incident process
- evidence availability review

## Evidence Needed

- vendor assessment
- vendor AI documentation
- admin configuration evidence
- data processing terms
- retention settings
- training/reuse settings
- logging documentation
- incident support contact

## Assurance Tests

- verify AI feature enablement status
- confirm training/reuse settings
- confirm prompt/output retention
- test admin disablement
- confirm logs can be exported
- review vendor incident response process

## Containment Actions

- disable vendor AI feature
- restrict user access
- update admin settings
- notify vendor
- request vendor evidence
- open exception if required controls cannot be met

---

# 5. Failure Scenario 3: Excessive AI Data Access

## What Happens

An AI capability can access more data than required for its approved purpose.

This may occur through broad service account permissions, inherited user access, poorly scoped retrieval, over-permissive SaaS integrations, or agent tool access.

## Why It Happens

- AI is given broad permissions for convenience.
- Service accounts are reused.
- Least privilege is not applied.
- Data classifications are not mapped.
- Access reviews do not include AI identities.
- Vendor AI inherits broad tenant permissions.
- Retrieval indexes include excessive sources.

## Affected AI Patterns

- Copilots
- RAG systems
- Internal LLM applications
- AI-enabled SaaS
- Agents
- Tool-using AI
- Developer AI

## Affected Pillars

- AI identity and access control
- Data boundary control
- Monitoring, logging, and evidence
- AI assurance and testing
- Incident containment and recovery

## Control Failures

- AI identity model undefined
- excessive access approved or unnoticed
- data owners not involved
- no least privilege review
- no access review cadence
- no revocation path
- incomplete data access logs

## Potential Impact

- sensitive data exposure
- unauthorized retrieval
- regulatory exposure
- legal privilege breach
- customer or employee data leakage
- insider misuse amplification
- incident investigation gaps

## Required Controls

- AI identity model
- least privilege review
- data source mapping
- data owner approval
- AI access review
- privileged access control
- revocation path
- data access logging

## Evidence Needed

- identity record
- access approval
- data source map
- data owner approval
- least privilege review
- access review record
- access logs
- revocation test result

## Assurance Tests

- compare AI access to approved use case
- test access to prohibited data
- test cross-user retrieval
- test cross-tenant retrieval
- review service account permissions
- confirm revocation path works

## Containment Actions

- revoke excessive permissions
- disable AI identity
- remove data sources
- rebuild retrieval index
- rotate credentials
- notify data owner
- preserve access logs

---

# 6. Failure Scenario 4: Unauthorized RAG Retrieval

## What Happens

A RAG system retrieves documents, records, or excerpts that the user or use case should not access.

The model may then summarize or expose the retrieved information in output.

## Why It Happens

- retrieval index includes sensitive sources
- document-level permissions are not enforced
- user permissions are not inherited
- metadata filtering is incomplete
- embeddings ignore classification boundaries
- tenant or customer boundaries are missing
- retrieval testing was not performed

## Affected AI Patterns

- RAG systems
- Knowledge assistants
- Customer support AI
- Legal assistants
- Internal LLM applications
- Developer AI
- Security AI

## Affected Pillars

- Data boundary control
- AI identity and access control
- Prompt and input control
- Monitoring, logging, and evidence
- AI assurance and testing
- Incident containment and recovery

## Control Failures

- data sources not mapped
- retrieval boundary not defined
- data classification not enforced
- permission inheritance not tested
- retrieval logs missing
- output sensitivity not preserved

## Potential Impact

- confidential document exposure
- customer data leakage
- employee data leakage
- legal privilege breach
- cross-tenant exposure
- regulatory impact
- loss of trust in AI system

## Required Controls

- data source mapping
- retrieval boundary design
- document-level access enforcement
- classification filtering
- tenant/customer boundary controls
- retrieval logging
- output sensitivity handling
- retrieval boundary testing

## Evidence Needed

- retrieval configuration
- data classification record
- access control design
- retrieval test results
- denied retrieval logs
- output logs or references
- data owner approval

## Assurance Tests

- test user without permission cannot retrieve restricted document
- test cross-tenant isolation
- test sensitive source exclusion
- test classification filtering
- test output does not expose denied context
- test retrieval evidence reconstruction

## Containment Actions

- disable retrieval
- remove sensitive index sources
- rebuild vector index
- revoke access
- quarantine outputs
- notify data owner
- preserve retrieval logs
- open incident where exposure occurred

---

# 7. Failure Scenario 5: Prompt Injection Through Retrieved Content

## What Happens

The AI retrieves or receives malicious or untrusted content containing instructions designed to override system behavior, leak data, ignore policies, call tools, or produce unsafe output.

The AI follows those instructions because it treats retrieved content as instruction rather than data.

## Why It Happens

- retrieved content is not treated as untrusted
- system instructions are not protected
- tool use is not separated from untrusted context
- prompt injection testing is not performed
- external content is allowed without controls
- agent uses retrieved content to decide actions

## Affected AI Patterns

- RAG systems
- Agents
- Tool-using AI
- Customer-facing AI
- Developer AI
- Security operations AI

## Affected Pillars

- Prompt and input control
- Data boundary control
- Tool and action control
- AI assurance and testing
- Monitoring, logging, and evidence
- Incident containment and recovery

## Control Failures

- untrusted content not labeled
- prompt injection risk not assessed
- no separation of instructions and content
- tool actions allowed from untrusted context
- no approval gate for high-risk actions
- no prompt injection monitoring

## Potential Impact

- data leakage
- unauthorized tool use
- unsafe output
- approval bypass
- system prompt exposure
- agent misuse
- customer-facing harm

## Required Controls

- trusted/untrusted content separation
- system prompt protection
- prompt injection controls
- tool-use restrictions from untrusted input
- approval gates
- prompt injection testing
- monitoring for policy violations

## Evidence Needed

- prompt/input control record
- system prompt version
- context isolation design
- prompt injection test result
- tool/action policy
- logs showing blocked or handled injection attempts

## Assurance Tests

- inject malicious instructions into retrieved documents
- test uploaded file prompt injection
- test tool-use prompt injection
- test system prompt extraction attempt
- test agent action under injected context
- confirm policy violation logging

## Containment Actions

- disable affected retrieval source
- quarantine malicious content
- disable tool access
- suspend agent
- update prompt/input controls
- preserve prompt and retrieval logs
- retest before restart

---

# 8. Failure Scenario 6: Sensitive Data Entered Into Prompts

## What Happens

Users enter sensitive, regulated, privileged, confidential, customer, employee, financial, security, or secret data into an AI prompt.

The data may be processed by a vendor, retained in logs, included in outputs, or reused in ways the enterprise did not approve.

## Why It Happens

- prohibited inputs are not defined
- users are not trained
- DLP or sensitive data detection is missing
- vendor processing terms are unclear
- prompt logs retain sensitive content
- no warning or blocking exists
- users treat AI as a private workspace

## Affected AI Patterns

- Copilots
- Internal LLM applications
- AI-enabled SaaS
- Customer-facing AI
- Developer AI
- Security AI

## Affected Pillars

- Prompt and input control
- Data boundary control
- Monitoring, logging, and evidence
- Human accountability model
- Incident containment and recovery

## Control Failures

- no prohibited input rules
- no sensitive data detection
- no user guidance
- no vendor processing review
- full prompt logging without controls
- no incident escalation for sensitive data exposure

## Potential Impact

- privacy breach
- legal privilege exposure
- customer data leakage
- credential exposure
- regulatory reporting obligation
- vendor data retention risk
- security incident

## Required Controls

- prohibited input policy
- sensitive data detection
- prompt warnings or blocking
- redaction or masking
- vendor data processing review
- prompt logging controls
- incident escalation path

## Evidence Needed

- prohibited input rules
- DLP or detection configuration
- warning/block logs
- prompt logging approach
- vendor retention settings
- incident record if exposure occurs

## Assurance Tests

- test prompt with sample sensitive data
- test secret or API key detection
- test regulated data warning/block
- verify redaction in logs
- verify vendor training/reuse disabled where required
- test escalation path

## Containment Actions

- delete or restrict prompt logs where permitted
- notify data owner
- rotate exposed credentials
- notify vendor where required
- open privacy/security incident
- update input controls
- educate users

---

# 9. Failure Scenario 7: AI Recommendation Becomes Final Decision

## What Happens

An AI-generated recommendation, score, summary, or classification is treated as the final decision without meaningful human review or accountable decision ownership.

## Why It Happens

- decision impact is not classified
- AI output is trusted because it appears authoritative
- workflow automatically uses AI output
- reviewer lacks time, context, or authority
- final decision is not recorded separately
- decision owner is not assigned
- output validation is missing

## Affected AI Patterns

- Decision-supporting AI
- Customer-facing AI
- HR AI
- Finance AI
- Legal/compliance AI
- Security operations AI
- High-impact AI

## Affected Pillars

- Output and decision control
- Human accountability model
- AI assurance and testing
- Monitoring, logging, and evidence

## Control Failures

- no decision owner
- no recommendation/final decision separation
- no validation rule
- no meaningful review
- no decision evidence
- no correction path

## Potential Impact

- incorrect customer decision
- employee impact
- financial loss
- legal or compliance exposure
- unfair or biased outcome
- security misclassification
- audit finding

## Required Controls

- decision impact classification
- decision owner assignment
- output validation
- human review model
- recommendation label
- final decision record
- correction/override path
- decision evidence retention

## Evidence Needed

- output classification
- decision owner mapping
- validation record
- reviewer record
- final decision evidence
- override or correction record
- assurance test result

## Assurance Tests

- verify AI recommendation is labeled
- verify final decision requires human approval
- verify reviewer has source material
- verify decision owner is recorded
- test rejection and override path
- test decision evidence reconstruction

## Containment Actions

- suspend automated decision use
- review affected decisions
- correct records
- notify affected parties where required
- update decision controls
- retrain reviewers
- open incident if harm occurred

---

# 10. Failure Scenario 8: Ceremonial Human Review

## What Happens

A human is formally required to review AI output, but the review is not meaningful.

The reviewer may lack context, time, authority, source material, training, or incentive to challenge the AI.

## Why It Happens

- human-in-the-loop is added as a checkbox
- reviewer role is not defined
- review criteria are vague
- reviewer cannot reject output
- workload makes review superficial
- no evidence of review quality
- overtrust in AI output develops

## Affected AI Patterns

- Decision-supporting AI
- Customer-facing AI
- High-impact AI
- Security operations AI
- AI-generated records
- Tool/action workflows

## Affected Pillars

- Human accountability model
- Output and decision control
- AI assurance and testing
- Monitoring, logging, and evidence

## Control Failures

- review model not defined
- reviewer lacks authority
- no review criteria
- no review evidence
- no override path
- no quality monitoring

## Potential Impact

- AI error passes through control
- accountability gap
- incorrect decisions
- customer or employee harm
- audit criticism
- false sense of control

## Required Controls

- meaningful review criteria
- reviewer authority
- source access for reviewer
- rejection and override paths
- review evidence
- reviewer training
- review quality monitoring

## Evidence Needed

- human accountability record
- review criteria
- reviewer record
- approval/rejection logs
- override records
- quality monitoring results
- assurance findings

## Assurance Tests

- observe review process
- sample reviewed AI outputs
- confirm reviewer can reject output
- confirm reviewer has source material
- test override path
- measure rejection or modification rate

## Containment Actions

- pause high-risk use
- require second-line review
- update review process
- train reviewers
- add sampling or monitoring
- reassess decisions made under weak review

---

# 11. Failure Scenario 9: AI-Generated Record Becomes Authoritative

## What Happens

AI-generated summaries, classifications, notes, reports, or case narratives become enterprise records without provenance, validation, or correction mechanisms.

## Why It Happens

- output becomes a record automatically
- AI involvement is not labeled
- source references are not retained
- reviewer evidence is missing
- generated records are not classified
- correction process is undefined

## Affected AI Patterns

- Copilots
- Internal LLM applications
- Customer support AI
- Legal AI
- HR AI
- Security AI
- Decision-supporting AI

## Affected Pillars

- Output and decision control
- Human accountability model
- Monitoring, logging, and evidence
- AI assurance and testing

## Control Failures

- no generated record control
- no provenance
- no validation
- no retention rule
- no correction path
- no decision evidence

## Potential Impact

- inaccurate official record
- legal or compliance exposure
- customer dispute
- employee impact
- audit evidence weakness
- operational errors

## Required Controls

- generated record classification
- AI provenance marker
- source references
- human review where required
- record owner assignment
- correction path
- retention rule
- evidence capture

## Evidence Needed

- generated record metadata
- source references
- review record
- approval record
- correction record
- output logs
- retention evidence

## Assurance Tests

- verify AI-generated record is labeled
- verify source references are retained
- verify record can be corrected
- verify reviewer approval is captured
- sample generated records for accuracy
- test evidence reconstruction

## Containment Actions

- quarantine affected records
- correct or amend records
- notify affected process owners
- suspend automatic record creation
- update generated record controls

---

# 12. Failure Scenario 10: Unauthorized Tool Use

## What Happens

AI calls a tool, API, plugin, workflow, or function it should not be able to use, or uses an approved tool for an unauthorized purpose.

## Why It Happens

- tool inventory incomplete
- tool permissions too broad
- AI identity has excessive access
- action boundaries not enforced
- prompt injection influences tool use
- approval gate missing
- tool logs incomplete

## Affected AI Patterns

- Tool-using AI
- Agents
- Internal LLM applications
- AI-enabled SaaS
- Developer AI
- Security operations AI

## Affected Pillars

- Tool and action control
- AI identity and access control
- Prompt and input control
- Monitoring, logging, and evidence
- Incident containment and recovery

## Control Failures

- no tool inventory
- no action classification
- no least privilege
- no approval gate
- no boundary enforcement
- no tool-call logging
- no kill switch

## Potential Impact

- record modification
- unauthorized communication
- workflow disruption
- access change
- security control change
- financial or operational impact
- production impact

## Required Controls

- tool inventory
- action classification
- tool access approval
- least privilege
- action boundaries
- approval gates
- tool/action logs
- kill switch
- rollback or compensation

## Evidence Needed

- tool inventory
- tool approval
- AI identity record
- action classification
- approval logs
- tool-call logs
- action logs
- kill switch test
- rollback evidence

## Assurance Tests

- attempt unauthorized tool call
- attempt authorized tool with unauthorized parameters
- test approval gate
- test prompt injection to tool use
- test tool-call logging
- test tool disablement

## Containment Actions

- disable tool access
- revoke AI identity
- stop workflow
- roll back action
- preserve logs
- open incident
- update action boundaries

---

# 13. Failure Scenario 11: Approval Bypass

## What Happens

AI performs, triggers, or requests a high-risk action without required human or policy approval.

This may occur because approval is advisory, poorly enforced, or bypassed through alternate workflow paths.

## Why It Happens

- approval gate is not technically enforced
- agent can call lower-level API directly
- workflow has alternate execution path
- approval threshold is unclear
- delegated authority too broad
- approval logs missing
- exception process misused

## Affected AI Patterns

- Tool-using AI
- Agentic AI
- AI workflow automation
- Security operations AI
- Financial AI
- Customer-facing AI

## Affected Pillars

- Tool and action control
- Human accountability model
- AI identity and access control
- Monitoring, logging, and evidence
- AI assurance and testing

## Control Failures

- approval gate not enforced
- approver not assigned
- no approval evidence
- action boundary missing
- no approval bypass testing
- no monitoring for bypass attempts

## Potential Impact

- unauthorized action
- financial loss
- customer impact
- security control failure
- production change
- compliance breach
- accountability gap

## Required Controls

- enforced approval gates
- approver assignment
- action thresholds
- approval evidence
- bypass prevention
- tool/API boundary
- monitoring for bypass attempts
- assurance testing

## Evidence Needed

- approval gate configuration
- approval matrix
- approval logs
- action logs
- denied action logs
- bypass test results
- exception records

## Assurance Tests

- attempt action without approval
- attempt direct API path
- test threshold-based approval
- test expired approval
- test denied approval
- confirm logs capture bypass attempts

## Containment Actions

- suspend action path
- revoke tool permission
- review actions executed without approval
- correct affected records
- update approval enforcement
- open incident

---

# 14. Failure Scenario 12: Agent Cannot Be Stopped

## What Happens

An AI agent continues to operate after it behaves incorrectly, loops, retries excessively, calls tools unexpectedly, or causes impact.

The enterprise cannot quickly disable the agent, revoke authority, stop workflows, or contain downstream actions.

## Why It Happens

- kill switch not designed
- agent identity not separate
- tool access cannot be revoked quickly
- workflows lack pause controls
- vendor feature cannot be disabled
- monitoring does not detect runaway behavior
- restart criteria are undefined

## Affected AI Patterns

- Agentic AI
- Tool-using AI
- AI workflow automation
- Security operations AI
- Developer AI
- Customer-facing AI with actions

## Affected Pillars

- Tool and action control
- AI identity and access control
- Monitoring, logging, and evidence
- Incident containment and recovery
- AI assurance and testing

## Control Failures

- no kill switch
- no revocation path
- no blast-radius limit
- no workflow stop path
- no monitoring
- no containment test

## Potential Impact

- repeated incorrect actions
- customer or employee impact
- operational disruption
- financial loss
- production issue
- security incident
- inability to preserve evidence

## Required Controls

- agent identity
- kill switch
- tool disablement
- workflow stop mechanism
- blast-radius limits
- monitoring for abnormal behavior
- containment testing
- restart criteria

## Evidence Needed

- kill switch design
- revocation matrix
- monitoring rules
- action logs
- kill switch test record
- incident containment record
- restart approval

## Assurance Tests

- test agent disablement
- test tool disablement
- test workflow stop
- test rate and retry limits
- test monitoring alert
- test restart approval process

## Containment Actions

- suspend agent
- disable identity
- revoke tools
- stop workflow
- disable vendor feature
- preserve logs
- roll back actions
- require retesting before restart

---

# 15. Failure Scenario 13: Vendor Logs Unavailable During Incident

## What Happens

An AI incident involves a vendor AI feature, but the enterprise cannot obtain prompt logs, output logs, data access logs, configuration history, or tool/action evidence from the vendor.

## Why It Happens

- logging was not reviewed before enablement
- vendor does not retain required logs
- logs are available only in higher plan
- contract lacks evidence obligations
- admin export is unavailable
- retention period expired
- vendor support process is unclear

## Affected AI Patterns

- AI-enabled SaaS
- Embedded vendor AI
- Hosted model APIs
- Vendor copilots
- Third-party agents

## Affected Pillars

- Monitoring, logging, and evidence
- Incident containment and recovery
- Data boundary control
- AI assurance and testing

## Control Failures

- vendor evidence not reviewed
- incident support not defined
- retention requirements not negotiated
- logs unavailable
- evidence package incomplete
- reconstructability not tested

## Potential Impact

- incident cannot be investigated
- regulatory response weakened
- audit finding
- inability to confirm data exposure
- inability to prove containment
- delayed recovery

## Required Controls

- vendor evidence review
- logging documentation
- retention review
- export capability review
- contractual evidence obligations
- vendor incident contact
- evidence reconstruction testing

## Evidence Needed

- vendor assessment
- logging documentation
- contract terms
- admin export evidence
- retention settings
- vendor incident process
- evidence gap record

## Assurance Tests

- request sample logs
- test log export
- verify retention period
- test vendor incident contact path
- confirm configuration history availability
- perform evidence reconstruction exercise

## Containment Actions

- preserve enterprise-side logs
- contact vendor immediately
- request evidence under contract
- disable feature if evidence gap is unacceptable
- document evidence limitation
- open exception or remediation item

---

# 16. Failure Scenario 14: AI Incident Cannot Be Reconstructed

## What Happens

After an AI incident, the enterprise cannot determine what happened.

It cannot reconstruct what AI saw, what prompt was submitted, what data was retrieved, what output was produced, what tool was called, who approved it, or what action occurred.

## Why It Happens

- logging requirements not defined
- logs are scattered
- prompt/output logs not retained
- retrieval logs unavailable
- tool/action logs incomplete
- approval evidence missing
- vendor logs unavailable
- evidence retention expired

## Affected AI Patterns

- All AI patterns
- Especially high-risk AI, agents, vendor AI, and decision-supporting AI

## Affected Pillars

- Monitoring, logging, and evidence
- Incident containment and recovery
- AI assurance and testing
- Human accountability model

## Control Failures

- no AI event taxonomy
- no evidence package
- no reconstructability requirement
- no log retention rule
- no evidence owner
- no reconstruction testing

## Potential Impact

- incident investigation failure
- audit failure
- regulatory response weakness
- inability to identify affected parties
- inability to remediate root cause
- loss of trust

## Required Controls

- AI event taxonomy
- logging requirements by risk tier
- evidence retention
- evidence owner
- prompt/input evidence
- retrieval evidence
- output evidence
- tool/action evidence
- approval evidence
- reconstruction testing

## Evidence Needed

- logs from AI system
- data access logs
- retrieval logs
- prompt/output records or metadata
- approval records
- action logs
- incident evidence package
- reconstruction test result

## Assurance Tests

- reconstruct sample AI interaction
- reconstruct decision-supporting workflow
- reconstruct tool action
- reconstruct vendor AI interaction where possible
- test evidence retrieval within retention period
- validate evidence completeness

## Containment Actions

- preserve available logs immediately
- collect evidence from related systems
- contact vendor
- suspend high-risk use if evidence gap is material
- update logging requirements
- open assurance finding

---

# 17. Failure Scenario 15: Exception Becomes Permanent

## What Happens

A temporary exception to an AI control requirement remains open indefinitely.

The exception becomes the operating model rather than a time-bound risk decision.

## Why It Happens

- no expiry date
- no exception owner
- weak review process
- remediation plan missing
- compensating controls not monitored
- governance does not track exceptions
- business pressure normalizes the gap

## Affected AI Patterns

- All AI patterns
- Especially high-risk AI, vendor AI, and agentic AI

## Affected Pillars

- Human accountability model
- Monitoring, logging, and evidence
- AI assurance and testing
- Incident containment and recovery

## Control Failures

- exception not owned
- no risk acceptance owner
- no expiry date
- no compensating controls
- no remediation due date
- no review cadence
- no escalation for overdue exception

## Potential Impact

- unmanaged residual risk
- normalized control weakness
- audit finding
- incident likelihood increases
- weak governance credibility
- risk accepted by wrong party

## Required Controls

- exception record
- business justification
- risk assessment
- compensating control
- expiry date
- remediation plan
- owner and approver
- periodic review
- closure evidence

## Evidence Needed

- exception record
- approval evidence
- compensating control evidence
- review records
- remediation plan
- expiry tracking
- closure evidence

## Assurance Tests

- sample AI exceptions
- check expiry dates
- check compensating controls
- check overdue exceptions
- check risk acceptance authority
- verify closure evidence

## Containment Actions

- escalate overdue exception
- restrict AI use until control gap is remediated
- require renewed approval
- strengthen compensating controls
- close exception when resolved

---

# 18. Failure Scenario 16: AI Output Reaches Customer Incorrectly

## What Happens

An AI-generated response, recommendation, summary, or instruction is sent to a customer and is incorrect, harmful, misleading, unauthorized, or inconsistent with policy.

## Why It Happens

- customer-facing output boundaries are not defined
- human review is missing or weak
- AI makes unauthorized commitments
- escalation triggers are not defined
- output validation is weak
- conversation evidence is missing
- correction process is not defined

## Affected AI Patterns

- Customer-facing AI
- AI-enabled SaaS
- Copilots used for customer response drafting
- RAG-based support assistant
- Tool-using customer service AI

## Affected Pillars

- Output and decision control
- Human accountability model
- Prompt and input control
- Monitoring, logging, and evidence
- Incident containment and recovery

## Control Failures

- no external output control
- no prohibited response categories
- no escalation path
- no review or approval
- no correction process
- no customer impact owner

## Potential Impact

- customer harm
- customer complaint
- unauthorized contractual commitment
- privacy exposure
- regulatory issue
- reputational damage
- legal dispute

## Required Controls

- customer-facing output boundaries
- prohibited output rules
- escalation triggers
- review or approval where required
- conversation logging
- correction/retraction path
- customer impact owner
- incident response process

## Evidence Needed

- customer-facing output policy
- conversation logs
- reviewer/approval record
- output record
- correction record
- incident record
- customer notification evidence where required

## Assurance Tests

- test prohibited customer response
- test escalation trigger
- test incorrect answer correction
- test privacy-sensitive customer prompt
- test customer complaint handling
- test conversation evidence retrieval

## Containment Actions

- block or withdraw output
- correct communication
- notify customer where required
- escalate to legal/privacy/compliance
- suspend customer-facing AI capability
- review similar outputs
- update output controls

---

# 19. Failure Scenario 17: AI Changes Production or Security State

## What Happens

AI performs or triggers a change in a production, security, access, infrastructure, financial, or operational system without adequate approval, testing, or rollback.

## Why It Happens

- AI has privileged tool access
- tool/action risk classification is missing
- approval gate is weak
- production access is over-permissive
- generated code or command is trusted
- rollback path is not defined
- action logs are incomplete

## Affected AI Patterns

- Agentic AI
- Tool-using AI
- Developer AI
- Security operations AI
- AI workflow automation

## Affected Pillars

- Tool and action control
- AI identity and access control
- AI assurance and testing
- Monitoring, logging, and evidence
- Incident containment and recovery

## Control Failures

- privileged AI access not controlled
- no production boundary
- no approval gate
- no change control integration
- no rollback plan
- no kill switch
- no action logging

## Potential Impact

- production outage
- security control disruption
- unauthorized access change
- financial loss
- data corruption
- operational disruption
- incident escalation

## Required Controls

- privileged access control
- production change boundary
- approval gates
- change management integration
- action classification
- kill switch
- rollback plan
- action logging
- assurance testing

## Evidence Needed

- access approval
- production change approval
- action logs
- tool-call logs
- approval records
- rollback plan
- kill switch test
- incident evidence

## Assurance Tests

- test unauthorized production action
- test approval gate
- test rollback
- test kill switch
- test action logging
- test change management integration

## Containment Actions

- stop workflow
- revoke privileged access
- roll back production change
- preserve action logs
- open incident
- require retesting before restart
- update privileged access controls

---

# 20. Failure Scenario 18: Model or Prompt Change Breaks Control

## What Happens

A change to model version, provider, system prompt, retrieval prompt, tool instruction, guardrail, policy prompt, or vendor feature changes AI behavior and weakens or bypasses an existing control.

## Why It Happens

- prompt changes are not versioned
- model upgrades are not reviewed
- vendor changes feature behavior
- regression testing is not required
- control assumptions are not documented
- deployment process treats prompts as content rather than control logic

## Affected AI Patterns

- Internal LLM applications
- RAG systems
- Agents
- Customer-facing AI
- Tool-using AI
- Vendor AI

## Affected Pillars

- Prompt and input control
- AI assurance and testing
- Output and decision control
- Tool and action control
- Monitoring, logging, and evidence

## Control Failures

- no prompt change control
- no regression testing
- no model change review
- no rollback capability
- no test baseline
- no monitoring after change

## Potential Impact

- degraded output quality
- prompt injection vulnerability
- data leakage
- tool misuse
- approval bypass
- customer-facing errors
- incident risk

## Required Controls

- prompt versioning
- model/provider change review
- regression testing triggers
- approval for prompt changes
- rollback capability
- post-change monitoring
- assurance evidence

## Evidence Needed

- change record
- prompt version history
- model version record
- approval record
- regression test results
- deployment evidence
- rollback plan

## Assurance Tests

- compare pre-change and post-change behavior
- retest prompt injection scenarios
- retest retrieval boundaries
- retest output validation
- retest tool/action controls
- monitor post-change incidents and errors

## Containment Actions

- roll back prompt or model version
- disable affected capability
- suspend tool access
- notify owners
- retest before redeployment
- update change controls

---

# 21. Failure Scenario 19: Data Retained or Reused Unexpectedly

## What Happens

Prompts, outputs, uploaded files, retrieved context, telemetry, logs, embeddings, or conversation history are retained or reused by a vendor, platform, model provider, or internal system beyond approved boundaries.

## Why It Happens

- vendor retention settings unclear
- training/reuse settings not reviewed
- logs capture sensitive content
- embeddings retained without classification
- deletion process undefined
- data residency not reviewed
- product improvement use not disabled

## Affected AI Patterns

- AI-enabled SaaS
- Hosted model API
- Embedded vendor AI
- Copilots
- Internal LLM applications
- RAG systems

## Affected Pillars

- Data boundary control
- Monitoring, logging, and evidence
- Incident containment and recovery

## Control Failures

- retention not defined
- training/reuse not restricted
- vendor terms not reviewed
- data deletion not defined
- log sensitivity not handled
- embeddings not governed

## Potential Impact

- privacy breach
- contractual breach
- regulatory issue
- legal privilege exposure
- sensitive data persistence
- inability to honor deletion requirements
- data used for training without approval

## Required Controls

- retention rules
- training/reuse restrictions
- vendor data processing review
- logging sensitivity controls
- deletion process
- evidence retention and expiry
- data owner approval

## Evidence Needed

- vendor terms
- retention settings
- training/reuse settings
- deletion process
- log configuration
- data owner approval
- exception record if controls cannot be met

## Assurance Tests

- verify training/reuse disabled where required
- verify retention settings
- test deletion process
- review log content sensitivity
- review embedding/index lifecycle
- confirm vendor data handling evidence

## Containment Actions

- disable retention where possible
- delete retained data where permitted
- request vendor deletion
- restrict data inputs
- notify data/privacy owners
- open incident if exposure occurred
- update vendor assessment

---

# 22. Failure Scenario 20: AI Failure Has No Recovery Path

## What Happens

An AI-generated output, decision, record, action, or workflow causes harm, but the enterprise has no clear way to correct, reverse, compensate, notify, or recover.

## Why It Happens

- recoverability not assessed
- output correction path missing
- generated records cannot be amended
- workflow rollback not designed
- vendor remediation path unclear
- action is irreversible
- restart criteria undefined

## Affected AI Patterns

- Customer-facing AI
- Decision-supporting AI
- Tool-using AI
- Agentic AI
- High-impact AI
- Vendor AI

## Affected Pillars

- Incident containment and recovery
- Output and decision control
- Tool and action control
- Human accountability model
- Monitoring, logging, and evidence

## Control Failures

- no recovery owner
- no correction process
- no rollback plan
- no compensation model
- no customer notification path
- no post-incident review
- no restart criteria

## Potential Impact

- unresolved customer harm
- incorrect enterprise records
- financial loss
- legal exposure
- operational disruption
- reputational harm
- repeated failure

## Required Controls

- recoverability assessment
- correction path
- rollback plan
- compensation process
- recovery owner
- evidence preservation
- communication plan
- restart criteria
- post-incident review

## Evidence Needed

- recovery plan
- rollback test
- correction record
- communication evidence
- incident record
- recovery approval
- restart approval
- post-incident review

## Assurance Tests

- test output correction
- test generated record amendment
- test workflow rollback
- test customer notification path
- test vendor remediation path
- conduct incident tabletop

## Containment Actions

- stop affected workflow
- quarantine output
- correct records
- notify affected parties where required
- roll back action where possible
- define compensation
- retest before restart

---

# 23. Cross-Scenario Themes

Across these scenarios, the same themes repeat.

## Theme 1: Visibility Comes First

AI cannot be controlled if it is not visible.

Minimum requirement:

```text
Every AI capability must be inventoried, owned, classified, and lifecycle-managed.
```

## Theme 2: Authority Requires Identity

AI cannot be allowed to act through invisible or excessive authority.

Minimum requirement:

```text
Every AI actor must have a defined identity and revocation path.
```

## Theme 3: Data Requires Boundaries

AI data access must be explicit, approved, classified, and testable.

Minimum requirement:

```text
Every AI data source must have an owner, classification, boundary, and evidence.
```

## Theme 4: Inputs Are Control Surfaces

Prompts, retrieved content, uploaded files, and tool responses can alter AI behavior.

Minimum requirement:

```text
Inputs must be classified, restricted, validated, isolated, and tested where required.
```

## Theme 5: Output Is Not Decision

AI-generated content must not silently become a decision, record, communication, or action.

Minimum requirement:

```text
High-impact output requires validation, human accountability, and evidence.
```

## Theme 6: Tools Turn AI Into an Actor

Once AI can use tools, it can affect enterprise state.

Minimum requirement:

```text
AI-accessible tools must be inventoried, permissioned, approval-gated, logged, and containable.
```

## Theme 7: Evidence Is Control

A control that cannot be evidenced is difficult to trust.

Minimum requirement:

```text
High-risk AI activity must be reconstructable.
```

## Theme 8: Failure Must Be Containable

The enterprise must know how to stop, investigate, correct, and recover from AI failure.

Minimum requirement:

```text
High-risk AI must have containment, recovery, and restart criteria.
```

---

# 24. Using Scenarios for Assurance

These scenarios can be converted into test cases.

Example:

| Risk Scenario | Assurance Test |
|---|---|
| Unauthorized retrieval | Attempt retrieval outside approved user or data boundary. |
| Prompt injection | Insert malicious instruction into retrieved document or uploaded file. |
| Approval bypass | Attempt high-risk action without approval. |
| Tool misuse | Attempt unauthorized tool call or unsafe parameters. |
| Missing evidence | Attempt to reconstruct AI interaction from logs. |
| Agent cannot be stopped | Activate kill switch test. |
| Vendor logs unavailable | Request vendor evidence and test export. |
| Output becomes decision | Verify final decision is separate and evidenced. |

---

# 25. Using Scenarios for Incident Tabletop Exercises

These scenarios can also be used for tabletop exercises.

Example tabletop prompts:

```text
A RAG assistant exposes confidential legal documents to an unauthorized user.
```

```text
A customer-facing AI gives incorrect advice to 500 customers before detection.
```

```text
An AI agent triggers a workflow that updates incorrect customer records.
```

```text
A vendor AI feature retains prompts containing regulated data.
```

```text
A security AI disables a legitimate user account based on incorrect AI triage.
```

For each tabletop, ask:

```text
Who detects it?
Who owns it?
What evidence exists?
How do we stop it?
What data was exposed?
What decisions or actions occurred?
What vendor support is needed?
How do we recover?
Who approves restart?
What control changes follow?
```

---

# 26. Related Templates

Use these templates when applying the scenarios:

```text
templates/risk-scenario-template.md
templates/ai-risk-assessment-template.md
templates/ai-control-assessment-template.md
templates/ai-assurance-test-plan-template.md
templates/ai-control-evidence-package-template.md
templates/ai-exception-record-template.md
templates/ai-incident-record-template.md
templates/ai-incident-containment-recovery-template.md
```

---

# 27. Summary

AI failure scenarios are predictable.

Most failures come from one or more missing controls:

```text
No inventory
No owner
No boundary
No identity
No validation
No approval
No evidence
No kill switch
No recovery
```

The AI Control Architecture exists to prevent these failures where possible, detect them when they occur, and contain them before they become enterprise-wide harm.