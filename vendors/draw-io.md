---
type: vendor
title: draw.io
slug: draw-io
air_id: AIR-95
status: Evaluating
labels: [Functional, AI Policy, Technology]
departments: []
url: https://linear.app/janusd/issue/AIR-95/drawio
created: 2026-05-08
updated: 2026-05-08
captured_by: jehad-altoutou
audience: department
sensitivity: dept
sensitivity_confidence: 0.9
---
<!-- jb:air-vendor-callout -->
> Part of [[ai-registry|AI Registry]]


# draw.io

> AI Registry entry [AIR-95](https://linear.app/janusd/issue/AIR-95/drawio) — status **Evaluating** as of 2026-05-08. Departments: —.

**Category:** Diagramming / Process & Architecture Modelling (open-source, XML-based)
**Cost:** $0 — fully free and open source (Apache 2.0)
**Departments:** AI Policy, Technology — broad cross-department use expected
**Entity:** JGraph Ltd. (maintainer)

## Overview

Free, open-source diagramming application. Flowcharts, BPMN, UML, network diagrams, ERDs, mind maps, org charts, ISO-style process diagrams. Runs as browser app, Electron desktop (Win/Mac/Linux), and embeddable libraries. Files stored locally or in Drive/OneDrive/GitHub/Dropbox.

**Defining feature for Janus:** native file format is fully open, human- and AI-readable XML — can be round-tripped through automation without lossy export.

## Capabilities

* Comprehensive shape libraries: ISO/BPMN, UML, AWS/Azure/GCP, networking, Lean/Six Sigma, ERD, mind-map
* Multi-runtime: browser, free Electron desktop, self-hosted Docker
* Open XML file format (`.drawio` / `.xml`) — mxGraph schema, plain text, diff-friendly
* SVG/PNG exports embed source XML — single image file is also re-editable diagram
* Storage-agnostic: local disk, Git, Drive, OneDrive, Confluence, S3/GCS
* Confluence/Jira/Notion integration
* Offline-first desktop
* Versioning-friendly (plain XML in Git)

## Integrations

* Confluence, Jira (Atlassian Marketplace)
* Drive, OneDrive, SharePoint, Dropbox, GitHub, GitLab, Nextcloud
* Notion (image/embed), Slack (shared file/preview)
* **[[vs-code|VS Code]] extension** (Hediet draw.io Integration)
* Self-hosted Docker
* CLI export tools, headless rendering for CI
* **AI/automation: any LLM ([[claude|Claude]], [[chatgpt|ChatGPT]]) can read, write, generate, modify diagrams** via open XML

## Security & Compliance

* Open source (Apache 2.0)
* Local-first by default — desktop and self-hosted keep diagrams inside Janus perimeter
* No mandatory account, telemetry, analytics in desktop binary

## Why Adopted (8 May 2026)

Adopted by AI Office as canonical diagramming tool for ISO platform-and-tool-development process documentation work with Simon. Three drivers:

1. **Free and open source** — removes licensing friction
2. **Desktop offline operation** — suitable for sensitive ISO process content
3. **XML format is text-based and AI-readable** — lets AI Office generate, review, maintain process diagrams programmatically rather than treating as opaque binary artefacts

Michael: Janus needs to move away from token-heavy proprietary formats (PPT, Word) toward text-native formats LLMs can manipulate cleanly.

**Selected after explicit comparison:**
* **Excalidraw rejected** — hand-drawn freeform unsuitable for formal ISO process documentation
* **[[figma|Figma]] ([[figma|AIR-55]], Sandbox)** — positioned as UI/UX/web tool, not process-flow diagramming

draw.io fills the structured-diagramming gap.

## Use Cases

* **ISO documentation** (primary) — process flows, RACI diagrams, control maps, ISMS scope
* **Architecture diagrams** — AI Office tooling, wider Janus platform stack
* **AI-generated process diagrams** — Claude authoring `.drawio` XML directly
* **Version-controlled diagrams** — Git-stored alongside code/policy
* **Cross-department diagramming** — org charts, swim-lane maps

*Evaluating. Functional tier. Adopted at AIO daily standup 8 May 2026.*
