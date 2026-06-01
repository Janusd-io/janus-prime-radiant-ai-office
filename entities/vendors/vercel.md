---
type: vendor
title: Vercel
slug: vercel
created: 2026-06-01
updated: 2026-06-01
departments: [marketing, technology]
status: active
confidence: high
sources: [marketing-stack-technical-writeup, agentic-lean-marketing-stack]
related: [cloudflare, cosmic, attio, resend, janus-website-cms, agentic-lean-marketing-stack, stack-composition-framework]
---

# Vercel

**Category:** Cloud Deployment & Hosting Platform
**AIR:** AIR-113 (Backlog → adopted for Janus marketing stack)
**Stack Composition score:** 3/3

Vercel is a cloud platform for frontend and full-stack web application deployment, built by the creators of Next.js. It provides zero-config CI/CD from GitHub, edge-function compute, and per-deployment preview URLs. As of 2026, Vercel reports ~30% of deployments are initiated by coding agents (approximately 75% via Claude Code specifically) — the first major hosting platform to confirm agent-initiated deployment as a default-mode usage pattern.

## Role in the Janus marketing stack

Selected as the hosting layer for `janusd.com` (and per-ccTLD deployments). The [[agentic-lean-marketing-stack]] recommends one Vercel project per ccTLD deployed from the same monorepo — clean per-region observability, per-region rollback, per-region deploy cadence. Combined with [[cloudflare]] in front for geo-routed DNS, Cloudflare Workers for edge logic, and [[cosmic]] for content. The pattern: Vercel owns the build + hosting layer; Cloudflare owns the perimeter and routing.

Data lock-in assessed as low: the Janus deployment does not use Vercel KV, Vercel Postgres, or Vercel Blob as primary data stores (code lives in GitHub; content in Cosmic). Migration to Cloudflare Pages from the same Next.js codebase is the known fallback.

## Stack Composition Framework scoring

- **Agent-operability:** ✅ — official MCP/Wrangler CLI; Vercel CLI is agent-operable; SDK for edge functions.
- **Reversibility:** ✅ — code in GitHub; no Vercel-proprietary storage dependencies in the Janus use.
- **Maintenance burden:** ✅ — zero-config deploys; GitHub integration handles CI/CD without manual pipeline maintenance.

## Watch for

- Reliability track record on Pro tier (Jehad to run 2-week monitoring window before full commitment).
- Fallback: Cloudflare Pages with same Next.js codebase if Pro reliability threshold not met.
