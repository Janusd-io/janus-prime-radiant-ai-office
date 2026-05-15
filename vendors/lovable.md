---
type: vendor
title: Lovable
slug: lovable
air_id: AIR-88
status: Backlog
labels: [Functional, Technology]
departments: []
url: https://linear.app/janusd/issue/AIR-88/lovable
created: 2026-05-04
updated: 2026-05-04
captured_by: jehad-altoutou
audience: department
sensitivity: dept
sensitivity_confidence: 0.9
---

# Lovable

> AI Registry entry [AIR-88](https://linear.app/janusd/issue/AIR-88/lovable) — status **Backlog** as of 2026-05-04. Departments: —.

**Category:** AI App / Website Builder (chat-to-app, "vibe coding")
**Status:** Backlog
**Cost:** Free; Pro $25/mo (100 credits shared unlimited users); Business $50/mo (SSO, team workspaces, RBAC, security); Enterprise custom
**Departments:** Technology (primary), Marketing, Commercial
**Entity:** Stockholm-based

## Overview

Highest-profile entrant in chat-to-app cohort. Claims millions of projects, tens of thousands per day. **Most enterprise-mature** of bakeoff cohort: SOC 2 Type II + ISO 27001 + GDPR, EU/US/Australia residency, SAML SSO + SCIM, explicit "no training on customer data."

## Capabilities

* Chat-to-build with image/screenshot/PDF input
* Templates marketplace (sizeable catalogue)
* Visual editing in-canvas
* **Lovable Cloud** — managed hosting + DB + auth with regional residency
* First-party integrations directory
* Mobile app (recently launched)
* Publishing controls: separate edit/approve/publish permissions; production publish can require approval
* Automatic security scanning (RLS policies, schema, app code, deps)
* **Code ownership** — generated code is yours; full export

## Security & Compliance — Cohort Leader

* ✅ **SOC 2 Type II**
* ✅ **ISO 27001**
* ✅ **GDPR** with DPA
* Trust center: trust.lovable.dev
* **Data residency: EU/US/Australia**
* **No model training** on customer prompts/code/workspace data
* Multi-tenant logical isolation, server-side RBAC, encrypted scoped secrets
* WAF + adaptive rate limits + abuse detection
* Automatic secret rotation without redeployment

## Bakeoff Position

**Strongest compliance position in cohort** — SOC 2 Type II + ISO 27001 + GDPR today. Pro plan shared across unlimited users (cost-efficient). Explicit no-CI/CD-access posture (IT-friendly).

**Vs Hercules (AIR-87):** Lovable wins on compliance + community/templates; Hercules wins on integrated stack (commerce, mobile).
**Vs Replit (AIR-32):** Lovable targets non-developers; Replit targets developers.
**Vs Bolt (AIR-89):** Lovable materially stronger compliance; Bolt has WebContainer runtime.
**Vs v0 (AIR-90):** Both mature; v0 Vercel/Next.js-coupled, Lovable end-to-end.

## Considerations

* Lovable Cloud lock-in for hosting (portability needs verification)
* Pricing opaque once credit consumption scales
* Primarily web-only (mobile newer)

*Backlog. Functional tier. Compliance front-runner of bakeoff cohort.*
