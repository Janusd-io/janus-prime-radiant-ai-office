---
type: vendor
title: Nomi Internal Intelligence
slug: nomi
created: 2026-05-14
updated: 2026-05-14
confidence: low
captured_by: jehad-altoutou
audience: [department]
sources: [readme-6, setup]
related: [jehad-altoutou, notion, linear, fireflies]
migrated_from: entities/vendors/nomi.md
---
Native macOS Swift/SwiftUI AI desktop companion that lives in the MacBook notch. Created under bundle ID `com.antigravity.nomi`; captured 2026-04-21 from `~/Desktop/Claude Projects/Nomi-Internal-Intelligence/`. As of capture date the project is personal R&D, not a Janus deliverable — listed here only because the OAuth-design notes in `setup` contain reusable Janus-relevant patterns.

## Architecture (per source)

State-machine driven UI (`CompanionState` transitions across `idle`, `listening`, `thinking`, `speaking`, `needsApproval`, `success`, `error`); `NSWindowController` for a borderless floating window attached to the notch; SwiftUI for UI and animations; Xcodegen to avoid `.xcodeproj` merge conflicts. Tools span Google Calendar (CRUD + invite + join), Gmail (search + send), [[linear]] (issue create), [[notion]] (search + page read + meeting-note publish), [[fireflies]] (transcript list + fetch).

## Reusable patterns surfaced for AIO

Per `setup`, Jehad documented two patterns worth lifting into AIO process knowledge: (1) Google OAuth in Testing mode supports up to 100 test users without verification — viable indefinitely for small beta cohorts, the yellow 'unverified' warning is click-through. (2) The Gmail scope economics: `gmail.readonly` + `gmail.send` are sensitive-tier (no annual cost); `gmail.modify` is restricted-tier and triggers a ~$15-75k annual third-party security assessment past 100 users. Staying on sensitive-tier scopes is the cost-conscious default.

## API vs MCP rationale (Nomi today)

Nomi uses direct API adapters because they exist and OpenAI function-calling is more battle-tested than its MCP client support, and retrofitting MCP would require a tool-dispatch refactor. The 2026-04 stance was: revisit MCP when adding a service for which no adapter exists (Slack, GitHub, Salesforce) — many of those ship MCP servers now.

Confidence is `low` (single-source personal repo).
