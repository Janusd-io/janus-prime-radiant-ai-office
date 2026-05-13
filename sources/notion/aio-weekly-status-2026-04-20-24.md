---
type: source
notion_url: https://www.notion.so/34c114fc090c81d6a254e84a54af8b5b
notion_id: 34c114fc-090c-81d6-a254-e84a54af8b5b
title: Weekly Status - AI Office Operations - 20-24 Apr 2026
source_type: notion-page
fetched: 2026-05-06
---

# Weekly Status - AI Office Operations (20-24 Apr 2026)

## Executive Summary

The AI Office moved from infrastructure and tool-selection uncertainty into more operational footing. Hostinger selected and set up as default self-hosting platform. Monday.com adopted as primary operations SoR. Notion remains documentation layer. Linear stays focused on engineering.

The week sharpened operating model: formal ISO workflow documentation must precede automation; agentic systems should avoid lock-in to any single LLM harness; and production tools now need explicit support and maintenance ownership.

## Overall status

| Area | Status | Summary |
|---|---|---|
| **Infrastructure** | Green | Hostinger setup completed; Malaysian DC; GCP narrowed to managed-service and departmental use. |
| **Operations SoR** | Green | Monday.com pilot completed and established as operations SoR; Notion remains documentation; Linear remains engineering. |
| **ISO / Process** | Amber | Simon kickoff completed; ISO programme active; automation now gated by documented, signed-off department workflows. |
| **HR Tooling** | Green/Amber | Assessify core platform done; onboarding and leave forms operational. Portal remains parked. |
| **Marketing / CRM** | Amber | HubSpot Gate 1 desk review completed; live Andrew call needed before recommendations circulated. |
| **Agent Platform** | Amber | Codex and Monday.com moved into Sandbox; Gemini MCP and Claude Agent SDK + Slack flagged for lock-in mitigation. |

## Key progress

### Infrastructure and Hosting
- **Reversed** default self-hosting from GCP to Hostinger after GCP showed unpredictable metered billing.
- **Hostinger selected:** flat pricing (~$920–1,020/2yr), Docker-ready, root access, better operational control.
- **Setup completed:** payment processed, Malaysian DC selected, company account established.
- **GCP narrowed** to managed-service and departmental use cases.

### Operating System of Record
- **Monday.com adopted** as primary operations SoR after evaluation and Pro plan pilot.
- **Notion remains** documentation and narrative layer; Linear remains engineering.
- **ClickUp discontinued.** Asana rollout for CEO weekly meeting killed (Monday replaces need).
- **Weekly PowerPoint reporting killed** in favour of Monday dashboards and executive management system.

### ISO and Workflow Standardisation
- **Simon collaboration confirmed** and kickoff completed.
- **Department-level processes** will be documented and signed off before automation begins.
- AI Office's tool evaluation and process discipline appears aligned with ISO expectations, but Simon's formal documentation now becomes the operating gate.

### HR Forms and Assessify
- **Assessify core platform marked Done** (AIP-21).
- **MCP connection to Claude Desktop operational** — HR can create assessments, forms, quizzes through Claude without UI.
- **Leave form live** with secure database, hashed credentials, Slack integration.
- **Onboarding form operational**; data migration to Deel needed once Deel becomes SoR.

### Marketing / CRM
- **HubSpot Gate 1 desk review completed** using new Claude Marketing project and CRM-evaluation skill.
- **Main concerns:** Breeze AI lock-in, vague data-training exclusion, complex API app approval.
- **Jehad confirmed:** HubSpot strongest for email marketing but harder to integrate; Pipedrive easier technically but weaker for marketing.
- **Andrew call should happen live** before written findings are shared, so requirements can be broadened into RFP-grade scope.

### Agent Platform Strategy
- **Codex moved to Sandbox** — actively evaluated alongside Claude.
- **Monday.com also moved to Sandbox** for active trial and integration testing.
- **Assessify MCP pattern emerged** as strategic template: own the data/service layer, then allow Claude/Gemini/OpenAI to connect through MCP.
- **Gemini MCP promoted** from background reading to explicit cost-alternative investigation.

## Decisions made this week

- Hostinger is default for self-hosted AI Office tools; GCP narrowed to managed-service/departmental.
- Malaysia initial Hostinger DC; UK/EU revisited when UK office live.
- Monday.com is primary operations SoR; Notion is documentation; Linear is engineering.
- ClickUp rejected; Asana CEO rollout killed.
- Weekly PowerPoint reporting killed in favour of Monday dashboards.
- **ISO workflow documentation and sign-off must precede automation.**
- Assessify core platform Done; remaining HR adoption/skills work under HR forms umbrella.
- HubSpot analysis to be walked through live with Andrew before circulating written conclusions.
- Post-production support workflow needs decision with Andre and Euclid.
- Gemini MCP treated as explicit cost-alternative experiment.

## Risks and watchpoints

- **Production support** now a real operating need as HR forms and Assessify move to live/maintenance.
- **Notion/Linear/project-status drift** — reconciliation after standups must stay disciplined.
- **Vendor lock-in rising** — OpenAI, Anthropic, Google, HubSpot all wrapping their own AI harnesses.
- **HubSpot may create integration and governance friction** despite strong marketing fit.
- **Deel migration path** must be planned for HR form data before temporary database becomes entrenched.
- **Infrastructure resilience** not yet fully specified; DR/BC planning parked pending specialist capacity.

## Next week focus

1. Schedule and run Andrew CRM / HubSpot review call; expand requirements into RFP scope.
2. Raise post-production support and maintenance workflow with Andre and Euclid.
3. Continue executive management system pilot in Monday.com.
4. Advance ISO workflow documentation with Simon; map which automations are blocked.
5. Run Gemini MCP cost-alternative experiment.
6. Write up HR forms umbrella.
