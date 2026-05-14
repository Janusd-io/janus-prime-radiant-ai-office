---
type: project
title: Assessify ISO/IEC 27001:2022 audit package
slug: assessify-iso-27001-audit-package
created: 2026-05-14
updated: 2026-05-14
departments: [ai-office, iso]
status: active
owner: jehad-altoutou
audience: department
captured_by: jehad-altoutou
sources: [iso-audit-package, sop, readme]
related: [assessify, assessify-hr-assessment-platform, iso-compliance-programme, iso-ims-puls, hostinger]
---

First formal ISO/IEC 27001:2022 audit package for [[assessify]], authored by Jehad Altoutou and dated 28 April 2026 (per `iso-audit-package`). v1.0, internal classification, written against Annex A 2022 — designed to extend cleanly to ISO 27017 (cloud) / 27018 (cloud PII) / SOC 2 if engagement scope shifts.

## Scope

- **In scope:** Assessify application on [[hostinger]] VPS (Kuala Lumpur), SQLite production DB in Docker volume, source code on GitHub, Resend email transit, Caddy reverse proxy, adjacent n8n container, nightly backups (30-day rotation), MCP/OAuth integration endpoint.
- **Out of scope:** candidate/employee personal devices, Janus corporate IT estate, Hostinger's hypervisor (covered by supplier attestations).

## Roles

- System owner / day-to-day ops / incident response: Jehad Altoutou.
- Data controller: Janus Digital HR.
- Data processor: Assessify.
- Hosting: Hostinger International Ltd.
- Email: Resend.
- CI: GitHub Actions.

## Key controls documented

- TLS 1.2+ via Caddy/Let's Encrypt; bcrypt-12 password hashing; HMAC-SHA256 session tokens with 24h httpOnly cookies; OAuth 2.1 + PKCE-S256 for MCP (1h access / 60d refresh).
- Audit log captures every admin action and every MCP tool call with userId, action, target, IP, UA, timestamp.
- Nightly SQLite `.backup` at 03:00 UTC, 30-day rotation.
- Auth gate on every `/api/admin/*` endpoint (verified by automated probe).
- Rate limits per endpoint (60 req/min on `/api/mcp`, 5/min on login etc.).

## Open audit items (most likely findings)

| Item | Severity | Target close |
| --- | --- | --- |
| No off-site backup — all 30 backups on same VPS | High | +30 days from audit |
| Per-category retention policy not documented in HR data-protection policy | Medium | +60 days |
| CSP / X-Frame-Options not set at app layer (relying on Caddy defaults) | Low | +60 days |
| Annual access-review process not scheduled | Low | Add to quarterly review |

## Why this matters

The audit package is the first concrete Assessify artefact that maps directly into the [[iso-ims-puls]] programme. It demonstrates the IMS pattern at the **single-platform** level — what a single AI Office-owned system looks like when documented to ISO 27001 Annex A 2022. The 27017/27018/SOC 2 extension hooks make it the prototype for how the AIO will package other internal SaaS systems for the PULS audit-ready surface.
