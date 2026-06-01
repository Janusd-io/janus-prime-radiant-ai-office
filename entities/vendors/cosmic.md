---
type: vendor
title: Cosmic
slug: cosmic
created: 2026-06-01
updated: 2026-06-01
departments: [marketing, technology]
status: active
confidence: high
sources: [marketing-stack-technical-writeup, agentic-lean-marketing-stack]
related: [vercel, cloudflare, attio, resend, janus-website-cms, agentic-lean-marketing-stack, stack-composition-framework]
---

# Cosmic

**Category:** Headless CMS
**AIR:** AIR-117
**Stack Composition score:** 3/3

Cosmic is a headless CMS selected as the content layer for the Janus marketing stack. REST-first with MongoDB-style query operators (industry-standard, portable), an official MCP server (17–18 tools), a published Agent Skill (`npx claude-skill add cosmic-headless-cms`), and multi-bucket multi-region architecture (5 buckets on Business at $499/month). Content exports in plain JSON — no lock-in.

## Role in the Janus marketing stack

Content layer for `janusd.com` and per-ccTLD deployments. The multi-bucket architecture maps directly to the Janus multi-region pattern: master bucket (global content) + per-region buckets (SG-specific case studies, UK-specific press). Cosmic's MCP and Agent SDKs explicitly support multi-bucket operation — an agent can query `janusd.sg` content separately from `janusd.com` content in a single context window.

Andrew Soane to prepare Cosmic requirements list by 2026-05-26 per the [[agentic-lean-marketing-stack]] brief. Full implementation follows the Singapore soft launch.

## Stack Composition Framework scoring

- **Agent-operability:** ✅ — 17–18-tool MCP server; published Agent Skill; REST-first query language (MongoDB-style, non-proprietary).
- **Reversibility:** ✅ — plain-JSON export; content not coupled to a Cosmic-specific schema language.
- **Maintenance burden:** ✅ — hosted; no CMS server to manage. Multi-bucket as a first-class feature, not a workaround.

## Why not Contentful or Adobe AEM

Contentful: hard limits on content types (48/150 max) and locales (3 on Basic); aggressive cost multiplication on multi-locale. AEM (AIR-121 Rejected): HTL templating accumulates vendor-specific state; wrong tier for Janus's size.

## Watch for

- Business plan pricing ($499/month) — justify vs. traffic and content volume before committing.
- Per-bucket permission model for multi-region content governance (SG vs. UK content approvals).
