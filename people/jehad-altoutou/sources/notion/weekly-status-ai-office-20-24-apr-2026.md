---
type: source
source_type: notion
slug: weekly-status-ai-office-20-24-apr-2026
title: Weekly Status - AI Office Operations - 20-24 Apr 2026
created: 2026-04-24
captured_by: jehad-altoutou
notion_url: https://www.notion.so/34c114fc090c81d6a254e84a54af8b5b
audience: department
departments: [ai-office]
sensitivity: dept
sensitivity_confidence: 0.5
---

# Executive Summary
The AI Office moved from infrastructure and tool-selection uncertainty into a more operational footing this week. Hostinger was selected and set up as the default self-hosting platform, [monday.com](http://monday.com) was adopted as the primary operations system of record, and Notion remains the documentation layer. Linear stays focused on engineering delivery.
The week also sharpened the AI Office operating model: formal ISO workflow documentation must precede automation; agentic systems should avoid lock-in to any single LLM harness; and production tools now need explicit support and maintenance ownership as HR forms and Assessify move into completed or live states.
# Overall Status
<table header-row="true">
<tr>
<td>Area</td>
<td>Status</td>
<td>Summary</td>
</tr>
<tr>
<td>Infrastructure</td>
<td>Green</td>
<td>Hostinger setup completed; Malaysian data centre selected; GCP narrowed to managed-service and departmental use cases.</td>
</tr>
<tr>
<td>Operations SoR</td>
<td>Green</td>
<td>[monday.com](http://monday.com) pilot completed and established as operations SoR; Notion remains documentation; Linear remains engineering.</td>
</tr>
<tr>
<td>ISO / Process</td>
<td>Amber</td>
<td>Simon kickoff completed and ISO programme active; automation now gated by documented, signed-off department workflows.</td>
</tr>
<tr>
<td>HR Tooling</td>
<td>Green / Amber</td>
<td>Assessify core platform done; onboarding and leave forms operational. Broader portal remains parked pending trainer arrival.</td>
</tr>
<tr>
<td>Marketing / CRM</td>
<td>Amber</td>
<td>HubSpot Gate 1 desk review completed; live Andrew call needed before written recommendations are circulated.</td>
</tr>
<tr>
<td>Agent Platform</td>
<td>Amber</td>
<td>Codex and [monday.com](http://monday.com) moved into Sandbox; Gemini MCP and Claude Agent SDK + Slack front-end flagged for lock-in mitigation.</td>
</tr>
</table>
# Key Progress
## Infrastructure and Hosting
- Reversed the default self-hosting direction from GCP to Hostinger after GCP showed unpredictable metered billing during setup.
- Hostinger selected for self-hosted AI Office tools based on flat pricing, Docker readiness, root access, and stronger fit for near-term operational control.
- Hostinger setup completed: payment processed, Malaysian data centre selected, company account established.
- Disaster recovery / business continuity plan identified as necessary, then parked until an infrastructure specialist is onboarded.
## Operating System of Record
- [monday.com](http://monday.com) adopted as the primary operations SoR after evaluation and Pro plan pilot.
- Notion remains the documentation and narrative layer; Linear remains the engineering execution tracker.
- ClickUp discontinued and formally rejected; Asana rollout for the CEO weekly meeting killed because [monday.com](http://monday.com) replaces the need.
- Weekly leadership PowerPoint deck killed; executive reporting now expected to flow through [monday.com](http://monday.com) dashboards and the executive management system.
## ISO and Workflow Standardisation
- Simon collaboration confirmed and kickoff completed.
- Department-level processes will be documented and signed off before automation begins.
- The AI Office's tool evaluation and process discipline appears aligned with ISO expectations, but Simon's formal process documentation now becomes the operating gate.
## HR Forms and Assessify
- Assessify core platform marked Done and archived; AIP-21 aligned as Done.
- Assessify MCP connection to Claude Desktop is operational, allowing HR to create assessments, forms, and quizzes through Claude without using the UI directly.
- Leave form is live with secure server-hosted database, hashed credentials, and Slack integration.
- Onboarding form is also operational; data migration to Deel will be needed once Deel becomes the SoR.
- Follow-on HR work consolidated under the HR forms umbrella, including Assessify HR skill work and candidate-side adoption once the trainer arrives.
## Marketing / CRM
- HubSpot Gate 1 desk review completed using the new Claude Marketing project and CRM-evaluation skill.
- Main concerns: Breeze AI lock-in for autonomous actions, vague data-training exclusion terms, and complex API app approval.
- Jehad confirmed HubSpot is strongest for email marketing but harder to integrate; Pipedrive is easier technically but weaker for marketing.
- Andrew call should happen live before written findings are shared, so requirements can be broadened into an RFP-grade scope covering technical, AI governance, migration, and security needs.
## Agent Platform Strategy
- OpenAI Codex moved to Sandbox and is being actively evaluated alongside Claude.
- [monday.com](http://monday.com) also moved to Sandbox for active trial and integration testing.
- Codex and OpenClaw remain separate AIO entries because they are fundamentally different tools.
- The Assessify MCP pattern emerged as a strategic template: own the data and service layer, then allow Claude, Gemini, OpenAI, or another reasoning model to connect through MCP.
- Gemini MCP experiment promoted from background reading to explicit cost-alternative investigation.
# Decisions Made This Week
- Hostinger is the default platform for self-hosted AI Office tools; GCP is narrowed to managed-service or departmental use cases.
- Malaysia is the initial Hostinger data centre; UK/EU options will be revisited when the UK office is live.
- [monday.com](http://monday.com) is the primary operations SoR; Notion is documentation; Linear is engineering.
- ClickUp is rejected; Asana rollout for CEO weekly meeting is killed.
- Weekly PowerPoint reporting is killed in favour of [monday.com](http://monday.com) dashboards / executive management system.
- ISO workflow documentation and sign-off must precede automation.
- Assessify core platform is Done; remaining HR-facing adoption and skills work moves under the HR forms umbrella.
- HubSpot analysis should be walked through live with Andrew before circulating written conclusions.
- Post-production support workflow needs a decision point with Andre and Euclid.
- Gemini MCP should be treated as an explicit cost-alternative experiment.
# Risks and Watchpoints
- Production support is now a real operating need as HR forms and Assessify move from build to live/maintenance.
- Notion, Linear, and project/action status can drift; reconciliation after standups needs to stay disciplined.
- Vendor lock-in risk is rising as OpenAI, Anthropic, Google, and HubSpot all wrap their own AI harnesses around workflows.
- HubSpot may create integration and governance friction despite strong marketing fit.
- Deel migration path must be planned for HR form data before the temporary operational database becomes entrenched.
- Infrastructure resilience is not yet fully specified; DR/BC planning is parked pending specialist capacity.
# Next Week Focus
1. Schedule and run Andrew CRM / HubSpot review call; expand marketing requirements into RFP-grade scope.
2. Raise post-production support and maintenance workflow with Andre and Euclid; decide [monday.com](http://monday.com) vs Zendesk-style issue tracking.
3. Continue executive management system pilot in [monday.com](http://monday.com) and clarify what Bonaventure should see first.
4. Advance ISO workflow documentation with Simon and map which automations are blocked pending sign-off.
5. Run Gemini MCP cost-alternative experiment and compare against Claude/Codex operating patterns.
6. Write up the HR forms umbrella so leave form, onboarding form, Assessify MCP, and follow-on HR skill work have clear ownership.
# Source Standups
- 2026-04-20 - Daily Standup #16: <mention-page url="https://www.notion.so/335114fc090c81919a6ecd2f2cacc64a">AI Office — Operations Notebook</mention-page>
- 2026-04-21 - Daily Standup #17: <mention-page url="https://www.notion.so/335114fc090c81919a6ecd2f2cacc64a">AI Office — Operations Notebook</mention-page>
- 2026-04-22 - Daily Standup #18: <mention-page url="https://www.notion.so/335114fc090c81919a6ecd2f2cacc64a">AI Office — Operations Notebook</mention-page>
- 2026-04-23 - Daily Standup #19: <mention-page url="https://www.notion.so/335114fc090c81919a6ecd2f2cacc64a">AI Office — Operations Notebook</mention-page>
- 2026-04-24 - Daily Standup #20: <mention-page url="https://www.notion.so/335114fc090c81919a6ecd2f2cacc64a">AI Office — Operations Notebook</mention-page>
