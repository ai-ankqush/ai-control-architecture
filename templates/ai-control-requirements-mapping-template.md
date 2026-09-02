# AI Control Requirements Mapping Template

This template is used to map an AI use case to the applicable AI Control Architecture requirements.

The purpose is to create traceability between:

- AI risk tier
- AI control pillars
- control objectives
- functional requirements
- non-functional requirements
- implementation controls
- evidence
- assurance testing
- exceptions
- ownership

This template helps ensure that AI controls are not applied informally or inconsistently.

---

# 1. Mapping Information

## AI Use Case Name

```text
[Enter AI use case name]
```

## Mapping ID

```text
[Enter mapping ID]
```

## Date

```text
[Enter date]
```

## Prepared By

```text
Name:
Function:
Email:
```

## Business Owner

```text
Name:
Function:
Email:
```

## Technical Owner

```text
Name:
Function:
Email:
```

## Related Documents

```text
AI intake record:
Risk assessment:
Control assessment:
Architecture decision record:
Assurance test plan:
Exception records:
```

---

# 2. AI Use Case Summary

## Short Description

```text
[Describe the AI use case]
```

## AI Pattern

Select all that apply:

```text
[ ] Copilot
[ ] Internal LLM application
[ ] RAG system
[ ] AI-enabled SaaS
[ ] Embedded vendor AI
[ ] Agent
[ ] AI-enabled workflow automation
[ ] Customer-facing AI
[ ] Employee-facing AI
[ ] Developer AI tool
[ ] Security operations AI
[ ] Decision-supporting AI
[ ] Action-capable AI
[ ] Other
```

## Assigned Risk Tier

Select one:

```text
[ ] Tier 1: Low-risk productivity or public-data use
[ ] Tier 2: Internal productivity with enterprise data
[ ] Tier 3: Decision-supporting AI
[ ] Tier 4: Action-capable AI
[ ] Tier 5: High-impact autonomous or regulated AI
```

## Highest Risk Drivers

Select all that apply:

```text
[ ] Sensitive data
[ ] Regulated data
[ ] Personal data
[ ] Customer impact
[ ] Employee impact
[ ] Financial impact
[ ] Legal or compliance impact
[ ] Security impact
[ ] Production impact
[ ] Decision influence
[ ] Tool/action capability
[ ] Agentic autonomy
[ ] External exposure
[ ] Vendor dependency
[ ] Low recoverability
[ ] Weak evidence
[ ] Unknown risk
```

---

# 3. Requirement Applicability Summary

| Pillar | Applicable? | Priority | Notes |
|---|---|---|---|
| AI inventory and classification | [Yes/No/Partial] | [Low/Medium/High/Critical] | [Notes] |
| AI identity and access control | [Yes/No/Partial] | [Low/Medium/High/Critical] | [Notes] |
| Data boundary control | [Yes/No/Partial] | [Low/Medium/High/Critical] | [Notes] |
| Prompt and input control | [Yes/No/Partial] | [Low/Medium/High/Critical] | [Notes] |
| Output and decision control | [Yes/No/Partial] | [Low/Medium/High/Critical] | [Notes] |
| Tool and action control | [Yes/No/Partial] | [Low/Medium/High/Critical] | [Notes] |
| Human accountability model | [Yes/No/Partial] | [Low/Medium/High/Critical] | [Notes] |
| AI assurance and testing | [Yes/No/Partial] | [Low/Medium/High/Critical] | [Notes] |
| Monitoring, logging, and evidence | [Yes/No/Partial] | [Low/Medium/High/Critical] | [Notes] |
| Incident containment and recovery | [Yes/No/Partial] | [Low/Medium/High/Critical] | [Notes] |

---

# 4. Pillar 1: AI Inventory and Classification Requirements

## Applicability

```text
[Applicable / Not applicable / Partially applicable]
```

## Requirement Mapping

| Requirement ID | Requirement | Applicable? | Implementation Control | Owner | Evidence | Status |
|---|---|---|---|---|---|---|
| AIC-FR-001 | Maintain an enterprise AI inventory. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| AIC-FR-002 | Register AI use cases. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| AIC-FR-003 | Identify embedded vendor AI. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| AIC-FR-004 | Assign AI ownership. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| AIC-FR-005 | Classify AI risk. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| AIC-FR-006 | Track AI lifecycle status. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| AIC-FR-007 | Map AI to business processes. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| AIC-FR-008 | Detect unmanaged AI. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| AIC-FR-009 | Review AI inventory periodically. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| AIC-FR-010 | Link inventory to control requirements. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |

## Notes

```text
[Document inventory and classification notes, gaps, assumptions, or exceptions]
```

---

# 5. Pillar 2: AI Identity and Access Control Requirements

## Applicability

```text
[Applicable / Not applicable / Partially applicable]
```

## Requirement Mapping

| Requirement ID | Requirement | Applicable? | Implementation Control | Owner | Evidence | Status |
|---|---|---|---|---|---|---|
| AIAC-FR-001 | Identify AI actors. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| AIAC-FR-002 | Define AI identity model. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| AIAC-FR-003 | Define delegated authority. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| AIAC-FR-004 | Enforce least privilege. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| AIAC-FR-005 | Separate AI-mediated activity. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| AIAC-FR-006 | Approve AI access. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| AIAC-FR-007 | Review AI access periodically. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| AIAC-FR-008 | Revoke AI access. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| AIAC-FR-009 | Control privileged AI access. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| AIAC-FR-010 | Maintain AI access evidence. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |

## Notes

```text
[Document identity and access notes, gaps, assumptions, or exceptions]
```

---

# 6. Pillar 3: Data Boundary Control Requirements

## Applicability

```text
[Applicable / Not applicable / Partially applicable]
```

## Requirement Mapping

| Requirement ID | Requirement | Applicable? | Implementation Control | Owner | Evidence | Status |
|---|---|---|---|---|---|---|
| DBC-FR-001 | Map AI data sources. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| DBC-FR-002 | Apply data classification. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| DBC-FR-003 | Enforce retrieval boundaries. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| DBC-FR-004 | Restrict sensitive data exposure. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| DBC-FR-005 | Define training and reuse restrictions. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| DBC-FR-006 | Define retention requirements. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| DBC-FR-007 | Prevent data leakage through outputs. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| DBC-FR-008 | Preserve sensitivity context. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| DBC-FR-009 | Control cross-boundary data movement. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| DBC-FR-010 | Monitor AI data access. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |

## Notes

```text
[Document data boundary notes, gaps, assumptions, or exceptions]
```

---

# 7. Pillar 4: Prompt and Input Control Requirements

## Applicability

```text
[Applicable / Not applicable / Partially applicable]
```

## Requirement Mapping

| Requirement ID | Requirement | Applicable? | Implementation Control | Owner | Evidence | Status |
|---|---|---|---|---|---|---|
| PIC-FR-001 | Define allowed AI inputs. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| PIC-FR-002 | Define prohibited AI inputs. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| PIC-FR-003 | Validate high-risk inputs. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| PIC-FR-004 | Protect system prompts. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| PIC-FR-005 | Manage prompt injection risk. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| PIC-FR-006 | Isolate context. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| PIC-FR-007 | Control external inputs. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| PIC-FR-008 | Log prompts and inputs. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| PIC-FR-009 | Manage prompt changes. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| PIC-FR-010 | Detect input policy violations. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |

## Notes

```text
[Document prompt and input notes, gaps, assumptions, or exceptions]
```

---

# 8. Pillar 5: Output and Decision Control Requirements

## Applicability

```text
[Applicable / Not applicable / Partially applicable]
```

## Requirement Mapping

| Requirement ID | Requirement | Applicable? | Implementation Control | Owner | Evidence | Status |
|---|---|---|---|---|---|---|
| ODC-FR-001 | Classify AI output types. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| ODC-FR-002 | Define validation rules. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| ODC-FR-003 | Separate AI recommendations from decisions. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| ODC-FR-004 | Control downstream use. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| ODC-FR-005 | Capture AI-assisted decision evidence. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| ODC-FR-006 | Define prohibited output uses. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| ODC-FR-007 | Manage output uncertainty. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| ODC-FR-008 | Review customer-facing outputs. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| ODC-FR-009 | Control generated records. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| ODC-FR-010 | Monitor output quality. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |

## Notes

```text
[Document output and decision notes, gaps, assumptions, or exceptions]
```

---

# 9. Pillar 6: Tool and Action Control Requirements

## Applicability

```text
[Applicable / Not applicable / Partially applicable]
```

## Requirement Mapping

| Requirement ID | Requirement | Applicable? | Implementation Control | Owner | Evidence | Status |
|---|---|---|---|---|---|---|
| TAC-FR-001 | Inventory AI-accessible tools. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| TAC-FR-002 | Classify AI actions by risk. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| TAC-FR-003 | Approve tool access. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| TAC-FR-004 | Enforce action boundaries. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| TAC-FR-005 | Require approval for high-risk actions. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| TAC-FR-006 | Limit autonomous execution. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| TAC-FR-007 | Log tool calls and actions. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| TAC-FR-008 | Provide kill switches. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| TAC-FR-009 | Define rollback or compensation. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| TAC-FR-010 | Monitor abnormal tool use. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |

## Notes

```text
[Document tool and action notes, gaps, assumptions, or exceptions]
```

---

# 10. Pillar 7: Human Accountability Model Requirements

## Applicability

```text
[Applicable / Not applicable / Partially applicable]
```

## Requirement Mapping

| Requirement ID | Requirement | Applicable? | Implementation Control | Owner | Evidence | Status |
|---|---|---|---|---|---|---|
| HAM-FR-001 | Assign business owners. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| HAM-FR-002 | Assign technical owners. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| HAM-FR-003 | Define decision owners. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| HAM-FR-004 | Define human review model. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| HAM-FR-005 | Define approval gates. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| HAM-FR-006 | Define escalation paths. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| HAM-FR-007 | Define override rights. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| HAM-FR-008 | Capture accountability evidence. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| HAM-FR-009 | Define exception ownership. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| HAM-FR-010 | Prevent vendor or model accountability gaps. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |

## Notes

```text
[Document human accountability notes, gaps, assumptions, or exceptions]
```

---

# 11. Pillar 8: AI Assurance and Testing Requirements

## Applicability

```text
[Applicable / Not applicable / Partially applicable]
```

## Requirement Mapping

| Requirement ID | Requirement | Applicable? | Implementation Control | Owner | Evidence | Status |
|---|---|---|---|---|---|---|
| AAT-FR-001 | Define assurance requirements by risk tier. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| AAT-FR-002 | Perform pre-deployment testing. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| AAT-FR-003 | Test prompt injection risk. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| AAT-FR-004 | Test data leakage risk. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| AAT-FR-005 | Test output integrity. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| AAT-FR-006 | Test tool and action misuse. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| AAT-FR-007 | Test control effectiveness. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| AAT-FR-008 | Perform regression testing. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| AAT-FR-009 | Track remediation. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| AAT-FR-010 | Retain assurance evidence. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |

## Notes

```text
[Document assurance and testing notes, gaps, assumptions, or exceptions]
```

---

# 12. Pillar 9: Monitoring, Logging, and Evidence Requirements

## Applicability

```text
[Applicable / Not applicable / Partially applicable]
```

## Requirement Mapping

| Requirement ID | Requirement | Applicable? | Implementation Control | Owner | Evidence | Status |
|---|---|---|---|---|---|---|
| MLE-FR-001 | Define AI logging requirements. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| MLE-FR-002 | Log AI interactions. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| MLE-FR-003 | Log AI data access. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| MLE-FR-004 | Log AI tool calls and actions. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| MLE-FR-005 | Log approvals and exceptions. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| MLE-FR-006 | Detect policy violations. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| MLE-FR-007 | Integrate with monitoring systems. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| MLE-FR-008 | Preserve investigation evidence. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| MLE-FR-009 | Define evidence retention. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| MLE-FR-010 | Protect AI logs. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |

## Notes

```text
[Document monitoring, logging, and evidence notes, gaps, assumptions, or exceptions]
```

---

# 13. Pillar 10: Incident Containment and Recovery Requirements

## Applicability

```text
[Applicable / Not applicable / Partially applicable]
```

## Requirement Mapping

| Requirement ID | Requirement | Applicable? | Implementation Control | Owner | Evidence | Status |
|---|---|---|---|---|---|---|
| ICR-FR-001 | Define AI incident scenarios. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| ICR-FR-002 | Define AI incident severity. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| ICR-FR-003 | Provide access revocation. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| ICR-FR-004 | Provide agent and tool kill switches. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| ICR-FR-005 | Preserve AI incident evidence. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| ICR-FR-006 | Define escalation paths. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| ICR-FR-007 | Define recovery actions. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| ICR-FR-008 | Manage vendor AI incidents. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| ICR-FR-009 | Review AI incidents. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |
| ICR-FR-010 | Feed lessons learned into control improvement. | [Yes/No] | [Control] | [Owner] | [Evidence] | [Status] |

## Notes

```text
[Document incident containment and recovery notes, gaps, assumptions, or exceptions]
```

---

# 14. Non-Functional Requirement Mapping

Use this section to map non-functional requirements that apply across the AI control design.

| Requirement Area | Applicable? | Implementation Approach | Evidence | Status |
|---|---|---|---|---|
| Auditability | [Yes/No] | [Approach] | [Evidence] | [Status] |
| Explainability | [Yes/No] | [Approach] | [Evidence] | [Status] |
| Enforceability | [Yes/No] | [Approach] | [Evidence] | [Status] |
| Scalability | [Yes/No] | [Approach] | [Evidence] | [Status] |
| Privacy preservation | [Yes/No] | [Approach] | [Evidence] | [Status] |
| Resilience | [Yes/No] | [Approach] | [Evidence] | [Status] |
| Recoverability | [Yes/No] | [Approach] | [Evidence] | [Status] |
| Vendor neutrality | [Yes/No] | [Approach] | [Evidence] | [Status] |
| Brownfield compatibility | [Yes/No] | [Approach] | [Evidence] | [Status] |
| Traceability | [Yes/No] | [Approach] | [Evidence] | [Status] |

---

# 15. Evidence Mapping

## Required Evidence Summary

| Evidence Type | Required? | Owner | Location | Retention | Status |
|---|---|---|---|---|---|
| Inventory record | [Yes/No] | [Owner] | [Location] | [Retention] | [Status] |
| Risk assessment | [Yes/No] | [Owner] | [Location] | [Retention] | [Status] |
| Identity/access approval | [Yes/No] | [Owner] | [Location] | [Retention] | [Status] |
| Data source approval | [Yes/No] | [Owner] | [Location] | [Retention] | [Status] |
| Prompt/input evidence | [Yes/No] | [Owner] | [Location] | [Retention] | [Status] |
| Retrieval logs | [Yes/No] | [Owner] | [Location] | [Retention] | [Status] |
| Output logs | [Yes/No] | [Owner] | [Location] | [Retention] | [Status] |
| Validation records | [Yes/No] | [Owner] | [Location] | [Retention] | [Status] |
| Decision evidence | [Yes/No] | [Owner] | [Location] | [Retention] | [Status] |
| Tool call logs | [Yes/No] | [Owner] | [Location] | [Retention] | [Status] |
| Action logs | [Yes/No] | [Owner] | [Location] | [Retention] | [Status] |
| Approval records | [Yes/No] | [Owner] | [Location] | [Retention] | [Status] |
| Exception records | [Yes/No] | [Owner] | [Location] | [Retention] | [Status] |
| Assurance test results | [Yes/No] | [Owner] | [Location] | [Retention] | [Status] |
| Incident evidence | [Yes/No] | [Owner] | [Location] | [Retention] | [Status] |
| Vendor evidence | [Yes/No] | [Owner] | [Location] | [Retention] | [Status] |

---

# 16. Assurance Mapping

## Required Assurance Activities

| Assurance Activity | Required? | Trigger | Owner | Evidence | Status |
|---|---|---|---|---|---|
| Design review | [Yes/No] | [Trigger] | [Owner] | [Evidence] | [Status] |
| Pre-deployment testing | [Yes/No] | [Trigger] | [Owner] | [Evidence] | [Status] |
| Prompt injection testing | [Yes/No] | [Trigger] | [Owner] | [Evidence] | [Status] |
| Data leakage testing | [Yes/No] | [Trigger] | [Owner] | [Evidence] | [Status] |
| Retrieval boundary testing | [Yes/No] | [Trigger] | [Owner] | [Evidence] | [Status] |
| Output validation testing | [Yes/No] | [Trigger] | [Owner] | [Evidence] | [Status] |
| Tool misuse testing | [Yes/No] | [Trigger] | [Owner] | [Evidence] | [Status] |
| Approval gate testing | [Yes/No] | [Trigger] | [Owner] | [Evidence] | [Status] |
| Logging completeness testing | [Yes/No] | [Trigger] | [Owner] | [Evidence] | [Status] |
| Evidence reconstruction testing | [Yes/No] | [Trigger] | [Owner] | [Evidence] | [Status] |
| Kill switch testing | [Yes/No] | [Trigger] | [Owner] | [Evidence] | [Status] |
| Rollback testing | [Yes/No] | [Trigger] | [Owner] | [Evidence] | [Status] |
| Vendor assurance review | [Yes/No] | [Trigger] | [Owner] | [Evidence] | [Status] |
| Regression testing | [Yes/No] | [Trigger] | [Owner] | [Evidence] | [Status] |
| Incident tabletop | [Yes/No] | [Trigger] | [Owner] | [Evidence] | [Status] |

---

# 17. Gap Summary

## Requirement Gaps

| Gap ID | Requirement ID | Gap Description | Severity | Owner | Due Date | Status |
|---|---|---|---|---|---|---|
| [Gap ID] | [Requirement ID] | [Description] | [Low/Medium/High/Critical] | [Owner] | [Date] | [Status] |

## Exception Required?

```text
[ ] No
[ ] Yes
[ ] Unknown
```

## Exception Summary

| Requirement ID | Exception Needed? | Rationale | Compensating Control | Expiry |
|---|---|---|---|---|
| [Requirement ID] | [Yes/No] | [Rationale] | [Control] | [Date] |

---

# 18. Approval

## Mapping Completed By

```text
Name:
Function:
Date:
```

## Business Owner Review

```text
Name:
Decision:
Date:
Notes:
```

## Architecture / Security Review

```text
Name or forum:
Decision:
Date:
Notes:
```

## Risk / Governance Review

```text
Name or forum:
Decision:
Date:
Notes:
```

---

# 19. Summary

```text
Use case:
Risk tier:
Applicable pillars:
Highest priority requirements:
Required evidence:
Required assurance:
Open gaps:
Exceptions required:
Approval status:
Next review date:
```