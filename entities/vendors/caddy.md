---
type: vendor
title: Caddy
slug: caddy
created: 2026-06-01
updated: 2026-06-01
departments: [ai-office, technology]
status: active
confidence: high
sources: [nanoclaw-prime-radiant-wiring]
related: [nanoclaw, hostinger, onecli-agent-vault, ngrok]
---

# Caddy

**Category:** Open-Source Web Server / Reverse Proxy with Automatic HTTPS
**AIR:** AIR-133 (Sandbox)
**License:** Apache 2.0

Caddy is an open-source web server written in Go, best known for automatic HTTPS via Let's Encrypt — TLS is on by default with no manual certificate management, no certbot cron jobs, and no nginx config-template gymnastics. Frequently deployed as a reverse proxy in front of application servers.

## Role in the Janus NanoClaw deployment

Planned as the reverse proxy + TLS layer replacing [[ngrok|Ngrok]] when NanoClaw migrates from Michael Bruck's MacBook to a Hostinger VPS (Monday item 2931866304). Once deployed:

- Caddy receives inbound HTTPS requests from Slack's webhook system (NanoClaw's Slack events API endpoint)
- Terminates TLS (auto-managed Let's Encrypt cert for the Hostinger domain)
- Proxies traffic to the NanoClaw container running on the same host

This eliminates the Ngrok dependency, removes the "tunnel up when Michael's laptop is on" availability constraint, and gives NanoClaw a stable, production-grade public endpoint on Hostinger.

## Why Caddy vs nginx vs Traefik

The deciding factor is **automatic HTTPS by default**. For a single-service Hostinger deployment, Caddy's one-stanza config (`reverse_proxy localhost:3000` with automatic cert provisioning) is vastly simpler than nginx (certbot cron + config templates) or Traefik (Docker labels + ACME config). The `Caddyfile` is human-readable, agent-editble, and idempotent — Claude Code can safely modify it.

## Status (as of 2026-06-01)

Not yet deployed. Pending NanoClaw migration to Hostinger. AIR-133 created 2026-05-22 (Sandbox). Page created per the `missing-vendor-pages-onecli-agent-vault-and-caddy` escalation to close the broken `[[caddy]]` wikilink in [[nanoclaw-prime-radiant-wiring]].

## Watch for

- NanoClaw Hostinger migration (Monday 2931866304, owner Jehad Altoutou) — Caddy deployment is a sub-step of that migration.
- Caddyfile backup in the Janus GitHub repo — infrastructure config should be version-controlled.
- Port binding on Hostinger VPS: confirm 443 is open and 80 is redirected to HTTPS before going live.
