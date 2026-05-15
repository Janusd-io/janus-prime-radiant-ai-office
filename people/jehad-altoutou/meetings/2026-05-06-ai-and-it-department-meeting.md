---
type: source
source_type: meeting
title: Ai and IT department meeting
slug: 2026-05-06-ai-and-it-department-meeting
created: 2026-05-06
captured_by: jehad-altoutou
attendees: [michael-bruck, euclid-wong, andrey-timokhov, jehad-altoutou]
duration_min: 55
fireflies_id: 01KQYFN8G0DWZW8X8TKKXHQ5VB
audience: "departments:ai-office,it-ops"
departments: [ai-office, it-ops]
dept_scope: [ai-office, it-ops]
sensitivity: dept
task_tracker: monday
parsed_at: 2026-05-15T09:25:59Z
parser_version: 3
summary: "Cross-department working session between AI Office (Michael, Jehad) and IT/Ops (Euclid, Andrey)"
topics: [claude-cowork, approved-tools-list, iso-bottleneck, sandbox-to-production, monday-rollout, standup-pipeline, it-support-bot, hiring]
decisions: [2026-05-06-add-claude-cowork-to-approved-tools-v3, 2026-05-06-pilot-aio-standup-pipeline-on-it-ops, 2026-05-06-andrey-owns-software-purchase-budget]
action_items_count: 6
confidence_overall: high
---

# Ai and IT department meeting

**Date:** 2026-05-06
**Attendees:** [[michael-bruck]], [[euclid-wong]], [[andrey-timokhov]], [[jehad-altoutou]]
**Duration:** 55 min
**Fireflies:** [original meeting](https://app.fireflies.ai/view/01KQYFN8G0DWZW8X8TKKXHQ5VB)

---

## Summary

Cross-department working session between AI Office (Michael, Jehad) and IT/Ops (Euclid, Andrey). Three threads ran in parallel: (1) Cloud / Claude Cowork sits outside the approved-tools list and Euclid agreed to add it (with the parenthetical 'including Cowork') to version three of the approved tools register, while keeping a department-by-department rationing model (marketing, finance, IT, engineering — not general purpose); (2) Euclid named ISO as the current blocker preventing the sandbox backlog from being released to production — he is waiting on Simon's documents and the team still needs to agree the sandbox-to-production handover procedure (SOP / README, training, tests, sign-off); (3) AI Office offered to clone its Fireflies-to-Monday-to-Notion standup pipeline (skills built by Jehad on top of Claude Cowork) for IT/Ops, starting as a pilot — Jehad will help tailor the skills since they aren't out-of-the-box portable. Andrey will push Monday to production this week, with a Monday.com onboarding call set for Thursday 3pm with Javon (Monday.com partner consultant). Side decisions: Andrey is the budget owner for new software (no per-person company cards), and Michael's new IT hire 'Tia' starts next week. A Singapore inquiries email (inquiries@janusd.sg) was requested mid-meeting.

## Decisions

- [[2026-05-06-add-claude-cowork-to-approved-tools-v3]] — Add Claude (including Cowork) to v3 approved tools list
- [[2026-05-06-pilot-aio-standup-pipeline-on-it-ops]] — Pilot the AIO Fireflies-to-Monday-Notion-Linear standup pipeline on IT/Ops first
- [[2026-05-06-andrey-owns-software-purchase-budget]] — Andrey is the budget owner for new software purchases

## Action items

- [ ] @euclid-wong Add Claude (including Cowork) to v3 of the approved tools list, distinct from Claude Code. (raised by @michael-bruck) — Monday
- [ ] @andrey-timokhov Push Monday to production this week. (due: 2026-05-10) — Monday
- [ ] @andrey-timokhov Send the Zoom link / calendar reminder for the Thursday 3pm Monday.com onboarding call with Javon. (due: 2026-05-07; raised by @michael-bruck) — Monday
- [ ] @jehad-altoutou Provision the inquiries@janusd.sg email address for the Singapore entity. (raised by @michael-bruck) — Monday
- [ ] @jehad-altoutou Help IT/Ops tailor the AIO standup skill suite (Fireflies -> Monday / Notion / Linear) so it works for IT/Ops rather than shipping it as-is. (raised by @euclid-wong) — Monday
- [ ] @andrey-timokhov Create a Monday board / category for the AI-and-IT cross-dept conversations (mirroring the per-function split already in place for training and Andrew/Simon). (raised by @michael-bruck) — Monday

## 🎯 This week

- @andrey-timokhov Run the Thursday 3pm Monday.com onboarding session with Javon (Monday.com partner consultant).
- @euclid-wong Continue waiting on Simon's ISO documents and chase if they don't land by end of week — this is the active bottleneck. (raised by @michael-bruck)
- @team Begin scoping the AIO -> IT/Ops standup-pipeline tailoring so the pilot can stand up alongside the Monday production push. (raised by @euclid-wong)

## 🏔️ Long horizon

- Build a company-wide knowledge base by federating the per-department Monday/Notion/skills pattern across every department, surfacing an agentic layer that operates across the whole company. (owner: @euclid-wong; horizon: quarter)
- Stand up a general-purpose AI agent (Claude-based, Slack-fronted) that lets non-technical users get things done in Monday and other tools without learning each tool's UI — explicitly not landing for at least the next year. (owner: @euclid-wong; horizon: year)
- Hire software engineers into AI Office (likely from EoC pipeline) as Jehad's bandwidth saturates and the project backlog grows. (owner: @michael-bruck; horizon: weeks)
- Migrate the Notion-as-memory layer to a more efficient storage substrate (Obsidian under evaluation) once the current setup becomes too large to be efficient. (owner: @jehad-altoutou)
- Develop tailor-made AI bots in addition to off-the-shelf tools — e.g., a Singapore government/energy news-collection bot requested by Bonaventure, an IT-support bot in Slack fronting Zendesk, and an AI-hub intake bot fronting Linear. (owner: @euclid-wong; horizon: quarter)

## Findings

- Claude on the web (without the desktop app) appears to drive significantly higher cost than the app — one user spiked to around $30 in a single session before the app was installed; cause is unconfirmed but suspected to be API usage being billed differently in browser mode. (stated by @euclid-wong; confidence: low)
- Claude's strategic advantage over Gemini for Janus is integrations (MCP + APIs into Zendesk, CRM, DEEL, etc.) — Google currently does not support MCP, which is why agentic, cross-system work has to be built on Claude. (stated by @euclid-wong)
- The current AIO standup pipeline (Fireflies -> Claude Cowork skills -> Monday + Notion + Linear) is already self-correcting: the skill flagged a production-vs-sandbox mismatch between the spoken conversation and the Monday board state and offered to fix it. (stated by @andrey-timokhov)
- Monday.com is not technically an AI tool and therefore should not sit in the AI Tools Registry — same applies to Notion, DEEL, Xero and Airwallex; they belong in a broader tools register. (stated by @euclid-wong)
- Monday.com support is delivered through third-party partner consultants (Javon, working for an external 'Cloud something' partner), not by Monday's own staff — analogous to the AWS partner-ecosystem model. (stated by @euclid-wong)
- NotebookLM presentations are effectively non-editable in practice — the system refuses to revise numbers or wording after the first generation; Gamma has come back into consideration for enterprise editable decks. (stated by @michael-bruck; confidence: medium)

## Open questions

- What is the formal sandbox-to-production handover procedure between IT/Ops and AI Office — SOP, README, training requirement, formal sign-off, test cases? (raised by @euclid-wong)
- Should Monday.com be released to users before the general-purpose AI agent is built, or only as a bundle once the agent layer exists? (raised by @michael-bruck)
- Does Singapore local staff need Claude, or is Gemini sufficient for them — and who approves that? (raised by @euclid-wong)
- Should the Janus AI subdomain (janusd.ai) be held by AI Office or assigned to Marketing — does anyone have an immediate need? (raised by @euclid-wong)
- Will Monday.com offer Janus a corporate / volume discount, and what is the per-seat economics once it becomes standard issue? (raised by @euclid-wong)

## Blockers

- ISO documentation (Simon-owned) is not yet ready, which blocks IT/Ops from moving its sandbox backlog of approved AI projects into production. (blocks: [[iso-ims-puls]]; owner: @simon-tarskih)
- Jehad is approaching bandwidth saturation across AI Office initiatives — pipeline tailoring for IT/Ops and the broader skills work depend on his availability until additional engineers are hired. (owner: @michael-bruck)

## Tool mentions

- [[claude-cowork]] — Whether Cowork requires its own approval line on the approved-tools register, separate from Claude Code.
- [[claude-code]] — Discussed as distinct from Cowork — ChatGPT's split into a separate Codex app is contrasted with Claude bundling both.
- [[gemini]] — Positioned as the general-purpose tool for most staff; very capable on deep research, weaker on presentations and lacks MCP/agent integrations.
- [[notebooklm]] — Considered for internal presentations but found stubborn and effectively non-editable.
- [[gamma]] — Re-evaluated as an editable presentation tool now that enterprise adoption has grown.
- [[monday-com]] — Primary task/project management surface — being pushed to production this week; Janus has an onboarding call with Monday partner Javon on Thursday.
- [[notion]] — Run-log / memory surface for AIO standups; reaffirmed not to be classified as an AI tool.
- [[linear]] — Used in place of Zendesk for IT-Ops AI tool registry ticketing; will receive AI-hub bot-generated tickets.
- [[zendesk]] — Current AIO ticketing surface; Slack-to-Zendesk integration discussed as a basic mechanical wire with a future Slack-side AI bot in front of it.
- [[slack]] — Front door for the planned IT-support bot and the AI-hub intake bot — bot answers basic questions before opening a ticket.
- [[fireflies]] — Source of transcripts that the AIO skills consume to update Monday, Notion and Linear.
- [[obsidian]] — Being evaluated as a more efficient long-term storage substrate to replace the Notion memory layer once it gets too big.
- [[google-slides]] — Considered for outbound decks but Gemini doesn't render to it well yet.
- [[asana]] — Being deprecated outside Singapore; only retained because of a Singapore-specific deployment.
- [[deel]] — Listed alongside Xero and Airwallex as a department-specific (HR / finance) non-AI tool that should not sit in the AI registry.
- [[xero]] — Same as DEEL — department-specific finance tool, not registry-worthy.
- [[airwallex]] — Department-specific finance tool; mentioned in the same breath as DEEL and Xero.

## Topics

- claude-cowork
- approved-tools-list
- iso-bottleneck
- sandbox-to-production
- monday-rollout
- standup-pipeline
- it-support-bot
- hiring

## Related

- Person: [[simon-tarskih]] — ISO Lead — his documents are the current blocker for sandbox-to-production releases
- Person: [[andrew-soane]] — Marketing CRM evaluation referenced as parallel work in IT/Ops support pipeline
- Person: [[bonaventure-wong]] — Requested a Singapore government/energy news-collection bot — example of the tailor-made bot pipeline
- Person: [[javon-monday]] — Monday.com partner consultant running the Thursday 3pm onboarding session
- Person: [[joyce-singapore]] — Singapore executive currently being certified by SG government to use AI; raised in context of Singapore tool needs
- Person: [[tia-it-hire]] — Michael's new IT hire joining next week; requires Entra / Google Workspace / Notion handover
- Department: [[ai-office]] — Owns the standup pipeline being shared with IT/Ops
- Department: [[it-ops]] — Pilot recipient of the standup pipeline; owns ISO sandbox backlog
- Department: [[iso]] — ISO documentation is the current blocker named in this meeting
- Department: [[marketing]] — Mentioned as a Claude-needing department alongside Finance and Engineering
- Department: [[finance]] — Mentioned as a Claude-needing department and as the user-base for the Excel plug-in case
- Department: [[engineering]] — Mentioned as the likely home for Claude Code dependency
- Project: [[ai-tool-registry]] — Approved-tools-list v3 update is the deliverable from this meeting
- Project: [[monday-rollout]] — Push-to-production this week + Javon onboarding call
- Project: [[it-support-bot]] — Slack-front-Zendesk bot scoped during the meeting
- Project: [[ai-hub-intake-bot]] — Linear-backed intake bot for AI tool requests scoped during the meeting
- Project: [[standup-pipeline]] — Fireflies->Monday/Notion/Linear skill suite being cloned for IT/Ops
- Concept: [[sandbox-to-production-handover]] — Procedure gap explicitly named; awaiting SOP, training, tests, sign-off
- Concept: [[mcp]] — Cited as the reason Claude beats Gemini for agentic, cross-system integrations
- Concept: [[agentic-layer]] — Long-horizon target: department pipelines federating into a company-wide agentic layer

---

## Transcript

Raw transcript stays in Fireflies — fetch via MCP when needed.
Fireflies: [original meeting](https://app.fireflies.ai/view/01KQYFN8G0DWZW8X8TKKXHQ5VB)
