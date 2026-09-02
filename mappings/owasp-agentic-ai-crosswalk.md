# OWASP Agentic AI Crosswalk

This document maps the AI Control Architecture to agentic AI security risk themes reflected in OWASP Agentic AI / Agentic Applications guidance.

The purpose of this crosswalk is to show how the AI Control Architecture can help enterprises translate agentic AI security risks into practical controls, assurance tests, evidence, monitoring, and incident response.

The AI Control Architecture is not a replacement for OWASP guidance.

It is an enterprise control implementation layer that can help operationalize agentic AI security expectations.

---

# 1. Positioning

Agentic AI changes the enterprise control problem.

A chatbot primarily generates output.

An agent can pursue a goal, plan steps, call tools, use APIs, interact with systems, update records, trigger workflows, communicate with other agents, and continue operating across multiple steps.

That means agentic AI must be controlled as a non-human actor inside the enterprise.

A useful positioning is:

```text
OWASP Agentic AI guidance = agentic AI security risk taxonomy
AI Control Architecture = enterprise control architecture and implementation layer
```

This crosswalk helps security, AppSec, identity, platform, architecture, red-team, governance, risk, and incident response teams connect agentic AI risks to operational control requirements.

---

# 2. Agentic AI Risk Themes

Agentic AI security risk themes include:

```text
Agent goal hijacking
Tool misuse and exploitation
Identity and privilege abuse
Unexpected code execution
Insecure inter-agent communication
Human-agent trust exploitation
Agentic supply chain vulnerabilities
Memory and context poisoning
Cascading failures
Rogue agents
```

These risks are especially important when agents can:

```text
Use tools
Call APIs
Access enterprise data
Trigger workflows
Modify records
Communicate with users
Communicate with other agents
Operate with delegated authority
Persist memory or context
Act across multiple systems
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

For agentic AI, the most important pillars are usually:

```text
AI identity and access control
Tool and action control
Human accountability model
AI assurance and testing
Monitoring, logging, and evidence
Incident containment and recovery
```

---

# 4. High-Level Crosswalk

| Agentic AI Risk Theme | Primary AI Control Architecture Pillars |
|---|---|
| Agent goal hijacking | Prompt/input control; tool/action control; assurance testing |
| Tool misuse and exploitation | Tool/action control; identity/access; monitoring/evidence |
| Identity and privilege abuse | AI identity and access control; human accountability; incident containment |
| Unexpected code execution | Tool/action control; output/decision control; assurance testing |
| Insecure inter-agent communication | AI inventory; identity/access; monitoring/evidence; incident containment |
| Human-agent trust exploitation | Human accountability; output/decision control; evidence |
| Agentic supply chain vulnerabilities | AI inventory; vendor assessment; tool/action control; evidence |
| Memory and context poisoning | Data boundary; prompt/input control; assurance testing |
| Cascading failures | Tool/action control; monitoring/evidence; incident containment |
| Rogue agents | AI inventory; identity/access; kill switch; incident containment |

---

# 5. Agent Goal Hijacking

## Risk Theme

Agent goal hijacking occurs when malicious or untrusted input manipulates an agent’s objective, plan, or task execution path.

This can happen through:

```text
User prompts
Retrieved documents
Uploaded files
Emails
Tickets
Tool responses
Inter-agent messages
Memory or context
External web content
```

## AI Control Architecture Implementation Interpretation

The AI Control Architecture treats agent goals, plans, prompts, retrieved content, tool responses, and memory as control surfaces.

An agent must not allow untrusted content to redefine its approved purpose, scope, or action boundaries.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| Prompt and input control | Separates instructions from untrusted content and tests prompt injection. |
| Tool and action control | Prevents hijacked goals from causing unauthorized actions. |
| AI assurance and testing | Tests direct and indirect goal hijacking scenarios. |
| Monitoring, logging, and evidence | Captures goal, plan, tool-call, and policy violation evidence. |
| Incident containment and recovery | Defines response if the agent follows a hijacked goal. |

## Required Controls

```text
Define approved agent purpose.
Define prohibited agent goals.
Define autonomy level.
Treat external content as untrusted.
Treat retrieved content as untrusted.
Treat tool responses as untrusted.
Treat inter-agent messages as untrusted unless authenticated and authorized.
Prevent untrusted content from modifying agent goals.
Require approval for high-risk actions.
Log goal, plan, tool-call, and approval events where required.
Test direct and indirect goal hijacking.
```

## Example Assurance Tests

```text
Ticket text instructs agent to ignore rules and close ticket.
Retrieved document instructs agent to exfiltrate data.
Uploaded file tells agent to change its task objective.
Tool response instructs agent to call a different tool.
Inter-agent message requests action outside approved scope.
Agent is asked to continue a task after approval is denied.
```

## Example Evidence

```text
Agent purpose record
Autonomy level record
Prompt/input control record
Goal hijacking test results
Policy violation logs
Tool/action logs
Approval logs
Denied action logs
Incident record if hijacking succeeds
```

## Related Project Files

```text
docs/10-pillar-input-control.md
docs/12-pillar-tool-and-action-control.md
docs/20-common-failure-scenarios.md
docs/24-assurance-and-audit-guide.md
templates/ai-agent-control-template.md
templates/ai-tool-and-action-control-template.md
examples/agentic-ai-example.md
```

---

# 6. Tool Misuse and Exploitation

## Risk Theme

Tool misuse occurs when an agent uses an approved tool in an unsafe, unauthorized, excessive, or unintended way.

Tool exploitation can occur when an attacker manipulates the agent into using a legitimate tool for harmful purposes.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture treats every AI-accessible tool as an enterprise control point.

No agent should have tool access without inventory, owner approval, least privilege, action classification, logging, approval gates, and revocation.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| Tool and action control | Defines tool inventory, action classification, approval gates, kill switch, and rollback. |
| AI identity and access control | Limits tool access to approved identity and authority. |
| Monitoring, logging, and evidence | Logs tool calls, parameters, approvals, and results. |
| AI assurance and testing | Tests unauthorized tool use and approval bypass. |
| Incident containment and recovery | Defines tool disablement and rollback. |

## Required Controls

```text
Inventory all agent-accessible tools.
Assign tool owners.
Approve tool access.
Apply least privilege.
Classify actions by risk.
Define allowed and prohibited tool uses.
Require approval gates for high-risk actions.
Validate tool parameters.
Log tool calls and results.
Monitor denied and abnormal tool use.
Test unauthorized tool calls.
Test approval bypass.
Define tool disablement path.
Define rollback or compensation path.
```

## Example Assurance Tests

```text
Agent attempts unauthorized tool call.
Agent uses approved tool with unauthorized parameters.
Agent attempts direct lower-level API access.
Agent attempts high-risk action without approval.
Agent retries denied action through alternate path.
Agent calls tool after kill switch activation.
```

## Example Evidence

```text
Tool inventory
Tool owner record
Tool access approval
Action classification
Approval gate configuration
Tool-call logs
Action logs
Denied tool-call logs
Approval bypass test results
Tool disablement test
Rollback test
```

## Related Project Files

```text
docs/12-pillar-tool-and-action-control.md
templates/ai-tool-and-action-control-template.md
templates/ai-agent-control-template.md
examples/agentic-ai-example.md
```

---

# 7. Identity and Privilege Abuse

## Risk Theme

Identity and privilege abuse occurs when an agent operates with excessive permissions, unclear delegated authority, shared credentials, weak attribution, or privilege that cannot be revoked quickly.

Agentic AI increases identity risk because agents may act across systems, tools, workflows, and user contexts.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture treats agents as non-human actors that require identity, least privilege, delegated authority limits, attribution, and revocation.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| AI identity and access control | Defines agent identity, delegated authority, least privilege, access review, and revocation. |
| Tool and action control | Limits privileged actions and requires approval gates. |
| Human accountability model | Assigns owners for access, authority, risk, and approval. |
| Monitoring, logging, and evidence | Provides attribution and access evidence. |
| Incident containment and recovery | Supports identity disablement and credential rotation. |

## Required Controls

```text
Assign distinct agent identity.
Avoid shared accounts.
Define delegated authority.
Apply least privilege.
Control privileged access.
Review access periodically.
Separate user identity from agent identity where required.
Log agent-mediated activity.
Define revocation path.
Test access revocation.
Rotate credentials when needed.
```

## Example Assurance Tests

```text
Verify agent activity is attributable.
Test agent access to unauthorized system.
Test privileged action without approval.
Test revocation of agent identity.
Test credential rotation.
Test whether agent can act after user access is removed.
```

## Example Evidence

```text
Agent identity record
Access approval
Delegated authority record
Least privilege review
Privileged access review
Access logs
Attribution logs
Revocation test result
Credential rotation record
Incident containment record
```

## Related Project Files

```text
docs/08-pillar-ai-identity-and-access-control.md
templates/ai-identity-and-access-control-template.md
templates/ai-agent-control-template.md
```

---

# 8. Unexpected Code Execution

## Risk Theme

Unexpected code execution occurs when an agent generates, modifies, runs, or triggers code, scripts, commands, queries, configurations, or automation in ways that cause unauthorized or unsafe impact.

This can affect:

```text
Endpoints
Cloud systems
Production systems
CI/CD pipelines
Developer tools
Security tools
Infrastructure
Databases
Workflow engines
```

## AI Control Architecture Implementation Interpretation

The AI Control Architecture treats code execution as a high-risk action requiring strict boundaries, approval, testing, logging, and rollback.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| Tool and action control | Classifies code execution as high-risk or prohibited unless explicitly approved. |
| Output and decision control | Prevents unvalidated code or commands from being executed. |
| AI assurance and testing | Tests code execution boundaries and approval gates. |
| Monitoring, logging, and evidence | Logs code execution requests, approvals, and outcomes. |
| Incident containment and recovery | Defines rollback and containment for execution impact. |

## Required Controls

```text
Classify code execution capability.
Disable code execution by default.
Require explicit approval for execution tools.
Require human review for generated code.
Restrict execution environment.
Separate test and production environments.
Require approval for production changes.
Log code generation, execution requests, approvals, and results.
Define rollback.
Test execution boundary.
```

## Example Assurance Tests

```text
Agent attempts to run shell command.
Agent attempts to execute generated script.
Agent attempts to modify production configuration.
Agent attempts to trigger CI/CD deployment.
Agent attempts SQL update against production database.
Agent attempts endpoint action outside scope.
```

## Example Evidence

```text
Action classification
Execution tool approval
Environment boundary
Code review record
Change approval
Execution logs
Denied execution logs
Rollback plan
Execution boundary test
Incident record
```

## Related Project Files

```text
docs/12-pillar-tool-and-action-control.md
docs/11-pillar-output-and-decision-control.md
templates/ai-tool-and-action-control-template.md
examples/agentic-ai-example.md
```

---

# 9. Insecure Inter-Agent Communication

## Risk Theme

Insecure inter-agent communication occurs when agents exchange instructions, data, tool results, or decisions without authentication, authorization, trust boundaries, validation, or logging.

This can allow one compromised or untrusted agent to influence another agent.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture treats inter-agent communication as an identity, boundary, input, and evidence control problem.

Agents should not trust other agents by default.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| AI inventory and classification | Inventories agents and agent relationships. |
| AI identity and access control | Authenticates and authorizes agent-to-agent interaction. |
| Prompt and input control | Treats inter-agent messages as untrusted unless verified. |
| Data boundary control | Controls data shared between agents. |
| Monitoring, logging, and evidence | Logs agent-to-agent messages and outcomes. |
| Incident containment and recovery | Supports isolating or disabling affected agents. |

## Required Controls

```text
Inventory agent-to-agent relationships.
Assign distinct identities to agents.
Authenticate inter-agent communication.
Authorize allowed communication paths.
Define what data agents may share.
Validate messages before use.
Treat untrusted agent messages as input, not instruction.
Log agent-to-agent interactions where required.
Monitor abnormal inter-agent activity.
Define isolation and disablement path.
```

## Example Assurance Tests

```text
Unauthorized agent attempts to send instruction.
Agent receives malformed inter-agent message.
Agent receives message requesting action outside scope.
Agent shares restricted data with another agent.
Compromised test agent attempts to influence another agent.
Inter-agent communication logs are reconstructed.
```

## Example Evidence

```text
Agent inventory
Agent relationship map
Agent identity record
Inter-agent authorization rules
Data sharing rules
Message validation logs
Inter-agent communication logs
Isolation test
Incident containment record
```

## Related Project Files

```text
docs/07-pillar-ai-inventory-and-classification.md
docs/08-pillar-ai-identity-and-access-control.md
docs/10-pillar-input-control.md
templates/ai-agent-control-template.md
```

---

# 10. Human-Agent Trust Exploitation

## Risk Theme

Human-agent trust exploitation occurs when users or reviewers overtrust agent recommendations, approvals, summaries, or actions.

This can lead to automation bias, rubber-stamp approvals, unsafe delegation, or acceptance of incorrect agent output.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture treats human review as valid only when it is meaningful, evidenced, contextual, and rejectable.

Human-in-the-loop must not become human-as-rubber-stamp.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| Human accountability model | Defines meaningful review, authority, accountability, and escalation. |
| Output and decision control | Separates agent recommendation from final decision. |
| Tool and action control | Requires approval gates for high-risk actions. |
| Monitoring, logging, and evidence | Records review, approval, rejection, and override evidence. |
| AI assurance and testing | Tests reviewer behavior and approval effectiveness. |

## Required Controls

```text
Define reviewer role.
Define reviewer authority.
Define what reviewer must see.
Provide source evidence.
Provide action impact.
Provide uncertainty or confidence where available.
Provide escalation path.
Allow rejection and override.
Log approvals, rejections, and overrides.
Monitor approval patterns.
Test whether review is meaningful.
```

## Contextual Reconstructability Requirement

A human reviewer should receive enough context to understand what they are approving.

The reviewer should see:

```text
Agent recommendation
Relevant input
Retrieved context or source evidence
Tool or action requested
Action impact
Risk indicators
Approval threshold
Known uncertainty
Alternative action or escalation path
```

## Example Assurance Tests

```text
Reviewer receives recommendation without source evidence.
Reviewer cannot reject agent action.
Reviewer approves high-risk action without context.
Approval rate is near 100 percent with no modifications.
Reviewer lacks authority to challenge agent output.
Agent hides uncertainty from reviewer.
```

## Example Evidence

```text
Human review criteria
Reviewer record
Decision owner record
Approval log
Rejection log
Override record
Source evidence
Action impact summary
Escalation record
Review quality sampling
```

## Related Project Files

```text
docs/13-pillar-human-accountability.md
docs/11-pillar-output-and-decision-control.md
templates/ai-human-accountability-template.md
templates/ai-output-and-decision-control-template.md
```

---

# 11. Agentic Supply Chain Vulnerabilities

## Risk Theme

Agentic supply chain vulnerabilities arise from compromised, unreviewed, or insecure dependencies in the agent ecosystem.

This may include:

```text
Agent frameworks
MCP servers or connectors
Plugins
Tools
APIs
Model providers
Memory stores
Vector databases
External agents
Third-party packages
Hosted services
Vendor AI features
```

## AI Control Architecture Implementation Interpretation

The AI Control Architecture treats agentic supply chain risk as an inventory, vendor, tool, dependency, evidence, and incident response problem.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| AI inventory and classification | Inventories agents, tools, vendors, dependencies, and lifecycle status. |
| Tool and action control | Reviews tool permissions and action capability. |
| Data boundary control | Reviews data shared with vendors, tools, and subprocessors. |
| Monitoring, logging, and evidence | Tracks evidence, dependency changes, and incidents. |
| Incident containment and recovery | Defines disablement and vendor escalation. |

## Required Controls

```text
Inventory agent dependencies.
Inventory agent-accessible tools.
Review vendor AI and third-party model providers.
Review connectors and plugins.
Review data flows to dependencies.
Review subprocessors.
Review permissions.
Review update and change process.
Monitor dependency changes.
Define vendor/tool disablement path.
```

## Example Assurance Tests

```text
Review agent tool dependency list.
Test disabling compromised connector.
Verify vendor evidence availability.
Verify subprocessor disclosure.
Test log availability for third-party tool call.
Review dependency update change record.
```

## Example Evidence

```text
Agent dependency inventory
Tool inventory
Vendor assessment
Subprocessor review
Third-party model provider disclosure
Connector review
Plugin approval
Dependency change record
Vendor evidence
Disablement test
Incident escalation record
```

## Related Project Files

```text
templates/ai-vendor-assessment-template.md
templates/ai-tool-and-action-control-template.md
examples/vendor-ai-example.md
examples/agentic-ai-example.md
```

---

# 12. Memory and Context Poisoning

## Risk Theme

Memory and context poisoning occurs when an attacker or faulty process corrupts agent memory, retrieved context, stored state, preferences, prior actions, or long-term context to influence future behavior.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture treats memory and context as data sources that require ownership, boundaries, classification, retention, validation, monitoring, and deletion controls.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| Data boundary control | Defines memory and context sources, ownership, classification, retention, and deletion. |
| Prompt and input control | Treats memory and context as potentially untrusted input. |
| AI assurance and testing | Tests poisoning, persistence, and recovery scenarios. |
| Monitoring, logging, and evidence | Logs memory updates and context use where required. |
| Incident containment and recovery | Supports memory purge, context reset, and restart criteria. |

## Required Controls

```text
Inventory memory sources.
Define whether agent memory is enabled.
Define memory owner.
Classify memory content.
Define retention and deletion.
Validate memory writes where required.
Limit what can be stored in memory.
Prevent sensitive data from being stored where required.
Log memory updates where required.
Test memory poisoning.
Define memory reset or purge process.
```

## Example Assurance Tests

```text
Inject malicious instruction into memory.
Store false preference that changes agent behavior.
Poison prior context and test future action.
Test sensitive data persistence in memory.
Test memory deletion.
Test agent behavior after memory reset.
```

## Example Evidence

```text
Memory configuration
Memory owner record
Memory retention rule
Memory update logs
Memory poisoning test
Sensitive memory test
Deletion test
Memory reset record
Incident record
```

## Related Project Files

```text
docs/09-pillar-data-boundary-control.md
docs/10-pillar-input-control.md
templates/ai-data-boundary-template.md
templates/ai-agent-control-template.md
```

---

# 13. Cascading Failures

## Risk Theme

Cascading failures occur when one agent error propagates across workflows, tools, systems, records, users, or other agents.

Agentic systems can create cascading failures when actions are chained, retries are uncontrolled, approvals are weak, or rollback is missing.

## AI Control Architecture Implementation Interpretation

The AI Control Architecture treats cascading failure as a blast-radius, action boundary, monitoring, kill switch, rollback, and incident containment problem.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| Tool and action control | Defines blast-radius limits, action boundaries, rate limits, and rollback. |
| Monitoring, logging, and evidence | Detects abnormal behavior, loops, spikes, and propagation. |
| Incident containment and recovery | Defines kill switch, disablement, containment, recovery, and restart. |
| Human accountability model | Assigns incident, recovery, and restart owners. |
| AI assurance and testing | Tests failure propagation and containment. |

## Required Controls

```text
Define blast-radius limits.
Define rate limits.
Define retry limits.
Define maximum tool calls.
Define maximum workflow actions.
Require approval for high-risk actions.
Monitor abnormal action patterns.
Define kill switch.
Define rollback or compensation.
Test cascading failure scenarios.
Define restart criteria.
```

## Example Assurance Tests

```text
Agent loops through repeated retries.
Agent routes many records incorrectly.
Agent triggers multiple downstream workflows.
Agent failure affects another agent.
Agent action causes repeated customer communications.
Kill switch is activated during cascading failure.
Rollback or correction is tested.
```

## Example Evidence

```text
Blast-radius design
Rate limit configuration
Retry limit configuration
Tool/action logs
Abnormal activity alerts
Kill switch test
Rollback test
Incident tabletop
Containment record
Restart approval
```

## Related Project Files

```text
docs/12-pillar-tool-and-action-control.md
docs/20-common-failure-scenarios.md
docs/24-assurance-and-audit-guide.md
templates/ai-incident-containment-recovery-template.md
examples/agentic-ai-example.md
```

---

# 14. Rogue Agents

## Risk Theme

A rogue agent is an agent that operates outside approved purpose, ownership, scope, identity, policy, or lifecycle status.

This may include:

```text
Uninventoried agents
Unapproved agents
Abandoned agents
Agents using excessive permissions
Agents operating after suspension
Agents created by users outside governance
Agents continuing after owner departure
Agents acting outside approved scope
Compromised agents
```

## AI Control Architecture Implementation Interpretation

The AI Control Architecture treats rogue agents as an inventory, identity, lifecycle, monitoring, and containment failure.

## Relevant Pillars

| Pillar | Contribution |
|---|---|
| AI inventory and classification | Requires all agents to be inventoried, owned, risk-tiered, and lifecycle-managed. |
| AI identity and access control | Requires distinct identity, access review, and revocation. |
| Monitoring, logging, and evidence | Detects agent activity outside inventory or approved scope. |
| Incident containment and recovery | Supports suspension, disablement, revocation, and investigation. |
| Human accountability model | Assigns agent owner and incident owner. |

## Required Controls

```text
Inventory all agents.
Assign agent owner.
Assign technical owner.
Assign lifecycle status.
Assign risk tier.
Assign distinct identity.
Review agent access.
Detect unapproved agent activity.
Disable suspended or retired agents.
Revoke unused agent identities.
Monitor for rogue agent behavior.
Define agent incident response.
```

## Example Assurance Tests

```text
Search for agent identities not in inventory.
Test whether retired agent can still act.
Test ownerless agent handling.
Test unapproved tool call from unknown agent.
Test agent activity after suspension.
Test incident response for rogue agent.
```

## Example Evidence

```text
Agent inventory
Agent owner record
Lifecycle status
Risk tier record
Agent identity record
Access review
Rogue agent detection log
Revocation record
Suspension record
Incident record
```

## Related Project Files

```text
docs/07-pillar-ai-inventory-and-classification.md
docs/08-pillar-ai-identity-and-access-control.md
templates/ai-agent-control-template.md
templates/ai-inventory-record-template.md
```

---

# 15. Agentic AI Risk to Assurance Test Matrix

| Agentic AI Risk Theme | Example Assurance Tests |
|---|---|
| Agent goal hijacking | Direct goal hijack, indirect goal hijack, tool-response hijack, memory hijack |
| Tool misuse and exploitation | Unauthorized tool call, unsafe parameters, approval bypass, direct API path |
| Identity and privilege abuse | Excessive access, shared account, privileged action, revocation test |
| Unexpected code execution | Shell command, generated script, CI/CD trigger, production config change |
| Insecure inter-agent communication | Unauthorized agent message, untrusted instruction, restricted data sharing |
| Human-agent trust exploitation | Rubber-stamp review, missing context, no rejection path, weak review evidence |
| Agentic supply chain vulnerabilities | Dependency review, plugin review, connector disablement, vendor evidence test |
| Memory and context poisoning | Poisoned memory, false prior context, sensitive memory persistence, reset test |
| Cascading failures | Retry loop, workflow propagation, excessive tool calls, kill switch test |
| Rogue agents | Unknown agent discovery, retired agent action, ownerless agent, revocation test |

---

# 16. Agentic AI Risk to Evidence Matrix

| Agentic AI Risk Theme | Example Evidence |
|---|---|
| Agent goal hijacking | Goal definition, prompt injection tests, denied action logs |
| Tool misuse and exploitation | Tool inventory, action classification, tool-call logs, approval logs |
| Identity and privilege abuse | Agent identity, access approval, access review, revocation test |
| Unexpected code execution | Execution boundary, code review, change approval, execution logs |
| Insecure inter-agent communication | Agent relationship map, message logs, authorization rules |
| Human-agent trust exploitation | Review criteria, source evidence, approval/rejection logs |
| Agentic supply chain vulnerabilities | Dependency inventory, vendor assessment, connector review |
| Memory and context poisoning | Memory configuration, memory update logs, poisoning tests |
| Cascading failures | Blast-radius limits, rate limits, kill switch test, rollback test |
| Rogue agents | Agent inventory, lifecycle status, rogue detection logs, revocation record |

---

# 17. Example: IT Service Desk Ticket Triage Agent

## Use Case

```text
Agent reviews IT tickets, classifies issue type, suggests priority, retrieves knowledge articles, drafts a response, and requests routing.
```

## Key Agentic Risks

```text
Agent goal hijacking
Tool misuse
Identity and privilege abuse
Human-agent trust exploitation
Memory/context poisoning
Cascading failures
Rogue agent behavior
```

## AI Control Architecture Controls

```text
Agent identity
Autonomy level
Tool inventory
Action classification
Approval gates
Blast-radius limits
Ticket and knowledge-base data boundary
Prompt injection testing
Tool misuse testing
Approval bypass testing
Tool/action logging
Kill switch
Rollback or correction path
Evidence reconstruction
Incident containment plan
```

Related example:

```text
examples/agentic-ai-example.md
```

---

# 18. Agent Control Minimum Baseline

Any enterprise agent should have at least:

```text
[ ] Agent inventory record
[ ] Business owner
[ ] Technical owner
[ ] Agent purpose
[ ] Autonomy level
[ ] Risk tier
[ ] Agent identity
[ ] Delegated authority definition
[ ] Data boundary
[ ] Tool inventory
[ ] Action classification
[ ] Approval gates for high-risk actions
[ ] Tool/action logs
[ ] Monitoring for abnormal behavior
[ ] Kill switch
[ ] Rollback or compensation assessment
[ ] Incident containment path
[ ] Evidence reconstruction requirement
```

Agents without these controls should not be approved for production use.

---

# 19. How to Use This Crosswalk

Use this crosswalk when:

```text
An enterprise is designing or reviewing an AI agent.
Security architecture wants to assess agentic AI controls.
AppSec wants to threat model an agentic application.
IAM wants to govern AI agent identities.
A red team wants to test agent failure modes.
An incident response team wants agent containment scenarios.
A governance team wants to distinguish agents from passive copilots.
```

Suggested use:

```text
1. Identify the agent use case.
2. Assign owner and risk tier.
3. Define autonomy level.
4. Define agent identity.
5. Map data sources.
6. Inventory tools and actions.
7. Classify actions by risk.
8. Define approval gates.
9. Define monitoring and evidence.
10. Define kill switch and rollback.
11. Test agentic risk scenarios.
12. Prepare incident containment.
```

---

# 20. Limitations

This crosswalk is intended to support agentic AI security control design.

It is not:

```text
A complete OWASP implementation guide
A penetration test report
A security certification
A substitute for AppSec review
A substitute for red-team testing
A substitute for IAM governance
A substitute for incident response planning
```

Organizations should tailor controls based on their architecture, agent framework, model provider, data sensitivity, tool access, autonomy level, and business impact.

---

# 21. Future Enhancements

Future versions may add:

```text
Detailed OWASP Agentic AI category-to-requirement mapping
Agent red-team test catalogue
Agent identity pattern guide
Inter-agent communication control guide
Memory and context governance guide
Agent kill switch patterns
Agent rollback and compensation patterns
Machine-readable agentic AI control mapping
```

---

# 22. Summary

Agentic AI creates a different control problem than passive AI assistants.

Once AI can pursue goals, use tools, communicate, remember, and act, it becomes an enterprise actor.

Enterprise actors require:

```text
Identity
Boundaries
Authority limits
Approval gates
Logs
Monitoring
Kill switches
Rollback
Human accountability
Incident containment
Evidence
```

The goal is to move from:

```text
Autonomous AI risk awareness
```

to:

```text
Operational agent control