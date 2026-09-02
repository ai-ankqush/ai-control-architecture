---
date: 2026-09-02
author: Ankush Chowdhary
category: [announcements]
tags: [launch, open-source]
meta:
  title: "We are opening the AI Control Architecture"
  description: "An openly licensed foundation for governing, securing, testing and monitoring enterprise AI, free to read, run, integrate and extend."
---

# We are opening the AI Control Architecture

*An openly licensed foundation for governing, securing, testing and monitoring enterprise AI, free to read, run, integrate and extend.*

Today we are releasing the AI Control Architecture (ACA) as an open, vendor-agnostic foundation that any organisation can use to answer one question about any AI it runs, "is this under control?", and to prove it.

The release is deliberately complete. It is not a whitepaper or a set of principles. It is the architecture itself, a machine-readable control catalogue, crosswalks to the regulations enterprises are actually measured against, an assessment engine, an MCP interface for tools and agents to consume, and a self-hostable Community Edition you can stand up on your own infrastructure. All of it is openly licensed and available now.

## Why we are giving this away

For years the accepted wisdom was that ideas were cheap and execution was everything. AI has changed that equation. A two-person team can now build what looks like a cybersecurity product in weeks, for a few hundred dollars. That is genuinely good news for builders. But it has an uncomfortable implication for buyers: enterprises should not pay enterprise prices for features that are now inexpensive to reproduce.

Look closely at most AI security and governance tools and you find the same components underneath, rebuilt over and over behind a different logo: a control catalogue, a set of connectors, an assessment questionnaire, a regulatory mapping. Every vendor rebuilds this plumbing, charges for it, and asks the customer to trust that their private version is the right one. The customer ends up locked to a small company for foundational capability that could vanish if that company is acquired, pivots or fails.

We think the reusable layer should be open. As the cost of building software falls, real commercial value moves away from easily copied features and toward the hard things: difficult research, trusted operation, continuous assurance, and enforcement at runtime. Those deserve invention. The shared foundation underneath them does not deserve to be reinvented in private a hundred times over.

## What the release actually contains

The architecture describes an AI system in terms of what it can see, what it can decide, and what it can do, and then assigns controls proportionate to that authority. A low-risk copilot and an action-capable agent should not carry the same burden, so controls are graduated across five risk tiers and organised into ten control pillars that span the full lifecycle, from initial classification through implementation, testing, monitoring and containment.

Around that core, the release includes:

A machine-readable control catalogue, so controls are not just prose in a document but structured identifiers that tools, vendors and agents can reference in common.

Crosswalks to the frameworks enterprises are already held to, including the EU AI Act, the NIST AI Risk Management Framework, ISO/IEC 42001, OWASP, SR 11-7 and NYDFS Part 500, so you can map a control once and speak to multiple regulators.

A rules-based assessment engine that turns a described use case into a risk tier, a required control set and an evidence checklist, replacing the subjective questionnaire with something repeatable.

ACA Tools and an MCP interface, so the catalogue and assessment are consumable directly by AI tooling and agents rather than trapped in a PDF.

A Community Edition you can self-host, plus a hosted edition and an AWS Marketplace deployment for teams that would rather not run it themselves.

## For enterprises, developers and vendors

Enterprises can adopt the architecture internally, today, without buying anything. You can assess your own AI use cases against it, produce evidence, and use the crosswalks to show regulators and auditors the same picture.

Developers can build integrations and control modules against the machine-readable interfaces, knowing they are building against a stable, public target rather than one company's private schema.

Security vendors can map their capabilities and their evidence to the same control identifiers, which makes their products easier to compare, combine and trust, and lets customers see exactly where a tool contributes.

Contributors, whom we call Stewards, can extend the architecture with free, open-source or commercial modules on top of the shared foundation. The point is not to eliminate cybersecurity startups. It is to raise the bar for what deserves to become one.

## On the word "standard"

I want to be careful here. I am not declaring ACA an industry standard. Standards are earned through implementation, adoption and challenge, not announced. But convergence requires something concrete to converge around, and that is what we are offering: a foundation open enough to argue with and complete enough to build on.

My ambition is straightforward. I want to build the largest open AI cybersecurity initiative there is, one where enterprises, researchers, engineers and vendors can all build on the same foundation without depending on any single company, including ours.

## A note on stewardship

ACA is vendor-agnostic and openly licensed. It is stewarded by Neo Control as its founding steward, and Neo offers hosted and commercial editions for teams that want a managed deployment. None of that is required. The architecture, the catalogue, the tools and the crosswalks are yours to read, self-host and extend independently, and they are designed to remain available regardless of the future of any single vendor, us included.

The architecture is live now. Read it, run it against a real use case, and tell us where it is wrong. That is how a foundation becomes worth building on.
