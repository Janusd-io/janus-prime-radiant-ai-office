---
type: source
source_type: meeting
title: AIO Standup 21 May 2026
slug: 2026-05-21-aio-standup
created: 2026-05-21
captured_by: jehad-altoutou
fireflies_id: 01KS4G5FC30FVBDRXVGPPQZB3V
fireflies_url: https://app.fireflies.ai/view/01KS4G5FC30FVBDRXVGPPQZB3V
attendees: [Michael Bruck, Jehad Altoutou]
duration_min: 80
audience: department
departments: [ai-office]
standup_skill_version: v3.22
parser_version: 3
related: [2928682913, 2928683517, 2928659254, 2917843553, 2931866304, 2931863368, 2931869394, 2931866589, 2931884687, AIR-103, AIR-79, AIR-129, AIR-131, AIR-132]
---

# AIO Standup 21 May 2026

**Attendees:** Michael Bruck, Jehad Altoutou
**Duration:** ~80 min
**Source:** [Fireflies](https://app.fireflies.ai/view/01KS4G5FC30FVBDRXVGPPQZB3V)

---

## Key Decisions

### NanoClaude is live — deploy to Hostinger to replace Ngrok

Michael demonstrated NanoClaude (the Janus instance of Nanoclaw, AIR-103) running in Docker on his MacBook, connected to Slack via Ngrok and to Prime Radiant (read-only). First-run capabilities confirmed: vault Q&A via Slack, daily 7AM news digest (25 articles, interest-profiled from 53 vault articles + 20 pulse entries + 7 briefs), HTML deck generation, SQLite working memory, Chrome MCP, and scheduled tasks.

The current Ngrok setup is explicitly a proof of concept — the free tier rotates the tunnel URL on reconnect, breaking the Slack webhook and requiring manual updates. Jehad proposed migrating to Hostinger VPS with Caddy reverse proxy for a stable URL. Michael agreed. Monday sub-item created: 2931866304 (Deploy NanoClaude to Hostinger, Caddy, replace Ngrok) — owner Jehad.

Michael is keeping vault access read-only until comfortable. The agent can read Prime Radiant via the filesystem/Git but cannot write to it directly.

### NanoClaude rename — "NanoClaude" exposes underlying AI tech

Michael raised the concern that the name "NanoClaude" reveals the underlying Anthropic/Claude technology, which is not desirable for a team-facing tool or when demonstrating the AI-native org capability to Bonaventure. Jehad agreed: "We need to rename everything." No candidate names settled in this meeting. Monday sub-item created: 2931863368 (Rename NanoClaude) — joint AIO decision.

### Andrew onboarding — confirmed for today

Jehad had been waiting for explicit confirmation from Michael before enrolling Andrew on Cowork and NanoClaude. Michael confirmed in this standup: "Let's do it today." The 2PM afternoon meeting with Andrew (AI strategy, skills, headcounts) is the enrollment opportunity. Monday item 2928659254 (Get Andrew onboarded on Cowork / Nanoclaw) updated accordingly.

### AI-native marketing — Bonaventure endorsed, afternoon meeting with Andrew

Bonaventure's endorsement of the AI-native marketing direction is confirmed. Andrew's 8-head Bangalore proposal was explicitly pushed back on by Bonaventure. Michael and Jehad's counter-position: build marketing as a fully AI-native organisation — agents cover content creation, social scheduling, SDR-type outreach, demand gen, and Martech operations; a single senior person with technical + content capability oversees. Human roles retained: video/events oversight, content approval.

The AIO team discussed the agent capability matrix before the 2PM Andrew meeting. Agreed approach: listen to Andrew first before presenting the AIO model — it is a negotiation. Jehad created an internal comparison deck (agent-replaceable vs human-retained roles) for AIO use only. Tool stack being identified in parallel — Kling AI for video generation. Monday parent 2928683517 updated.

### Kling AI — evaluate for video generation

Jehad recommended Kling AI for video generation: "A lot of people were telling me about Kling AI. It's really nice for video generation." Michael was impressed by the AI video quality demos viewed live. AIR-129 created (Kling AI, Gate 1: CONDITIONAL PASS — Kuaishou PRC ownership; IT/Legal review required, same channel as Seedance AIR-128).

### HTML deck skill — print/PDF CSS is broken, not yet releasing

Michael demonstrated the HTML deck skill (v1.1) live. Screen rendering is correct. Print-to-PDF produces content overflow — some slides have too much content to fit the print page. Michael: "This is why I'm not releasing it yet." Fix requires a dedicated print CSS stylesheet separate from the screen CSS. Monday sub-item created: 2931866589 (Fix HTML deck skill print/PDF CSS overflow bug) — owner Jehad.

### Brand guidelines MD in Prime Radiant — out of sync with skill v1.1

Michael located the brand guidelines markdown in the Prime Radiant processes/ folder live during the meeting — it is at v1 while the skill is at v1.1. CSS tweaks, updated SVG logo variants (colour + all-white), and other refinements from v1.1 are not reflected. Michael: "We need to just put in the request on Cowork to update it." Monday sub-item created: 2931884687 (Sync brand guidelines MD to janus-html-deck skill v1.1) — owner Jehad.

### NanoClaude handoff doc — Michael to write

Michael proposed creating a complete setup + deployment handoff doc covering everything he did: Docker config, Slack app manifest, Ngrok webhook wiring, Prime Radiant read-only vault configuration, SQLite memory layer, Claude API connection, daily digest setup. Monday sub-item created: 2931869394 — owner Michael.

### Paused projects remain paused

Jehad explicitly confirmed all current pauses: ISO (blocked on Simon), website (hold per Bonaventure direction), IT (waiting on scope), marketing website (pivot in progress). Michael reframed ISO as "blocked, high priority" rather than "on hold." Marketing is not fully paused — the Singapore launch support and AI-native org build are both active priorities under the marketing umbrella.

---

## Action Items

- Deploy NanoClaude to Hostinger (Docker + Caddy, replace Ngrok) — Jehad
- Rename NanoClaude — choose name that doesn't expose underlying AI tech — AIO team
- Onboard Andrew to NanoClaude + Cowork today — Jehad (Michael confirmed "today")
- Create NanoClaude deployment + setup handoff doc — Michael
- Meeting with Andrew re: AI-native marketing org (2PM 21 May) — Michael + Jehad
- Fix HTML deck skill print/PDF CSS overflow — Jehad
- Sync brand guidelines MD in Prime Radiant to janus-html-deck skill v1.1 — Jehad
- Evaluate Kling AI (video generation) — pending IT/Legal PRC-vendor policy (align with AIR-128 Seedance)

---

## Registry Dispatch Summary

4 new AIR entries created from this meeting:

**New entries:**
- AIR-129 (Kling AI, Backlog — Gate 1 CONDITIONAL PASS — Kuaishou PRC ownership, IT/Legal review required)
- AIR-131 (Ngrok, Backlog — Gate 1 PASS — transitional tool, recommend Monitor then archive once Caddy live)
- AIR-132 (Mnemon, Backlog — Gate 1 PASS — hold until NanoClaude multi-session use case triggers)

**Rejected/voided:**
- AIR-130 (Columbus Sign) — Rejected. "Columbus signed" in Fireflies transcript was a transcription artefact; not a real tool discussed in the meeting.

**Enrichment comments added:**
- AIR-103 (Nanoclaw — live deployment context, Slack integration, daily digest, Hostinger migration plan, Monday sub-item cross-links)
- AIR-79 (Hostinger — NanoClaude new infrastructure use case, Caddy proxy plan)

---

## Monday Coverage

**Context Coverage Invariant: PASS** — all 9 touched items carry `<h2>Description (from meeting notes)</h2>` blocks.

New sub-items created (Step 3G): 2931866304, 2931863368, 2931869394, 2931866589, 2931884687

Existing source-bumped items (Step 3H): 2928659254, 2928682913, 2928683517, 2917843553

**Deduplication Gate:**
- 1 HIGH block: "Onboard Andrew to NanoClaude + Cowork" blocked by existing 2928659254 (4-token match: onboard, andrew, cowork, nanoclaw)
- 2 MEDIUM flags resolved: HTML deck (3-token technical HIGH, operational LOW — different action verb) and brand guidelines (2-token MEDIUM — different scope); both proceeded
- 4 LOW / no-overlap: proceeded without flags
