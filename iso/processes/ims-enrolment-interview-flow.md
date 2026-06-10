---
type: process
title: IMS enrolment interview flow
slug: ims-enrolment-interview-flow
created: 2026-05-14
updated: 2026-05-14
departments: [iso]
status: active
sources: [interview-department-head, interview-activity-owner, interview-first-voice, parent-department-process, sub-process, first-voice-questionnaire, handover-to-simon, diagram-prompt]
related: [ims-enrolment, iso-ims-puls, iso-9001-figure-1, iso-process-schematic, simon-tarskih]
captured_by: jehad-altoutou
owner: simon-tarskih
audience: department
---

# IMS enrolment interview flow

The five-phase interview methodology the `/ims-enrolment` skill (see [[ims-enrolment]]) uses to walk any Janus department from "no IMS documentation" to a Simon-ready handover bundle. Phases 2-4 produce documents; Phase 5 packages them for [[simon-tarskih]] (ISO Lead).

## Phase shape

| Phase | Document produced | Interviewee | Duration | Template |
| --- | --- | --- | --- | --- |
| 1 | (Foundation read — no doc) | — | ~10 min | — |
| 2 | `parent-process.md` | Department head | 30-45 min | [[parent-department-process]] |
| 3 | `sub-process-[slug].md` × N | Activity owner per activity | 20-30 min each | [[sub-process]] |
| 4 | `first-voice-[person].md` × M | Each dept member | 15-20 min each | [[first-voice-questionnaire]] |
| 5 | Handover bundle | — | ~30 min packaging | [[handover-to-simon]] |

## Critical handoffs

- **Phase 2 Q3 (Activities) seeds Phase 3.** The dept head's 3-10 activities list determines how many sub-process interviews follow. The interview prompt instructs the model to pause and confirm completeness before moving on.
- **Phase 2 Q8 (Process Owner) is a hard requirement.** ISO 9001 demands a single accountable name; "TBD" or "the team" is refused.
- **Phase 4 has two delivery modes.** Live (≤ 5 people) is default. Async (Slack/email distribution) is recommended for > 5 or for split timezones.
- **Phase 4 Q3 (Tools & systems) feeds Linear AIR coverage**, not the questionnaire itself. The AI department verifies coverage independently — no one outside AI creates AIR entries.

## Diagram generation

Each process doc carries a Mermaid Figure-1 block as guaranteed-perfect-text. The bundle also includes a ChatGPT image prompt per process (see [[diagram-prompt]]) producing the polished ultra-wide ISO-grade business diagram. If the image generator garbles text, the Mermaid block is the fallback.

## Output of the handover bundle

All artefacts land on Desktop in a single folder per the bundle template. Simon receives the bundle, assigns IMS-PRC-XXX-NNN codes, confirms the Process Owner, reviews the 7-section structure for ISO 9001 / 27001 / 42001 conformance, maps controls to clause numbers, and flags open items before the documents enter the formal IMS document set.

## See also

- [[ims-enrolment]] — the project that runs this flow
- [[iso-9001-figure-1]] / [[iso-process-schematic]] — the schematic every template mirrors
- [[iso-ims-puls]] — Janus's certification programme
