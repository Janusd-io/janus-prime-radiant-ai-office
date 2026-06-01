---
type: vendor
title: OneCLI Agent Vault
slug: onecli-agent-vault
created: 2026-06-01
updated: 2026-06-01
departments: [ai-office, technology]
status: active
confidence: high
sources: [nanoclaw-prime-radiant-wiring]
related: [nanoclaw, hostinger, caddy, 2026-04-22-per-user-data-control-hard-requirement-agent-platforms]
---

# OneCLI Agent Vault

**Category:** Local Credential Vault & Outbound HTTP Proxy
**AIR:** Not yet in AIR — triage recommended (inherits much of AIR-103 NanoClaw's Gate 1 logic)
**Vendor:** NanocoAI (same organisation as [[nanoclaw|NanoClaw]])

OneCLI Agent Vault is a local credential isolation primitive that NanoClaw depends on for its security model. It is the technical solution to the [[2026-04-22-per-user-data-control-hard-requirement-agent-platforms|per-user data control hard requirement]] — without it, secrets would have to live in container environment variables, exposing them for the container's entire lifetime with no per-agent allow-listing.

## Architecture

Runs as a local service on the host machine. Agent containers proxy all outbound HTTP through OneCLI, which:

- Injects credentials at request time based on host-pattern matching rules
- Enforces per-agent secret allow-lists (`selective` mode = only explicitly assigned secrets; `all` mode = all secrets for that agent)
- Provides approval gating for credentialed actions (server-side rule + host-side delivery callback)
- Issues a CA certificate that agent containers must trust (so TLS inspection can inject credentials mid-request)

SDK: `@onecli-sh/sdk`. CLI: `onecli`. Web UI: `http://127.0.0.1:10254`.

## Janus deployment (as of June 2026)

Active on Michael Bruck's MacBook as part of the NanoClaw install. Approval gating has not yet been configured. Agents start in `selective` mode with zero secrets by default — must be flipped to `all` or have specific secrets assigned via the `onecli` CLI. This is a known operational gotcha for new NanoClaw deployments.

## Why this is load-bearing

The NanoClaw security argument depends entirely on OneCLI. Without per-agent credential isolation, the "container per agent = isolated from other agents" promise breaks — a compromised agent container could exfiltrate secrets from the host environment. OneCLI closes this gap by ensuring credentials are never in the container at all; they're proxied in at request time, scoped to what that agent's allow-list permits.

## AIR status

Not yet in AIR. Recommended for AIR triage — it is a distinct shipping product (separate SDK, CLI, versioning, issue tracker) from NanoClaw. Gate 1 evaluation can inherit much of AIR-103's logic (same vendor, same security model, complementary scope).

## Watch for

- Approval gating configuration: not yet set up on Michael's instance. Should be addressed before NanoClaw is used for any credentialed production action.
- Hostinger deployment: when NanoClaw moves to Hostinger (Monday item 2931866304), OneCLI moves with it. The host-pattern matching rules will need updating for the new environment.
