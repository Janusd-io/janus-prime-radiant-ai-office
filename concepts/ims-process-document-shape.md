---
type: concept
title: IMS process document shape — the seven sections
slug: ims-process-document-shape
created: 2026-05-14
updated: 2026-05-14
captured_by: jehad-altoutou
audience: department
departments: [ai-office, iso]
sources: [seven-section-template, iso-9001-figure-1, plain-english-overview]
related: [iso-9001-figure-1, iso-process-schematic, iso-ims-puls, iso-compliance-programme, ims-enrolment]
---

# IMS process document shape — the seven sections

Every one of Janus's 20 IMS process documents (10 Core, 3 Support, 5 Management, 2 Additional) has exactly the same internal structure: **seven sections**, in a fixed order, sourced from slide 9 of Simon's IMS Development Programme deck. The names and order are non-negotiable — auditors check for them explicitly.

## The seven sections

1. **Controls** — which laws, policies, and ISO clauses apply (UAE / SG / UK jurisdictional + specific ISO clause numbers).
2. **Inputs** — what triggers the process (events, requests, predecessor outputs, data feeds, scheduled jobs).
3. **Activities & control points** — the actual step-by-step procedure, with RACI per step and control points between steps.
4. **Monitoring & measurement** — KPIs per process, target values, measurement frequency. "Proposed KPIs" is acceptable for v1 if formal ones aren't tracked yet.
5. **Resources** — Process Owner (one named person), team roles, systems, tools, budget, training. AI tools live in [[ai-registry|Linear AIR]] (the AI Systems Register); other departments only list the tools they use.
6. **Outputs & records** — deliverables (to next process / client / audit) and records (evidence retained for audit). ~55 records defined across the IMS (L5 in the document hierarchy).
7. **Process Owner** — one named C-level (or designated lead) accountable for performance and compliance. Not "the team." Not "TBD." Not "shared."

## Mapping to [[iso-9001-figure-1]]

| Figure 1 element | Section |
| --- | --- |
| Sources of Inputs | implicit in §2 Inputs |
| Inputs | §2 Inputs |
| Activities | §3 Activities & control points |
| Outputs | §6 Outputs & records |
| Receivers of Outputs | implicit in §6 Outputs & records |
| Controls (top box) | §1 Controls |
| Resources (bottom box) | §5 Resources |
| Monitoring (dashed line) | §4 Monitoring & measurement |
| Owner (process header) | §7 Process Owner |

Some Janus templates split Sources/Receivers into their own sections for clarity — that gives 9 surface sections but still maps to the 7 ISO-required elements.

## Audit checklist

The auditor expects, in order: all 7 sections present and populated · Controls cite specific ISO clauses and jurisdiction-specific regulations · Process Owner is a name not a role · Activities have control points · KPIs have target values (or are explicitly marked "to be defined") · Records have retention periods · Resources list AI tools (the AI department independently verifies each against [[ai-registry|Linear AIR]] coverage). A missing or hand-waved section is an audit finding.

## Drill-down levels

The same shape applies at three levels: **parent process** (the department as a whole — Activities are the major chapters), **sub-process** (one activity within the department — Activities are the step-by-step procedure), and **operational task** (one task — Activities are the individual actions). [[ims-enrolment]] walks each department through producing all three levels.
