# RAG Assistant Example

This example shows how the AI Control Architecture can be applied to a retrieval-augmented generation system.

This is a filled example, not a blank template.

---

# 1. Use Case Summary

## Use Case Name

```text
Internal Policy Knowledge Assistant
```

## Description

```text
The enterprise is building an internal RAG assistant that allows employees to ask questions about approved internal policies, standards, procedures, and guidance documents.

The assistant retrieves relevant source documents and generates answers with references.
```

## Business Purpose

```text
Help employees find and understand approved internal policy guidance faster, reduce repetitive support questions, and improve consistency in policy interpretation.
```

## AI Pattern

```text
[ ] Copilot
[x] Internal LLM application
[x] RAG system
[ ] AI-enabled SaaS
[ ] Embedded vendor AI
[ ] Agent
[ ] AI-enabled workflow automation
[ ] Customer-facing AI
[x] Employee-facing AI
[ ] Developer AI tool
[ ] Security operations AI
[x] Decision-supporting AI
[ ] Action-capable AI
```

## Lifecycle Status

```text
Design review
```

---

# 2. Ownership

## Business Owner

```text
Name: Head of Enterprise Policy
Function: Governance / Risk / Compliance
Responsibility: Owns business purpose, approved content scope, user adoption, and policy interpretation boundaries.
```

## Technical Owner

```text
Name: AI Platform Engineering Lead
Function: Technology
Responsibility: Owns RAG application, model integration, retrieval pipeline, access controls, logging, and technical remediation.
```

## Data Owner

```text
Name: Enterprise Policy Repository Owner
Function: Governance / Knowledge Management
Responsibility: Owns approved policy documents, source classification, publication rules, and document lifecycle.
```

## Security Owner

```text
Name: Security Architecture Lead
Function: Cybersecurity
Responsibility: Reviews identity, access, retrieval boundaries, prompt injection controls, and logging.
```

## Incident Contact

```text
Name: GRC Operations Lead
Function: Governance / Risk / Compliance
Responsibility: Coordinates business response if the assistant provides incorrect, outdated, unauthorized, or harmful guidance.
```

---

# 3. Initial Risk Tier

## Assigned Tier

```text
Tier 3: Decision-supporting AI
```

## Tier Rationale

```text
The assistant provides policy guidance that may influence employee decisions and operational behavior.

It does not execute actions, modify records, or trigger workflows. However, incorrect or unauthorized guidance could affect compliance, risk decisions, or internal process execution.

Risk may increase if the assistant is connected to workflow systems, can open tickets, or can trigger approvals.
```

## Risk Drivers

```text
[x] Internal enterprise data
[x] Policy interpretation
[x] Decision support
[x] Retrieved enterprise content
[x] Potential outdated source risk
[x] Prompt injection through retrieved content
[ ] Customer-facing exposure
[ ] Tool/action capability
[ ] Autonomous execution
```

---

# 4. What Can AI See?

The assistant can see:

```text
User prompts
Approved policy documents
Approved standards
Approved procedures
Approved internal guidance
Document metadata
Retrieved excerpts
Source references
Conversation context within session
```

The assistant must not see:

```text
Draft policies not yet approved
Legal privileged documents
HR case files
Customer records
Employee records
Confidential investigations
Security incident details
Unapproved repositories
Restricted or regulated data unless separately approved
```

---

# 5. Data Boundary

## Approved Data Sources

| Data Source | Owner | Classification | Approved? |
|---|---|---|---|
| Published enterprise policy repository | Enterprise Policy Repository Owner | Internal / Confidential | Yes |
| Published standards repository | Enterprise Policy Repository Owner | Internal / Confidential | Yes |
| Published procedures repository | Process Owners | Internal / Confidential | Yes |
| Draft policy workspace | Enterprise Policy Repository Owner | Confidential | No |
| Legal advice repository | Legal | Privileged | No |
| HR case management system | HR | Restricted | No |

## Retrieval Boundary

```text
The assistant may retrieve only from approved published policy, standards, and procedure repositories.

The assistant must not retrieve from draft workspaces, legal privileged repositories, HR case systems, customer systems, security incident repositories, or unapproved collaboration folders.
```

## Data Boundary Controls

```text
[x] Source repository allowlist
[x] Sensitive repository denylist
[x] Data owner approval
[x] Document classification review
[x] Retrieval metadata filtering
[x] Source attribution required
[x] Retrieval logs required
[ ] Cross-user permission test completed
[ ] Prompt injection in retrieved content test completed
```

---

# 6. What Can AI Decide?

The assistant may influence:

```text
Employee understanding of policy
Employee operational choices
Internal compliance behavior
Escalation decisions
Interpretation of standards and procedures
```

The assistant must not:

```text
Make formal compliance decisions
Approve exceptions
Provide legal advice
Override policy owners
Issue binding interpretations
Replace human review for high-risk decisions
```

## Decision Boundary

```text
The assistant provides guidance and references.

Final interpretation, exceptions, approvals, and binding decisions remain with the relevant policy owner, compliance owner, legal owner, or governance forum.
```

---

# 7. What Can AI Do?

In this design, the assistant can:

```text
Search approved policy content
Retrieve relevant excerpts
Generate answers
Summarize policy sections
Provide source references
Suggest escalation to policy owner
```

The assistant cannot:

```text
Approve exceptions
Create records
Modify policies
Send official communications
Trigger workflows
Open tickets
Update systems
Grant access
```

## Tool and Action Capability

```text
Current status: Read-only retrieval only.

No write-capable tools, workflow triggers, or autonomous actions are approved.
```

---

# 8. Prompt and Input Controls

## Allowed Inputs

```text
Policy questions
Procedure questions
Standards clarification
Requests for source references
Questions about approved guidance
```

## Prohibited Inputs

```text
Requests for legal advice
Requests to bypass policy
Requests to approve exceptions
Sensitive personal data
Customer data
Employee case information
Secrets or credentials
Restricted investigation details
Prompt injection attempts
```

## Prompt Injection Risk

```text
High
```

## Prompt Injection Controls

```text
[x] Retrieved content treated as untrusted context
[x] System prompt instructs assistant not to treat retrieved content as controlling instruction
[x] Source allowlist limits retrieval sources
[x] Tool/action capability disabled
[x] User guidance warns against entering sensitive data
[ ] Prompt injection test cases completed
[ ] Monitoring for prompt injection indicators implemented
```

---

# 9. Output Controls

## Output Types

```text
Policy answer
Policy summary
Procedure explanation
Source-grounded guidance
Escalation recommendation
```

## Output Rules

```text
Answers must include source references where possible.

The assistant must distinguish between policy text, summary, and interpretation.

The assistant must state when a question requires policy owner, legal, privacy, security, HR, or compliance review.

The assistant must not invent policy requirements where source material is unavailable.
```

## Output Risks

```text
Incorrect summary
Outdated policy used
Missing source reference
Hallucinated requirement
Overconfident interpretation
User treats answer as formal approval
```

## Output Controls

```text
[x] Source references required
[x] No-source fallback defined
[x] Policy owner escalation defined
[x] Formal decisions prohibited
[x] Output validation required before production
[ ] Output quality sampling implemented
[ ] Hallucination testing completed
```

---

# 10. Human Accountability

## Accountability Statement

```text
The assistant provides source-grounded guidance only.

Policy owners remain accountable for policy content.

Employees remain accountable for following approved policy.

Compliance, legal, HR, privacy, or security owners remain accountable for specialist interpretations and formal decisions.
```

## Human Review Model

```text
Human-on-the-loop for routine policy questions.

Human-in-the-loop required for:
- policy exceptions
- legal interpretation
- HR-sensitive matters
- privacy-sensitive matters
- security-sensitive matters
- disputed or ambiguous guidance
```

---

# 11. Monitoring and Evidence

## Evidence Required

```text
Inventory record
Risk assessment
Architecture decision record
Data source map
Data owner approval
Retrieval configuration
Source allowlist
Sensitive source denylist
Prompt/input control record
Output validation test results
Retrieval boundary test results
Prompt injection test results
Logging configuration
Incident escalation path
```

## Logging Approach

```text
Prompt metadata, retrieval metadata, source document references, output metadata, and policy violation events should be logged.

Full prompt and output content logging requires privacy, legal, and data governance approval.

Retrieval evidence must be sufficient to reconstruct which source documents were used to generate an answer.
```

---

# 12. Assurance Tests

## Required Tests Before Pilot

```text
[ ] Source allowlist test
[ ] Sensitive source exclusion test
[ ] Retrieval boundary test
[ ] Cross-user access test
[ ] Prompt injection through retrieved content test
[ ] No-source answer behavior test
[ ] Source citation accuracy test
[ ] Output hallucination test
[ ] Escalation trigger test
[ ] Logging completeness test
[ ] Evidence reconstruction test
```

## Example Test Cases

| Test Case | Expected Result |
|---|---|
| Ask about approved policy | Assistant answers with source reference. |
| Ask about draft policy | Assistant does not retrieve draft content. |
| Ask for legal advice | Assistant refuses or escalates to legal. |
| Ask for policy exception approval | Assistant states it cannot approve exceptions. |
| Inject malicious instruction in retrieved document | Assistant treats content as data and does not follow malicious instruction. |
| Ask question with no source | Assistant says it cannot find approved source material. |

---

# 13. Incident Containment

## Potential Incident Scenarios

```text
Assistant retrieves unauthorized document
Assistant exposes confidential source
Assistant gives incorrect policy guidance
Assistant answers from outdated policy
Prompt injection affects output
User treats assistant answer as formal approval
Logs contain sensitive prompt content
```

## Containment Actions

```text
Disable affected retrieval source
Disable RAG assistant if leakage occurs
Remove or rebuild vector index
Quarantine incorrect output if recorded
Notify policy owner
Notify data owner
Notify security/privacy/legal where required
Preserve retrieval logs
Review affected user interactions
Update source allowlist or denylist
Retest before restart
```

## Restart Criteria

```text
Root cause identified
Affected data source removed or corrected
Retrieval boundary retested
Prompt injection controls retested where relevant
Evidence preserved
Policy owner approval obtained
Security approval obtained where required
```

---

# 14. Open Issues

| Issue | Owner | Due Date | Status |
|---|---|---|---|
| Complete data owner approval for procedures repository | Data Owner | TBD | Open |
| Complete prompt injection testing | Security Owner | TBD | Open |
| Complete retrieval boundary testing | Technical Owner | TBD | Open |
| Define logging retention | Evidence Owner | TBD | Open |
| Finalize no-source fallback wording | Business Owner | TBD | Open |
| Validate source citation accuracy | Assurance Owner | TBD | Open |

---

# 15. Decision

## Pilot Decision

```text
Conditionally approved for internal pilot.
```

## Conditions

```text
1. Retrieval must be limited to approved published policy sources.
2. Draft, legal, HR, customer, and security incident repositories must be excluded.
3. Prompt injection testing must be completed before pilot launch.
4. Retrieval boundary testing must be completed before pilot launch.
5. Source references must be included in answers where source material exists.
6. The assistant must not approve exceptions or provide legal advice.
7. Evidence reconstruction must be tested before production rollout.
```

---

# 16. Summary

```text
Use case: Internal Policy Knowledge Assistant
Pattern: RAG system / Internal LLM application / Employee-facing AI
Risk tier: Tier 3
Business owner: Head of Enterprise Policy
Technical owner: AI Platform Engineering Lead
Data owner: Enterprise Policy Repository Owner
Data boundary: Approved published policy repositories only
Decision impact: Policy guidance, not formal decision
Tool/action capability: Read-only retrieval only
Key risks: Unauthorized retrieval, prompt injection, outdated policy, overreliance
Key controls: Source allowlist, sensitive source exclusion, source attribution, retrieval testing, prompt injection testing, escalation path
Pilot decision: Conditionally approved
```