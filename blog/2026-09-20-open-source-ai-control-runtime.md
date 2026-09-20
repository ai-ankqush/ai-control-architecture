---
date: 2026-09-20
author: Ankush Chowdhary
category: [announcement]
tags: [open-source, action-fabric, agpl, runtime]
meta:
  title: "Neo's AI Control Runtime is now open source"
  description: "The control plane for AI authority is now yours to run. The core Neo AI Control Runtime, including the AI Action Fabric, is released under AGPL-3.0."
---

# Neo's AI Control Runtime is now open source

*The control plane for AI authority is now yours to run.*

Today we are releasing the core Neo AI Control Runtime under the AGPL-3.0 licence.

This is not a demo, a client library or a limited community edition. It is the production engine that classifies AI use cases, assigns risk tiers, selects controls, governs agent actions and produces evidence.

Clone it. Inspect it. Run it in your environment using your own model key and database.

Your infrastructure. Your data. Your usage. Your control.

An AI Control Runtime is not where you build agents. It is the layer that controls them. It sits between agents and the systems they can affect, deciding what each agent is allowed to see, decide and do when it attempts an action.

That is what we have opened.

## AI Action Fabric

The AI Action Fabric is the heart of the runtime.

Traditional access control authorises an actor. An agent receives permissions when it is deployed and carries that authority into every subsequent interaction. That works for software performing one predictable function. It breaks down when an agent chains tools, changes systems and decides its next step based on information nobody anticipated.

The Action Fabric extends Zero Trust from identities to actions. No standing agent authority. Every consequential action becomes a fresh delegation. Each request is evaluated at the moment of action against:

- The intended outcome
- The data and systems involved
- The scope of the requested authority
- The potential blast radius
- Whether the action can be reversed

A read-only retrieval and a financial reconciliation trigger from the same agent can therefore receive different decisions. Identity alone cannot make that distinction. The decision must happen inside the execution path.

### Delegation

Every requested action receives a new verdict:

- Granted
- Granted with conditions
- Held for human approval
- Blocked

The decision records its rationale, scope, blast radius and recovery path. The agent never receives permanent authority simply because it was trusted at deployment.

### Observe

The Action Fabric is shadow-first. Run it in Observe mode and it evaluates every action without changing the outcome. This shows you what agents are actually doing and identifies the small number of actions carrying meaningful consequence.

Observe first. Learn the pattern. Enforce only where it matters. The Fabric begins as a checkpoint, not a wall.

### Recovery

Controlling AI is not only about saying no. It is about being able to undo a yes.

Every governed action receives a reversibility grade:

- **Reversible:** the original action can be undone.
- **Compensatable:** a separate action can neutralise the effect.
- **Irreversible:** the consequence cannot reliably be recovered.

Reversible actions have their undo path armed. Compensatable actions carry a defined recovery step. Irreversible actions are clearly identified and are never automatically approved. The recovery ledger records the action, its consequence and the available way back.

Reversibility changes the economics of enforcement. Teams are more willing to activate controls when they know an incorrect decision can be recovered.

### Enforcement

Blocking is deliberate and opt-in. An integration moves from observation to enforcement only after its behaviour has been understood and the relevant controls have been tested. A kill switch can return all governed integrations to Observe mode immediately, without rewriting individual policies.

Autonomy is earned, and it remains revocable.

## AI Supply Chain

Organisations map their software dependencies. Very few map the authority embedded in their AI dependencies.

An AI system may depend on:

- A model provider
- A vendor that fine-tuned the model
- Retrieved enterprise data
- MCP servers and plugins
- External tools and APIs
- Other agents with their own permissions

The runtime builds an AI dependency and authority graph showing what every AI system relies on, what each dependency can reach and how far a compromised component could propagate.

Underneath the graph sits an AI Bill of Materials, or AI-BOM. It gives organisations a defensible answer when an auditor, customer or regulator asks: what AI are you actually running, and what authority does it carry?

## AI Vendor Risk

The runtime includes a structured assessment for evaluating AI products before they begin making decisions in production.

It examines:

- What the product does
- What information it can access
- What decisions it influences
- What actions it can perform
- How it could fail
- Which controls must hold

"The vendor says it is safe" becomes a claim that can be examined, evidenced and tested.

## Shadow AI

The AI you know about is not the only AI you need to govern.

Shadow AI often first appears through financial evidence: corporate cards, expense claims, procurement records and invoices for tools that never passed through security review. Spend is difficult to hide.

The runtime uses those signals to identify potential undeclared AI use and convert each finding into a governed use case. The goal is not to flag and shame employees. It is to bring useful experimentation inside a visible and proportionate control boundary.

## AI Red Team

Generic AI red teaming produces generic findings. Neo's Red Team uses the actual authority graph of the system being tested.

It instantiates known attack patterns, follows the path through real data and tools, and marks an attack step as blocked only when a verified control stops it. A control that has been documented but not proven does not count.

You can watch the attack advance through the system and see exactly where the architecture contains it, or where the path remains open.

## The assessment core

Underneath every module is the assessment engine that started Neo. It:

1. Classifies the AI use case.
2. Assigns the appropriate risk tier.
3. Selects the applicable controls.
4. Defines the required evidence and tests.
5. Produces the decision record and assurance report.

The controls are crosswalked to the frameworks organisations already need to address:

- NIST AI Risk Management Framework
- ISO/IEC 42001
- EU AI Act
- OWASP LLM and Agentic guidance
- Federal Reserve SR 11-7
- NYDFS Part 500

The runtime also includes the estate map, control graph and a library of pre-mapped use cases. You do not begin every assessment with a blank page, and you do not invent a private compliance standard.

## What remains managed

Two capabilities remain managed by Neo.

**The trained adversary model.** Anticipate uses a trained adversary model to examine a digital twin of the customer environment and identify how emerging attacks could traverse it. Customers receive and can act on its complete output. The model weights are not distributed.

The model remains useful because it learns from attack signals pooled across multiple environments. A single isolated deployment could not safely reproduce that learning, and publishing the weights would reveal the exact model being used to anticipate attacks. Self-hosted deployments include the open attack-pattern radar. They can optionally call the managed adversary model when they need the learned analysis.

**The trust layer.** Neo also retains the managed trust layer:

- Independent assurance
- Certification
- Cross-estate intelligence
- Continuous managed operation
- Enterprise support and accountability

The distinction is intentional. The engine is yours. The independent assurance and operational backstop are ours.

## Deploy it

1. Clone the repository.
2. Add your own Anthropic, Amazon Bedrock or Google Vertex AI credentials.
3. Connect a PostgreSQL database (a Supabase project is the quickest path) and apply the schema.
4. Install, build and run.

Your model usage is billed directly to your own account. There is no Neo-controlled model key and no requirement to route your operational data through our platform.

Self-host it. Inspect it. Fork it. Extend it. The core runtime is licensed under AGPL-3.0.

Repository and quickstart: [github.com/ai-ankqush/neo-community-edition](https://github.com/ai-ankqush/neo-community-edition)

We will follow this announcement with a separate piece explaining why we opened the runtime and where the genuinely difficult work in an AI security program has moved.

For now, the important point is simpler: the architecture is open. The runtime is open. The AI control plane can now belong to you.
