---
type: brief
title: Agentic-lean marketing stack — why MCP-native tooling collapses SaaS sprawl risk for Janus
slug: agentic-lean-marketing-stack
created: 2026-05-19
updated: 2026-05-23
departments: [ai-office, marketing, it-ops]
confidence: high
sources: [marketing-stack-technical-writeup, 2026-05-19-aio-mktg-meeting, 2026-05-18-ai-native-ceo, 2026-05-12-aio-andrew-marketing, 2026-05-23-aie-singapore-5-person-conference-singh]
related: [stack-composition-framework, ai-tool-evaluation-framework, marketing-prime-radiant, janus-website, janus-website-cms, janus-crm-selection, singapore-launch, crm-evaluation-and-selection, mcp, claude-code, ai-native-mandate, post-rag-agent-data-stack, agent-skills, builders-sellers-measurers, ai-native-enterprise-restructuring, resend, 2026-05-23-aie-singapore-5-person-conference]
---

# Agentic-lean marketing stack — why MCP-native tooling collapses SaaS sprawl risk for Janus

The marketing stack is the most tool-dense surface in the company — CMS + CRM + email + edge + analytics + consent + analytics layers all interlock. With ~1 marketing-tech engineer planned for 2026 ([[andrew-soane]]'s 8–9 hires this year are nearly all marketing roles, not technical ones), a conventional martech stack is unmanageable. **The aha: MCP-native + agent-operable tooling, evaluated through the [[stack-composition-framework|Stack Composition Framework]], lets a one-engineer team run a stack that previously required a department.** This is the operating thesis behind the May 2026 marketing stack selections.

## Why this matters to the AI Office

The marketing stack decision is the **first concrete validation** of three converging AIO bets:

1. **Agentic-lean operating model.** The [[ai-native-mandate|AI-native mandate]] argues Janus can run more capability per head than conventional companies by routing operations through agents. Marketing tech is the highest-cardinality test case (8+ interlocking tools), so if agent-operation works here it works everywhere. The recommendation tells us we can give Andrew a full MarTech stack — CMS, CRM, transactional email, hosting, edge, consent, analytics — with one dedicated engineering head, *if* every tool is selected on the three lenses.
2. **Pre-G1 stack composition filter.** The framework is now a load-bearing analytical contribution of the AIO, not just a marketing-stack one-off. Proposed for inclusion in [[ai-tool-evaluation-framework]] as a pre-G1 filter; if ratified, future AI Registry triage gets faster and more architecturally sound.
3. **Compounding tool selection across domain Prime Radiants.** The marketing instance is the **second** Prime Radiant ([[marketing-prime-radiant]]). HR, Finance, IT/Ops, Office-of-CEO, Engineering, Training, ISO are queued. Every instance will eventually face a stack-composition decision in its own domain. The framework gives them a shared evaluation language — instead of every department head re-deriving "is this tool agent-operable?" from first principles, the answer is captured here and applied per-domain.

Operationally: the [[janus-website|janus.com / janusd.com website project]], the [[singapore-launch|Singapore launch]], the [[janus-crm-selection|CRM selection]], and the [[janus-website-cms|website CMS selection]] are all *locked in* on the basis of this framework as of 2026-05-19. Re-opening any of them requires either new vendor information or a defect in the framework itself.

## Below: the analysis

## What changed

Two structural shifts in 2024–2026 collapsed the operating cost of multi-tool stacks for lean teams:

- **MCP went from "Anthropic-shipped protocol" to "vendor-neutral default."** By mid-2026, every credible SaaS in Janus's adjacent categories ships an MCP server — Cosmic, Attio, Vercel, Cloudflare, Sanity, Contentful, Salesforce (60+ tools), HubSpot, Monday, Notion, Linear, Stripe, Resend, and hundreds of others. The "agent operability" lens went from speculative to commodity-grade.
- **Claude Code crossed an adoption threshold.** Vercel reporting 30% of deployments initiated by coding agents (~75% via [[claude-code]] specifically) is the load-bearing signal. The hour-long refactor of janusd.com from static HTML to TypeScript/React (Jehad, May 2026) is the local data point — Janus's own evidence that agent-operation is now a default mode, not an experiment.

Together: tool selection done right yields a stack a one-engineer team can run; tool selection done wrong (UI-first, proprietary query language, schema-in-the-UI) yields the same headcount drag as 2018-era martech.

## What was recommended — and why

| Layer | Pick | Score | Stack-composition reasoning | AIR ID |
|---|---|---|---|---|
| **CMS** | Cosmic | 3/3 | REST-first; MongoDB-style query operators (industry-standard); official MCP server (17–18 tools); published Agent Skill (`npx claude-skill add cosmic-headless-cms`); multi-bucket multi-region (5 buckets on Business at $499/mo); plain-JSON export | AIR-117 |
| **CRM** | Attio | 3/3 | Agent-native by design ("MCP server cannot be designed like a public API" — Attio positioning); MongoDB-style queries; relationship-graph data model with standard objects; published pricing (no "contact sales"); plain-JSON / CSV export | AIR-76 |
| **Email (transactional)** | [[resend]] | 3/3 (existing) | Already integrated; developer-first API + CLI; Broadcasts now covers marketing campaigns too — may obsolete the need to add Mailchimp | AIR-118 |
| **Hosting** | Vercel | 3/3 | Reliability concerns addressable on Pro tier; data lock-in low (code in GitHub; we're not using Vercel KV / Postgres / Blob as primary data store) | AIR-113 |
| **Edge / DNS / WAF** | Cloudflare | 3/3 | Wrangler CLI agent-rebuilt; official MCP server gives access to 2,500+ endpoints via 2 tools (`search()` / `execute()`); DA already familiar — onboarding friction near zero | AIR-116 |
| **Consent** | Cookiebot | TBD | Procurement target by 2026-06-02 (Singapore campaign legal pre-launch dependency) | AIR-124 |
| **Analytics** | Google Analytics | Production | Production layer for the marketing site | AIR-125 |

### What was rejected (and why the framework explains it cleanly)

- **Adobe AEM (CMS, 1.5/3)** — HTL templating + content fragments accumulate vendor-specific state; enterprise DXP pricing; wrong tier. Explicitly called out by Michael in the 2026-05-19 meeting as "legacy system." Linear: AIR-121 Rejected.
- **HubSpot CMS Hub (CMS, 1.5/3)** — HubL templating is HubSpot-proprietary; HubDB is HubSpot-only; MCP coverage read-heavy.
- **Salesforce (CRM, 2/3)** — Deepest MCP integration in the category but loses on reversibility because of Apex. Viable with the explicit constraint of writing zero Apex; risky once that line is crossed.
- **HubSpot (CRM, 2/3)** — Bundling play only; standalone weaker than Attio at our stage.
- **Contentful (CMS, 2/3)** — Mature, but hard limits on content types (48 / 150) and locales (3 on Basic) plus aggressive cost multiplication on multi-locale.
- **Klaviyo** — E-commerce-focused, overkill for B2B.

### Status as of 2026-05-19 (per AIO-Marketing meeting)

Andrew confirmed direction on Cosmic, Vercel, Cloudflare, Attio, Resend. Andrew to prepare requirements lists for Cosmic and Attio by 2026-05-26. Jehad to coordinate Vercel + Cloudflare setup with DA / IT by 2026-05-26. Mailchimp (AIR-111) moved Rejected → Backlog (hold-open) pending Andrew's decision on broadcast email tooling. Cookiebot procurement (AIR-124) due 2026-06-02. Michael preparing a holistic MarTech vendor assessment deck for [[bonaventure-wong]] (no hard due date).

## Multi-region pattern (technical answer)

The "multi-domain vs IP-based geo-routing" question raised by Jehad in standup resolves to a layered pattern:

1. **Single Next.js codebase**, locale-aware middleware (incoming domain preferred; IP fallback).
2. **One Vercel project per ccTLD** deployed from the same monorepo — clean per-region observability, per-region rollback, per-region deploy cadence.
3. **Cloudflare in front of all of them** — geo-routed DNS resolution gives the Singapore-resolved-IP / UK-resolved-IP locality [[bonaventure-wong|Bonaventure]] wants (DNS resolution itself becomes geo-routed via Cloudflare's POP map).
4. **Cosmic multi-bucket** — master bucket (global content) + per-region buckets (SG-specific case studies, UK-specific press). Cosmic's MCP and Agent SDKs explicitly support multi-bucket operation.

The Bonaventure demo test: VPN to Singapore, `dig janusd.sg`, see a Singapore-resolved Cloudflare IP. That's the "local presence" requirement met without per-region servers.

## Singapore launch — 10-day plan (no new tooling)

For the immediate 2026-09 Singapore lunch event (postponed from July 8–9 per [[2026-05-19-aio-mktg-meeting]]), the stack stays minimal:

1. Existing Next.js site on whatever hosting is current (Hostinger or already-migrated Vercel) with Cloudflare DNS in front.
2. Landing page form → Next.js API route → Google Sheet (using Jehad's personal Google account as a workaround until marketing service account provisioning lands).
3. [[resend|Resend]] for the white paper auto-reply.
4. Cookiebot for cookie / privacy compliance.
5. `/singapore`, `/singapore/thank-you`, `/privacy` pages — half-day of [[claude-code|Claude Code]] work on top of the existing build.

Cosmic, Attio, and the full MarTech orchestration come **in June** post-Singapore-soft-launch, on a six-week window leading into the (deferred) lunch event.

## Open items needing Michael's or Jehad's input

1. **Vercel reliability test** — 2-week monitoring window on Vercel Pro before committing fully ([[sentry]] + Vercel metrics). Fallback: Cloudflare Pages with same Next.js codebase.
2. **Google Sheet API permissions** — long-term marketing service account; raise with IT / DA.
3. **Cookie management service** — Cookiebot vs Iubenda vs OneTrust vs hand-rolled. Commodity tooling; Andrew can pick.
4. **hreflang implementation** — every multi-region page needs `<link rel="alternate" hreflang="...">`. Critical for SEO; dedicate a Claude Code session once Cosmic is in place.
5. **Privacy policy CLO review** — using Andrew's working draft for soft Singapore launch; CLO review before paid traffic.
6. **Building / product terminology** — Jehad to sync with Rosa on the property-management naming before the Singapore site goes wide.

## External validation — AI Engineer Singapore conference, 2026-05-23

Agrim Singh published a [writeup](https://x.com/agrimsingh/status/2057919355808288946) on 2026-05-23 of how a **5-person part-time team ran the AI Engineer Singapore conference for 1,000+ attendees** — see [[2026-05-23-aie-singapore-5-person-conference]] for the AIO pulse entry; source filed at [[2026-05-23-aie-singapore-5-person-conference-singh]]. Same operating model as this brief, executed at conference scale in Singapore.

Their stack overlap with Janus's marketing-stack picks is notable: **[[resend|Resend]]** is in both stacks (transactional + campaign email). They additionally used Convex (realtime backend), Next.js (web), Devin AI + OpenAI Codex + Cursor Cloud (build agents), Manus AI (browser outreach), and Notion (lightweight human-readable layer where it made sense). The architecture posture is identical: custom apps over a thin backend whenever a workflow repeats, agent-readable APIs over every internal system, lightweight human-readable layer only where state needs human eyeballs.

Singh's **seven operating principles** are the cleanest articulation yet of the operating model this brief argues for:

1. If data matters, put it in a backend.
2. If a workflow repeats, build a small app.
3. If staff need to inspect something, make an admin view.
4. If attendees need to act, give them a direct surface.
5. **If agents need to help, expose an API.**
6. If email depends on state, send from state.
7. If data is incomplete, save it anyway.

Principle 5 is the one this brief's [[stack-composition-framework]] doesn't yet cover explicitly. The framework's agent-operability lens currently asks: *is this vendor agent-operable?* Singh's piece adds: *have we exposed our own data layer so an agent can act on it?* Worth proposing as a candidate fourth lens or as an addendum to the existing agent-operability lens — *agent operability is symmetric: the tools we adopt must be agent-operable, and the systems we build around them must be agent-readable too*. For Janus this means the website CMS API surface, the CRM data layer, the email-state queries, and the standup pipeline all need to be queryable by an agent without screen-scraping.

External validation matters here for two reasons: (1) it shows the operating model is *being practised already in Singapore*, where Janus's [[singapore-launch]] is happening — relevant signal for the September 2026 launch lunch positioning; (2) it provides a 5-to-1000 ratio empirical proof point that mirrors the [[builders-sellers-measurers|Drucker frame]]'s large-scale claims (JPMorgan, Cloudflare) at small scale. Cite alongside the Cloudflare layoff-while-growing data when the position needs a relatable mid-size example.

## Cross-references

- [[stack-composition-framework]] — the three-lens framework that produced these picks.
- [[ai-tool-evaluation-framework]] — the formal G1–G4 framework this brief proposes to pre-filter.
- [[marketing-prime-radiant]] — the marketing-domain Prime Radiant where this thinking will compound across future tool decisions.
- [[singapore-launch]], [[janus-website]], [[janus-website-cms]], [[janus-crm-selection]] — the operational projects this brief locks in.
- [[ai-native-mandate]] — the procurement principle this brief operationalises for marketing.
- [[post-rag-agent-data-stack]] — sibling brief; both surface the same underlying shift (tooling re-shaped around agent consumption) but for different layers of the stack.
- [[ai-native-enterprise-restructuring]] — sibling brief on the enterprise restructuring thesis; the 5-person conference exemplar is the small-scale companion to the JPMorgan / Cloudflare / KPMG large-scale signals.
- [[builders-sellers-measurers]] — the Drucker frame; the 5-people-to-1000-attendees ratio is a clean small-scale instance of the frame's claim.
