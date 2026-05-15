---
type: vendor
title: Hercules
slug: hercules
created: 2026-05-04
updated: 2026-05-04
status: Backlog
confidence: low
sources: [2026-05-04-bonaventure-michael-jehad-and-andrew-meeting]
related: []
audience: department
captured_by: jehad-altoutou
departments: []
air_id: AIR-87
---
<!-- jb:air-vendor-callout -->
> Part of [[ai-registry|AI Registry]]


# Hercules

Vendor stub created from meeting [[2026-05-04-bonaventure-michael-jehad-and-andrew-meeting]] on 2026-05-04.

_Mention context:_ test tool driving the registry-pipeline walkthrough

_To populate: replace this stub with real content and remove this notice._


---

## AI Registry — AIR-87

> [[linear|Linear]]: [AIR-87](https://linear.app/janusd/issue/AIR-87/hercules) · status **Backlog** · updated 2026-05-11.

**Category:** AI App / Website Builder (chat-to-app, "vibe coding")
**Status:** Backlog
**Cost:** Freemium; Business tier unlocks SSO/SAML; Enterprise custom
**Departments:** Technology (primary), Marketing, Commercial
**Entity:** Zeus AI Labs (SF)

## Overview

AI app/website builder. Chat with AI agent to build full-stack web and mobile applications. Claims 100k+ users. Competes with [[lovable|Lovable]], [[replit|Replit]], [[bolt|Bolt]], v0. **Differentiator: batteries-included stack** — auth, database, backend, payments, email, push, file storage, AI gateway, analytics, hosting all built-in + provisioned automatically. Plus first-class mobile (App Store / Play Store) and commerce.

## Capabilities

* Chat-to-build agent — SaaS apps, eCommerce, internal tools, mobile, microsites
* Multi-agent modes
* Built-in backend stack (managed DB, auth, storage, email, push, AI gateway, analytics)
* Native Commerce module (SaaS subs, physical/digital goods)
* Mobile builds + App Store/Play publishing
* Embedded code editor, version control, secrets, environments, security audit, code download
* Visual edit + AI image generation
* One-click publish (Hercules domain or custom)

## Security

* SOC 2 Type I (Type II on roadmap)
* GDPR claimed (cert in progress)
* HIPAA listed for Enterprise (verify with BAA)
* TLS 1.3 in transit, AES-256-GCM at rest
* Tenant isolation, audit logs, RBAC
* Data residency: US (Virginia) or EU (Frankfurt); Enterprise can pin
* **Default-on AI training** — Team/Enterprise can disable
* Identity: SAML 2.0 (Okta, Entra ID, Workspace, OneLogin, Auth0, Ping); SCIM on Enterprise

## Bakeoff Cohort

In same cohort as Lovable ([[lovable|AIR-88]]), Replit ([[replit|AIR-32]]), Bolt ([[bolt|AIR-89]]), v0 ([[v0|AIR-90]]). Janus should pick ONE primary vibe-coding tool, not approve all five.

## Considerations

* SOC 2 Type II not yet achieved (vs Lovable's strongest in cohort)
* Default-on training is concern
* Pricing tiers not publicly listed
* Long-term portability of generated apps off Hercules Cloud unverified
* Janus already on Cloudflare + Convex via Hercules — coupling concern

*Backlog. Functional tier. Bakeoff cohort with Lovable/Replit/Bolt/v0.*
