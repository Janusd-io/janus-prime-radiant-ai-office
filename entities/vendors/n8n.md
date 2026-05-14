---
type: vendor
title: n8n
slug: n8n
created: 2026-05-14
updated: 2026-05-14
departments: [ai-office, engineering]
status: active
confidence: medium
related: [hostinger, monday, 2026-04-22-self-host-n8n-on-hostinger, 2026-04-20-gcp-self-host-metering-complexity-hostinger-simplicity-wins, 2026-04-23-monday-hostinger-notion-stack-adopted]
---

# n8n

Open-source workflow automation platform (Zapier-style). Self-hosted at Janus per the 2026-04-22 decision to self-host on [[hostinger]] rather than [[google-cloud|GCP]] — the per-trigger metering complexity of GCP was the trigger; n8n on Hostinger keeps automation costs predictable.

## Janus use

- Workflow glue for ingestion pipelines feeding the AI Office (Fireflies → Monday → wiki).
- Part of the three-tool stack adopted on 2026-04-23: [[monday]] (ops SoR) + [[hostinger]] (self-host substrate, including n8n) + [[notion]] (docs).

## Posture

Workflow automation isn't an AI tool (per the 2026-05-06 taxonomy decision — see [[2026-05-06-ai-tool-taxonomy-scope-policy]]), but n8n's role in stitching together AI tooling (webhook receivers for Fireflies, scheduled triggers for ingest jobs) makes it load-bearing operational plumbing. Retained where the work is plumbing; superseded by purpose-built [[agent-skills|Claude skills]] where the work is AI-shaped.
