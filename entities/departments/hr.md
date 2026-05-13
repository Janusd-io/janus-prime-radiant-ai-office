---
type: department
title: HR
slug: hr
created: 2026-05-08
updated: 2026-05-11
departments: [hr]
status: active
owner: theresa-wong
sources: [2026-05-11-aio-standup-with-jehad]
related: [theresa-wong, mariam-mahmood, recruitment-automation-pipeline, 2026-05-04-recruitment-execution-on-hr-dashboard-board, 2026-05-04-centralised-fireflies-webhook-for-interviews, 2026-05-05-recruitment-scoring-as-claude-skill, 2026-05-07-rubric-scoring-as-claude-skill, yusuf-apple-dubai]
---

# HR

Janus's Human Resources department, with active recruitment automation and employer-brand workstreams. Recruitment is the most automated HR surface so far — interview transcripts via centralised Fireflies webhook, candidate scoring via the Rubric Claude skill, multi-stage pipeline tracked on the HR Dashboard board.

## People

- **[[theresa-wong]]** — Head of HR.
- **[[mariam-mahmood]]** — HR operator; recruitment workstream owner.

## Prime Radiant instance

Queued. No HR-specific Prime Radiant has been stood up. HR-relevant signal currently flows into the AIO Prime Radiant when AI tooling is implicated (e.g., Assessify, Deel, Rubric scoring decisions). When HR's knowledge surface grows enough, a dedicated **Janus Prime Radiant · HR** instance will be spun up per the rollout pattern in [[janus-prime-radiant-build]].

## Infrastructure layer (per three-layer model)

When the HR instance stands up, this layer will need: hiring profiles per role, scoring rubrics (already a Claude skill), employment contract templates by jurisdiction (GDPR / UK / SGP / UAE), employer brand guidelines (overlaps with [[marketing]]), policy frameworks.

## Tools currently relevant to HR

[[assessify]] (interview scoring; AI Registry) · [[deel]] (employment contracts and payroll across jurisdictions; AI Registry) · Rubric scoring as a Claude skill ([[2026-05-07-rubric-scoring-as-claude-skill]]) · centralised Fireflies webhook for interview transcript capture ([[2026-05-04-centralised-fireflies-webhook-for-interviews]])

## Key projects

[[recruitment-automation-pipeline]] — end-to-end automated candidate flow from inbound CV to interview scoring to decision.

## Cross-instance federation

HR will federate with [[ai-office]] (Rubric / scoring tools live there), [[marketing]] (employer brand), and [[office-of-ceo]] (strategic hires).

## Talent watch

- **[[yusuf-apple-dubai|Yusuf]]** — Apple Store Dubai sales associate; 3rd-year CS student at American University in Dubai; potential internship candidate for a non-technical-AIO-rollout interface role. AIO to raise with Theresa whether interns are supported at Janus and what the structure would be. Filed at `confidence: low` pending surname and contact details. Surfaced in the 11 May AIO standup.
