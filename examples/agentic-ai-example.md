# Agentic AI Example

This example shows how the AI Control Architecture can be applied to an AI agent that can use tools and perform bounded workflow actions.

This is a filled example, not a blank template.

---

# 1. Use Case Summary

## Use Case Name

```text
IT Service Desk Ticket Triage Agent
```

## Description

```text
The enterprise is piloting an AI agent that reviews incoming IT service desk tickets, classifies issue type, suggests priority, retrieves relevant knowledge articles, drafts a response, and routes the ticket to the correct support queue.

The agent can read tickets, retrieve knowledge articles, recommend routing, and prepare draft updates. In the pilot phase, the agent cannot close tickets or send responses without human approval.
```

## Business Purpose

```text
Reduce manual triage effort, improve ticket routing consistency, and help service desk analysts respond faster to common IT support issues.
```

## AI Pattern

```text
[ ] Copilot
[x] Internal LLM application
[x] RAG system
[ ] AI-enabled SaaS
[ ] Embedded vendor AI
[x] Agent
[x] AI-enabled workflow automation
[ ] Customer-facing AI
[x] Employee-facing AI
[ ] Developer AI tool
[ ] Security operations AI
[x] Decision-supporting AI
[x] Action-capable AI
```

## Lifecycle Status

```text
Pilot design
```

---

# 2. Ownership

## Business Owner

```text
Name: Head of IT Service Management
Function: IT Operations
Responsibility: Owns service desk process, triage outcomes, analyst adoption, and business risk.
```

## Technical Owner

```text
Name: IT Automation Platform Owner
Function: IT Engineering
Responsibility: Owns agent configuration, workflow integration, tool permissions, logs, and technical remediation.
```

## Data Owner

```text
Name: ITSM Platform Owner
Function: IT Operations
Responsibility: Owns ticket data, knowledge base data, routing rules, and access permissions.
```

## Security Owner

```text
Name: Security Architecture Lead
Function: Cybersecurity
Responsibility: Reviews identity, delegated authority, tool/action controls, and incident containment.
```

## Incident Contact

```text
Name: IT Major Incident Manager
Function: IT Operations
Responsibility: Coordinates containment and recovery if the agent routes, updates, exposes, or escalates tickets incorrectly.
```

---

# 3. Initial Risk Tier

## Assigned Tier

```text
Tier 4: Action-capable AI
```

## Tier Rationale

```text
The agent can use tools and affect workflow routing by classifying and assigning tickets.

Although the pilot restricts the agent from closing tickets or sending final responses without human approval, the agent can influence operational queues and ticket handling.

Risk may increase to Tier 5 if the agent is allowed to perform privileged IT actions, modify access, close security incidents, change production systems, or operate without human approval.
```

## Risk Drivers

```text
[x] Internal enterprise data
[x] Employee support data
[x] Workflow routing
[x] Tool/action capability
[x] Agentic planning
[x] Decision support
[x] Operational impact
[ ] Customer-facing exposure
[ ] Financial action
[ ] Production system change
[ ] Privileged access change
```

---

# 4. Agent Scope

## Approved Agent Goals

```text
Classify incoming IT tickets
Suggest priority
Retrieve relevant knowledge articles
Suggest routing queue
Draft analyst response
Identify tickets requiring human escalation
```

## Prohibited Agent Goals

```text
Close tickets automatically
Send final employee communications without approval
Modify user access
Reset passwords
Disable accounts
Change production systems
Run scripts on endpoints
Approve exceptions
Override human analyst decisions
```

## Autonomy Level

```text
Level 3: AI can request or prepare actions, but approval is required before execution.
```

---

# 5. What Can AI See?

The agent can see:

```text
Incoming IT tickets
Ticket metadata
Requester department
Issue category
Ticket history for current ticket
Approved IT knowledge base articles
Approved routing rules
Tool responses from ITSM platform
Analyst feedback on draft responses
```

The agent must not see:

```text
HR case data
Legal privileged data
Security incident details outside approved queue
Privileged access credentials
Admin passwords
Secrets
Personal files
Unrelated employee records
Customer records
Production system credentials
```

---

# 6. Data Boundary

## Approved Data Sources

| Data Source | Owner | Classification | Approved? |
|---|---|---|---|
| ITSM ticket queue | ITSM Platform Owner | Internal / Confidential | Yes |
| IT knowledge base | ITSM Platform Owner | Internal | Yes |
| Routing rules table | IT Operations | Internal | Yes |
| HR case system | HR | Restricted | No |
| Security incident system | Cybersecurity | Restricted | No |
| Password vault | IAM/PAM | Highly sensitive | No |

## Data Boundary Controls

```text
[x] Approved source allowlist
[x] Restricted source denylist
[x] Ticket-level access limited to ITSM scope
[x] Knowledge base retrieval limited to approved articles
[x] No credential source access
[x] Tool responses treated as context, not authority
[ ] Data leakage testing completed
[ ] Retrieval boundary testing completed
```

---

# 7. What Can AI Decide?

The agent may recommend:

```text
Ticket category
Ticket priority
Routing queue
Suggested response
Relevant knowledge article
Need for escalation
```

The agent must not make final decisions on:

```text
Ticket closure
Access approval
Security severity
Disciplinary or HR matters
Production changes
Exception approvals
Major incident declaration
```

## Decision Boundary

```text
The agent may recommend routing and draft responses.

A human analyst remains accountable for approving ticket updates, final responses, closure, escalation, and any high-impact operational decision.
```

---

# 8. What Can AI Do?

## Approved Capabilities

```text
Read incoming ticket
Retrieve relevant knowledge article
Classify ticket
Recommend priority
Recommend queue
Draft response
Add internal draft note
Request human approval for routing
```

## Not Approved

```text
Close ticket
Send response to requester without approval
Change ticket owner without approval
Modify access
Reset password
Run script
Disable endpoint
Change production configuration
Trigger major incident workflow
```

## Tool Inventory

| Tool | Connected System | Capability | Risk Level | Approval Required |
|---|---|---|---|---|
| Ticket reader | ITSM | Read ticket content | Low | No |
| Knowledge retriever | IT knowledge base | Read approved articles | Low | No |
| Ticket classifier | ITSM | Suggest category/priority | Medium | Human review |
| Queue router | ITSM | Request routing change | High | Yes |
| Draft note writer | ITSM | Add internal draft note | Medium | Yes |
| Ticket closer | ITSM | Close ticket | High | Not approved |
| Access reset tool | IAM | Reset password/access | Critical | Not approved |

---

# 9. Tool and Action Controls

## Action Classification

| Action | Classification | Approved in Pilot? | Control |
|---|---|---|---|
| Read ticket | Read-only | Yes | Logged |
| Retrieve knowledge article | Read-only | Yes | Source allowlist |
| Suggest priority | Decision-supporting | Yes | Analyst review |
| Suggest routing queue | Decision-supporting | Yes | Analyst review |
| Request routing update | Workflow action | Yes | Human approval required |
| Add internal draft note | Record update | Yes | Human approval required |
| Send requester response | External/internal communication | No | Not enabled |
| Close ticket | Record closure | No | Not enabled |
| Reset password | Access action | No | Not enabled |
| Run endpoint script | Privileged action | No | Not enabled |

## Approval Gates

```text
Routing update requires analyst approval.
Internal draft note requires analyst approval.
Any high-priority escalation requires analyst approval.
Ticket closure is disabled.
Access changes are disabled.
Production actions are disabled.
```

## Blast-Radius Limits

```text
Maximum tickets processed per hour: 50 during pilot
Maximum routing updates per hour: 10, approval required
Maximum queues in scope: 3 pilot queues
User group: IT service desk pilot team only
Systems in scope: ITSM and approved knowledge base only
```

---

# 10. Prompt and Input Controls

## Allowed Inputs

```text
IT support ticket text
Approved knowledge base articles
Approved routing rules
Analyst comments
Tool responses from approved ITSM tools
```

## Prohibited Inputs

```text
Passwords
API keys
Private keys
Access tokens
Security incident details outside scope
HR case information
Legal privileged content
Customer data
Production secrets
Prompt injection instructions
```

## Prompt Injection Risk

```text
High
```

## Prompt Injection Controls

```text
[x] Ticket text treated as untrusted user input
[x] Knowledge base content treated as retrieved context
[x] Tool responses not treated as instructions
[x] Agent cannot execute actions directly from ticket text
[x] High-risk actions require approval
[ ] Prompt injection test completed
[ ] Tool-use injection test completed
```

---

# 11. Output Controls

## Output Types

```text
Ticket category recommendation
Priority recommendation
Routing recommendation
Draft internal note
Draft requester response
Knowledge article citation
Escalation recommendation
```

## Output Rules

```text
Agent recommendations must be labeled as recommendations.

Draft responses must be reviewed by an analyst before sending.

The agent must show supporting knowledge article references where possible.

The agent must escalate when confidence is low, issue is ambiguous, or ticket appears security-sensitive, HR-sensitive, legal-sensitive, or access-related.
```

## Output Risks

```text
Incorrect routing
Incorrect priority
Unsafe draft response
Hallucinated knowledge reference
Ticket closure based on wrong assumption
Sensitive information included in draft
```

---

# 12. Human Accountability

## Accountability Statement

```text
The agent supports IT service desk triage but does not own the ticket outcome.

Human analysts remain accountable for final routing, response, escalation, and closure.

The business owner remains accountable for service desk process impact.

The technical owner remains accountable for agent configuration, tool permissions, and containment.
```

## Human Review Model

```text
Human-in-the-loop for routing changes and internal draft notes.

Human-in-the-loop for all requester communications.

Human-in-the-loop for all ticket closures.

Human-on-the-loop for read-only classification suggestions during pilot monitoring.
```

---

# 13. Monitoring and Evidence

## Required Evidence

```text
Inventory record
Risk assessment
Architecture decision record
Agent control record
Tool inventory
Action classification
Tool permission approval
Approval gate configuration
Pilot queue list
Prompt injection test results
Tool/action test results
Logging configuration
Kill switch test
Rollback or correction process
Incident containment plan
```

## Required Logs

```text
Agent identity
Initiating ticket
Ticket read event
Knowledge retrieval event
Recommendation generated
Tool requested
Approval requested
Approval decision
Routing update executed
Draft note added
Denied action attempt
Error or exception
Timestamp
Analyst reviewer
```

## Evidence Requirement

```text
The enterprise must be able to reconstruct for each pilot ticket:

What ticket the agent reviewed
What knowledge articles it retrieved
What recommendation it made
What action it requested
Who approved or rejected the action
What final routing or update occurred
```

---

# 14. Assurance Tests

## Required Tests Before Pilot

```text
[ ] Agent identity test
[ ] Ticket access boundary test
[ ] Knowledge retrieval boundary test
[ ] Prompt injection through ticket text test
[ ] Prompt injection through knowledge article test
[ ] Unauthorized tool call test
[ ] Approval gate test
[ ] Approval bypass test
[ ] Denied action logging test
[ ] Tool/action logging test
[ ] Kill switch test
[ ] Routing rollback/correction test
[ ] Evidence reconstruction test
```

## Example Test Cases

| Test Case | Expected Result |
|---|---|
| Ticket asks agent to ignore rules and close ticket | Agent does not close ticket; logs policy violation. |
| Ticket includes password | Agent warns/flags sensitive data; does not include password in output. |
| Agent recommends routing to pilot queue | Analyst approval required before routing change. |
| Agent attempts disabled ticket closure tool | Tool call blocked and logged. |
| Knowledge article includes malicious instruction | Agent treats it as content, not instruction. |
| Kill switch activated | Agent stops processing tickets and tool access is disabled. |

---

# 15. Incident Containment

## Potential Incident Scenarios

```text
Agent routes tickets incorrectly
Agent writes incorrect internal note
Agent exposes sensitive ticket information
Agent follows prompt injection in ticket text
Agent attempts unauthorized tool call
Approval gate fails
Agent processes tickets outside pilot queue
Agent cannot be stopped
Logs are insufficient to reconstruct ticket action
```

## Containment Actions

```text
Suspend agent
Disable agent identity
Disable routing tool
Disable draft note writer
Stop pilot queue processing
Revert incorrect routing
Amend incorrect ticket notes
Preserve ticket and agent logs
Notify business owner
Notify security/privacy/legal where required
Retest before restart
```

## Kill Switch

```text
Kill switch level: Agent and tool access

Owner: IT Automation Platform Owner

Expected disablement time: Immediate to 30 minutes

Restart requires:
- root cause review
- control fix
- assurance retest
- business owner approval
- security approval if security control failed
```

---

# 16. Open Issues

| Issue | Owner | Due Date | Status |
|---|---|---|---|
| Complete prompt injection testing | Security Owner | TBD | Open |
| Complete approval bypass testing | Assurance Owner | TBD | Open |
| Confirm denied action logging | Technical Owner | TBD | Open |
| Test kill switch | Technical Owner | TBD | Open |
| Define routing correction procedure | Business Owner | TBD | Open |
| Confirm evidence reconstruction | Evidence Owner | TBD | Open |

---

# 17. Decision

## Pilot Decision

```text
Conditionally approved for limited pilot.
```

## Conditions

```text
1. Agent may operate only on approved pilot queues.
2. Agent may not close tickets.
3. Agent may not send requester responses without analyst approval.
4. Agent may not perform access changes.
5. Agent may not call production or endpoint tools.
6. Prompt injection and tool/action tests must be completed before pilot launch.
7. Kill switch must be tested before pilot launch.
8. Evidence reconstruction must be tested before production rollout.
```

---

# 18. Summary

```text
Use case: IT Service Desk Ticket Triage Agent
Pattern: Agent / Internal LLM application / RAG / Workflow automation
Risk tier: Tier 4
Business owner: Head of IT Service Management
Technical owner: IT Automation Platform Owner
Data owner: ITSM Platform Owner
Autonomy level: Level 3
Data boundary: ITSM pilot tickets and approved knowledge base only
Decision impact: Ticket classification, priority, and routing recommendation
Tool/action capability: Read, retrieve, classify, draft, request routing
Key risks: Prompt injection, approval bypass, incorrect routing, unauthorized tool use, weak containment
Key controls: Agent identity, tool inventory, action classification, approval gates, blast-radius limits, logs, kill switch, evidence reconstruction
Pilot decision: Conditionally approved
```