---
type: project
title: Singapore Launch
slug: singapore-launch
created: 2026-05-12
updated: 2026-05-19
status: active
owner: andrew-soane
captured_by: jehad-altoutou
departments: [marketing, ai-office, it-ops, office-of-ceo]
countries: [sg]
sources: [2026-05-12-aio-andrew-marketing, marketing-stack-technical-writeup, 2026-05-19-aio-mktg-meeting, 2026-05-18-ai-native-ceo, 2026-05-15-singapore-marketing-launch-plan-v1, 2026-05-14-janus-singapore-white-paper-storms-ahead]
related: [janus-website, janus-website-cms, janus-crm-selection, agentic-lean-marketing-stack, marketing-prime-radiant, joyce-woo]
audience: department
---

# Singapore Launch

The first regional launch of Janus's outbound presence. Originally targeting an 8–9 July 2026 client lunch; **postponed to September 2026** per [[bonaventure-wong|Bonaventure]] and [[joyce-woo|Joyce]]'s assessment that Singapore lacks sales and delivery capacity to absorb hot-shot leads before then ([[2026-05-19-aio-mktg-meeting]]). The supporting marketing campaign continues on the original timeline — only the in-person lunch event slips.

## Stack (operational, no new tooling for soft launch)

Per the [[agentic-lean-marketing-stack]] thesis, the Singapore soft launch runs on the **already-in-place** tooling. New tools (Cosmic, Attio) land in June post-soft-launch.

1. **Hosting** — whatever's hosting the Next.js site (current Hostinger setup or Vercel if migration has happened by then). Cloudflare DNS in front.
2. **Code** — Next.js codebase in GitHub. Single codebase, regional content via Jehad's existing IP-based geo-routing or domain-based middleware.
3. **Forms** — `/singapore` landing page form submits to a Next.js API route that writes to a Google Sheet via the Sheets API. Workaround: Jehad uses his own Google account (since the marketing service account isn't yet provisioned by IT) and shares the sheet with Andrew.
4. **Email** — [[resend|Resend]] for the white-paper auto-reply.
5. **Privacy / cookie consent** — Cookiebot (AIR-124) inserted via script tag. Procurement target 2026-06-02 (Andrew).
6. **Pages** — `/singapore`, `/singapore/thank-you`, `/privacy`. Half-day of [[claude-code|Claude Code]] work on top of the existing site.

## Hard pre-launch dependencies

- **Cookie compliance (Cookiebot)** — Andrew to procure by 2026-06-02.
- **Privacy policy** — Andrew to draft and publish by 2026-06-02. Working draft in hand; CLO review needed before paid traffic but CLO hasn't joined yet.
- **`dig janusd.sg` returns a Singapore-resolved IP** — Cloudflare DNS configuration. This is [[bonaventure-wong|Bonaventure]]'s "local presence" demo test.
- **White paper attachment ready** — `2026-05-14-janus-singapore-white-paper-storms-ahead.pdf` already filed; final review pending.

## Multi-region pattern (applied here first)

Singapore is the first concrete test of the multi-region pattern documented in [[agentic-lean-marketing-stack]] and the website project hub:

1. Single Next.js codebase in GitHub.
2. Vercel project pointed at `janusd.sg`.
3. Cloudflare in front, with Singapore-edge DNS resolution.
4. (Post-Cosmic onboarding, June) — SG bucket in Cosmic for Singapore-specific overrides.

When UK launches, it's a clone exercise: new Vercel project, new Cloudflare-routed DNS, new bucket / locale. Days of work, not weeks.

## Stakeholders

- **Operational lead:** [[andrew-soane]]
- **Engineering lead:** [[jehad-altoutou]]
- **Singapore market lead:** [[joyce-woo]]
- **Strategic veto / approval:** [[bonaventure-wong]]
- **AI Office sponsor:** [[michael-bruck]]

## Timeline (as of 2026-05-19)

- **2026-05-26** — Andrew's CMS + email requirements lists; Jehad's Vercel + Cloudflare coordination with DA/IT.
- **2026-06-02** — Cookiebot procurement + privacy policy live.
- **2026-06-XX** — Soft launch: `/singapore` page goes live, campaign runs.
- **2026-06–07** — Cosmic comes in. Migrate content from hand-coded Next.js into Cosmic. Set up MCP + Agent Skill.
- **2026-06–07** — Attio CRM. Import the Google Sheet leads as seed data.
- **2026-09** — Lunch event with hot-shot clients (postponed from July).

## Watch for

- CLO joining — privacy policy hard dependency for paid traffic.
- DA / IT capacity to coordinate Vercel + Cloudflare setup by 2026-05-26.
- Vercel reliability over the soft-launch window (Jehad's Vercel reliability concern is being addressed by Pro tier + 2-week monitoring before commit).
- Whether the postponement to September creates campaign pacing issues — campaign goes ahead even without the lunch event.
