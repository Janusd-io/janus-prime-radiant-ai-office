---
type: vendor
title: Dubai Property Leads
slug: dubai-property-leads
created: 2026-05-14
updated: 2026-05-14
confidence: medium
captured_by: jehad-altoutou
audience: [department]
sources: [llms, readme-7]
related: [jehad-altoutou, hostinger]
migrated_from: entities/vendors/dubai-property-leads.md
---
UAE-based B2B PropTech marketplace selling verified Dubai off-plan and investor real-estate leads to brokers and agencies. Founded by [[jehad-altoutou]] (per `readme-7`, captured 2026-04-23) — listed here as a vendor entity because the platform is a working production system that surfaces in Jehad's tech-stack discussions; it is not a Janus product.

As of 2026-04-23 the public surface (`dubaipropertyleads.ae`) markets four lead tiers from 25 leads at 150 AED/lead to 600 leads at 115 AED/lead plus a custom Enterprise tier (2000+ leads). The product differentiates on exclusivity (no shared inquiries), 24-48 hour freshness, multi-channel acquisition (Google Ads / Meta / SEO), and a manually-validated replacement guarantee for invalid leads. The stack is Next.js 14 App Router + Tailwind + Postgres in Docker, deployed on a [[hostinger]] VPS via Traefik reverse proxy and a custom `deploy_secure.exp` Expect script that streams the build over SCP and rebuilds the container over SSH.

A separate Real Estate Data API (`/real-estate-api`) exposes 2,700+ off-plan projects with unbranded floor plans via a cached JSON API and is marketed as an Enterprise platform alongside the lead-buyer marketplace.

Relevance to AIO: provides an existence-proof of the SaaS Default Stack pattern in production under Jehad's direct ownership — comparable architecture to internal platforms like [[assessify]]. Confidence is `medium` because all knowledge here is from a single source captured by the owner.
