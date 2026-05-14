---
type: source
source_type: notion
slug: ai-nomi-office-operations-notebook
title: AI Nomi Office — Operations Notebook
created: 2026-04-06
captured_by: jehad-altoutou
notion_url: https://www.notion.so/33a114fc090c8047bc60c9e8c0f5916f
audience: department
departments: [ai-office]
sensitivity: dept
sensitivity_confidence: 0.5
---

# Purpose
Running log of AI Office standups, decisions, and action items. Used to maintain continuity between sessions and keep Bonaventure current on progress.
**Team:** Michael Bruck, Jehad Altoutou
**Standup cadence:** Daily — 09:30 AM
---
# Open Action Items
<table header-row="true">
<colgroup>
<col width="60">
<col width="274.328125">
<col>
<col>
<col>
</colgroup>
<tr>
<td>#</td>
<td>Action</td>
<td>Owner</td>
<td>Source</td>
<td>Status</td>
</tr>
<tr>
<td>1</td>
<td>Evaluate OpenClaw vs NemoFlow — compare capability and hosting options. Initial finding (02 Apr): NemoFlow is a corporate-focused variant of OpenClaw — more guardrails, fewer integrations, less flexibility. OpenClaw more flexible but personal-use oriented. Decision (03 Apr): NemoClaw preferred — ISO 42001 ready, better compliance posture. Both pass evaluation functionally. OpenClaw moved to Monitor. NemoClaw to be deployed on Mac Mini for trial as Slack bot.</td>
<td>Jehad</td>
<td>2026-04-01 Registry Review</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>Evaluate Dify — compare to N8N, medium priority</td>
<td>Jehad</td>
<td>2026-04-01 Registry Review</td>
<td>Done</td>
</tr>
<tr>
<td>3</td>
<td>~~Evaluate Lindy — compare to N8N~~ — Rejected (03 Apr). Fails Gate 1 on data training policies; SaaS only, no self-hosting option. N8N confirmed as primary, Dify retained as secondary for RAG.</td>
<td>Jehad</td>
<td>2026-04-01 Registry Review</td>
<td>Done</td>
</tr>
<tr>
<td>4</td>
<td>~~Connect remaining MCP tools in Linear (Jehad's account)~~ — Completed 03 Apr.</td>
<td>Jehad</td>
<td>2026-04-01 Registry Review</td>
<td>Done</td>
</tr>
<tr>
<td>5</td>
<td>Invoice bot review session — compare Google Apps Script version vs Jehad's N8N version; decide go-forward approach</td>
<td>Michael + Jehad</td>
<td>2026-04-01 Registry Review</td>
<td>In Progress</td>
</tr>
<tr>
<td>6</td>
<td>Airwallex API sandbox access — unlock direct invoice upload to Airwallex (call today)</td>
<td>Michael</td>
<td>2026-04-01 Registry Review</td>
<td>In Progres</td>
</tr>
<tr>
<td>7</td>
<td>Conversation with Euclid re Asana — confirm use remains scoped to Singapore-in-a-box project only. (06 Apr CEO call: Bonaventure says Asana is not an AI tool — leave outside AI Registry scope. Reassess only if AI integration features become relevant.) **Transfer to IT:** Asana ownership to be handed to IT/Euclid’s team. AI Office to coordinate handover so the ball doesn’t get dropped — ensure Euclid understands he owns Asana governance going forward. Not tracked in AIO/AIP Linear.</td>
<td>Michael</td>
<td>2026-04-01 Registry Review</td>
<td>Open</td>
</tr>
<tr>
<td>8</td>
<td>Conversation with Ann re ERP alternatives — walk through Artifact AI, Campfire, Rillet; get her view. (06 Apr: Bonaventure saw Artifact AI demo and was interested. Ann still setting up Xero — defer until she's stabilised, expected w/c 14 Apr.)</td>
<td>Michael + Ann</td>
<td>2026-04-01 Registry Review</td>
<td>Open</td>
</tr>
<tr>
<td>9</td>
<td>Flag to Joyce (Singapore) re Manus — informal note that it is not on the approved list; personal use fine given regional access constraints</td>
<td>Michael</td>
<td>2026-04-01 Registry Review</td>
<td>Open</td>
</tr>
<tr>
<td>10</td>
<td>Update AI Tool Evaluation Framework — reduce review cycle from 12 months to 3–6 months</td>
<td>Michael</td>
<td>2026-04-01 Registry Review</td>
<td>Open</td>
</tr>
<tr>
<td>11</td>
<td>Gate 1 documentation pass for Fireflies and Wilson AI — both grandfathered in pre-framework; run through G1.1–G1.5 as a box-check</td>
<td>Michael + Jehad</td>
<td>2026-04-01 Registry Review</td>
<td>Open</td>
</tr>
<tr>
<td>12</td>
<td>~~Context/prompt management system — decide on approach~~ — Resolved (03 Apr). Using GitHub-based skills repo. Supersedes Notion approach.</td>
<td>Michael + Jehad</td>
<td>2026-04-01 Registry Review</td>
<td>Done</td>
</tr>
<tr>
<td>13</td>
<td>~~Resolve Gemini Ultra licence on ~~[~~janusd.io~~](http://janusd.io) — Parked (03 Apr). Not needed right now; will revisit if required.</td>
<td>Michael</td>
<td>2026-04-01 Registry Review</td>
<td>Done</td>
</tr>
<tr>
<td>14</td>
<td>~~Move Linear to Production~~ — Reversed 2026-04-02. Linear remains in Sandbox. Production implies company-wide access; AI Office only at this stage.</td>
<td>Michael</td>
<td>2026-04-01 Registry Review</td>
<td>Done</td>
</tr>
<tr>
<td>15</td>
<td>Expand AIP-1 scope from Airwallex expense integration to Finance Department API Integration — broader phased project; start requirements gathering with Ann once she is settled on Xero. (06 Apr CEO call: Bonaventure confirms Ann needs this week to finish Xero/Airwallex setup — do not engage until she signals ready. Xero has rich APIs; Airwallex now running payroll-out.)</td>
<td>Michael + Ann</td>
<td>2026-04-02 Standup</td>
<td>Open</td>
</tr>
<tr>
<td>16</td>
<td>AI Internal Hub Slack bot — auto-acknowledge tool suggestions, create Linear Backlog entries, post status updates in thread; evaluate Viktor/RunBear or build own</td>
<td>Michael + Jehad</td>
<td>2026-04-02 Standup</td>
<td>Open</td>
</tr>
<tr>
<td>17</td>
<td>Employee Resource Portal — Google Sites + Deel API; self-service for employees; AI bot for HR queries (handbook RAG); coordinate with Teresa/HR</td>
<td>Michael + Jehad</td>
<td>2026-04-02 Standup</td>
<td>In Progress</td>
</tr>
<tr>
<td>18</td>
<td>Company Spec document — centralised org knowledge base covering all departments; meta-prompt/context file for AI use company-wide; each dept contributes their section</td>
<td>Michael</td>
<td>2026-04-02 Standup</td>
<td>Open</td>
</tr>
<tr>
<td>19</td>
<td>~~Internal Skills Library on GitHub~~ — Completed 03 Apr. Repo set up by Jehad; Jehad to continue curating.</td>
<td>Jehad</td>
<td>2026-04-02 Standup</td>
<td>Done</td>
</tr>
<tr>
<td>20</td>
<td>Check in with Lysander/Rosa (Andre's team) — Claude CoWork thread length issue on document translation; Jehad to introduce himself and offer technical support. (03 Apr: deprioritised — not urgent. More about learning what other teams are doing. Entro replication not needed.) (06 Apr CEO call: Lysander also using Claude Code, N8N, and MiniMax. Michael to sync with him — switch him off MiniMax to Gemini; provide Gemini API key. Lysander didn’t know to ask AI Office for API keys — highlights need for better internal comms on AI Office services. **MiniMax added to AI Registry as AIR-71 (Backlog)** for formal tracking and disposition. Help Lysander migrate his project off MiniMax.)</td>
<td>Michael+Jehad</td>
<td>2026-04-02 Standup</td>
<td>Open</td>
</tr>
<tr>
<td>21</td>
<td>Enterprise security and SSO protocol — establish Microsoft Entra compatibility requirements with Euclid and Andre's teams; must gate any company-wide tool deployment</td>
<td>Michael</td>
<td>2026-04-02 Standup</td>
<td>Park</td>
</tr>
<tr>
<td>22</td>
<td>Assess Obsidian — Andrey uses it alongside Notion to back up CoWork outputs; evaluate as knowledge management and context backup tool for AI Office</td>
<td>Jehad</td>
<td>2026-04-02 Standup</td>
<td>Open</td>
</tr>
<tr>
<td>23</td>
<td>~~Rename/close Prompt Library AIP project~~ — Done (03 Apr). Superseded by Skills Library on GitHub.</td>
<td>Jehad</td>
<td>2026-04-02 Standup</td>
<td>Done</td>
</tr>
<tr>
<td>24</td>
<td>Deploy NemoClaw on Mac Mini — install as Slack app; Michael and Jehad each get an instance for experimentation. Archive Michael's personal OpenClaw setup first.</td>
<td>Jehad</td>
<td>2026-04-03 Standup</td>
<td>In Progress</td>
</tr>
<tr>
<td>25</td>
<td>Trial Viktor and RunBear as Slack bots alongside NemoClaw — compare all three agent platforms in sandbox Slack; evaluate which is best fit for AI Internal Hub bot and general-purpose agent use</td>
<td>Jehad</td>
<td>2026-04-03 Standup</td>
<td>Open</td>
</tr>
<tr>
<td>26</td>
<td>Run Gate 1 analysis on N8N — for completeness since it is in Sandbox; ensure compliance documentation is on file</td>
<td>Jehad</td>
<td>2026-04-03 Standup</td>
<td>Open</td>
</tr>
<tr>
<td>27</td>
<td>Town hall transcript processing — pilot project to apply standup methodology (transcript → actions → system-of-record updates) to the company-wide all-hands meeting. Bonaventure endorsed as next step after AI Office internal proof-of-concept. Determine which SoR (Asana? Notion?) and which departments receive routed actions. **Tracked as AIP-16.**</td>
<td>Michael + Jehad</td>
<td>2026-04-06 CEO Weekly</td>
<td>Open</td>
</tr>
<tr>
<td>28</td>
<td>CEO Dashboard — Bonaventure needs a consolidated view of global operations. Architect requirements: what data sources feed it, what surfaces (Slack, web, Notion?), what cadence. Not yet a formal project — scoping only. **Tracked as AIP-17 (Backlog).**</td>
<td>Michael</td>
<td>2026-04-06 CEO Weekly</td>
<td>Open</td>
</tr>
<tr>
<td>29</td>
<td>Cross-department action routing from meeting transcripts — Bonaventure's vision: any meeting transcript should route actionable items to relevant departments (finance, commercial, etc.) with appropriate access controls. Design the methodology and identify tooling requirements. Requires solving confidentiality/siloing of data between departments. **Tracked as AIP-18 (Backlog).**</td>
<td>Michael + Jehad</td>
<td>2026-04-06 CEO Weekly</td>
<td>Open</td>
</tr>
<tr>
<td>30</td>
<td>Lysander sync — sit down with Lysander to understand his AI usage (Claude Code, N8N, MiniMax); provide Gemini API key; offer AI Office support. Potential to take some N8N workload off him as he's not a coder.</td>
<td>Michael + Jehad</td>
<td>2026-04-06 CEO Weekly</td>
<td>Open</td>
</tr>
<tr>
<td>31</td>
<td>MiniMax usage review — Lysander using MiniMax without AI Office awareness. **Added to registry as AIR-71 (Backlog).** China-based, no enterprise certs, Section 5.2.3 concerns. Likely Rejected unless self-hosted use case emerges. Michael steering Lysander to Gemini. Disposition pending Lysander sync (#30).</td>
<td>Michael</td>
<td>2026-04-06 CEO Weekly</td>
<td>In Progress</td>
</tr>
</table>
---
# Standup Log
## 2026-04-06 — Weekly CEO Update
**Attendees:** Michael Bruck, Jehad Altoutou, Bonaventure Wong
**Format:** Weekly CEO briefing (video call — Bonaventure in Singapore, Grand Hyatt)
**Duration:** \~35 minutes
### What we covered
First formal weekly update with Bonaventure since the AI Office stood up. Michael walked through the week’s progress using a Claude-generated PowerPoint, then demoed Linear (AI Registry + AI Projects) and Notion (Operations Notebook) live. Discussion shifted to strategic vision for AI-native operations company-wide.
### Progress presented
- **Foundations complete:** GitHub repo, Antigravity IDE, Claude Code, Gemini tools all configured. Google Workspace integration done.
- **AI Registry operational:** 53 tools tracked in Linear. Pipeline flowing: Backlog → Evaluating → Sandbox → Production. Registry managed conversationally via Claude — no need to manually edit Linear.
- **Skills methodology established:** Internal skills library on GitHub. Jehad curated from \~1,300 public skills. Skills are shareable, versioned, composable. Both Michael and Jehad using the same skill set for consistency.
- **Standup workflow automated:** Daily standup → Fireflies transcript → Claude skill processes it → updates Linear + Notion. \~5 minutes end-to-end. Looking to fully automate (trigger on standup end).
- **Core stack decision:** Google + Anthropic foundation. NemoClaw for enterprise agents. Dify for RAG. Several tools rejected (Lindy, ClickUp, Open Interpreter).
- **Deel API evaluation (AIP-15):** Created to assess Deel’s developer platform ahead of HR standardisation.
- **Artifact AI demo:** Showed Bonaventure an AI-powered ERP/finance layer that sits on top of Xero. ISO certified. Interesting potential fit — may reduce need to build custom finance automations.
### Bonaventure’s strategic direction
- **Asana is not an AI tool** — leave it outside the AI Registry scope. Reassess only if AI-specific integration becomes relevant. Let people use it as a project management tool without AI Office gatekeeping.
- **Ann / Xero / Airwallex:** Let Ann finish setting up Xero and Airwallex this week. Airwallex now running payment-out (not just expenses). Do not engage Ann on AI augmentation until she signals readiness — expected w/c 14 April.
- **Lysander:** Using Claude Code, N8N, and MiniMax independently. Didn’t know to approach AI Office for API keys. Michael to sync with him, switch off MiniMax to Gemini, and offer support.
- **Town hall as next pilot:** Apply the standup methodology (transcript → actions → system updates) to the company-wide all-hands meeting. Bonaventure endorsed this as a way to demonstrate AI-native operations to the broader team and shift culture.
- **Cross-department action routing:** Bonaventure’s vision — meeting transcripts from any call should automatically route actionable items to relevant departments (finance, commercial, etc.). Requires solving confidentiality boundaries between departments. Not just informational reports — should drive actions.
- **CEO Dashboard:** Bonaventure needs a global operations view. Every international meeting recorded and processed; insights surfaced. Not yet architected.
- **No back office in country offices:** Strategic aim — AI coordination layer replaces traditional back-office functions in regional offices. Slack as primary employee interface; everything else under the hood.
- **SaaS = the new database:** Bonaventure’s framing — SaaS platforms are the new data layer, highly integratable. Tool assessment must include how data flows between systems.
- **Skills and upskilling challenge:** Acknowledged that Claude/Cowork is powerful but complex for non-technical staff. Need to hide complexity behind managed interfaces (Slack bots, controlled portals). Learning curve is real — AI Office’s role is to bridge the gap between capability and accessibility.
### Decisions made
- Asana out of AI Registry scope (Bonaventure directive)
- Ann/Xero: hold off engagement until w/c 14 April
- Town hall transcript processing endorsed as next pilot project
- Lysander sync prioritised — provide Gemini API key, switch off MiniMax
- CEO Dashboard identified as future need — scoping to begin
- Cross-department action routing added as strategic design challenge
### Carried forward
See Open Action Items table above. New items 27–31 added. Existing items 7, 8, 15, 20 updated with CEO call context.
---
## 2026-04-01 — AI Registry Review Session
**Attendees:** Michael Bruck, Jehad Altoutou
**Format:** Working session (not standup)
### What we covered
Full walkthrough of the Linear AI Registry pipeline — Production, Sandbox, Evaluating, and Backlog. Reviewed every entry, cleaned up stale items, set priorities, and enriched descriptions via CoWork.
### Key outcomes
**Production** reviewed and confirmed accurate. Fireflies and Wilson AI flagged for a retrospective Gate 1 pass — both grandfathered in before the evaluation framework existed.
**Sandbox** priorities set. OpenClaw rated high — Jehad to compare against NemoFlow (Jehad's suggestion; Nvidia-backed, potentially more secure). ChatGPT set to low priority. Shortcut AI set to urgent (Ann actively evaluating). Viktor flagged high priority but governance concern noted: too broad-ranging without access controls in place.
**Evaluating** cleaned up significantly. [Make.com](http://Make.com) rejected (per-execution pricing, limited data manipulation, inferior to N8N per Jehad). Repo Prompt rejected (superseded by Claude skills and projects). Agent Mode in Excel marked duplicate. Figma moved to Sandbox. Linear and Antigravity moved to Sandbox.
**Backlog** reviewed. ClickUp and Open Interpreter rejected — no clear use case, Claude/Gemini cover the ground. Databricks kept — enterprise-grade data lake, relevant as data collection scales. Glean kept — knowledge and access control layer, potential fit for Fireflies conversation classification and zero-trust access.
**New entries added:** AIO-61 (Notebook LM — universally used, missing from registry), AIP-12 (Claude Access Control — governance project to route Claude access through a controlled interface rather than the full desktop app).
### Decisions made
- Asana remains scoped to Euclid's Singapore-in-a-box project only. Conversation with Euclid required to confirm his team understands this.
- Manus: low priority for Janus Digital. Joyce (Singapore) can use personally given HK/SG access constraints — not a company tool.
- N8N preferred over [Make.com](http://Make.com) — confirmed by Jehad on pricing model and integration breadth.
- Prompt/context management system needed. Notion tentative candidate. Not a formal project yet.
- Claude Access Control is a formal project (AIP-12). Direction: surface Claude through a controlled interface (Slack bot or Google Sites) rather than the full desktop app.
- Daily standups confirmed — 09:30 AM start. Cadence to be reviewed once Jehad is fully onboarded.
### Carried forward
See Open Action Items table above.
---
## 2026-04-02 — Daily Standup #1
**Attendees:** Michael Bruck, Jehad Altoutou
**Format:** Daily standup (first one — ran longer than usual given volume of context to cover)
**Duration:** \~52 minutes
### Registry
- Registry in good shape following yesterday's review. Notion notebook confirmed as useful running log — will use weekly summaries from it for Bonaventure's Monday meetings.
- Slack Canvas: acknowledged as manual and incomplete. Flagged for improvement — needs department-specific tool tables. Will revisit when marketing person joins to handle internal comms. Claude cannot auto-generate Canvas tables so a different rendering surface may be needed long-term.
- Linear status for Linear (AIO-36): **reversed** — remains in Sandbox. Production implies company-wide access; AI Office only at this stage.
### Projects
- **AIP-1 (Airwallex Expense Integration):** Scope to be broadened to a full Finance Department API Integration project. Phased approach — start with Ann's requirements once she is settled on Xero. Xero API also being explored alongside Airwallex.
- **AIP-11 (AI-Assisted Discovery Tool):** Confirmed as active priority alongside the finance project. The tool will assist in generating PRDs — particularly useful as we scope the finance integration.
- **AI Internal Hub Slack bot (new):** Currently the hub is a passive channel with no response mechanism. A bot should auto-acknowledge suggestions, log them to Linear Backlog, and post status updates in thread. Viktor or RunBear may serve this role; alternatively build our own. This also sets an example internally of AI in action.
- **Employee Resource Portal (new):** Google Sites-based internal portal covering employee handbook, self-service forms, HR links. Integrate with Deel API. Include an AI bot (handbook RAG) to answer HR queries. Coordinate with Teresa/HR to replace PDF forms.
- **Company Spec document (new):** Centralised org knowledge base — business context, technology, positioning, departmental operations. Each dept contributes their section. Serves as meta-prompt/context for AI use across the company. Inspired by AI Engineering conference concept of a 'SPEC' file.
- **Skills Library on GitHub (new):** Replaces the Prompt Library concept. Jehad to build and curate tailored skills for the company, combined from public sources and adapted. Primary onboarding resource for future team members.
- **Prompt Library AIP project:** To be renamed or closed — superseded by Skills Library approach.
### NemoFlow vs OpenClaw — Initial Finding
Jehad reviewed NemoFlow documentation. Initial assessment: NemoFlow is essentially OpenClaw built for corporate use — more guardrails, fewer integrations, less flexibility. OpenClaw is more flexible but oriented toward personal use. This aligns with the enterprise mindset shift Michael flagged: we need to think of ourselves as an enterprise client, not a startup, especially given multi-country expansion and data residency requirements.
### Security and Enterprise Controls
- All company-wide tool deployments must go through Euclid and Andre's teams for security review. Microsoft Entra (SSO) compatibility is a hard requirement.
- Data residency and regulatory compliance vary by country — Singapore is the first go-to-market and has strict rules. UAE deferred as a market for now.
- Andre's team is using Claude CoWork heavily for document translation (thousands of docs from China). Hit a thread-length limit issue yesterday — couldn't compact. Jehad to check in with Lysander/Rosa to offer support.
- Andre uses Obsidian alongside Notion to back up CoWork outputs — every session is saved externally to avoid loss when threads hit limits. Useful technique to adopt.
### Decisions made
- Linear stays in Sandbox, not Production.
- AIP-1 scope expanded to Finance Department API Integration.
- Prompt Library project replaced by Skills Library on GitHub.
- Enterprise security/SSO protocol with Euclid and Andre's teams is a mandatory gate for company-wide deployments.
- Obsidian to be assessed as a knowledge/context backup tool.
- Skills Library to be maintained on GitHub by Jehad; tailored to company needs.
### Carried forward
See Open Action Items table above. New items 15–23 added.
---
## 2026-04-03 — Daily Standup #2
<empty-block/>
**Attendees:** Michael Bruck, Jehad Altoutou
**Format:** Daily standup (titled "AI Tools Compliance and Strategy Meeting" in calendar)
**Duration:** \~38 minutes
### Registry updates
- **Lindy (AIR-21): REJECTED.** Fails Gate 1 on data training policies — SaaS only, no self-hosting, ambiguous ToS on data usage. Cannot meet compliance requirements.
- **OpenClaw (AIR-39): Sandbox → Monitor.** Not actively being sandboxed. NemoClaw preferred for corporate use; OpenClaw retained for reference.
- **NemoClaw (AIR-60): Remains in Sandbox.** ISO 42001 ready, better compliance posture than OpenClaw. To be deployed on Mac Mini for hands-on trial as a Slack bot. Michael and Jehad each get an instance.
- **Dify (AIR-22): Remains in Evaluating.** Retained as secondary tool for RAG-intensive workflows. N8N confirmed as primary workflow automation tool.
- **N8N (AIR-19):** Flagged for a Gate 1 analysis for completeness — currently in Sandbox without formal compliance documentation.
- **Viktor (AIR-38) and RunBear (AIR-56):** Both to be trialled alongside NemoClaw as Slack bots. Comparison exercise to determine best fit for AI Internal Hub bot and general-purpose agent use.
### Projects
- **AI Internal Hub Slack bot (#16):** Confirmed as a future AIP project. Bot should auto-acknowledge tool suggestions in the Slack channel, create Linear Backlog entries, and post status updates in thread. NemoClaw, Viktor, or RunBear could serve this role. Build in sandbox Slack first.
- **Finance items (#5, #6, #8, #15):** All grouped as Ann-related. Need to understand her workflow first before proposing solutions. Airwallex API and invoice bot dependent on Ann's requirements and Xero setup.
- **Employee Resource Portal (#17):** Needs Teresa and Deel to be up and running first. Parked for now.
- **Company Spec (#18):** Low priority. Open but not actively being worked.
### Key findings / discussions
- **NemoClaw vs OpenClaw deep dive:** Both pass evaluation functionally. NemoClaw differentiator is ISO 42001 compliance, hardware privacy router for sensitive data routing to local LLM (Ollama), and OpenShell runtime isolation. OpenClaw more flexible but personal-use oriented. NemoClaw routes sensitive prompts to on-device LLM, non-sensitive to cloud APIs (Claude, OpenAI). Mac Mini too underpowered (16GB) for local models — Hostinger VPS could host Ollama in future.
- **Lindy vs N8N vs Dify three-way comparison:** Michael ran a thorough Gate 1 analysis. N8N wins on integration breadth (300+), self-hosting, and flexibility. Dify better for RAG and visual prototyping. Lindy suited to non-technical users but fails on data training and SaaS lock-in. Agreed: N8N primary, Dify secondary, Lindy dropped.
- **Skills \> Prompts:** Team confirmed the shift from prompt libraries to skills repos. Skills are persistent, versioned, and composable — prompts are ephemeral. GitHub repo is the right home. This methodology also serves as training material for future hires.
- **Self-serve AI tools for non-technical staff:** Discussed risks. Agreed that self-serve is too risky at this stage — non-technical users could inadvertently corrupt internal data. Better approach: provide a managed agent (e.g. NemoClaw) with guardrails rather than giving direct access to workflow builders.
- **Context/prompt management (#12):** Resolved — GitHub-based skills repo is the answer. No need for a separate Notion-based system.
- **Gemini Ultra licence (#13):** Parked. Not needed right now.
### Decisions made
- NemoClaw over OpenClaw for corporate agent use (ISO compliance)
- OpenClaw moved to Monitor; NemoClaw stays in Sandbox for active trial
- Lindy rejected — fails Gate 1, SaaS-only, data training concerns
- N8N confirmed as primary workflow tool; Dify retained as secondary for RAG
- Context/prompt management resolved via GitHub skills repo
- Gemini Ultra licence parked
- Skills Library on GitHub confirmed done; Prompt Library AIP closed
- Non-technical self-serve AI tools too risky — managed agent approach preferred
- Gate 1 analysis needed for N8N (for compliance hygiene)
### Carried forward
See Open Action Items table above. New items 24–26 added.
