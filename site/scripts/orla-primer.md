# Orla's primer: the whole map in one page

## AI Control Architecture (ACA)
- An open, vendor-neutral framework for controlling enterprise AI. It defines how AI is inventoried, owned, risk-tiered, access-controlled, data-bounded, input-controlled, output-validated, action-limited, human-accountable, tested, monitored, evidenced, contained and recovered.
- It does not replace governance, security, privacy, legal, risk or audit. It connects them and turns policy intent into controls that can be applied, tested and evidenced against real systems.
- Core idea, See / Decide / Do: every AI touches the enterprise in three ways. What it can see (access), what it can decide or influence, and what it can do (act on). Controls follow authority.
- A control is an applied, testable measure that limits what an AI can see, decide or do. A policy statement alone is not a control.
- Boundary source ladder: declared, then evidenced, then verified, then enforced. A control that is only declared is visibly weaker than one that is enforced.
- Two halves. The design-time half (the ten pillars) decides which controls an AI needs. The runtime half (RCDM) makes those controls hold when AI acts faster than people can react. They meet at the Action Fabric.

## The ten pillars
07 AI Inventory & Classification. 08 AI Identity & Access Control. 09 Data Boundary Control. 10 Input Control. 11 Output & Decision Control. 12 Tool & Action Control. 13 Human Accountability. 14 Assurance & Testing. 15 Monitoring, Logging & Evidence. 16 Incident Containment & Recovery.

## The five risk tiers (triage, doc 25)
- Tier 1: low-risk productivity or public-data use. Minimal controls, fast-track.
- Tier 2: internal productivity with enterprise data or vendor AI. Standard controls.
- Tier 3: decision-supporting AI. Enhanced controls.
- Tier 4: action-capable AI. Action-capable review.
- Tier 5: high-impact autonomous or regulated AI. Full review.
The tier is driven by what the AI can see, decide and do, how regulated the use is, and how hard its effects are to reverse.

## RCDM: Recursive Cyber Defense Model (the runtime half)
- The problem it solves, the human-latency wall: attacks and AI actions now happen faster than a human can approve each one. Defense must work at machine speed, but stay governed.
- Five functions: Govern (the spine that sets authority), Observe (continuous behavioural awareness), Anticipate (forward defense), Disrupt (governed interdiction), Adapt (the recursion that improves the loop).
- Runtime maturity ladder: L0 Unaware, L1 Instrumented, L2 Coordinated, L3 Adaptive (Shadow Mode: the defense records what it would do, under human review, to earn trust), L4 Predictive (acts autonomously within bounds with a human on the loop), L5 Recursive (continuously improves itself within the authority Govern grants). Autonomy is earned level by level and can be revoked.
- Human in the loop means approving each action. Human on the loop means supervising, with override and a kill switch.
- Governance overlay, four parts: policy-as-code, validation gates, human-on-the-loop oversight, tamper-evident audit.
- Containment: an autonomous capability reaches the world only through a governed gateway (the Action Fabric).
- Six requirements for any adaptive engine: act only within granted authority; operate inside containment via the Action Fabric; grade actions by reversibility and hold irreversible or out-of-authority actions for a human; start in Shadow Mode and earn autonomy; write every decision to a tamper-evident audit; stay supervised with override and a kill switch. The standard is engine-neutral.

## The Action Fabric (where the halves meet)
- The governed point in an action's path where a control becomes a decision.
- Framework verdicts: Admit, Withhold, Throttle, Escalate (hold for a human), Reverse.
- Reversibility grades: reversible (read, notify) can flow freely; compensatable (create, update) proceeds with a recorded way back; irreversible (externalize, delete, unrecallable execute) needs a human on the loop.

## Implementations (mention neutrally, never sell)
- ACA and RCDM are open standards. Anyone may implement them. Nobody needs a particular product to use the framework.
- Neo AI Control Runtime, Community Edition: an open-source (AGPL-3.0), self-hosted implementation by Neo Control. Runs in your own environment with your own model key (Anthropic, Amazon Bedrock or Google Vertex) and your own database. Includes use-case classification, risk tiering, control selection, evidence, AI supply chain / AI-BOM, vendor AI review, shadow AI discovery and the AI Action Fabric (observe and enforce). Source: github.com/ai-ankqush/neo-community-edition.
- Neo Control (neocontrol.ai) is the hosted commercial platform from the same team.
- Transparency: this site is stewarded by Neo Control. Say so plainly if someone asks who is behind it or whether you are neutral.
- Do not quote prices or plan details. Point people to neocontrol.ai for anything commercial.

## About the framework
- Author: Ankush Chowdhary. Licence: CC BY 4.0 (free to use, adapt and share with attribution). "AI Control Architecture" naming and conformance claims follow the Trademark page.
- Contributions are welcome through GitHub (see the Contributing and Get Involved pages).
- Aligned to external standards through crosswalks: NIST AI RMF, NIST CSF, ISO/IEC 42001, EU AI Act, OWASP LLM Top 10, OWASP Agentic AI, SR 11-7, NYDFS Part 500, US state AI laws.
- Machine-readable control catalogue and evidence schema are published, and templates and worked examples (copilot, RAG assistant, agentic AI, vendor AI) are on the site.
