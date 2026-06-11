---
type: meeting
title: Twenty CRM Demo — Michael Bruck, Andrew Soane, Jehad Altoutou with Felix Malfait
slug: 2026-06-10-michael-bruck-twenty-crm-demo
date: 2026-06-10
created: 2026-06-11
participants: [michael-bruck, andrew-soane, jehad-altoutou, felix-malfait-twenty]
departments: [marketing, ai-office]
---

# Twenty CRM Demo — Michael Bruck, Andrew Soane, Jehad Altoutou with Felix Malfait

**Date:** 10 June 2026, 2:04 PM
**Participants:** Michael Bruck, Andrew Soane, Jehad Altoutou (Janus); Felix Malfait (Twenty CRM, founder/CEO)
**Attribution:** All speakers named explicitly in transcript. No attribution uncertainty.

## Context

Fourth vendor in Janus's CRM evaluation week (one dropped prior — described as corporate, "their way or the highway"). Follow-up/commercial discussion to be scheduled for next week.

## Company background (Felix Malfait)

- **Age:** 3 years old (older than the team expected)
- **Registration:** US company (Delaware-style); not French despite founder being French
- **Previous company:** Founded Kunai (consulting firm), sold to Airbnb; same engineering team (8 years together) now at Twenty
- **Clients:** Bayer (migrating from Salesforce to Twenty; large services contract ~200k); PwC (via Kunai acquisition)
- **Funding:** Not publicly disclosed; Felix describes being in "phase 1" (build infrastructure, not focused on revenue); targeting profitability end of 2026
- **Open source:** GitHub repo public; ~"one of the best projects at the application layer last year"; OSS treated primarily as marketing rather than contribution value
- **Pricing strategy:** Aggressive on CRM seat pricing ($10/user currently on legacy tier); margin strategy is AI credits

## Product overview

- **Fully configurable data model:** Custom objects, custom layouts, relational self-references (e.g., B2B2B company hierarchy — parent/child/grandparent)
- **API-first / MCP server:** Everything in the AI chat is also exposed via MCP server. REST API + Graph API. Auto-generates endpoints when objects are created.
- **RBAC for agent API keys:** Can scope an API key to specific object-level permissions — agents cannot escalate privilege. Key question from Jehad; confirmed fully supported.
- **Fuelty Edge (enterprise):** Declare custom React components, layouts, backend functions as code-in-source → deploy to CRM. Source of truth is the codebase. Like Salesforce Apex but open.
- **Workflows / automation:** Trigger webhooks, automate on record creation, AI-generated workflows
- **Call transcription:** Built in (via Fireflies-like capability in-product). Attaches to records, enables in-call queries.
- **Forms:** No native drag-drop form builder; approach is webhook-triggered workflows or Fuelty Edge custom HTML form hosted elsewhere; or AI generates the raw HTML
- **Dashboard:** Custom components embeddable via Fuelty Edge apps; doesn't cover all dashboard needs natively

## Limitations flagged

- Fireflies native integration launching end of June (not yet live)
- Microsoft Entra SSO: has Microsoft 365 OAuth but Felix said "not Microsoft Entra" specifically — needs verification
- Form builder is DIY-heavy vs HubSpot/Monday native forms
- Integration marketplace launching end of June (currently limited pre-built integrations)
- Services/deployment support is via 500-partner network (50 vetted); Twenty itself doesn't do services except for very large clients like Bayer

## Janus team reactions

- **Michael:** "Big fan of open source... more than I was expecting actually." Raised the key question of full configurability via AI/Claude (not just data but config). Confirmed happy. Noted Slack's hypocrisy: all AI talk, but can't configure a Slack app without 90s-era manual UI.
- **Andrew:** Ranked it above HubSpot. Appreciated Felix's honest answers (contrast with dropped vendor). Concern about company age/sustainability — addressed by: 3 years old (not months), Bayer + PwC as anchors, founding team stability.
- **Jehad:** Reviewed the codebase. "It's nicely built, it's well defined." Asked the RBAC/agent-scoping question — satisfied with the answer.

## Decision status as of June 10

- Shortlist to 1–2 vendors next week
- Commercials discussion next week
- Decision expected next week
- Andrew's current mental ranking (unstated but implied): Twenty and Attio as top contenders; HubSpot lower; Monday acceptable but board-model mismatch for CRM use

## Michael's operating pattern framing (shared with Felix)

Per [14:37] in transcript: described the Janus AIO operating pattern — internal meeting recorded → transcript fed to Claude skill → Linear updated automatically (issues moved, recategorized, enriched). "We hardly ever look at the screen. The transcript drives is not just a recording... It is a core driver of our knowledge and the actions that it takes." Flagged this as the pattern they want to replicate with the CRM as well.
