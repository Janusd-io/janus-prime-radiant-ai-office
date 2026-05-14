---
type: process
title: Platform & Tool Development Process
slug: platform-development-process
created: 2026-05-14
updated: 2026-05-14
captured_by: jehad-altoutou
audience: department
departments: [ai-office]
sources: [sub-process-platform-development, diagram-prompt-platform-development]
related: [ai-tool-evaluation, assessify-hr-assessment-platform, meeting-to-task-workflow, ims-process-document-shape, iso-9001-figure-1, jehad-altoutou]
---

# Platform & Tool Development Process

How a new internal platform — a custom tool, not a third-party purchase — goes from "we have a problem" to "live for the company" at Janus Digital. The long-form sibling of the [[meeting-to-task-workflow|Meeting→Task→Build sub-process]] and the [[ai-tool-evaluation|AI Tool Evaluation procedure]]. Process Owner: [[jehad-altoutou]]. The canonical worked example is [[assessify-hr-assessment-platform|Assessify]] (HR assessment platform).

## When this process applies

A platform build is *not* a small feature. Use this process only when:
- The pain point isn't solved by any third-party tool clearing Gates 1-4 of [[ai-tool-evaluation]] (build-vs-buy gate has been run first).
- Strategic approval from [[michael-bruck]] is on file before sunk cost grows.
- A deliberate stack choice fits Janus's standard tech stacks.
- Real handover to IT is expected at the end — not just "a Docker container running on someone's laptop."

## Nine stages from pain point to live

1. **Identify need** — pain point captured · build-vs-buy decided · Tool Evaluation run if relevant.
2. **Scope & approval** — one-pager · Obsidian project note created from `_TEMPLATE.md` · Linear AIP issue · Michael approves before any code is written.
3. **Stack selection** — pick from `05 Tech Stacks/` (SaaS Default · AI App · Creative Dev); justify any deviation in the project note.
4. **Sandbox build (phased)** — Phase 1A → 1B → 2A → …; each phase is a coherent vertical slice; isolated Docker + ngrok; **standing rule: never `docker compose down -v` unless schema changed**.
5. **Graphify + Obsidian sync** — `/graphify --update --obsidian` after each significant change; AI agents read the graph (~2400× token reduction) before raw source.
6. **AI / agentic layer** — n8n workflows · Claude Code skill or MCP connector · register in [[ai-registry|Linear AIR]] · auto-chained Gate 1 evaluation.
7. **Stress test + internal demo** — standard 5-area test (Functionality · UI/UX · Security · APIs · Stability) · requester sign-off gate.
8. **Documentation** — README + SOP + implementation plan (all three mandatory pre-handover).
9. **IT handover + go-live** — handover bundle to IT · IT acceptance recorded on AIP · production deploy with custom domain · TLS · SSO · backups · monitoring · cost allocation.

## The Obsidian-as-spine invariant

Every stage updates the Obsidian project note. **Note staleness is a process failure** — the auditor doesn't just see "we have docs," they see a continuously-updated knowledge graph that proves the docs are *living*, that decisions trace to commits, that AI agents reasoning over the codebase use the same source-of-truth as humans. Strong §7.5 + §9.1.3 evidence pattern.

## ISO clause coverage

- ISO 9001:2015 §8.3 Design and development · §8.5 Production and service provision · §7.5 Documented information · §9.1.3 Analysis and evaluation
- ISO/IEC 27001:2022 A.5.7 Threat intelligence · A.8 Asset management · A.8.25-A.8.34 Secure development
- ISO/IEC 42001:2023 §6.1 AI risk · §8.2 AI Impact Assessment (auto-chained Gate 1 for embedded AI components)

## Becomes

The Activities section of the **C2 (Software Development & Release)** IMS process document, once Process Owner assignments are confirmed.
