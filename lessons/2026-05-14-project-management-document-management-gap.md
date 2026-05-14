---
type: lesson
title: Project Management document/version management is an acknowledged gap — Prime Radiant is the operational answer
slug: 2026-05-14-project-management-document-management-gap
created: 2026-05-14
updated: 2026-05-14
departments: [ai-office, it-ops, iso]
status: active
sources: [2026-05-14-pm-workflow-walkthrough-lysander]
related: [project-management-digital-delivery-workflow, michael-bruck, euclid-wong, janus-prime-radiant-build, iso-compliance-programme, llm-wiki, peer-to-peer-mesh-federation-pattern, 2026-05-14-ai-bounded-role-in-project-management]
---

# Project Management document/version management is an acknowledged gap

## What we learned

Toward the end of the 14 May Project Management workflow walkthrough, [[michael-bruck|Michael]] probed Lysander on how Project Management handles document control, version management, and the relationship between templates and project-specific artefacts today. The probe was triggered by what was on screen: Lysander had been presenting the entire 28-phase workflow from a **complex Excel master spreadsheet** with extensive cross-links to Google Docs templates and working documents — one cell linking to a charter template, another to a handoff-minutes template, another to a verification deliverables list, etc. The visual was the gap-in-action: a single brittle Excel with versioned Google-Docs links serving as the canonical workflow surface for the entire function. Lysander's answer confirmed it:

> "In our project development before, every project manager — he had his open files. All of his files. Many people are paying. ISO — that's not possible."

> "Document control is very important for all companies. This is the basic rule."

Michael walked through the analogy from his IBM days — Engineering Change Orders (ECOs):

> "When I was in high school, my first job was at IBM. My work was to go to the computer mainframe and make some changes. This line moves from there, separated, reconnected — everything in the book. A big book. It also says exchange commands — you remember ECO? Engineering Change Order, right? Because that's what you did. Engineering Change Order. My work was — so engineers also did this thing... This is my thinking. We need to figure out how to implement, maybe AI can help us, but the core issue is, I'm looking for every company's different functions. For example, the system of record — this is the gold standard, this is the real version."

And the synthesis:

> "Knowledge, methods, decisions — the change is easy to get because it is the decision knowledge: why we change this, why we change that — that's the key knowledge. This is not what AI will replace; this is the knowledge layer of mastery. How to use this knowledge. We are building a knowledge circle — you use Obsidian, you know how it operates."

## Why this matters

The lesson here is two-sided:

### Side 1 — Project Management has the discipline but not the substrate

Project Management is highly process-aware (see [[project-management-digital-delivery-workflow|the full workflow walkthrough]]) and uses templates extensively — Lysander demonstrated linking a CAPO project template to actual project data. The current operational substrate is:

- **An Excel master spreadsheet** that walks the 28-phase workflow visually with hyperlinks to per-phase Google Docs (charter template, handoff minutes template, project management plan template, verification deliverables list, training matrix, etc.). This is what Lysander demoed during the walkthrough.
- **Per-project Google Docs** instantiated from those templates as projects begin.
- **Monday.com** alongside for task / project / action tracking (the Janus-wide execution surface).
- Versions of templates exist as files (e.g. version 1.0, version 2.0) but live wherever the individual Project Manager keeps them.
- Each Project Manager keeps their own working copies of the master and the templates.
- There is no canonical "system of record" — Google Docs versioning exists ("Google has versioning, yes Google has versioning") but isn't operationalised as the authoritative store.
- This is acknowledged as an **ISO problem** — Lysander flagged it explicitly: *"ISO — that's not possible."*

### Side 2 — Prime Radiant is shaped exactly to solve this

Michael's response in the meeting reframed the gap as the operating problem Prime Radiant addresses:

- **Decision knowledge as the load-bearing layer** — not the templates themselves, but *why we change things, the decision rationale*. This maps directly onto the wiki's `decisions/` folder discipline.
- **Knowledge layer of mastery** — durable understanding about how to do Project Management work. Maps onto `processes/` and `lessons/`.
- **System of record for changes** — version-controlled, decision-trail-preserving. Maps onto the GitHub-backed Prime Radiant substrate per [[janus-prime-radiant-build|the program-level hub]].

The Prime Radiant pattern is, by design, the answer to "where does Project Management's decision history actually live." This lesson captures the moment that fit became explicit in the conversation.

## Three layers Michael drew out

| Layer | What it is | Lives in (Prime Radiant) |
|---|---|---|
| **Knowledge** | Durable understanding of how Project Management operates | `processes/` + `concepts/` |
| **Methodology** | How to do things — templates, playbooks | `processes/` (the [[project-management-digital-delivery-workflow|workflow page]] is an instance) |
| **Decisions** | Why we changed something — the rationale chain | `decisions/` |

The decision layer is the load-bearing piece: *"this is the knowledge layer of mastery."* AI does not replace it — AI surfaces it.

## ISO connection

Lysander's explicit "ISO — that's not possible" links this gap to the [[iso-compliance-programme|ISO programme]]:

- ISO 9001 quality management requires document control.
- ISO 27001 information security requires versioning + audit trails.
- ISO 42001 AI management requires decision traceability — exactly the layer Michael flagged as the most important.

The Project Management document-management gap is therefore not just an operational nuisance; it is an **ISO compliance gap**. Prime Radiant closing it is part of the trust-layer story under [[ai-native-janus-positioning|the AI Native pitch]].

## What changes in the Project Management rollout

Concrete implications for how the Project Management instance is initialised:

1. **Templates live in the Prime Radiant**, version-controlled by Git semantics. Each template has its own page (or set of pages) with explicit version annotations and decision history. The current Google-Docs-template-set becomes the seed content for the Project Management Prime Radiant once it stands up.
2. **Per-project content links to templates** rather than copying them — when the template evolves, the link follows; when a project diverges intentionally, the divergence is captured as a project-level decision page.
3. **`decisions/` is the load-bearing folder for Project Management** — every "why did we change this" goes there. AI surfaces it on request; the Project Manager owns the authoring (per [[2026-05-14-ai-bounded-role-in-project-management]]).
4. **ECO-style change discipline** — Michael's IBM ECO analogy is a useful frame for how Project Management should think about each material change: what changed, why, who approved, what's affected. The wiki's append-only `log.md` + `decisions/` pattern is the ECO log in our context.
5. **The Prime Radiant works *alongside* the current Excel + Google Docs structure, not in place of it.** Lysander's master spreadsheet remains the working surface during the rollout; the Prime Radiant captures decisions, lessons, and durable knowledge. The systems coexist until the Project Management Prime Radiant proves out and the team chooses what (if anything) to migrate.
6. **Ingest of the Excel + Google Docs structure is explicitly deferred to the Project Management instance** (per [[michael-bruck|Michael]], 2026-05-14): we do not ingest Lysander's Excel master and the Google Docs network into the AI Office Prime Radiant. That content is operational Project Management content; it belongs in the Project Management Prime Radiant once that vault stands up. Understanding the structure remains important for *initialising* the Project Management Prime Radiant — i.e. designing the folder taxonomy, template structure, and decision-trail discipline so the migration path is clean when it happens.

## Why this is non-obvious

Most companies attempt to solve document-management with another *system* — SharePoint, Confluence, Notion, Box, sometimes an ECM platform. Lysander already named that "Google has versioning" — and Janus has tried Notion + Google Drive + others. The gap persists because *systems* alone do not enforce the *decision-trail discipline*; they just store files. The Prime Radiant difference is that the schema enforces decision-as-first-class: every change is captured as a dated, traced, linked decision page. The substrate is the discipline, not just the storage.

This is what the AIO instance has been quietly demonstrating since 5 May. The Project Management instance is the first test of whether the same discipline transfers cleanly to a function that already has heavy process documentation.

## Watch for

- Whether Project Management's existing template version chaos genuinely transfers into the version-controlled Prime Radiant cleanly — or whether the messy initial migration burns the early momentum.
- Whether the decision-layer authoring discipline holds under Project Management workload — *do Project Managers actually write `decisions/` pages, or do they revert to email-only decision capture as soon as deadlines hit?*
- ISO 9001 audit-readiness implications when Project Management is fully on Prime Radiant — both the upside (decision-trail finally exists) and the surface-area expansion (now there's more to audit).
- Whether the ECO-style framing resonates with the rest of Janus's engineering and IT-Ops culture — could be a useful internal-comms angle for the IT-Ops rollout.

## Related

- [[project-management-digital-delivery-workflow]] — the workflow this gap shows up in.
- [[2026-05-14-ai-bounded-role-in-project-management]] — sibling lesson from the same meeting.
- [[iso-compliance-programme]] — ISO connection (PULS programme).
- [[janus-prime-radiant-build]] — program-level hub; Project Management rollout context.
- [[llm-wiki]] — the methodology Prime Radiant implements.
- [[2026-05-05-kb-direction-markdown-progressive-exposure-not-rag]] — the earlier decision that anchored Janus on Markdown + progressive exposure rather than RAG; this lesson reinforces why that direction was correct for Project Management specifically.
