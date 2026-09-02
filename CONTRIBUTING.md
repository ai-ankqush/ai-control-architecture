# Contributing

The AI Control Architecture is open and openly licensed. It aims, over time, to become a shared standard for AI control; for now it is an openly developed body of work anyone can adopt. It improves fastest when the people using it, security architects, risk and audit teams, privacy teams, and builders, feed back what works and what is missing. Contributions are welcome.

---

## What belongs here

This repository holds the AI Control Architecture and its supporting assets:

```text
docs/       the architecture: foundation, the ten pillars, operating model, glossary
mappings/   crosswalks to external standards and regulations
templates/  reusable intake, tiering, control, assurance, evidence, incident templates
examples/   worked use-case examples
```

Good contributions include: corrections and clarifications; new or improved standards crosswalks; additional templates and worked examples; sharper requirements; and better explanations of existing controls.

## What does not belong here

The AI Control Architecture is deliberately separate from any one implementation of it. Please do not contribute:

- product-specific, vendor-specific, or tool-specific instructions;
- assessment scoring logic, risk-tiering thresholds, control-selection rules, or pricing, these are operational choices each adopter or vendor makes;
- anything that presumes a particular commercial offering.

The AI Control Architecture says *what* good AI control looks like and *how to evidence it*. It stays neutral on *whose product* you use to get there.

---

## How to propose a change

- For small fixes (typos, broken links, clarifications), open a pull request directly.
- For anything that changes a requirement, a pillar's scope, or the requirement identifiers, open an issue first so the change can be discussed before the work.
- Keep pull requests focused on one thing. Explain the *why*, not just the *what*.
- Run the link checker before submitting: `python3 scripts/check-links.py`. It must report OK.

### Style

The docs follow a deliberately plain house style. Match it:

- short, declarative lines; prose over decoration;
- fenced ` ```text ` blocks for structured lists and diagrams;
- ASCII box-drawing for diagrams, not images, where practical;
- no em-dashes (use commas, colons, or separate sentences);
- every doc ends with a `**Next:**` pointer and the version/licence footer line.

### Requirements

Requirements are normative and identified as `ACA-<pillar>-<n>`. Identifiers are stable: do not renumber or reuse a retired ID. To add a requirement, use the next free number in that pillar. To retire one, mark it rather than deleting the number.

---

## Licensing of contributions

By contributing, you agree that your contribution is licensed under [CC BY 4.0](LICENSE.md), the same licence as the rest of the architecture, and that you have the right to contribute it. You retain copyright in your contribution; you grant everyone the rights CC BY 4.0 provides. Contributions do not grant any rights in the project name or conformance marks (see [TRADEMARK.md](TRADEMARK.md)).

---

## Stewardship and governance

The AI Control Architecture is stewarded by Neo Control (neocontrol.ai). Stewardship means keeping it coherent, versioned, and moving: reviewing contributions, arbitrating changes to requirements and structure, and maintaining the crosswalks. It does not mean owning the text, that is open under CC BY 4.0.

- **Versioning** follows semantic versioning, tracked in `VERSION.md`. Editorial fixes are patch releases; new requirements or templates are minor releases; changes that alter the meaning of existing requirements or the pillar structure are major releases and are announced.
- **Decisions** on requirements and structure rest with the stewards, informed by issues and discussion. The bias is toward neutrality, evidence, and keeping the AI Control Architecture usable across vendors and sectors.
- **Neutrality** is a design goal. The AI Control Architecture must remain something a competitor of Neo Control can adopt in good conscience.

Questions about stewardship, conformance, or use of the name: neocontrol.ai.

---

*Version 0.1.0 · Architecture licensed under [CC BY 4.0](LICENSE.md) · Stewarded by Neo Control · neocontrol.ai*
