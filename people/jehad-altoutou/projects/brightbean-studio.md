---
type: project
title: Brightbean Studio
slug: brightbean-studio
created: 2026-05-14
updated: 2026-05-14
status: active
owner: jehad-altoutou
captured_by: jehad-altoutou
audience: [personal]
confidence: high
sources: [feature-spec-social-media-management-v2, architecture, readme-5, requirements, security-2, contributing-2, graph-report-2, notification, digest, invite, magic-link, logged-in]
related: [django, htmx, postgresql, tailwind, hetzner, cloudflare-r2, resend]
---

# Brightbean Studio

**Personal open-source side project.** Brightbean Studio is Jehad's open-source, self-hostable social-media-management SaaS — agency / SMB / creator alternative to Sendible, SocialPilot, and ContentStudio. AGPL-3.0, Django 5 + HTMX + Alpine.js + Tailwind, Postgres 16 as both data store and job queue (django-background-tasks, no Redis/Celery).

The product spans ten platform integrations (Facebook, Instagram, LinkedIn, TikTok, YouTube, Pinterest, Threads, Bluesky, Google Business Profile, Mastodon) via a single abstract `SocialProvider` base class — adding a platform is one file in `providers/`. Multi-tenant org -> workspace -> member hierarchy with custom-roles RBAC and a separate external `Client` role for review/approval.

Deployment story prioritises Hetzner CX32 (~EUR10/mo) for the cloud version with one-click self-host buttons on Heroku/Render/Railway plus a documented bare-VPS Docker Compose path. Per `architecture`, Heroku Eco dynos are explicitly disallowed (sleep breaks the publisher worker). Inbound webhooks for Facebook/Instagram (HMAC-SHA256 verified) and YouTube (PubSubHubbub); polling-only fallback for the other platforms. AES-256-GCM at rest for OAuth tokens via HKDF-derived key.

## Status (2026-05-14)

Development-spec stage with working scaffolding. Spec v2 (`feature-spec-social-media-management-v2`) is 177KB and covers F-1.x through F-7.x feature blocks. Architecture companion (`architecture`) defines stack and deployment paths. Graphify report (`graph-report-2`) shows 2336 nodes / 8779 edges across the repo with `WorkspaceMembership` / `SocialAccount` / `Post` / `PlatformPost` / `Workspace` as god-nodes.

## Why this isn't in the AIO instance

Brightbean Studio is **Jehad's after-hours work, not Janus IP**. Pages are kept in `people/jehad-altoutou/private/` so they don't surface in the shared ai-office vault. They're filed here as a project hub purely for Jehad's own future reference.
