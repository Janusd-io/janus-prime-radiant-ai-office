---
type: vendor
title: Hostinger
slug: hostinger
created: 2026-05-06
updated: 2026-05-12
departments: [it-ops, ai-office]
status: active
confidence: medium
sources: [aio-2026-05-06]
related: [linear, ai-tool-evaluation, 2026-04-20-gcp-self-host-metering-complexity-hostinger-simplicity-wins, google-cloud]
---

# Hostinger

Web hosting and infrastructure provider. At Janus, in active use — auto-promoted from Evaluation → Sandbox in Linear AIR by the standup skill v3.12 on 2026-05-06 upon noticing active use. The auto-promotion was cited in [[aio-2026-05-06]] as validation that the sub-skill orchestration design works.

## Status

- **Linear AIR stage:** Sandbox (as of 2026-05-06)
- **Classification:** Infrastructure (vs Tool) per the [[ai-tool-evaluation]] Tool/Infrastructure/Workload framework. Confirm during next gate review — Infrastructure classification has implications for which Gate 1 criteria apply.

## Why Hostinger (vs the alternative)

Adopted in preference to [[google-cloud|GCP]] self-hosting on metering-complexity grounds: ~$920–1,020 (Hostinger) vs ~$4,290–5,000 (GCP) for equivalent self-hosted workloads. See [[2026-04-20-gcp-self-host-metering-complexity-hostinger-simplicity-wins]] for the full lesson — the recurring cost overhang of GCP's per-resource metering vs Hostinger's flat plan was the deciding factor.

## Watch for

- Gate 2 / Gate 3 evaluation outcomes if Janus moves it toward Production.
- Workload candidates running on Hostinger — those need their own G1.2 / G1.4 evaluations per the framework.
