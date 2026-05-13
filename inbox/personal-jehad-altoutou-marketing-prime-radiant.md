---
type: project
title: Janus Prime Radiant · Marketing
slug: marketing-prime-radiant
created: 2026-05-08
updated: 2026-05-13
departments: [marketing, ai-office]
status: active
owner: michael-bruck
sources: [pr-backup-2026-05-11-project-marketing-prime-radiant]
related: [andrew-soane, prime-radiant-marketing-rollout, janus-prime-radiant-build, llm-wiki, crm-evaluation-and-selection, singapore-news-monitoring]
audience: [department]
captured_by: jehad-altoutou
---

# Janus Prime Radiant · Marketing

Build hub for the Marketing-department Prime Radiant — a **full institutional knowledge base for the Marketing department**, not a "PR project." Scope clarified 2026-05-08: this is the second live Prime Radiant instance (after [[ai-office]]'s), with its own Google Shared Drive vault and its own `CLAUDE.md` derived from the AIO one. Pilot kicked off in the 2026-05-08 working session with [[andrew-soane]] (CMO).

> Dedupe note: see also the canonical stub [[prime-radiant-marketing-rollout]]; this is the richer build hub restored from PR backup. The curator should reconcile or merge.

## Origin

Authorised in the 2026-05-08 brainstorm with Andrew Soane. Michael demoed the AIO Prime Radiant to Andrew, walked through synthesised insights / concepts / projects / decisions / lessons / pulse / briefs, and Andrew's response was: build one for Marketing.

The originating context goes back further — the Marketing instance was anticipated in the 2026-05-07 decision when the AIO prototype was first validated.

## Scope

Stand up a Marketing-domain Prime Radiant that:
- Captures all the right Signals (Fireflies, Slack, CRM once selected, inbound web messages, emails, news scraping, competitor intel, industry analyst opinions across Janus's verticals — real estate, real assets, built environments, asset management, sustainability, private equity, credits).
- Documents the Infrastructure layer Marketing needs to make explicit (ICP, Target Personas, Bonaventure's mission, country plans, topic taxonomy).
- Generates Outputs that compress operational marketing work — strategic POVs, white papers, blog posts, marketing plans, campaigns + assets, positioning documents, reporting that feeds back to learning.

Inherits the three-layer architecture model from CLAUDE.md v0.8 (Signals / Infrastructure / Outputs).

## Architecture (per three-layer model)

**Signals layer (sensors):** Fireflies meeting transcripts; Slack threads (bookmarked); CRM (once selected — see [[crm-evaluation-and-selection]]); inbound web messages from janus.com forms; emails (CRM-routed); curated articles via Web Clipper; industry-vertical news feeds; competitor intel and industry analyst opinion pieces.

**Infrastructure layer (durable reference — required for Outputs):** Ideal Customer Profile (pending; Andrew action item); Target buyer Personas (pending); Mission and multi-year strategy (sourced from [[bonaventure-wong]] / [[office-of-ceo]]); Country plans (SGP W19 launch, GB W20 launch, expansion targets); Topic taxonomy (sustainability regulation, AI in real estate, asset management trends, finance verticals).

**Outputs layer (what the instance produces):** Strategic POV documents; white papers and long-form pieces; blog posts and short-form; marketing plans (annual / quarterly); campaign briefs + supporting assets (positioning *first*, then assets per Andrew); reporting decks feeding back into Signals as performance data.

## Build sequence

Per CLAUDE.md §1 Architecture build pattern (Signals → Infrastructure → Outputs):

1. **Signals first** (immediately doable): Fireflies + Slack + curated articles via Web Clipper.
2. **Infrastructure next** (Andrew dependency): ICP, Personas, mission, country plans documented as durable reference pages.
3. **Outputs follow** (when Infrastructure is in place): briefs, POVs, campaign drafts.

## Status (as of 2026-05-08)

- Greenlit: ✅.
- Vault topology decided: ✅ — separate Google Shared Drive folder + own `CLAUDE.md` derived from AIO one.
- Schema available: CLAUDE.md v0.8.
- Department entity page in AIO vault: created.
- Drive folder: not yet created — Michael action.
- Marketing CLAUDE.md: not yet authored. First draft will derive from AIO CLAUDE.md v0.8 with entity vocabulary adapted.
- Inputs status: Fireflies and Slack accessible; CRM blocked on [[crm-evaluation-and-selection]]; Web Clipper Marketing-themed channel pending setup.
- Infrastructure status: ICP / Personas / mission / country plans / topic taxonomy not yet documented. Andrew action item.

## Architecture work that proceeds pre-CRM

CRM-independent design work that should happen *now*:

1. **Vault stand-up** (Michael).
2. **Marketing CLAUDE.md derivation** (Michael).
3. **Infrastructure layer scaffolding** (Andrew + Michael).
4. **Federation linkages to AIO**.
5. **Seed entity pages**.
6. **Inaugural source ingest** — the 2026-05-08 Andrew brainstorm transcript filed in the Marketing vault as the originating source.

## Action items from the 2026-05-08 brainstorm

1. **Andrew**: read Michael's HubSpot CRM evaluation document.
2. **Andrew**: draw up signals / inputs / outputs sketch for the Marketing instance.
3. **Andrew**: be more disciplined about labelling speakers in Fireflies.
4. **Michael**: feed transcript back to Claude and seed the Marketing instance design.
5. **Michael**: expand CRM benchmark beyond HubSpot to Monday, Salesforce, HubSpot, Attio (Zoho on watch).
6. **Both**: align on CRM requirements — Andrew's draft has gaps; Michael adds MCP / agentic-capability as a hard criterion.

## Open dependencies

- **CRM selection** — gating dependency for Signals layer richness *only*.
- **Marketing infrastructure documents** — Andrew dependency.
- **Marketing CLAUDE.md derivation** — Michael action.
- **Federation mechanism** — cross-instance signal sharing is light at v0.8.
- **Tier 3 brief on the "10 → 2-3 strategic operators" hypothesis** — explicitly on hold.

## Cross-instance federation

Federates with: [[ai-office]] (AI tooling decisions); [[office-of-ceo]] (mission, strategy, country plans); [[hr]] (employer brand crossover).
