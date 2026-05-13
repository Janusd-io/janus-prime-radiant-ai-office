---
type: project
title: IT Department Standup Methodology Pilot
slug: it-department-standup-pilot
created: 2026-05-07
updated: 2026-05-07
departments: [it-ops, ai-office]
status: active
owner: jehad-altoutou
sources: [aio-2026-05-06, it-discussion-tracker, automations-2896120147]
related: [andrew-soane, jehad-altoutou, michael-bruck, andrey-timokhov, euclid-wong, monday, notion]
---

# IT Department Standup Methodology Pilot

Hub for rolling out the AI Office's standup methodology — `/standup` skill + [[monday]] Automations board pattern + [[notion]] sub-page journal — to the IT department. Sibling pilot to [[andrew-soane]]'s Marketing rollout ([[2026-05-06-andrew-as-standup-skill-rollout-pilot]]).

## Why a pilot

Validates the "standup methodology generalises across departments" claim. AI Office's own standup workflow (Fireflies → Monday → Linear AIP → Notion) has been operating since 1 May; the IT pilot is the first proof point that the methodology transfers to a different department with different workflows and stakeholders.

## Scope

- **Skill tailoring** — adapt the `/standup` skill for IT-specific concerns (helpdesk-triage, infrastructure status, sandbox→production handoffs).
- **Notion sub-page** — IT department journal, mirroring the AIO Operations Notebook layout.
- **Morning-meeting co-design** with [[andrey-timokhov|Andrey]] — IT's existing meeting cadence is the hook; the pilot adapts to that rather than imposing AIO's cadence.
- **Pilot week** starts 2026-05-13.

## Success criteria

- First-week IT standups captured end-to-end (transcript → Monday updates → Notion entry).
- IT participants report the workflow doesn't add friction to their existing day.
- At least one decision and one action item per standup is properly threaded into Monday.

## Dependencies

- **Skill v3 ISO alignment** (per [[2026-05-01-iso-compliance-gate-before-automation]]) — the IT pilot uses the standup skill, which is still iterating toward ISO-aligned production.
- **Monday production push** ([[2026-05-06-monday-com-to-production-this-week]]) — Andre's IT team would prefer not to use a sandbox tool for live work.
- **Notion sub-pages** for IT department — Jehad to build by 2026-05-13.

## Owners

- **Build / tailor:** [[jehad-altoutou]]
- **Co-design partner:** [[andrey-timokhov]] (IT), with [[euclid-wong]] (head of IT/Ops) as the senior IT-side stakeholder
- **Stakeholder review:** [[michael-bruck]]

## Cross-references

- Andrew's Marketing pilot is the sibling rollout — see [[andrew-soane]] tracker for marketing-side notes.
- The [[it-helpdesk-triage-bot]] project sits adjacent — different problem space (user support) but emerges from the same IT collaboration cadence.

## Watch for

- First-week standup capture quality.
- Whether IT-specific friction surfaces tweaks the skill should adopt globally.
- Generalisability claim: if IT works, the standup methodology can be pitched as org-wide infrastructure rather than an AIO idiosyncrasy.
