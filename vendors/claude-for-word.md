---
type: vendor
title: Claude for Word
slug: claude-for-word
air_id: AIR-81
status: Evaluating
labels: [Legal, Commercial, Office of CEO, Functional]
departments: [office-of-ceo]
url: https://linear.app/janusd/issue/AIR-81/claude-for-word
created: 2026-04-20
updated: 2026-04-20
captured_by: jehad-altoutou
audience: department
sensitivity: dept
sensitivity_confidence: 0.9
---
<!-- jb:air-vendor-callout -->
> Part of [[ai-registry|AI Registry]]
> Departments: [[office-of-ceo]]


# [[claude|Claude]] for Word

> AI Registry entry [AIR-81](https://linear.app/janusd/issue/AIR-81/claude-for-word) — status **Evaluating** as of 2026-04-20. Departments: office-of-ceo.

**Category:** AI Document Agent (Word Add-in)
**Cost:** Included with Claude Team ($25/seat) or Enterprise. Also via Bedrock/Vertex AI/Foundry.
**Departments:** Legal, Commercial, Office of CEO
**Assignee:** Michael Bruck

## Overview

Anthropic's native Microsoft Word add-in. Brings Claude's reasoning/writing into Word. Purpose-built for professionals working extensively with documents — accelerates review, redlining, drafting workflows. Companion to Claude for Excel ([[claude-by-anthropic-in-excel|AIR-30]]) and PowerPoint ([[claude-for-powerpoint|AIR-63]]).

## Capabilities

* Document review and redlining — triage counterparty redlines, produce counter-redlines via native tracked changes
* Drafting from templates — Claude populates structured content from briefs, prior drafts
* Multi-section reasoning — reads ENTIRE document for context/consistency
* Consistency passes — terminology, tone, defined terms, cross-references
* Conversational editing in natural language
* Cross-app conversation — shares context with Excel and PowerPoint add-ins
* Skills support — packageable workflows (contract reviews, client reports)

## Integrations

* Microsoft Word native add-in (Marketplace) — Windows + Mac
* Cross-app with Claude Excel/PowerPoint
* LLM gateway: Bedrock / Vertex AI / Foundry

## Security

* Inherits Anthropic enterprise (SOC 2 Type II, GDPR, HIPAA-eligible)
* No training on enterprise data
* Works within existing compliance framework — Claude already Core Infrastructure
* LLM gateway via Vertex AI for data residency in Janus [[google-cloud|Google Cloud]] tenant

## Considerations

* **Low Marketplace rating** — 1.4/5 from 18 ratings. Sample reviews during evaluation.
* No new vendor relationship — Claude already approved
* Word documents often contain client-confidential/privileged content — confirm Teams data protections sufficient
* Tracked changes fidelity test needed — round-trip with counterparty markups
* Overlap with Microsoft 365 Copilot for Word

*Evaluating. Functional tier. Companion to AIR-30 (Excel) and AIR-63 (PowerPoint).*
