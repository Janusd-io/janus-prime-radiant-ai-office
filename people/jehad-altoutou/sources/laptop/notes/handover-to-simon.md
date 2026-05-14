---
type: source
source_type: laptop
title: handover-to-simon
slug: handover-to-simon
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-puls-onboarding/skills/ims-enrolment/templates/handover-to-simon.md
original_size: 3782
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.95
sensitivity_reason: "Template document for the IMS-enrolment skill — internal dept-shared process artefact."
---

# handover-to-simon

_Extracted from `Documents/janus-puls-onboarding/skills/ims-enrolment/templates/handover-to-simon.md` on 2026-05-14._

# [DEPARTMENT NAME] — IMS Enrolment Handover Bundle

**To:** Simon (ISO Lead)
**From:** [Department head name], [Role], Janus Digital
**Date:** [YYYY-MM-DD]
**Bundle version:** v0.1

---

Hi Simon,

The **[Department Name]** has completed its IMS enrolment using the `/ims-enrolment` skill in Claude Desktop. Attached is the full bundle for your review and integration into the formal IMS document set.

## What's in the bundle

### Process documents

| # | File | Purpose |
|---|---|---|
| 1 | `parent-process.md` | The [Department] as a whole, in the ISO 9001:2015 Figure 1 schematic |
| 2 | `sub-process-[activity-1].md` | Detailed sub-process: [Activity 1] |
| 3 | `sub-process-[activity-2].md` | Detailed sub-process: [Activity 2] |
| ... | ... | ... |

### Diagrams (one per process document)

| Process | ChatGPT prompt | Rendered image |
|---|---|---|
| Parent process | `diagram-prompt-parent-process.md` | `diagrams/diagram-parent-process.png` |
| [Activity 1] | `diagram-prompt-[activity-1].md` | `diagrams/diagram-[activity-1].png` |
| [Activity 2] | `diagram-prompt-[activity-2].md` | `diagrams/diagram-[activity-2].png` |
| ... | ... | ... |

> Each diagram prompt was used in ChatGPT (GPT-5/GPT-4o image gen) to produce the polished image. The Mermaid blocks inside each process doc provide a guaranteed-perfect-text backup if the AI-generated image is unsatisfactory.

### First Voice forms (one per department member)

| # | File | Purpose |
|---|---|---|
| N+1 | `first-voice-[person-1].md` | First Voice form for [Person 1] |
| N+2 | `first-voice-[person-2].md` | First Voice form for [Person 2] |
| ... | ... | ... |

## What we'd like from you

1. **Assign IMS-PRC-XXX-NNN codes** to the parent and sub-process documents
2. **Confirm Process Owner** for the parent (currently proposed: [Name])
3. **Review the 7-section structure** — is anything missing for ISO 9001 / 27001 / 42001 conformance?
4. **Identify which controls** map to which clause numbers in the official IMS Manual
5. **Flag any open items** you'd like resolved before the document enters the formal IMS

## Open items we've flagged

(These are also listed at the end of each sub-process document — consolidated here for visibility.)

1. **[Open item title]** — [decision needed] / [why it's blocking] / [who answers]
2. ...

## How this was produced

This bundle was generated using the **`/ims-enrolment`** skill (v1.0) in Claude Desktop. The skill walked the department head through:

- **Phase 1 — Foundation:** Read the IMS deck summary, ISO 9001 Figure 1 schematic, the 7-section template, and the AI Department worked example
- **Phase 2 — Parent process interview:** 7-section structured interview with the department head produced `parent-process.md`
- **Phase 3 — Sub-process interviews:** One interview per activity from Phase 2's list, with the activity owner, produced each `sub-process-*.md`
- **Phase 4 — First Voice:** Each department member completed their individual questionnaire
- **Phase 5 — Handover:** This bundle, generated for your review

Source skill: `~/.claude/skills/ims-enrolment/SKILL.md` (also available in the [Janus PULS Onboarding repo](https://github.com/Jehada-Janusd/janus-puls-onboarding) under `skills/ims-enrolment/`)

## Next steps proposed

| # | Step | Owner | Target date |
|---|---|---|---|
| 1 | Simon's review of bundle | Simon | [YYYY-MM-DD] |
| 2 | Department head responds to Simon's findings | [Name] | [YYYY-MM-DD] |
| 3 | v0.2 bundle reflects changes | [Name] | [YYYY-MM-DD] |
| 4 | Bundle merged into formal IMS document set | Simon | [YYYY-MM-DD] |
| 5 | Department status → "Enrolled" in PULS | Jehad (AI Ops) | After step 4 |

---

Best,
[Department head name]

*[Role] · [Department] · Janus Digital · [email]*
