---
type: vendor
title: Cloudflare
slug: cloudflare
created: 2026-06-01
updated: 2026-06-01
departments: [marketing, technology, it-ops]
status: active
confidence: high
sources: [marketing-stack-technical-writeup, agentic-lean-marketing-stack]
related: [vercel, cosmic, attio, janus-website-cms, agentic-lean-marketing-stack, stack-composition-framework]
---

# Cloudflare

**Category:** CDN, Edge Network & Security Platform
**AIR:** AIR-116 (Backlog → adopted for Janus marketing stack)
**Stack Composition score:** 3/3

Cloudflare is a global cloud platform providing content delivery, DDoS protection, DNS management, Web Application Firewall, and edge compute (Workers / Pages). Its MCP server exposes 2,500+ API endpoints via two tools (`search()` / `execute()`), making it one of the most agent-operable infrastructure platforms available. Wrangler CLI is fully agent-rebuildable. The DA (DevOps/Admin) is already familiar — onboarding friction near zero for Janus.

## Role in the Janus marketing stack

Sits in front of all Vercel deployments as the perimeter layer. Provides: geo-routed DNS resolution (Singapore-resolved IP for `janusd.sg`; UK-resolved IP for `janusd.com/gb`), WAF, DDoS mitigation, and Cloudflare Workers for edge logic (locale-aware middleware, A/B testing without cold starts). The Bonaventure demo test: VPN to Singapore → `dig janusd.sg` → see a Singapore-resolved Cloudflare IP. That's the "local presence" requirement met without per-region servers.

Combined with [[vercel]] (hosting), [[cosmic]] (content), and [[attio]] (CRM) as the four corners of the agent-friendly Janus marketing stack.

## Stack Composition Framework scoring

- **Agent-operability:** ✅ — 2,500+ endpoints via MCP server; Wrangler CLI agent-rebuildable.
- **Reversibility:** ✅ — DNS can be migrated; WAF rules are portable; no Cloudflare-proprietary data storage.
- **Maintenance burden:** ✅ — DA-familiar; Workers edge-compute requires minimal server management.

## Vercel + Cloudflare pattern

Per [[agentic-lean-marketing-stack]]: one Vercel project per ccTLD (same monorepo) + Cloudflare geo-routed DNS. Combined: `janusd.sg` resolves to Singapore POP, `janusd.com` resolves to global nearest POP. Single Next.js codebase handles locale routing.

## Watch for

- Worker script limits on the Free tier (100k requests/day) — monitor if Singapore launch drives material organic traffic.
- Cloudflare for SaaS (custom domains for multi-tenant sites) as a future consideration if Janus builds tenant-facing portals.
