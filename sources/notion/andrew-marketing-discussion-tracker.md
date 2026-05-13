---
type: source
notion_url: https://www.notion.so/357114fc090c81d08791f0cfccd9c515
notion_id: 357114fc-090c-81d0-8791-f0cfccd9c515
title: Andrew / Marketing — Discussion & Task Tracker
source_type: notion-page
fetched: 2026-05-06
---

# Andrew / Marketing — Discussion & Task Tracker

Persistent log of weekly meetings with **Andrew** (UK-based marketing leader, recently joined) covering AI-augmented marketing strategy, brand, CRM, content, and outbound. Follows standup format.

## Latest: Bonaventure / Andrew / Michael — Singapore News Monitoring — 6 May 2026

**Attendees:** Bonaventure Wong, Andrew Soane, Michael Bruck
**Duration:** ~32 min

### Summary

Bonaventure asked Michael to build an AI agent surfacing Singapore market signals (news, government releases, analyst newsletters) to seed thought-leadership content, LinkedIn engagement, and conversation starters. Quality-over-quantity bar: 1–2 nuggets per week. Two-pass architecture: wide keyword/site collection, then semantic theme matching. Andrew framing it as same find-and-react capability discussed for LinkedIn outreach, scoped today to Singapore. Phase 2 adds response-content generation; strategic intent is fueling round-table breakfast events Bonaventure wants to seed.

### Key decisions

- Build in-house — commercial monitoring tools previously weak.
- Two-pass: broad keyword/site filter first, then semantic theme matching.
- Quality: 1–2 weekly nuggets, not daily digest.
- Singapore first; framework country-agnostic, swap source list per country.
- Anchor with Joyce's recommended outlets; iterate source list as signal/noise emerges.
- Twitter/X explicitly de-prioritised; LinkedIn deferred to Phase 1.5.
- Output is Slack-delivered conversation starters and content seeds — explicitly NOT news summary.

### Phase 1 scope

**In scope:** Straits Times, Business Times, gov.sg ministry sites, niche REIT/asset-manager newsletters. Themes: energy, sustainability, AI, labour, urbanisation, real estate/asset management, REITs, PM/minister statements. Volume: 1–2/week to human.

**Out of scope:** Twitter/X, mainstream non-Asian press, auto-publishing, multi-country, LinkedIn scraping.

**Phase 2:** Content generation skill. **Phase 3:** Multi-country generalisation.

---

## Michael / Jehad / Andrew Weekly Meeting — 5 May 2026

**Attendees:** Michael Bruck, Jehad Altoutou, Andrew
**Duration:** 1h 11m

### Summary highlights

- **Five-bucket marketing capability framework adopted:** competitive analysis / brand voice / formatting / ICP+messaging / social outreach — structural backbone for every downstream marketing decision.
- **CRM is non-negotiable as SoR** before SaaS phase-out. HubSpot leans favourite; Andrew running AI matrix across HubSpot / Attio / Monday CRM / Salesforce. Bonaventure to be re-engaged.
- **Brand identity refresh routed to UK agency** (~£20k, 4–5 wks) — one area they will NOT DIY; replaces Persegy work.
- **Website built in-house** using Lovable / Claude / Stitch direction — keeps brand-AI integration tight.
- **AI model split formalised:** Opus default, Gemini for daily/deep research/image+video, Claude for reasoning+code+harness+Cowork. Markdown is LLM default format. NotebookLM banned for external decks.
- **Shared workspace stood up immediately:** Claude project "AI marketing" + Google Shared Drive + 3-person Slack channel (Jehad to action by 6 May).

### Key decisions

- Five-bucket marketing capabilities framework as structural backbone.
- CRM non-negotiable; HubSpot lean; Andrew's matrix in flight; Bonaventure to be re-engaged this week.
- Brand refresh via UK agency (~£20k); only DIY exception.
- Website built in-house (Lovable/Claude/Stitch direction).
- Markdown is LLM default format.
- Opus default, Gemini for research+image+video, Claude for reasoning+code+harness+Cowork.
- Term "capabilities" preferred over "skills" for marketing framing.

### Key findings

- *"Anti-AI-smell" content principle:* external content must not look LLM-generated. Brand voice doc must enforce.
- Long-term: phase off SaaS in 2–3 years; custom dashboards on databases; JanusD itself a future commercial offering.
- LinkedIn outreach automation feasibility uncertain — needs scoping.
- NotebookLM banned for external presentations; Copilot weaker than Claude Office plugins.

### Monday items created/updated

- AI marketing workspace setup (Claude project + Drive + Slack)
- Brand identity refresh — UK agency (~£20k, 4–5 wks)
- Marketing capabilities framework (5 buckets)
- Website CMS build (in-house: Lovable/Claude/Stitch)
- CRM evaluation updated with matrix runs

### AI Registry outcomes

- **AIR-77 HubSpot — Gate 1 PASS.** All 5 criteria met. Status remains Evaluating; queued for Stage 2.
- **AIR-93 Salesforce — Created in Backlog as benchmark.** Gate 1 PASS; status Backlog→Evaluating (benchmark, not adoption candidate).
- **AIR-94 Attio — Possible duplicate.** Subagent reported no existing entry; HubSpot subagent reported AIR-76 exists for Attio. Manual dedup required.
- **AIR-83 Monday.com — Enriched** with CRM-module use case alongside project-management context.
- **AIR-5 Gemini — Enriched** with operational use-case decisions.

---

## Standing context

**Andrew's role:** UK-based marketing leader, recently joined; co-leading marketing direction with Michael. Owns brand identity, CRM matrix, capabilities framework.

**Cadence:** Weekly with Michael + Jehad. Fireflies recorded; processed via standup methodology.

**No Monday account yet** — Andrew-owned tasks are narrative-only attribution.

---

## How to maintain

For each new Andrew weekly meeting:
1. Add new `## <title> — DD Mon YYYY` section at top.
2. Use standup template: Attendees, Source, Summary, 🎯 / 📅 / 🏔️ next steps, Decisions, Findings, Monday items, Linear AIP, AIR outcomes.
3. Marketing tasks live in **Marketing Department** group on board 5095012818. Cross-cutting CEO items go in **Office of CEO**.
4. Per Step 3G of standup skill, every new Monday item gets Context Update immediately.
