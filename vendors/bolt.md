---
type: vendor
title: Bolt
slug: bolt
air_id: AIR-89
status: Backlog
labels: [Functional, Technology]
departments: []
url: https://linear.app/janusd/issue/AIR-89/bolt
created: 2026-05-04
updated: 2026-05-04
captured_by: jehad-altoutou
audience: department
sensitivity: dept
sensitivity_confidence: 0.9
---
<!-- jb:air-vendor-callout -->
> Part of [[ai-registry|AI Registry]]


# Bolt

> AI Registry entry [AIR-89](https://linear.app/janusd/issue/AIR-89/bolt) — status **Backlog** as of 2026-05-04. Departments: —.

**Category:** AI App / Website Builder (chat-to-app, "vibe coding")
**Status:** Backlog
**Cost:** Free $0 (1M tokens/mo); Pro $25/mo (10M tokens); Teams $30/user (centralised billing); Enterprise custom (SSO, audit logs)
**Departments:** Technology (primary), Marketing, Commercial
**Entity:** StackBlitz

## Overview

StackBlitz's chat-to-app product, built on WebContainer browser-runtime. Pitches as "professional vibe coding tool" — multi-agent across frontier labs, large codebase support. Bolt Cloud bundles hosting/DBs/auth/integrations. Most "developer-feeling" of cohort.

## Capabilities

* Chat-to-build with [[figma|Figma]] + GitHub import
* Multi-agent across frontier labs (routes coding agents inside single UI)
* **WebContainer runtime** — full Node toolchain in browser
* Bolt Cloud — hosting, unlimited DBs, auth, custom domains
* Design system import (Porsche, WaPo, Material UI, Chakra, Shadcn customers)
* Auto test/refactor/iterate — "98% fewer errors"
* Large-project context — "1000× larger than prior limits"
* Private NPM registries on Teams

## Security & Compliance — WEAKEST IN COHORT

* **SOC 2: unclear public position** — Enterprise marketing references "compliance support" but NO public certification page
* GDPR: TBD; rely on StackBlitz privacy policy
* **No published trust center**
* SSO Enterprise only
* Audit logs Enterprise only
* Data residency: NOT publicly documented
* Training opt-out: NOT publicly documented
* Encryption/tenant isolation/abuse detection: TBD on public pages

**This is the weakest public compliance posture in the bakeoff cohort. Needs explicit clarification before Janus content goes near it.**

## Bakeoff Position

* **Vs [[lovable|Lovable]]**: Bolt's compliance posture is opaque outside Enterprise
* **Vs [[hercules|Hercules]]**: Hercules has SOC 2 Type I + GDPR-in-progress + privacy page
* **Vs [[replit|Replit]]**: Replit has SOC 2 Type II + more mature platform
* **Vs v0**: v0 has SOC 2 Type 2 (Vercel) + clearer enterprise security docs

## Considerations

* **Compliance gap** — biggest single concern
* Token-based pricing — predictability harder than seat-based
* Free tier exposure — easy shadow IT on personal accounts; needs domain controls
* Training/retention public stance not clearly documented

*Backlog. Functional tier. Compliance gap = sandbox/non-sensitive data only.*
