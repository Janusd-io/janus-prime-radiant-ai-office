---
type: decision
title: Janus Digital website hosts on Hostinger Node.js tier, not Vercel
slug: 2026-05-18-janus-website-hostinger-deploy
created: 2026-05-18
updated: 2026-05-18
status: resolved
owner: jehad-altoutou
decided_by: jehad-altoutou
departments: [marketing, ai-office]
countries: [sg]
confidence: high
related: [janus-website, andrew-soane, 2026-05-12-singapore-as-lead-market]
---

## Decision

The Janus Digital marketing website (`janusd.com`, with `janusd.sg` mirrored 301 → .com) is hosted on **Hostinger Node.js tier**, not Vercel. The same Hostinger account also holds DNS.

## Why

- Andrew Soane already lined up Hostinger as the campaign-stack substrate during the 2026-05-15 AIO/Marketing/IT meeting (one place to manage DNS + the landing page + GDPR posture). Switching to Vercel would have meant fragmenting hosting between two providers when the campaign is starting in a week.
- Hostinger's Node.js tier supports the bits we actually need: `npm run build && npm start` behind their process manager, env vars in hPanel, custom-domain routing to the Node app port.
- Site is small (5–10 routes); no need for Vercel-specific features like incremental static regeneration or edge functions.

## Trade-offs accepted

- We lose Vercel's preview-deploy-per-PR. Mitigated by local dev quality + the `next build` sanity check in the pre-commit / pre-push flow.
- We lose Vercel's `next/og` edge-rendered OG images. For Phase 1 we'll either ship a static OG image or render via a separate worker if needed.
- The form Route Handlers (`/api/leads`, `/api/white-paper`) require Node — a pure-static Hostinger plan won't work. We're on the Premium / Business tier.

## Mirror domain

`janusd.sg` is treated as a **301 redirect** to the equivalent `janusd.com` path, not as a separate hreflang'd country site. This keeps all SEO authority on one domain while preserving the Singapore presence Bonaventure wanted. Could be revisited later if Andrew wins his "country-folders on a single domain" architecture argument with Bonaventure.

## What to do with this decision

If the next person picks up the website work and proposes Vercel — point them here. The choice is made; revisit only if Hostinger's Node tier fails us at scale (cold-start latency, build constraints).
