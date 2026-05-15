---
type: source
source_type: meeting
title: "Bonaventure, Michael, Jehad and Andrew Meeting"
slug: 2026-05-04-bonaventure-michael-jehad-and-andrew-meeting
created: 2026-05-04
captured_by: jehad-altoutou
attendees: [michael-bruck, bonaventure-wong, jehad-altoutou]
duration_min: 74
fireflies_id: 01KQSAG8Q4JYBB63VZ5XXM750Y
audience: department
departments: [ai-office]
dept_scope: [ai-office]
sensitivity: dept
task_tracker: monday
parsed_at: 2026-05-15T09:25:59Z
parser_version: 3
summary: "Working session mapping the AI Tool Registry pipeline onto Bonaventure's ISO-style process schematic (source / input / activity / output, with gates between stages)"
topics: [ai-registry-pipeline, process-modelling, iso-schematic, standup-skill-v3-9, tool-categorisation, hercules-evaluation, confidence-bands, digital-twin-vision]
decisions: [2026-05-04-air-intake-form-fields, 2026-05-04-keep-enrichment-and-evaluation-as-two-skills, 2026-05-04-evaluation-gate-is-binary-four-of-four, 2026-05-04-standup-skill-confidence-bands, 2026-05-04-standup-skill-treats-fireflies-summary-as-unreliable, 2026-05-04-each-pipeline-stage-pings-slack]
action_items_count: 5
confidence_overall: high
---

# Bonaventure, Michael, Jehad and Andrew Meeting

**Date:** 2026-05-04
**Attendees:** [[michael-bruck]], [[bonaventure-wong]], [[jehad-altoutou]]
**Duration:** 74 min
**Fireflies:** [original meeting](https://app.fireflies.ai/view/01KQSAG8Q4JYBB63VZ5XXM750Y)

---

## Summary

Working session mapping the AI Tool Registry pipeline onto Bonaventure's ISO-style process schematic (source / input / activity / output, with gates between stages). Michael walked through the current flow: Slack request hub captures a URL + submitter + timestamp + location, a Claude skill enriches the entry into Linear (the AIR registry, system of record), then a separate evaluation skill scores against the AI policy (binary 4-of-4 hard gates such as no-training-on-our-data and Google integration), then sandbox where the tool is paid for, installed and tested, then handoff to IT. Bonaventure pushed Michael to document each stage with explicit source/input/activity/output and to add Slack status pings between stages and a clear rejection branch with documented reasons. Jehad then demoed the rewritten standup skill (v3.9, up from v2.7) which pulls the Fireflies transcript directly, discards the Fireflies summary, cross-references Monday + Linear + Notion, and auto-updates with confidence bands (>=90% auto-apply, 60-80% prompt user, <60% ignore); it also dispatches sub-skills (ai-registry, ai-evaluation) and writes a daily Notion log. Hercules was the test tool driving the conversation — Michael identified it as a no-code full-stack builder comparable to Lovable, Replit, Claude Design and Google Stitch, and a new finding was that Hercules goes further than Replit/Lovable by running the entire stack including payment and OAuth. Open thread: how to define a tool-categorisation taxonomy so the 'comparables' lookup doesn't miscategorise; how to extend the same agentic pipeline pattern across departments (the long-horizon company-wide digital twin / system-of-record ambition).

## Decisions

- [[2026-05-04-air-intake-form-fields]] — AI Registry intake form: URL + submitter + timestamp + location only
- [[2026-05-04-keep-enrichment-and-evaluation-as-two-skills]] — Keep enrichment and evaluation as two distinct skills
- [[2026-05-04-evaluation-gate-is-binary-four-of-four]] — Evaluation gate is binary, four-of-four pass required
- [[2026-05-04-standup-skill-confidence-bands]] — Standup skill writes to Monday using three confidence bands
- [[2026-05-04-standup-skill-treats-fireflies-summary-as-unreliable]] — Standup skill ignores Fireflies' own summary and uses the raw transcript
- [[2026-05-04-each-pipeline-stage-pings-slack]] — Each pipeline stage emits a Slack status reply

## Action items

- [ ] @jehad-altoutou Finish updating the AI Registry / AI evaluation skills so the standup skill can dispatch them as sub-skills end-to-end. (raised by @michael-bruck) — Monday
- [ ] @michael-bruck Document the AI Registry pipeline against the ISO source/input/activity/output schematic — including the rejection branch and Slack status pings between stages. (raised by @bonaventure-wong) — Monday
- [ ] @michael-bruck Define a tool-categorisation taxonomy so the enrichment skill's 'comparables' step doesn't miscategorise (e.g. confusing a no-code stack-builder with unrelated categories). (raised by @bonaventure-wong) — Monday
- [ ] @michael-bruck Co-design the sandbox -> IT handoff template with the IT team so the AI Office's output matches IT's required input. — Monday
- [ ] @michael-bruck Tighten the 'reject' vs 'watch list' distinction in Linear so rejection reasons are documented rather than left as subjective 'garbage' calls. (raised by @bonaventure-wong) — Monday

## 🎯 This week

- @michael-bruck Pick a guinea-pig department to extend the standup / agentic pipeline pattern beyond the AI Office. (raised by @bonaventure-wong)
- @bonaventure-wong Schedule a follow-up working session this week to continue the ISO-schematic pass over the pipeline (and to apply it to Bonaventure's own work as a candidate test).

## 🏔️ Long horizon

- Build a company-wide centralised system of record — one massive 'digital twin' fed by every meeting, email and calendar event across all Janus markets — that supports joined-up decision-making across departments. (owner: @jehad-altoutou; horizon: year)
- Solve role-based access / compartmentalisation (by role, person, department) on top of the unified data layer so finance, marketing, HR etc. each see only what they should. (owner: @michael-bruck; horizon: quarter)
- Position the agentic pipeline pattern externally — sell it to clients — once NDA / GDPR / privacy concerns can be handled engineering-side. (horizon: year)
- Stand up a LinkedIn-style AI agent that scans posts for buying-trigger keywords and engages on Janus's behalf, generating inbound sales leads at scale. (owner: @bonaventure-wong; horizon: quarter)
- Continuous-improvement loop: every iteration of the registry/evaluation pipeline accumulates more category knowledge in Linear, making each future enrichment pass cheaper and richer (flywheel effect). (owner: @michael-bruck)

## Findings

- Hercules is materially different from Lovable / Replit / Claude Design / Google Stitch: it runs the entire stack including payment and OAuth from a single command, where Replit and Lovable still require configuration and Stitch only does design. (stated by @michael-bruck; confidence: medium)
- The standup skill jumped from v2.7 to v3.9 in this rewrite — it now cross-references Monday + Notion + Linear + Fireflies in a single run and dispatches sub-agents (e.g. for AI Registry updates) automatically. (stated by @michael-bruck)
- Cowork is being used in production by the AI Office but is not formally approved as an AI tool. (stated by @michael-bruck)
- Claude Enterprise allows per-user feature toggling but requires roughly 50 seats minimum, so Janus is not yet at the size to justify it. (stated by @bonaventure-wong; confidence: low)
- Context-window overload is already a live engineering constraint on the standup pipeline — old Monday/Notion content had to be compacted to keep runs fast. (stated by @michael-bruck)
- Most candidate AI tools fail the policy evaluation because they lack a clear policy on whether they train on customer data. (stated by @michael-bruck; confidence: medium)

## Open questions

- How should AI tools be categorised so the 'comparables' enrichment step doesn't miscategorise (the example given was Janus itself being miscategorised as a BMS company)? (raised by @bonaventure-wong)
- Which department should be the first non-AIO test of the standup / agentic pipeline pattern? (raised by @bonaventure-wong)
- How do we extend the agentic pipeline externally (to clients) while satisfying NDA, GDPR and privacy obligations? (raised by @bonaventure-wong)
- Can marketing-relevant outputs be cleanly separated and streamed into role-specific work streams from a single source of truth? (raised by @jehad-altoutou)
- Should the AI Registry intake form authenticate the Slack submitter (e.g. confirm they're an employee, confirm department fit) or trust Slack channel membership? (raised by @bonaventure-wong)

## Blockers

- External rollout of the agentic pipeline is blocked on NDA / GDPR / privacy controls and on staffing up engineering resources to build them. (owner: @jehad-altoutou)
- Sandbox-to-IT handoff is unblocked-but-incomplete: there is no template yet for what the AI Office hands to IT, and IT needs to co-design it. (owner: @michael-bruck)

## Tool mentions

- [[hercules]] — the tool driving today's evaluation walkthrough — no-code full-stack agent builder; Bonaventure surfaced it
- [[lovable]] — comparable cited during enrichment-step categorisation discussion
- [[replit]] — comparable cited during enrichment-step categorisation discussion
- [[claude-design]] — comparable — does the design but not the full stack
- [[google-stitch]] — comparable — design-only, contrasted with Hercules' full-stack runtime
- [[linear]] — system of record for the AI Registry (AIR); enrichment skill writes the rich memo here
- [[monday-com]] — primary execution surface for AI Office tasks/projects; standup skill writes proposed updates here with confidence bands
- [[notion]] — running log / memory surface; standup writes the daily summary here and uses it as context for confidence scoring
- [[fireflies]] — transcript source; the rewritten standup skill ingests the raw transcript and discards the Fireflies-generated summary
- [[slack]] — intake channel for the AI Registry pipeline; also the surface for inter-stage status pings
- [[cowork]] — Claude orchestration surface running the standup skill; in production use but not formally approved
- [[whisper-flow]] — voice-capture tool surfaced from the transcript and auto-updated in the AI Registry during the demo
- [[chatgpt-5-5]] — being trialled by AI Office; Jehad uses it for writing software
- [[claude-enterprise]] — evaluated and dismissed — per-user feature controls available but minimum seat count too high for Janus today

## Topics

- ai-registry-pipeline
- process-modelling
- iso-schematic
- standup-skill-v3-9
- tool-categorisation
- hercules-evaluation
- confidence-bands
- digital-twin-vision

## Related

- Project: [[ai-registry]] — the pipeline being mapped is the AI Tool Registry workflow
- Project: [[standup-skill]] — demo of the v3.9 rewrite was the second half of the meeting
- Concept: [[iso-process-schematic]] — Bonaventure pushed the source/input/activity/output framing as the documentation discipline
- Concept: [[ai-policy]] — the four binary gates at the evaluation stage are the AI policy in operational form
- Concept: [[agentic-pipeline]] — the long-horizon pattern Jehad and Bonaventure want to take company-wide
- Concept: [[digital-twin]] — Jehad's framing of the year-scale ambition
- Vendor: [[hercules]] — test tool driving the registry-pipeline walkthrough
- Vendor: [[linear]] — AI Registry system of record
- Vendor: [[monday-com]] — primary execution surface; standup skill writes here
- Vendor: [[notion]] — running log; memory layer for confidence scoring
- Vendor: [[fireflies]] — transcript source; summary explicitly distrusted
- Vendor: [[cowork]] — Claude orchestration surface used by standup
- Person: [[simon-tarskih]] — ISO facilitator skill build came up as a Monday parent task auto-detected by the standup demo
- Person: [[andrew-soane]] — named in the meeting title but did not attend
- Person: [[ann-greed]] — referenced in passing re: finance/marketing crossover decisions Joyce wouldn't otherwise see
- Department: [[it-ops]] — IT is the downstream of sandbox; handoff template needs co-design with them
- Department: [[finance]] — named as the next test department for the agentic pipeline and as the sandbox payment owner
- Department: [[marketing]] — Jehad cited marketing as a candidate cross-functional use case
- Department: [[hr]] — named via Theresa as a cross-functional touchpoint

---

## Transcript

Raw transcript stays in Fireflies — fetch via MCP when needed.
Fireflies: [original meeting](https://app.fireflies.ai/view/01KQSAG8Q4JYBB63VZ5XXM750Y)
