---
type: vendor
title: Hostinger
slug: hostinger
air_id: AIR-79
status: Sandbox
labels: [Technology, AI Office Infrastructure, Core Infrastructure]
departments: [ai-office]
url: https://linear.app/janusd/issue/AIR-79/hostinger
created: 2026-04-20
updated: 2026-04-22
captured_by: jehad-altoutou
audience: department
sensitivity: dept
sensitivity_confidence: 0.9
---

# Hostinger

> AI Registry entry [AIR-79](https://linear.app/janusd/issue/AIR-79/hostinger) — status **Sandbox** as of 2026-04-22. Departments: ai-office.

**Category:** IaaS / VPS Hosting — self-hosted AI Office infrastructure
**Cost per User/Month:** Flat VPS pricing — ~$8-12/month baseline 2-year term
**Number of Licences:** 1 VPS (N8N) initially
**Total Monthly Cost:** ~$40-45 (baseline)
**Departments:** AI Policy, Technology

**Legal entity:** Hostinger International Ltd — Kaunas, Lithuania. Founded 2004. ~1,000+ employees. 2024 revenue ~$100M. 29M customers. Ranked #2 in FT & Statista Long-term Growth Champions Europe 2026. Tesonet shareholder group (same investor cluster as NordVPN).

## Overview

IaaS provider — VPS, cloud hosting, managed WordPress, domain registration, growing one-click Docker app library. Chosen as Janus's primary infrastructure host after 20 Apr 2026 GCP pilot surfaced unpredictable metered billing, single-CPU specs at equivalent cost, DNS complexity. Hostinger VPS delivers dedicated root-access servers at flat predictable fee, Docker-ready Ubuntu, one-click deploys for N8N, NemoClaw.

## Key Decision: GCP → Hostinger Migration (20 April 2026)

April GCP pilot exposed opaque, non-forecastable unit costs (egress, per-request charges). Hostinger KVM VPS pricing significantly cheaper for same N8N workload. Decision: move N8N to Hostinger VPS. Transparent fixed monthly pricing, Malaysia regional DC, Docker-native, one-click N8N app. GCP retained only for managed-service departmental projects.

## Capabilities

* VPS (KVM-based) — dedicated CPU/RAM/NVMe with root SSH. Baseline: 2 CPU / 8GB / 100GB
* Ubuntu (default), Debian, CentOS, Rocky, AlmaLinux
* One-click catalogue: N8N, NemoClaw, OpenClaw, LLAMA/Ollama, WordPress, GitLab, Nextcloud
* Docker-native, Docker Compose pre-configured
* Weekly automated backups + one free manual rollback
* 13 DC partners: NA, UK, France, Germany, NL, Finland, Lithuania, India, Indonesia, Malaysia, Singapore, Brazil
* Managed DNS panel
* Domain registration & transfer

## Integrations

* Public REST API — developers.hostinger.com
* **Official MCP server** — github.com/hostinger/api-mcp-server
* Official SDKs: PHP, Python, TypeScript
* Postman collection
* Google Workspace email routing support
* No native Slack notifications (workloads can use webhooks)
* Control-panel auth: email + password + 2FA; no SAML/OIDC SSO at panel level

## Security & Compliance

* ISO/IEC 27001 certified
* GDPR — EU-headquartered, full compliance regime
* Data Processing Addendum (DPA) — explicit Customer Data protection clause
* Configurable jurisdiction at deploy time
* Automated weekly + manual snapshot/rollback

## Considerations

* **Data-training ToS ambiguity (Gate 1 condition)** — VPS-specific interpretation needs vendor-confirmed via DPA. Draft letter flagged.
* No SSO at control panel — per-user accounts with 2FA
* Financial-approval gate — new finance process requires Anne approval
* IaaS not PaaS — no managed databases, Vertex-style ML services, TPU access
* DevOps responsibility sits with Jehad — low ongoing effort given Docker + one-click but not zero

## Relevance

Pragmatic compromise between full hyperscaler sprawl (GCP/AWS) and back-of-napkin side project. For 30-person AI Office needing to host N8N, NemoClaw, LLAMA, future SaaS pilots — but no DevOps team — Hostinger flat pricing and one-click deploys remove "become DevOps engineer first" tax that hit Jehad on GCP. Official API + MCP server means Claude can drive VPS lifecycle programmatically.

*Moved to Evaluating 20 Apr 2026 following reversal of 17 Apr GCP hosting decision. Promoted to Sandbox 22 Apr.*
