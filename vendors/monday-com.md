---
type: vendor
title: Monday Com
slug: monday-com
created: 2026-04-22
updated: 2026-04-22
status: Sandbox
confidence: low
sources: [2026-04-22-it-team-meeting]
related: []
audience: department
captured_by: jehad-altoutou
departments: []
air_id: AIR-83
---

# Monday Com

Vendor stub created from meeting [[2026-04-22-it-team-meeting]] on 2026-04-22.

_Mention context:_ destination for multi-agent contributor's task tracking

_To populate: replace this stub with real content and remove this notice._


---

## AI Registry — AIR-83

> Linear: [AIR-83](https://linear.app/janusd/issue/AIR-83/mondaycom) · status **Sandbox** · updated 2026-05-05.

**Category:** Work Management Platform / Project & Task Management / CRM (under evaluation)
**Cost per User/Month:** Free (2 seats); Basic $9; Standard $12; Pro $19; Enterprise custom. Minimum 3 seats on paid. Annual ~18% cheaper.
**Departments:** Office of CEO (requested), Commercial (CRM evaluation)
**Entity:** monday.com Ltd. (Israel; NASDAQ: MNDY)
**Requested by:** Bonaventure Wong via CEO Executive Management System design discussion (20 Apr 2026); CRM use-case raised by Michael Bruck and Andrew during Andrew Weekly 5 May 2026.

## Overview

Cloud-based work management platform built around customisable "boards". Suite includes monday Work Management, monday CRM, monday dev, monday service. ~250,000 organisations globally. Repeat Gartner Magic Quadrant Leader.

## Capabilities

* Boards — configurable tables with typed columns (status, person, date, formula, location)
* Multiple view types: table, kanban, timeline, Gantt, calendar, map
* Dashboards aggregating data across boards
* No-code automations (250/mo Standard, 25k/mo Pro, 250k/mo Enterprise)
* Workflow builder
* Real-time collaborative Docs with embedded live board data
* AI assistant (credit-based)
* Guardian add-on (Enterprise) — TLE, BYOK, DLP

## Integrations

* Native: Slack, Teams, Gmail/Outlook, Drive, Dropbox, OneDrive, Zoom, Salesforce, HubSpot, Jira, GitHub, Zendesk, 200+ others
* REST + GraphQL API
* Webhooks
* SCIM (Enterprise)
* SAML SSO (Okta, Entra ID, custom) on Enterprise only
* monday code — hosted app platform

## Security & Compliance

* ISO 27001:2022, ISO 27017, ISO 27018, ISO 27032, ISO 27701
* SOC 1 Type II, SOC 2 Type II, SOC 3, CSA STAR, TX-RAMP
* GDPR/UK GDPR, CCPA, LGPD, HIPAA (BAA), PIPEDA
* DORA-aligned for EU financial services
* AES-256 at rest; TLS 1.3 in transit; FIPS 140-2 validated
* AWS hosting US/EU/AUS with cross-region DR

## Relevance to Janus Digital

Surfaced during CEO Executive Management System design (20 Apr 2026) as Asana replacement. Bonaventure decided to retire Asana. Jehad raised Monday.com — full dashboard-oriented view suits CEO-level cross-departmental visibility; task/project model more mature than Notion databases. ISO 27001:2022 and SOC 2 Type II posture matches compliance bar Simon's ISO programme establishes. As of Andrew Weekly 5 May 2026, monday CRM under evaluation alongside HubSpot, Attio, Salesforce. Bundle pricing flagged as potential decision driver.

## Considerations

* **Overlap with ClickUp (AIR-44)** — single decision should close out one or the other
* **Overlap with Notion** — Janus also evaluating Notion as SOR for CEO Executive Management System. Notion strength: documentation + flexible databases + KB. Monday strength: opinionated task/project workflows with mature dashboarding.
* **CRM matrix (5 May 2026)** — monday CRM vs HubSpot/Attio/Salesforce. CRM module priced separately from Work Management.
* **3-seat minimum** + bucket pricing inflates effective per-user cost
* **SAML SSO and SCIM are Enterprise-only** — broad adoption requires Enterprise tier
* AI credits metered separately
* Automation ceilings — agent-driven workflows can hit Standard 250 actions/month quickly

*Sandbox. Already adopting for project management (board 5095012818).*
