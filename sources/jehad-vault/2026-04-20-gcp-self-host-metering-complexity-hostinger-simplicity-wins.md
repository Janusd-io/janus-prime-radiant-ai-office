---
type: lesson
title: GCP metering complexity vs Hostinger simplicity — self-host default changed
slug: 2026-04-20-gcp-self-host-metering-complexity-hostinger-simplicity-wins
created: 2026-05-06
updated: 2026-05-13
departments: [ai-office, it-ops]
countries: [sg, gb, us]
status: resolved
owner: michael-bruck
confidence: high
sources: [jehad-vault-import-2026-05-13]
related: [hostinger, google-cloud, n8n]
captured_by: jehad-altoutou
---

> _Jehad's personal-vault articulation of this topic, imported 2026-05-13. The canonical wiki page is at `lessons/2026-04-20-gcp-self-host-metering-complexity-hostinger-simplicity-wins.md` — this file is preserved as a source for divergent framing / additional context._

# GCP metering complexity vs Hostinger simplicity

**Date:** 17–20 April 2026. **Owner:** Jehad Altoutou (inquiry), Michael Bruck (decision). **Status:** Resolved.

## What happened

In mid-April, the AI Office was running a pilot to self-host [[n8n]] on Google Cloud. During the GCP setup phase, Jehad surfaced two critical issues:

1. **Metered per-cron billing:** Every n8n scheduled job triggers a Cloud Run invocation, metered at fractional rates. Setup alone showed $13–30 spikes. Projected annual cost trajectory: $4,290–5,000 over two years.
2. **DNS and subdomain complexity:** GCP requires Cloud CDN setup, DNS delegation to Google nameservers, and multi-step subdomain configuration under `janusd.io`.

In parallel, [[hostinger]] was evaluated as a simpler alternative (flat-rate VPS under `janusd.io`): $920–1,020 for two years, 2 CPU / 8 GB RAM / 100 GB storage, flat monthly fee, Docker-ready, one-click n8n installer, root access to subdomain.

## Why the old assumption failed

The original design assumed [[google-cloud]] because Janus was already using Google Cloud for departmental services and managed services are GCP's strength. But n8n is not a GCP-native workload — it's a self-hosted container application. GCP's metering model (per-invocation, per-request) is designed for bursty, event-driven workloads, not steady-state container hosting. Hostinger's flat-rate VPS is the right tool for the job.

## The decision

On **20 April 2026**, the default self-hosting platform for AI Office tools was changed from GCP to Hostinger. **GCP narrowed to managed-service and departmental use cases only** (HR forms, Marketing databases, future Cloud SQL/TPU needs).

## Lesson learned

1. **Metering models matter more than vendor familiarity.** GCP is fantastic for managed services, but its pricing model punishes steady-state container hosting.
2. **"We're already in X" is not a reason to force fit.** Janus can use multiple cloud providers simultaneously.
3. **Flat pricing beats variable pricing for operational predictability.**
4. **Docker-ready and root access are production requirements for AI Office tooling.** Hostinger delivers both cleanly; GCP requires wrapper layers.

## Implications

- n8n runs on Hostinger, not GCP.
- GCP = managed services ground layer (Cloud SQL, Cloud Functions, TPU).
- Hostinger = self-hosted AI Office tools (n8n, future agents, infrastructure).
