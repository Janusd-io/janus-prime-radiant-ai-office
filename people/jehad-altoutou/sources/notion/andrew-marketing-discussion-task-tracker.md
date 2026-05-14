---
type: source
source_type: notion
slug: andrew-marketing-discussion-task-tracker
title: Andrew / Marketing — Discussion & Task Tracker
created: 2026-05-06
captured_by: jehad-altoutou
notion_url: https://www.notion.so/357114fc090c81d08791f0cfccd9c515
audience: department
departments: [ai-office, marketing]
sensitivity: dept
sensitivity_confidence: 0.5
---

# Purpose
Persistent log of weekly meetings with **Andrew** (UK-based marketing leader, recently joined) covering AI-augmented marketing strategy, brand, CRM, content, and outbound. Each meeting follows the same format as the daily AIO standup entries in the [AI Office Operations Notebook](https://www.notion.so/335114fc090c81919a6ecd2f2cacc64a) — clean summary, time-bucketed next steps with Monday hyperlinks, decisions, findings, items touched, AIR / evaluation outcomes. Newest meeting at the top.
Marketing-driven operational work lives in the **Marketing Department** group on the [Automation Plans & Task Tracking](https://janusd-company.monday.com/boards/5095012818) board.

---

## Bonaventure / Andrew / Michael — Singapore News Monitoring — 6 May 2026
**Attendees:** Bonaventure Wong, Andrew Soane, Michael Bruck
**Source transcript:** uploaded markdown via Cowork session — Fireflies link to be added
**Duration:** ~32 min

### Clean meeting summary
Bonaventure asked Michael to build an AI agent that surfaces Singapore market signals (news, government releases, niche analyst newsletters) to seed thought-leadership content, LinkedIn engagement, and conversation starters with prospects. Explicit quality-over-quantity bar: 1–2 nuggets per week, not a daily firehose. Michael has built similar bots before (Conor's Asia semiconductor / EV digest) and confirmed off-the-shelf commercial monitoring tools have been weak. The agreed architecture is two-pass — wide keyword/site collection first, semantic theme matching second. Andrew framed it as the same find-and-react capability discussed yesterday for LinkedIn outreach, scoped today to Singapore news. Phase 2 adds response-content generation; the strategic intent is to fuel a series of small round-table breakfast events Bonaventure wants to seed. Joyce is the human curator for the Singapore source list.

### Decisions made
- Build in-house — commercial monitoring tools previously evaluated were weak.
- Two-pass architecture: broad keyword/site filter first, then semantic theme matching.
- Quality over quantity: target 1–2 weekly nuggets, not a daily digest.
- Singapore first; framework is country-agnostic, swap the source list per country.
- Anchor with Joyce's recommended outlets; iterate the source list as signal/noise emerges.
- Twitter/X explicitly de-prioritised; LinkedIn deferred to Phase 1.5 (algorithm fight + Google-via-LinkedIn-search workaround acknowledged).
- Output is Slack-delivered conversation starters and content seeds — explicitly *not* a news summary.
- Trigger heuristic (Andrew): multi-theme intersection ⇒ priority 1.

### First-pass project requirements (v1 — expect refinement)
**Objective.** Surface a small, curated stream of Singapore market signals that the marketing team can repurpose into LinkedIn posts, conversation starters, and round-table seed content — without any salesy tone.

**In scope (Phase 1 — Singapore).**
- Sources: Straits Times, Business Times, gov.sg ministry sites (energy, sustainability, urbanisation, labour), niche REIT / asset-manager newsletters, key-account press-release pages — final list confirmed with Joyce.
- Pipeline: scheduled (daily) crawl → keyword filter → semantic theme match → ranked Slack post to a marketing channel.
- Theme profile: energy, sustainability, AI, labour, urbanisation, real estate / asset management, REITs, senior-government statements (PM / ministers).
- Volume target: 1–2 high-signal items per week reach the human; everything else stays filtered.
- Source-list management: trivial to add/remove sources, keywords, and themes as the team learns what's signal vs noise.
- Delivery: Slack post (channel TBD), framed as a conversation starter with link + 1–2 line angle hint.

**Out of scope (Phase 1).**
- Twitter / X scraping.
- Mainstream non-Asian financial press already covered by existing tools (Bloomberg etc.).
- Auto-publishing of content; content drafting is Phase 2.
- Multi-country generalisation (Phase 3).
- LinkedIn scraping (Phase 1.5).

**Phase 2 — content generation.** Skill that takes a surfaced item plus Janus context (Bonaventure's repository as a shared Claude skill) and proposes a draft (LinkedIn post / blog / white-paper outline) with an explicit angle (thought-leadership vs commercial — Andrew to define rubric).

**Phase 3 — multi-country.** Same framework; country-specific source list, accounts, and ministry list. Joyce-equivalent curator per country.

---

## Michael / Jehad / Andrew Weekly Meeting — 5 May 2026
**Attendees:** Michael Bruck, Jehad Altoutou, Andrew
**Source transcript:** [Fireflies — Michael, Jehad, Andrew Weekly Meeting](https://app.fireflies.ai/view/01KQVT19PCMHGNB9X38M9XSFSB)
**Duration:** 1h 11m

### Clean meeting summary
- Five-bucket marketing capability framework adopted (competitive analysis / brand voice / formatting / ICP+messaging / social outreach) — the structural backbone for every downstream marketing decision. Term "capabilities" deliberately chosen over "skills".
- CRM is non-negotiable as the company's system-of-record hub before SaaS phase-out; HubSpot leans favourite, Andrew running an AI matrix across HubSpot / Attio / Monday CRM / Salesforce. Bonaventure to be re-engaged on the CRM decision before he leaves next week.
- Brand identity refresh routed to UK agency (~£20k, 4–5 wks) — the one area they will not DIY; replaces Persegy work; deliverables will include corporate identity manual + deck templates + sales-enablement collateral.
- Website built in-house using Lovable / Claude / Stitch direction (not agency) — keeps brand-AI integration tight; CMS placement (inside CRM vs separate) still open.
- AI model split formalised: Opus default, Gemini for daily / deep research / image+video, Claude for reasoning + code + harness + Cowork. Markdown is the LLM default working format. Notebook LM banned for external decks.
- Stand up shared workspace immediately: Claude project "AI marketing" + Google Shared Drive folder + 3-person Slack channel — Jehad to action by 6 May.

### Decisions made
- Five-bucket marketing capability framework adopted as structural backbone.
- CRM is non-negotiable; HubSpot is Michael's lean; Andrew's matrix in flight; Bonaventure to be re-engaged this week.
- Brand identity refresh via UK agency (~£20k); the one DIY exception.
- Website built in-house (Lovable / Claude / Stitch direction).
- Markdown is the LLM default working format.
- AI model split: Opus default, Gemini for research+image+video, Claude for reasoning+code+harness+Cowork.
- Term "capabilities" preferred over "skills" for marketing-side framing.

### Key findings / discussions
- "Anti-AI-smell" content principle: external content must not look LLM-generated. Brand voice doc must enforce this.
- Long-term: phase off SaaS in 2–3 yrs; custom dashboards on top of databases; JanusD itself a future commercial offering.
- LinkedIn outreach automation feasibility uncertain due to tightened bot rules — needs scoping before committing to a marketing-outreach bot.
- Notebook LM banned for external presentations; Microsoft Copilot deemed weaker than Claude Office plugins.

### AI Registry / Tool Evaluation Outcomes
- [ai-registry] **AIR-77 HubSpot** — Tool already existed (Evaluating). Enriched with CRM matrix peers (AIR-83 Monday.com, AIR-76 Attio) and standup discussion.
- [ai-tool-evaluation] **AIR-77 HubSpot — Gate 1 (chained) — Result: PASS.** All 5 criteria met. Status remains Evaluating; queued for Stage 2.
- [ai-registry] **AIR-93 Salesforce** — Created in Backlog as benchmark/comparison anchor (not adoption candidate).
- [ai-tool-evaluation] **AIR-93 Salesforce — Gate 1 (chained) — Result: PASS.** Status moved Backlog → Evaluating. Stage 2 intentionally NOT chained.
- [ai-registry] **AIR-94 Attio (POSSIBLE DUPLICATE)** — Manual dedup required — verify whether AIR-76 and AIR-94 both exist and merge if duplicated.
- [ai-registry] **AIR-83 Monday.com** — Enriched with CRM-module use case alongside existing project-management context.
- [ai-registry] **AIR-5 Gemini (Google)** — Enriched with operational use-case decisions (daily/deep research, image+video gen, Canvas, split with Claude).
