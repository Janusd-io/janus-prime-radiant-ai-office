---
type: question
title: "Missing vendor / concept pages: OneCLI Agent Vault + Caddy"
slug: missing-vendor-pages-onecli-agent-vault-and-caddy
created: 2026-05-24
updated: 2026-05-24
departments: [ai-office]
status: active
owner: michael-bruck
related: [nanoclaw, nanoclaw-prime-radiant-wiring, hostinger, 2026-05-18-nanoclaw-as-personal-ai-coa-candidate]
---

# Missing vendor / concept pages: OneCLI Agent Vault + Caddy

Surfaced by the 2026-05-24 curation pass on the NanoClaude deployment ([[nanoclaw-prime-radiant-wiring]]). Both `[[onecli-agent-vault]]` and `[[caddy]]` are referenced load-bearingly in the new brief and will lint as broken references until pages are created.

## The two missing pages

### 1. OneCLI Agent Vault

**Trigger context.** OneCLI is the credential isolation primitive that NanoClaude depends on. Without it the per-container-data-control story collapses — secrets would have to live in container env vars, bound for the whole container's lifetime, with no per-agent allow-listing. The [[2026-04-22-per-user-data-control-hard-requirement-agent-platforms]] hard requirement is satisfied *by OneCLI*, not by NanoClaw itself.

**What the page would say (skeleton).**
- **What it is.** Local credential vault + outbound HTTP proxy. Distributed by NanocoAI (same outfit as [[nanoclaw|NanoClaw]]), but a separate product with its own SDK (`@onecli-sh/sdk`), CLI (`onecli`), and web UI (`http://127.0.0.1:10254`).
- **Architecture.** Runs as a local service on the host. Agent containers proxy outbound HTTP through it; OneCLI injects credentials at request time based on host-pattern matching and the per-agent secret allow-list (`selective` or `all` mode).
- **Key behaviours.** Per-agent secret allow-lists; host-pattern matching; approval gating for credentialed actions (server-side rule + host-side delivery callback); CA cert that agent containers must trust.
- **Janus deployment.** Active on Michael's MacBook as part of the NanoClaude install. Approval gating not yet configured. Known gotcha: agents start in `selective` mode with zero secrets — must be flipped to `all` or have specific secrets assigned via the `onecli` CLI.
- **Type.** Probably `vendor` (it's a distinct shipping product); could be argued as `concept` (it's an architectural primitive Janus has adopted). Vendor seems right — there's an upstream maintainer, a version cadence, a license, an issue tracker.

**Open questions.**
- Vendor page or concept page? Lean vendor.
- AIR triage? Probably yes — it's a tool we depend on, evaluation discipline applies. Would inherit much of the Gate 1 logic that AIR-103 NanoClaw established.
- Where does the "approval gating not configured" gap get tracked? In the OneCLI vendor page (limitation noted) or in a separate questions/ page about credentialed-action approvals? Defer until the gap becomes operational.

### 2. Caddy

**Trigger context.** Caddy is the reverse proxy planned to replace Ngrok as NanoClaude's public Slack-webhook receiver once the Hostinger migration ships (Monday item 2931866304, owner [[jehad-altoutou|Jehad]]; AIR-133 created 2026-05-22). When the migration lands, Caddy will be the load-bearing TLS + reverse-proxy layer between the public internet and the NanoClaude host process. It will also matter for any other public-facing Janus surfaces that the AIO touches.

**What the page would say (skeleton).**
- **What it is.** Open-source web server with automatic HTTPS via Let's Encrypt, written in Go. Often deployed as a reverse proxy in front of application servers. MIT license.
- **Janus use.** Reverse proxy + automatic TLS for the Hostinger-hosted NanoClaude instance (replacing Ngrok). Possibly other future internal services.
- **Why Caddy vs nginx vs Traefik.** Caddy's automatic-HTTPS-by-default is the deciding feature for this use case — no manual cert management, no certbot cron, no nginx-config-template gymnastics. Worth capturing the rationale on the page when written.
- **Type.** Vendor (open-source product with maintainer + versions). Linear AIR-133 already exists.

**Open questions.**
- Is Caddy worth its own page before the migration ships, or wait until it's actually running? Argument for now: lint will flag the broken ref every pass. Argument for later: writing a stub before deployment risks bit-rotting against the eventual config. Lean toward writing a thin stub now (just enough to satisfy the ref) and expanding when the migration lands.
- Does Caddy belong under `entities/vendors/` or somewhere else? Vendor is correct — same shape as nginx, Traefik would be if Janus used them.

## Proposed approach

Two options:

1. **Write both as thin stubs now.** Minimal frontmatter + 2–3 paragraph descriptions, status: `active` (OneCLI) / `monitored` (Caddy until deployment ships). Satisfies lint immediately. Risk: stubs become permanent thin pages if no one revisits them.

2. **Write OneCLI now, defer Caddy until Hostinger migration ships.** OneCLI is already deployed and operationally relevant; Caddy isn't until the migration completes. Acknowledged broken-ref will persist for Caddy. Risk: lint findings clutter until then.

Recommendation: **option 1** for both. The Caddy page can be 3 paragraphs (what it is, why Janus picked it, AIR-133 status as Sandbox-pending). OneCLI deserves a fuller treatment because it's load-bearing for the NanoClaude security model — closer to a half-page than a stub.

## Tangentially related — `curation` as a §5 workflow

This question page is itself an artefact of the new *curation* workflow (read-existing-evidence + ground-truth-against-live-install + synthesise + file follow-ups). Not strictly in scope here, but flagged in the 2026-05-24 12:46 `log.md` entry as a separate deferred item — should propose adding `curation` to CLAUDE.md §5 as a third named operation alongside Ingest / Query / Lint. Defer to a separate questions/ page when the moment arrives.

## Decision needed

Michael's call on:
1. Option 1 (both stubs now) vs option 2 (OneCLI now, Caddy deferred).
2. Vendor vs concept categorisation for OneCLI (vendor is the leaning).
3. AIR triage for OneCLI (probably yes; could inherit much of AIR-103's Gate 1 logic).
