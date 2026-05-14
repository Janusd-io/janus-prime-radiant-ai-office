---
type: lesson
title: PM document/version management is an acknowledged gap — Prime Radiant is the operational answer
slug: 2026-05-14-pm-document-management-gap
created: 2026-05-14
updated: 2026-05-14
departments: [ai-office, it-ops, iso]
status: active
sources: [2026-05-14-pm-workflow-walkthrough-lysander]
related: [pm-digital-delivery-workflow, michael-bruck, euclid-wong, janus-prime-radiant-build, iso-compliance-programme, llm-wiki, peer-to-peer-mesh-federation-pattern, 2026-05-14-ai-bounded-role-in-pm]
---

# PM document/version management is an acknowledged gap

## What we learned

Toward the end of the 14 May PM workflow walkthrough, [[michael-bruck|Michael]] probed Lysander on how PM handles document control, version management, and the relationship between templates and project-specific artefacts today. Lysander's answer surfaced an operational gap PM already recognises:

> "In our project development before, every project manager — he had his open files. All of his files. Many people are paying. ISO — that's not possible."

> "Document control is very important for all companies. This is the basic rule."

Michael walked through the analogy from his IBM days — Engineering Change Orders (ECOs):

> "When I was in high school, my first job was at IBM. My work was to go to the computer mainframe and make some changes. This line moves from there, separated, reconnected — everything in the book. A big book. It also says exchange commands — you remember ECO? Engineering Change Order, right? Because that's what you did. Engineering Change Order. My work was — so engineers also did this thing... This is my thinking. We need to figure out how to implement, maybe AI can help us, but the core issue is, I'm looking for every company's different functions. For example, the system of record — this is the gold standard, this is the real version."

And the synthesis:

> "Knowledge, methods, decisions — the change is easy to get because it is the decision knowledge: why we change this, why we change that — that's the key knowledge. This is not what AI will replace; this is the knowledge layer of mastery. How to use this knowledge. We are building a knowledge circle — you use Obsidian, you know how it operates."

## Why this matters

The lesson here is two-sided:

### Side 1 — PM has the discipline but not the substrate

PM is highly process-aware (see [[pm-digital-delivery-workflow|the full workflow walkthrough]]) and uses templates extensively — Lysander demonstrated linking a CAPO project template to actual project data. But:

- Templates exist as files (e.g. version 1.0, version 2.0).
- Each PM keeps their own working copies of those templates.
- There is no canonical "system of record" — Google Docs versioning exists ("Google has versioning, yes Google has versioning") but isn't operationalised as the authoritative store.
- This is acknowledged as an **ISO problem** — Lysander flagged it explicitly: *"ISO — that's not possible."*

### Side 2 — Prime Radiant is shaped exactly to solve this

Michael's response in the meeting reframed the gap as the operating problem Prime Radiant addresses:

- **Decision knowledge as the load-bearing layer** — not the templates themselves, but *why we change things, the decision rationale*. This maps directly onto the wiki's `decisions/` folder discipline.
- **Knowledge layer of mastery** — durable understanding about how to do PM work. Maps onto `processes/` and `lessons/`.
- **System of record for changes** — version-controlled, decision-trail-preserving. Maps onto the GitHub-backed Prime Radiant substrate per [[janus-prime-radiant-build|the program-level hub]].

The Prime Radiant pattern is, by design, the answer to "where does PM's decision history actually live." This lesson captures the moment that fit became explicit in the conversation.

## Three layers Michael drew out

| Layer | What it is | Lives in (Prime Radiant) |
|---|---|---|
| **Knowledge** | Durable understanding of how PM operates | `processes/` + `concepts/` |
| **Methodology** | How to do things — templates, playbooks | `processes/` (the [[pm-digital-delivery-workflow|workflow page]] is an instance) |
| **Decisions** | Why we changed something — the rationale chain | `decisions/` |

The decision layer is the load-bearing piece: *"this is the knowledge layer of mastery."* AI does not replace it — AI surfaces it.

## ISO connection

Lysander's explicit "ISO — that's not possible" links this gap to the [[iso-compliance-programme|ISO programme]]:

- ISO 9001 quality management requires document control.
- ISO 27001 information security requires versioning + audit trails.
- ISO 42001 AI management requires decision traceability — exactly the layer Michael flagged as the most important.

The PM document-management gap is therefore not just an operational nuisance; it is an **ISO compliance gap**. Prime Radiant closing it is part of the trust-layer story under [[ai-native-janus-positioning|the AI Native pitch]].

## What changes in the PM rollout

Concrete implications for how the PM instance is initialised:

1. **Templates live in the Prime Radiant**, version-controlled by Git semantics. Each template has its own page (or set of pages) with explicit version annotations and decision history.
2. **Per-project content links to templates** rather than copying them — when the template evolves, the link follows; when a project diverges intentionally, the divergence is captured as a project-level decision page.
3. **`decisions/` is the load-bearing folder for PM** — every "why did we change this" goes there. AI surfaces it on request; PM owns the authoring (per [[2026-05-14-ai-bounded-role-in-pm]]).
4. **ECO-style change discipline** — Michael's IBM ECO analogy is a useful frame for how PM should think about each material change: what changed, why, who approved, what's affected. The wiki's append-only `log.md` + `decisions/` pattern is the ECO log in our context.

## Why this is non-obvious

Most companies attempt to solve document-management with another *system* — SharePoint, Confluence, Notion, Box, sometimes an ECM platform. Lysander already named that "Google has versioning" — and Janus has tried Notion + Google Drive + others. The gap persists because *systems* alone do not enforce the *decision-trail discipline*; they just store files. The Prime Radiant difference is that the schema enforces decision-as-first-class: every change is captured as a dated, traced, linked decision page. The substrate is the discipline, not just the storage.

This is what the AIO instance has been quietly demonstrating since 5 May. The PM instance is the first test of whether the same discipline transfers cleanly to a function that already has heavy process documentation.

## Watch for

- Whether PM's existing template version chaos genuinely transfers into the version-controlled Prime Radiant cleanly — or whether the messy initial migration burns the early momentum.
- Whether the decision-layer authoring discipline holds under PM workload — *do PMs actually write `decisions/` pages, or do they revert to email-only decision capture as soon as deadlines hit?*
- ISO 9001 audit-readiness implications when PM is fully on Prime Radiant — both the upside (decision-trail finally exists) and the surface-area expansion (now there's more to audit).
- Whether the ECO-style framing resonates with the rest of Janus's engineering and IT-Ops culture — could be a useful internal-comms angle for the IT-Ops rollout.

## Related

- [[pm-digital-delivery-workflow]] — the workflow this gap shows up in.
- [[2026-05-14-ai-bounded-role-in-pm]] — sibling lesson from the same meeting.
- [[iso-compliance-programme]] — ISO connection (PULS programme).
- [[janus-prime-radiant-build]] — program-level hub; PM rollout context.
- [[llm-wiki]] — the methodology Prime Radiant implements.
- [[2026-05-05-kb-direction-markdown-progressive-exposure-not-rag]] — the earlier decision that anchored Janus on Markdown + progressive exposure rather than RAG; this lesson reinforces why that direction was correct for PM specifically.
