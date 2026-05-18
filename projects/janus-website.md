---
type: project
title: Janus Digital marketing website (janusd.com)
slug: janus-website
created: 2026-05-15
updated: 2026-05-18
captured_by: jehad-altoutou
status: active
owner: jehad-altoutou
departments: [marketing, ai-office]
countries: [sg]
confidence: working
audience: department
path: /Users/jehad/Desktop/Claude Projects/JanusDigital Website
repo: https://github.com/Janusd-io/janus-website
branch: phase-1/singapore-landing
related: [singapore-news-monitoring, marketing-prime-radiant, ai-native-janus-positioning, 2026-05-12-singapore-as-lead-market, 2026-05-14-janus-singapore-white-paper-storms-ahead, joyce-woo, andrew-soane]
---

# Janus Digital marketing website

The public-facing marketing site for **Janus Digital Singapore Pte. Ltd**. Rebuild driven by the [[2026-05-12-singapore-as-lead-market|Singapore lead-market decision]] and the 8–9 July 2026 executive lunch, with the [[2026-05-14-janus-singapore-white-paper-storms-ahead|"How agentic AI can answer the storms ahead" white paper]] as the gated lead magnet.

## Status — 🟢 Active

Phase 1 in flight on `phase-1/singapore-landing`. All routes live locally; nothing deployed yet.

## Stack

- **Framework:** Next.js 15 App Router + TypeScript, root at `web/`
- **Styling:** Tailwind with custom Janus tokens; Montserrat via `next/font`
- **Motion:** Framer Motion v11 (`--legacy-peer-deps` for React 19 RC peer-dep)
- **Icons:** Lucide
- **Forms:** Zod-validated Route Handlers → Google Sheets (service account) + Resend (white-paper delivery)
- **Hosting target:** Hostinger Node.js tier (premium/business plan)
- **Domains:** janusd.com primary, janusd.sg mirror (301 → .com)

## Brand

Official Janus Branding v1.0 (`web/public/janus-brand-guidelines.pdf`) applied:

| Token | Hex | Role |
|---|---|---|
| Main | `#FCB745` | Energy, reality (yellow) |
| Sub 01 | `#000000` | Structure, transition (black) |
| Sub 02 | `#013A7D` | Technology, digital space (navy) |
| Sub 03 | `#028CDC` | Azure accent |
| BG | `#FFFFFF` | Pure white |

Typography diverges from the guidelines — Montserrat across the board for both display and body (the guideline says Arial for body; the user rejected that on review).

## Routes

- `/` — upgraded home with hero video, 5 highlight cards (with brand-illustrated backgrounds), stats, AI Brain video showcase, Property Types grid, contact form
- `/platform` — Stats strip, **VoltAgent-style topology diagram** (asset systems → Janus operating layer → outputs, with travelling yellow current pulses), four capability cards, commercial model band
- `/insights/white-paper` — fully **gated**; only path to the PDF is the email-capture form
- `/contact` — full contact form
- `/privacy`, `/cookies` — draft (pending Simla review)
- `/api/leads`, `/api/white-paper` — lead capture endpoints

## Key decisions

- *(2026-05-12)* [[2026-05-12-singapore-as-lead-market|Singapore is Janus's lead commercial market]] — drives the site's geographic focus and the Singapore lunch flow
- *(2026-05-15)* Hosted on Hostinger, not Vercel — see [[2026-05-18-janus-website-hostinger-deploy]]
- *(2026-05-15)* White paper gated behind email capture — see [[2026-05-18-gated-white-paper-pattern]]
- *(2026-05-15)* Removed the standalone Singapore lunch subpage in favour of routing the demo CTA to `/contact`
- *(2026-05-18)* Typography locked to Montserrat across the board, diverging from the Brand Guidelines body-font spec (Arial) — to be defended with Andrew on review

## Performance

- Hero MP4 lazy-loaded via `DeferredVideo` (poster paints first, video mounts after idle); plus the hero video was ffmpeg-recompressed from 14 MB to 932 KB
- Showcase tab videos 59 / 41 MB → 2 MB each
- Total media weight on a full home-page visit: **114 MB → ~5 MB**
- First-load JS on home: 168 KB

## Outstanding blockers

1. Andrew Soane to review the brand application
2. Simla to review the draft privacy policy
3. Provisioning before launch: Google Sheets (`Leads` tab + service account), Resend API key, GA4 ID (consent-gated), DNS for both domains
4. OG image `/og.png` not yet in `web/public/`
5. Hostinger Node.js account access for deploy

## Handover note

`HANDOVER.md` at the repo root captures the full live state, the nine critical lessons from this build cycle, the dev-server recovery one-liner, named blockers, and recommended next moves. Next Claude session should read it first.
