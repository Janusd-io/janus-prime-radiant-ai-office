---
type: vendor
title: Microsoft Copilot in Excel
slug: microsoft-copilot-in-excel
air_id: AIR-72
status: Monitor
labels: [Finance, Office of CEO, Functional]
departments: [finance, office-of-ceo]
url: https://linear.app/janusd/issue/AIR-72/microsoft-copilot-in-excel
created: 2026-04-06
updated: 2026-04-06
captured_by: jehad-altoutou
audience: department
sensitivity: dept
sensitivity_confidence: 0.9
---
<!-- jb:air-vendor-callout -->
> Part of [[ai-registry|AI Registry]]
> Departments: [[finance]], [[office-of-ceo]]


# Microsoft Copilot in Excel

> AI Registry entry [AIR-72](https://linear.app/janusd/issue/AIR-72/microsoft-copilot-in-excel) — status **Monitor** as of 2026-04-06. Departments: finance, office-of-ceo.

**Category:** AI Spreadsheet Agent (bundled with M365)
**Cost:** $30/user/month as M365 Copilot add-on. Requires M365 Business/Enterprise. No standalone Excel-only pricing.
**Departments:** Finance, Office of CEO (potential: All)

## Overview

AI assistant built into Excel as part of M365 Copilot suite. Powered by OpenAI GPT. Natural language interaction — data analysis, formula generation, visualisation, scenario modelling. Unlike [[shortcut-ai|Shortcut AI]] ([[shortcut-ai|AIR-28]]) and [[claude|Claude]] for Excel ([[claude-by-anthropic-in-excel|AIR-30]]), Copilot is bundled (not standalone) covering Word, PowerPoint, Teams, Outlook + Excel.

## Capabilities

* Data analysis and visualisation via natural language
* Formula generation from description
* Scenario modelling, what-if projections
* Data insights — trends, outliers, patterns
* Formatting/cleanup
* Python in Excel — Copilot generates/runs Python
* Cross-app context flow across Word/PowerPoint/Teams/Outlook

## Security

* Inherits M365 compliance (SOC 1/2/3, ISO 27001/27018, GDPR, HIPAA, FedRAMP)
* **Microsoft Entra integration — full SSO** (meets Action #21)
* Data stays within M365 tenant
* No training on customer data
* Purview sensitivity labels + DLP
* Audit logging

## Comparison Matrix (AI Spreadsheet Agents)

| | Shortcut AI (AIR-28) | Claude for Excel (AIR-30) | Copilot in Excel |
|---|---|---|---|
| Cost | $20 Pro | Included with Claude Teams | $30 (M365 Copilot bundle) |
| SpreadsheetBench | 59.25% | 42.9% | 57.2% |
| SSO | Teams+ | Via Claude Teams | **Entra native** |
| Cross-app | Excel only | Excel+PowerPoint | Full M365 |
| New vendor? | Yes | No | No |

## Why Monitor (Michael 2026-04-06 assessment)

Currently behind Shortcut AI and Claude for Excel on financial modelling and complex spreadsheet tasks. Microsoft scale/investment means could catch up. Bundled pricing advantageous if M365 Copilot needed for other apps. **Strongest SSO/identity story of the three** — natively meets Microsoft Entra requirement.

*Monitor. Functional tier. Last reviewed 2026-04-06.*
