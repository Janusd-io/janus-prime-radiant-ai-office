---
type: source
source_type: document
title: High-level CRM requirements and use cases
slug: crm-requirements-high-level
created: 2026-04-23
updated: 2026-06-12
captured_by: claude
author: andrew-soane
departments: [marketing, ai-office]
confidence: high
related: [janus-crm-selection, crm-evaluation-and-selection, 2026-06-09-salesforce-janus-digital-global, andrew-soane]
---

> **Note:** Internal requirements document (marketing-authored; file dated 2026-04-23) defining Janus Digital's CRM platform requirements across 9 functional areas with High/Medium priorities. This is the "requirements list" Andrew committed to send Salesforce in the [[2026-06-09-salesforce-janus-digital-global]] call, and the baseline for the June 2026 CRM evaluation sprint. Authorship inferred from context (Andrew's CRM workstream) — unconfirmed.

**High-level CRM requirements and use cases**

### **Executive Summary**

This document sets out the proposed high-level CRM requirements for Janus Digital to inform platform evaluation and selection.

We operate as a B2B2B business, selling predominantly through partners into a precisely defined audience of asset managers (GPs), asset owners (LPs), and real estate operators globally, in the first instance with a particular focus on the UK and Singapore. Our sales cycles are likely to be typical for the enterprise B2B space (6 to 60 months), they will involve multiple senior stakeholders per account, and require sustained coordination across marketing, sales, and partner channels. In this context, a CRM is not a contact database, it is the operational backbone of our entire revenue function.

The requirements reflect four imperatives:

* First, **account-based, not contact-based**. The platform must manage complex institutional hierarchies and multi-stakeholder buying committees, not just individual contacts.   
* Second, **built for the long cycle**. Data retention, nurture sequencing, and pipeline management must be configured for an up to 60-month journey, including compliance obligations arising from the tension between GDPR/PDPA retention norms and our sales timeline.   
* Third, **partner-first**. Partners are our primary route to market and the CRM must manage co-marketing, deal registration, and partner-attributed pipeline natively.   
* Fourth, and critically, **AI-native**. The CRM must support agentic enrichment from day one: AI agents autonomously updating and synchronising account and contact records from third-party sources, maintaining the CRM as a living single source of truth without manual intervention. This is a core architectural requirement, not a future-state ambition. Vendors will be required to demonstrate this capability during evaluation.

Requirements are organised across eight functional areas, each prioritised as High (non-negotiable), Medium (required or on confirmed roadmap), or deferred to a Year 2+ appendix.

**1\. Core functionality**

| Ref | Functionality | What is it? | Priority |
| :---- | :---- | :---- | :---- |
| **1.1** | **Pipeline & Opportunity Management**  | Including:\- Stage-gate management\- Probability weighting\- Multi-period/multi-year forecast modelling.  | High |
| **1.2** | **Multi-Stakeholder Deal Management** | Ability to track multiple stakeholders *across a single deal* | High |
| **1.3** | **Sales Activity & Interaction Logging** | Calls, meetings, emails logged against accounts and contacts. | High |
| **1.4** | **Customer Success / Post-Sale Record Management** | Ability to track the full customer lifecycle, not just the sales funnel. | High |

**2\. Advanced ABM & Account Mapping**

| Ref | Functionality | What is it? | Priority |
| :---- | :---- | :---- | :---- |
| **2.1** | **Hierarchical Account Mapping** | Ability to map complex institutional structures (e.g., Parent Funds vs. Asset Managers) and identify relationships between key personas like CFOs, CTOs, COOs and Asset Managers. | High |
| **2.2** | **Target Account Lists (TAL) / Account Based Marketing (ABM)** | Ability to segment and sync the 20–50 priority accounts per geography directly with LinkedIn for sponsored content and InMail (may require 3rd party marketing platform plug-in)*Native or via certified integration: must be demonstrated in evaluation.* | High |
| **2.3** | **Account-Level Health Scoring** | A dashboard that aggregates intent signals, content downloads, and event attendance at the account level, not just the individual level. (Related to 2.2) | Medium |

## 

## **3\. Long-Cycle Nurture & Automation**

With a buying journey spanning up to 60 months, the CRM must handle extreme longevity in data retention and engagement tracking.

| Ref | Functionality | What is it? | Priority |
| :---- | :---- | :---- | :---- |
| **3.1** | **Role-Aware Automation** | Integration with Marketing Automation Platform (MAP) to trigger role-specific sequences (e.g., different tracks for a CFO vs. a technical user) based on CRM persona tags. | High |
| **3.2** | **Intent Signal Integration** | Ability to ingest third-party intent data to trigger programmatic digital outreach or coordinated sales and marketing sequences. (Related to 1.3). | Medium |

## **4\. High-Touch Event & Experience Management**

Events and roundtables are likely to represent a significant %age of total marketing budget.

| Ref | Functionality | What is it? | Priority |
| :---- | :---- | :---- | :---- |
| **4.1** | **Field Marketing Attribution** | Capability to track ROI from executive breakfast briefings and curated industry conferences across the UK and Singapore. | High |
| **4.2** | **Exclusive Invite Workflows** | Management of "invite-only" logic for webinars and roundtables to ensure exclusivity, relevance and attendance. | Low(year 2\) |

## **5\. Partner & Channel Enablement**

Since Partner Marketing is a "primary route to market," the CRM must facilitate external collaboration.

| Ref | Functionality | What is it? | Priority |
| :---- | :---- | :---- | :---- |
| **5.1** | **Partner Portal/PRM Integration** | A shared view for co-marketing campaigns and joint demand generation efforts. Note partner portal TBD so this requirement related to breadth/depth of API/integration with 3rd party platforms. | High |
| **5.2** | **Referral & Advocacy Tracking** | Formalized workflows for referrals, advocacy and other recommendations. | Medium |

## 

## 

## 

## 

## 

## 

## **6\. Sales Enablement & Content Attribution**

Marketing’s job continues through the handoff, requiring the CRM to be the "source of truth" for sales collateral.

| Ref | Functionality | What is it? | Priority |
| :---- | :---- | :---- | :---- |
| **6.1** | **Content Usage Tracking** | Integration with your sales enablement tools to see which pitch decks, battlecards, or case studies are actually closing deals. | Medium |
| **6.2** | **Full-Funnel Attribution** | Tracking the influence of "earned media" and "executive thought leadership" on the pipeline to justify the 20–25% spend in the "High Priority" tier. | Medium |

## **7\. Multi-Regional Compliance** 

| Ref | Functionality | What is it? | Priority |
| :---- | :---- | :---- | :---- |
| **7.1** | **GDPR/privacy**  | Built in compliance to manage variable data privacy and differing marketing consent regulations based on up-to-date legislation across multiple markets (e.g. Europe, Singapore, UK). Includes,but not limited to:\- Consent capture and audit logging\- Data subject access request (DSAR) workflows\- Right-to-erasure handling | High |
| **7.2** | **Data Retention vs. Sales Cycle Tension** | Ability to set timeline for data retention policies that accommodate sales timeline(legitimate interest) | High |

## 

**8\. Dashboards and reporting**

| Ref | Functionality | What is it? | Priority |
| :---- | :---- | :---- | :---- |
| **8.1** | **Standard dashboards/reporting** | Ability to generate a range of standard dashboards (real-time) and reports including but not limited to:\- Partner contribution\- Attribution\- Downstream revenue\- Marketing ROI\- Retention NRR\- Partner lifecycle\- Co-sell velocity\- Financial health (weighted pipeline, gross margin per customer, NRR etc) [See reporting requirements for details](https://docs.google.com/document/d/166WeyCjV40MwVBgz3umflRA76zfdcKYCJyxRd7bTpSE/edit?usp=drive_link) | High |
| **8.2** | **Additional dashboards/reporting** | Ability to generate a range of standard dashboards (real-time) and reports including but not limited to:\- Partner lead time and ramp/velocity\- Channel conflict\- Sales rep productivity\- Discounting impact[See reporting requirements for details](https://docs.google.com/document/d/166WeyCjV40MwVBgz3umflRA76zfdcKYCJyxRd7bTpSE/edit?usp=drive_link) | Medium |
| **8.3** | **Self-service BI / ad-hoc reporting** | Ability for users to build dashboards and reports using simple widgets and tools, purpose built to their specific requirements. | High |

**9\. AI and integrations**

| Ref | Functionality | What is it? | Priority |
| :---- | :---- | :---- | :---- |
| **9.1** | **Full-Stack Extensibility & Universal API Gateway** | Two-way API capability with ability to connect to, ingest and extract data from and to a variety of other tools and platforms, including but not limited to:\- Marketing automation platform\*\- Website CMS\*, Google Analytics\- Email marketing platform\*\- Google Workspaces (esp. Mail/Calendar)\- Slack\- Asana\- Fireflies\- Google Gemini TBC\- Claude (Projects and Cowork) TBC\- Others TBC *\* If not native functionality* | High |
| **9.2** | **LinkedIn Sales Navigator Integration**  | In addition to the above, specific LinkedIn Sales Navigator integration (account and lead sync, InMail activity tracking back to CRM, saved account lists) | High |
| **9.3** | **Agentic Record Enrichment & Sync** | Ability to autonomously (via agents) to update relevant account/contact records with data ingested from 3rd party platforms ensuring records are the single source of truth across the business. | High |

