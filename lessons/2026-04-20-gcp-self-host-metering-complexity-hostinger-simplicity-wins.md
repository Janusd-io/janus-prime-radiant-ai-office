---
type: lesson
title: GCP Metering Complexity vs Hostinger Simplicity — Self-Host Default Changed
slug: 2026-04-20-gcp-self-host-metering-complexity-hostinger-simplicity-wins
created: 2026-05-06
updated: 2026-05-13
status: resolved
owner: michael
departments: [ai-office, it-ops]
countries: [sg, gb, us]
confidence: high
sources: [aio-completed-action-items-archive, aio-weekly-status-2026-04-20-24, jehad-vault-2026-04-20-gcp-self-host-metering-complexity-hostinger-simplicity-wins]
related: [hostinger, google-cloud, n8n]
---

# Lesson: GCP Metering Complexity vs Hostinger Simplicity — Self-Host Default Changed

**Date:** 17–20 April 2026  
**Owner:** Jehad Altoutou (Inquiry), Michael Bruck (Decision)  
**Status:** Resolved  
**Confidence:** High  

## What happened

In mid-April, the AI Office was running a pilot to self-host [[n8n]] on Google Cloud. During the GCP setup phase, Jehad surfaced two critical issues:

1. **Metered per-cron billing:** Every N8N scheduled job triggers a Cloud Run invocation, metered at fractional rates. Setup alone showed $13–30 spikes. Projected annual cost trajectory: $4,290–5,000 over two years.
2. **DNS and subdomain complexity:** GCP requires Cloud CDN setup, DNS delegation to Google nameservers, and multi-step subdomain configuration under `janusd.io`. Setup friction was high.

In parallel, Hostinger was evaluated as a simpler alternative (flat-rate VPS under `janusd.io`):

- **Hostinger:** $920–1,020 for two years. 2 CPU / 8GB RAM / 100GB storage. Flat monthly fee. Docker-ready. One-click N8N installer. Root access to subdomain.
- **GCP:** Variable metering. Complex billing atomics. Best-in-class for managed services (Cloud SQL, TPU), not for straightforward container hosting.

## Why the old assumption failed

The original design assumed GCP because:
- Janus was already using Google Cloud for departmental services (HR, Marketing, some data pipelines).
- Managed services (Cloud Run, Cloud SQL) are GCP's strength.
- The assumption was that "we're already in GCP, so add N8N there."

**But:** N8N is not a GCP-native workload. It's a self-hosted container application. GCP's metering model (per-invocation, per-request) is designed for bursty, event-driven workloads — not steady-state container hosting. Hostinger's flat-rate VPS is the right tool for the job.

## The decision

On **20 April 2026**, the default self-hosting platform for AI Office tools was changed from GCP to Hostinger. **GCP narrowed to managed-service and departmental use cases only** (HR forms, Marketing databases, future Cloud SQL/TPU needs).

### Hostinger setup (completed 20 Apr)

- Payment processed via Anne.
- Malaysian data centre selected (first region; UK/EU revisited when UK office live).
- Company account established.
- DNS/subdomain under `janusd.io` verified and tested.

## Lesson learned

1. **Metering models matter more than vendor familiarity.** GCP is fantastic for managed services, but its pricing model punishes steady-state container hosting.
2. **"We're already in X" is not a reason to force fit.** Janus can use multiple cloud providers simultaneously. GCP + Hostinger + [[monday]] is better than forcing everything onto GCP.
3. **Flat pricing beats variable pricing for operational predictability.** Hostinger's transparent, flat fee eliminates billing surprises and eases capacity planning.
4. **Docker-ready and root access are production requirements for AI Office tooling.** Hostinger delivers both cleanly. GCP requires wrapper layers.

## Related decisions

- **2026-04-23 — Monday.com + Hostinger + Notion stack adopted** (this lesson directly informed that decision).

## Implications

- **N8N runs on Hostinger**, not GCP.
- **GCP** = managed services ground layer (Cloud SQL, Cloud Functions, TPU).
- **Hostinger** = self-hosted AI Office tools (N8N, future agents, infrastructure).
- **[[monday]]** = operations SoR.
- **[[notion]]** = documentation.

This separation of concerns simplifies both cost management and operational responsibility.

## Key quote

*"Hostinger is markedly cheaper ($920–1,020 for two years) with better specs (2 CPU / 8GB / 100GB) and flat monthly fee vs GCP's $4,290–5,000 metered trajectory. We're moving N8N to Hostinger."* — Paraphrased from Jehad and Michael, 20 April 2026.
