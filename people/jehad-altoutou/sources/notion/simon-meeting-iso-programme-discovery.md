---
type: source
source_type: notion
slug: simon-meeting-iso-programme-discovery
title: Simon Meeting — ISO Programme Discovery
created: 2026-04-23
captured_by: jehad-altoutou
notion_url: https://www.notion.so/348114fc090c81cf9ea9dc6dcff92674
audience: department
departments: [ai-office]
sensitivity: dept
sensitivity_confidence: 0.5
---

> **Meeting:** Simon (ISO lead) ↔ AI Office
> **Scheduled:** This week (Apr 2026)
> **Duration:** 60 minutes
> **Attendees:** Simon, Michael Bruck, Jehad Altoutou
> **Format:** Conversation, recorded via Fireflies. Transcript feeds back to AI Office Operations Notebook.
> **Meeting held:** 22 April 2026 — see Meeting Notes below.
> **Related:** [SOR Tooling Analysis — Notion vs ](https://www.notion.so/348114fc090c81d79220ef9b4e001c7f)[Monday.com](http://Monday.com)
## Meeting Notes — 22 April 2026
> **Recorded:** Fireflies — transcript `AI-ISO-22-April`
> **Duration:** \~1h54m
> **Attendees:** Simon Tarskih, Michael Bruck, Jehad Altoutou
### Summary — the working-relationship model
Simon and the AI Office exit this meeting aligned on a two-sided partnership. Simon owns the ISO domain — he defines standards, documents compliance, leads the audit. The AI Office leads automation and tooling and serves as Simon's technical accelerator. Michael explicitly positioned the AI Office as **Simon's first ISO pilot** — the group most ready to be audited — and Simon accepted. Both sides committed to building this "together," with standards as the foundation and automation layered on top.
The framing Michael used: Janus is currently "a jazz band" (improv-heavy) and needs to become "a symphony orchestra" (standardised, conducted). You can't automate what isn't standardised — Simon's work unblocks the AI Office's work.
### Simon's ISO roadmap
**Scope — Integrated Management System combining three standards:**
- **ISO 9001** — quality management (baseline structure: context, leadership, risk, planning, competence, awareness, internal audit, document/record control, corrective action)
- **ISO 27001** — information security management
- **ISO 42001** — AI management system (new standard; few auditors experienced with it yet)
Michael has paid for copies of all three. The standards share common clauses with system-specific additions — hence the integrated approach rather than three parallel efforts. One manual, one audit, one set of common clauses.
**Artefacts Simon will produce, in order:**
1. Assessment of the current state (in progress — he is observing how Janus works before writing anything)
2. Organisational structure document (position titles + RACI for each ISO requirement)
3. Standards map (process diagram of the IMS)
4. List of ISO standards relevant to Janus (certifiable standards plus guide-type standards)
5. List of compliance documents (laws, regulations — GDPR central; jurisdiction-specific additions for Dubai and Singapore)
6. Requirements-to-role matrix (accountable / responsible / consulted / informed per requirement)
7. Integrated management system manual aligned with the ISO structure — the single master document an auditor reads to understand how Janus operates
**Audit plan:** German certification body preferred (reputable, cross-border accreditations, good for Janus brand). First audit scoped to Dubai HQ + Singapore. UK deferred. Simon will contact the certification body next week and intends a preparation audit before the certification audit to avoid critical non-conformity.
**Pace:** Simon asked for 2–3 days to prepare a full plan before the next session. He is confident on the audit mechanics ("I did it 20 years") — his focus is system design and implementation, not certification ritual.
### Tooling and documentation direction
- **Notion confirmed** as the central ISO repository — the "digital binder" for the IMS manual and supporting documents. Simon was previously ambivalent on tooling; after Michael walked through Notion's AI integration and hierarchy, he agreed it is the right surface. Andre's Notion experience flagged as a help resource.
- **Markdown is the format.** The AI Office's argument landed — LLMs are trained on Markdown, PDFs are lossy, and machine-readable + human-readable versions can stay in sync. Simon confirmed familiarity and will draft in it.
- **Mermaid and Figma** flagged as diagramming options for process maps — Simon liked the Mermaid "text + visual dual representation" model.
- **PDFs discouraged.** Michael proposed banning PDF creation within Janus; Simon agreed the manual-entry-from-PDF handovers (e.g. Mariam's onboarding forms routed HR → Finance) are an anti-pattern.
- **Specialist ISO tools (Greenlight Guru, Qualio, MasterControl) not needed** at this stage — Simon is comfortable with Notion + Markdown unless something breaks.
### Automation philosophy — Simon's colour-coded map
Simon walked through a draft map classifying ISO processes by automation potential:
- **Green — automatable:** documentation, monitoring, record control, document control, analysis
- **Yellow — automatable with human oversight:** policy, management review, corrective action
- **Red — cannot be automated:** context setting, stakeholder definition, leadership
This aligns cleanly with the AI Office's risk / task-complexity model and can feed directly into the automation-identification step of Bonaventure's reframed ISO-first stack. Simon will produce a refined version next session.
### Agenda outputs — what resolved, what deferred
<table header-row="true">
<tr>
<td>Agenda goal</td>
<td>Outcome</td>
</tr>
<tr>
<td>ISO standards shortlist</td>
<td>**Resolved.** 9001 + 27001 + 42001 integrated.</td>
</tr>
<tr>
<td>Tooling preference</td>
<td>**Resolved.** Notion + Markdown.</td>
</tr>
<tr>
<td>Pilot department selection</td>
<td>**Deferred.** Simon is starting with organisational structure and standards map before selecting the first workflow pilot. Finance and HR named as highest-value automation targets once processes are documented. AI Office itself offered — and tacitly accepted — as the first ISO audit pilot.</td>
</tr>
<tr>
<td>Simon's asks of the AI Office</td>
<td>**Partial.** Wants 2–3 days to prepare a plan, then regular working sessions. Raised the tool-purchase approval process gap (surfaced via his Monday payment request to Anne — no formal process exists, Bonaventure approved informally).</td>
</tr>
<tr>
<td>Real-time compliance viability</td>
<td>**Resolved — yes, in scope.** Simon agreed that an AI-assisted knowledge base can act as a "real-time ISO spell-checker" once the IMS is in place and structured correctly. Consistent with Bonaventure's continuous-compliance ambition.</td>
</tr>
</table>
### Open questions surfaced (not resolved)
- **Tool ISO certification as an evaluation gate.** Michael raised: if Janus uses a tool that has no ISO certification, is that an audit risk? Should the AI Office's Gate-1 screen include an "is ISO-certified" weighting or a hard requirement? Michael committed to defining this with Simon's input. Likely becomes a new criterion in the tool-evaluation framework.
- **Formal tool-purchase approval workflow.** Michael's Monday.com subscription request to Anne exposed the absence of a standard approval process. Bonaventure's verbal approval was sufficient, but this doesn't scale. Strong candidate for the first cross-department workflow Simon documents and the AI Office automates.
### Action items
- **Simon** — produce organisational structure doc, standards map, relevant-standards list, compliance list, requirements-to-role matrix. Target: next session (\~1 week).
- **Simon** — contact German certification body, discuss audit plan, initiate timeline.
- **Simon + Michael** — set regular standing meeting cadence (weekly suggested).
- **Michael** — define ISO-certification as a new tool-evaluation criterion in the Gate framework (input from Simon).
- **Michael + Jehad** — add "formalise tool-purchase approval workflow" to Ops Notebook as a candidate first workflow pilot.
- **AI Office** — prepare to serve as first ISO audit pilot (self-audit readiness).
### Insights worth preserving
- **Simon's background is deeper than the title suggests.** \~20 years of ISO auditing, former head of a private certification body
- **Michael has some background on standards:** Established some industry standards during his tenure at Intel. Familiar with TQM / DemingConnected into BSI leadership (university friend is chairman). He is not a corporate box-ticker — he wants to design a useful management system, not just pass an audit.
- **The integrated management system saves effort** — one manual, one audit, one set of common clauses. Don't let downstream workflow documentation fragment this.
- **The AI-native operations model translated cleanly to Simon in one sitting** — coordination-tax reduction, three-layer architecture (individual → department → organisation), systems-of-record as sensors, agentic orchestration as the coordination layer, digital-twin framing. Simon understood and accepted the model.
- **Don't rush certification, don't delay the system.** Simon explicitly distinguished — the audit is easy for him; the hard and valuable work is designing and implementing the IMS itself. AI Office priorities should weight system-build over audit-prep.
### Follow-up
Michael to extract actions to the Operations Notebook and share the transcript back to Simon for confirmation. Next working session scheduled after Simon's 2–3 day planning window.
---
## Purpose
Understand Simon's ISO plans so the AI Office can design the automation, documentation, and management system infrastructure to support them. This is **discovery, not a design session**. Outputs feed v3 of the CEO Executive Management System design document and resolve the Notion vs [Monday.com](http://Monday.com) tooling decision.
## Context going in
In the Bonaventure meeting on 20 April 2026, the CEO significantly reframed the CEO Executive Management System project. Rather than starting with a weekly CEO meeting and building down, he put the **ISO-driven workflow foundation** at the top of the stack:
1. Simon defines the ISO standards Janus will comply with
2. Each department documents its own workflows against those standards
3. AI identifies gaps and automation opportunities within each workflow
4. AI agents orchestrate across workflows and detect discrepancies
5. End state: real-time continuous ISO compliance → the eventual "Janus standard" commercial play
Simon is the critical path. The AI Office's job is to give him leverage, not dictate direction.
## Agenda
### 1. Framing (5 min) — Michael opens
Short framing of where the AI Office fits: Janus is building an AI-native organisational model. Each department documents workflows that comply with ISO, agents identify automation opportunities within those workflows, and a cross-departmental agent layer coordinates across them. Bonaventure's ambition is real-time continuous compliance rather than annual audit — a "Janus standard" built on top of ISO. Simon is the domain authority; the AI Office is here to support and accelerate.
### 2. Simon's ISO roadmap (20 min) — Listen mode
Open questions:
- Which ISO standards is Janus implementing, in what order, and why those?
- What's the minimum viable baseline (the "foundation" Bonaventure referenced — the part that can be added to but not subtracted from)?
- What's the realistic timeline to first audit-readiness? Bonaventure's ambition is weeks, not months.
- What evidence artefacts does ISO certification actually require at Janus's stage?
- How does Simon see the relationship between ISO standards and AI-assisted operations — friction, neutral, or accelerant?
### 3. Workflow documentation (15 min)
- How does Simon want departments to document their workflows? Freeform prose, standardised templates, flowchart notation (BPMN, Mermaid), specialist ISO tool?
- Does he have a preferred documentation platform? Has he worked with tools like Greenlight Guru, MasterControl, Qualio, iTrust, or equivalents before, and does he want to use one here?
- If no specialist preference, is Notion acceptable as the documentation substrate?
- Where should the master index of ISO-compliant workflows live so the AI Office can programmatically reference it?
- **Terminology ambiguity to resolve**: the word "workflow" is used differently by ISO (business process) and by AI tooling (agent workflow). Simon's usage wins — the AI Office will adopt his terminology and rename internally.
### 4. Pilot department selection (10 min)
- Which department should be the first workflow pilot? Bonaventure suggested focus areas but deferred to Simon on sequencing. Candidates: Finance (AP/AR, payroll approval — Jennifer already building some of this), HR (onboarding — prior work exists), ISO itself as a self-referential pilot.
- Decision criterion: which department has a workflow well-enough understood that documenting it produces real value in a week, not a month?
- What support does Simon need from AI Office to accelerate the pilot? (Document templates, transcription of workflow interviews, Mermaid diagram generation, draft ISO clause mappings, etc.)
### 5. The real-time compliance vision (5 min)
- Bonaventure is genuinely excited about continuous/real-time ISO compliance rather than annual audit. Does Simon see this as viable?
- Where's the limit — what parts of ISO certification must remain human-audit rituals, and what parts can become automated continuous checks?
- If viable, what data feeds would Simon need the AI Office to surface for him to monitor compliance in real time?
### 6. What Simon needs from us (5 min)
- What blockers does he have right now that the AI Office can unblock this week?
- Who does he need access to? What systems? What decisions from Bonaventure?
- What's the right forum for ongoing Simon ↔ AI Office collaboration — standing sync, ad-hoc, async via Slack?
## Outputs we want to leave with
1. A shortlist (not a decision) of which ISO standards Janus is implementing and in what order.
2. Simon's preference on workflow documentation tooling — specialist, Notion, or either.
3. The pilot department selection.
4. Simon's specific asks of the AI Office for this week.
5. A read on whether real-time compliance is in-scope or aspirational.
## What we're NOT trying to resolve in this meeting
- [Monday.com](http://Monday.com) vs Notion tooling decision (dependent on this meeting's output, but not debated here).
- v3 of the CEO Executive Management System design (this meeting's outputs feed v3; we don't design it live).
- The automation implementation details (those come after workflows are documented).
- Bonaventure's strategic ambitions around the "Janus standard" commercial play (those are separate conversations with him).
## Facilitation notes
**Do it in listening mode.** Simon is new, he's been handed the hardest and most foundational assignment in the company, and he hasn't yet had the airtime to articulate his own plan. If he walks out feeling heard rather than interrogated, the working relationship compounds for the rest of the year. If he feels the AI Office is coming in with an agenda, the opposite.
**Bring Jehad, resist the urge to bring Bonaventure.** Jehad's presence signals the AI Office is showing up technical, not political. Bonaventure's presence would compress Simon's honest answers — Simon won't surface risks or blockers as readily in front of the CEO in his first substantive working session. Report back to Bonaventure separately.
## Meeting follow-up
Michael will extract action items and decisions from the Fireflies transcript into the AI Office Operations Notebook and share back to Simon for confirmation within 24 hours.
---
*Agenda drafted 20 April 2026. Meeting held 22 April 2026 — see Meeting Notes section above for outcomes.*
