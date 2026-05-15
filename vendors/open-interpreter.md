---
type: vendor
title: Open Interpreter
slug: open-interpreter
air_id: AIR-43
status: Rejected
labels: [Functional]
departments: []
url: https://linear.app/janusd/issue/AIR-43/open-interpreter
created: 2026-02-25
updated: 2026-04-06
captured_by: jehad-altoutou
audience: department
sensitivity: dept
sensitivity_confidence: 0.9
---

# Open Interpreter

> AI Registry entry [AIR-43](https://linear.app/janusd/issue/AIR-43/open-interpreter) — status **Rejected** as of 2026-04-06. Departments: —.

**Category:** AI Agent / Code Execution Platform
**Status:** REJECTED
**Cost:** Free (open source); cloud plans TBD

## Overview

Open-source project enabling LLMs to run code (Python, JavaScript, Shell) locally on user's computer. ChatGPT-like terminal interface that can execute code, manipulate files, browse web, interact with local OS.

## Rejection Rationale

* **Superseded by Claude Code (AIR-13)** — agentic capabilities with better safety controls, permission models, Claude ecosystem integration
* **Security risk** — executes arbitrary code without robust sandboxing
* **No enterprise features** — no SSO, admin controls, audit logging, certifications
* **Open-source project** — community-maintained, no enterprise support/SLA
* **Redundant** — Gemini CLI (AIR-12) and Claude Code (AIR-13) cover same use cases with better governance

*Rejected. Superseded by Claude Code (AIR-13) and Gemini CLI (AIR-12).*
