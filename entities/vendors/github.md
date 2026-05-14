---
type: vendor
title: GitHub
slug: github
created: 2026-05-14
updated: 2026-05-14
departments: [ai-office, engineering]
status: active
confidence: high
related: [janus-prime-radiant-build, prime-radiant-storage-substrate, 2026-05-13-migrate-prime-radiant-vaults-from-google-drive-to-github, 2026-05-05-github-as-skill-library, obsidian, bonaventure-wong]
---

# GitHub

Code hosting and version control. As of 2026-05-13, **GitHub is the confirmed substrate for Prime Radiant vault sync** — personal repos, department repos, and (eventually) a company-level repo, all synced via the Obsidian Git plugin. Supersedes the earlier Google Shared Drive substrate, which streamed file content on demand and presented as empty directories to Claude / Cowork ingest passes (the failure mode that triggered the migration).

## Janus use

- **Prime Radiant vault substrate** for every instance. See [[prime-radiant-storage-substrate]] brief and [[2026-05-13-migrate-prime-radiant-vaults-from-google-drive-to-github]] decision.
- **Skill library** per [[2026-05-05-github-as-skill-library]] — canonical home for Claude skills (`/standup`, `/ai-registry`, `/ai-tool-evaluation`, `/ims-enrolment`, `/janus-pulse`).
- General software development infrastructure (out of scope for this wiki).

## Janus Org

`Janusd-io` GitHub Organization hosts the `janus-prime-radiant-template` repo (template seed for new instances; currently v0.9.0) and per-instance vault repos. AIO instance: `janus-prime-radiant-ai-office`. Currently on GitHub Free tier; Team upgrade (~$4/seat/month, unlocks enforced branch protection on private repos) pending [[bonaventure-wong|Bonaventure]] approval.
