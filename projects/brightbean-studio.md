---
type: project
title: Brightbean Studio
slug: brightbean-studio
created: 2026-05-14
updated: 2026-05-14
departments: [ai-office]
status: active
owner: jehad-altoutou
captured_by: jehad-altoutou
audience: [personal]
sources: [connection-page, connection-success, connection-expired, notification, digest, drawer, history, history-list, preferences, platform-icon-2, post-row, post-list, comment-list, comment-form, queue, org-queue, version-diff, version-diff-2, signup, logout]
related: [jehad-altoutou]
---

Brightbean Studio is Jehad Altoutou's personal side-project: a multi-tenant social-media management and approval platform aimed at agencies that manage clients' social presence. As of 2026-05-14, the codebase under `/Users/jehad/brightbean-studio/` is a Django + HTMX + Alpine.js + Tailwind app with `django-allauth` for sign-up (Google OAuth + email/password).

## Domain model (inferred from templates)

- **Org → Workspace → Post** hierarchy. An org (the agency) manages multiple workspaces (clients); each workspace has many posts.
- **Post** has versions (v1 initial through vN), platform_posts (one per target platform), media_attachments, comments. Statuses: `pending_review`, `pending_client`, `approved`, `changes_requested`, `rejected`. Supports `scheduled_at`.
- **Comment** has `visibility` (`internal` agency-only vs client-visible), attachments, one-level threaded replies.
- **Social account** is linked at workspace level via time-limited agency-issued connection links. Supported platforms: Facebook (Pages/Groups), Instagram (Business/Creator), LinkedIn (personal + company), TikTok, YouTube, Pinterest, Threads, Bluesky (handle + app-password), Google Business, Mastodon (instance URL), Twitter/X.
- **Notification** has event types: `post_approved`, `post_rejected`, `post_failed`, `post_published`, `post_submitted`, `post_changes_requested`, `new_inbox_message`, `social_account_disconnected`, `inbox_sla_overdue`, `report_generated`. Per-channel delivery preferences (matrix); quiet hours with IANA timezone; daily-digest email batching.

## Architecture signals

- **HTMX** for partial swaps (notification drawer mark-read, queue refresh on `approvalAction`/`bulkActionComplete` events).
- **Alpine.js** for client-side state (bulk-selection bar, modal show/hide, quiet-hours collapse).
- **django-allauth** for auth with Google OAuth as a social provider.
- **Tailwind** stone/orange palette (primary `#F97316`).
- Public site at `brightbean.xyz` (ToS + Privacy Policy live there per `signup.html`).

## Status (as of 2026-05-14)

Active personal project — not Janus dept work. Listed here for Jehad's own reference only; `audience: personal` so it does not federate to the AI Office instance.

## Open questions

- Whether this overlaps with any Janus marketing-stack tool decisions (e.g. Hootsuite / Buffer / Postiz evaluations).
- Monetisation / launch status — not visible in template-only capture.