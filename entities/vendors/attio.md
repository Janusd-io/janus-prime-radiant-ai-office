---
type: vendor
title: Attio
slug: attio
created: 2026-06-01
updated: 2026-06-01
departments: [marketing, office-of-ceo]
status: active
confidence: high
sources: [marketing-stack-technical-writeup, agentic-lean-marketing-stack]
related: [cosmic, vercel, resend, janus-crm-selection, agentic-lean-marketing-stack, stack-composition-framework]
---

# Attio

**Category:** CRM (agent-native)
**AIR:** AIR-76
**Stack Composition score:** 3/3

Attio is an agent-native CRM selected as the relationship layer for the Janus marketing stack. MongoDB-style queries, a relationship-graph data model with standard objects, published pricing (no "contact sales"), and plain-JSON / CSV export. Attio's positioning is explicit: "an MCP server cannot be designed like a public API" — they built agent-operability as a first-class design constraint, not an afterthought.

## Role in the Janus marketing stack

CRM layer for the Singapore campaign: managing the 100-account direct-outreach target list, tracking Bonaventure + Joyce Woo relationship touches, and feeding [[resend]] for automated follow-up sequences. Post-Singapore: becomes the primary account-management and pipeline-tracking tool for Andrew's marketing team.

Andrew Soane to prepare Attio requirements list by 2026-05-26 per the [[agentic-lean-marketing-stack]] brief.

## Stack Composition Framework scoring

- **Agent-operability:** ✅ — MCP server designed from the ground up for agent access (not bolted on); MongoDB-style query language (industry-standard).
- **Reversibility:** ✅ — standard object model (companies, people, deals) exportable to CSV / JSON. Not locked into Attio's data schema.
- **Maintenance burden:** ✅ — published pricing (no "contact sales" lock-in); relationship graph is human-readable and agent-readable simultaneously.

## Why not Salesforce or HubSpot

Salesforce (AIR score 2/3): deepest MCP integration in the category but Apex scripting accumulates irreversible vendor-specific state the moment any customisation touches it. HubSpot (AIR score 2/3): bundling play; standalone CRM is weaker than Attio at Janus's stage.

## Watch for

- Attio's MCP server coverage for complex relationship queries (e.g., "which accounts has Joyce touched but Bonaventure hasn't yet?") — validate before the Singapore campaign goes live.
- Pricing on scale: Attio is startup-friendly today; re-evaluate at >50 seats.
