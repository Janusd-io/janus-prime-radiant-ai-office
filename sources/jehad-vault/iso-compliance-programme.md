---
type: project
title: ISO Compliance Programme
slug: iso-compliance-programme
created: 2026-05-07
updated: 2026-05-13
departments: [it-ops, ai-office, office-of-ceo]
status: active
owner: michael-bruck
sources: [jehad-vault-import-2026-05-13]
related: [simon-tarskih, bonaventure-wong, michael-bruck, jehad-altoutou, ai-tool-evaluation-framework, ai-tool-evaluation-iso-procedure, iso-certification-programme, iso-ims-puls, whisperflow]
captured_by: jehad-altoutou
---

> _Jehad's personal-vault articulation of this topic, imported 2026-05-13. The canonical wiki page is at `projects/iso-compliance-programme.md` — this file is preserved as a source for divergent framing / additional context._

# ISO Compliance Programme

Hub for Janus's ISO compliance work. Top priority for [[bonaventure-wong]]; working partnership between [[michael-bruck]] (programme owner) and [[simon-tarskih]] (ISO programme facilitator). Multi-process scope — not just documentation, but aligning the AI Office's existing process stack against ISO standards.

> Dedupe note: closely related to the canonical concept page [[iso-certification-programme]], [[iso-ims-puls]], and project page [[ai-tool-evaluation-iso-procedure]]. This is the cross-cutting programme hub restored from PR backup; the curator should reconcile.

## Why this is its own project hub

ISO compliance has been showing up across the wiki as a *gate* on other work — automation projects blocked behind it, the standup skill iterating toward ISO alignment, `ai-tool-evaluation` needing ISO-compliance work. That cross-cutting role means it earns a dedicated narrative hub rather than being scattered across decision pages and Monday items.

Bonaventure reordered the executive-management-system architecture so ISO-compliant workflows come first.

## Scope

Multi-track programme:

| Track | What | Owner | Status |
|---|---|---|---|
| **ISO documentation foundation** | Input → activities → output template captured for Janus's processes (the work Simon facilitates). | [[simon-tarskih]] | Recurring blocker — Michael following up across multiple AIO standups. |
| **AI Tool Evaluation framework ISO alignment** | Make [[ai-tool-evaluation-framework]]'s gates and dossier requirements ISO-compliant. | [[michael-bruck]] + Simon Tarskih | Active. |
| **Standup skill v3.x ISO alignment** | Skill v3.x continues iterating until ISO-aligned; v2.1 stays in production until v3 ships. | [[jehad-altoutou]] | Active. |
| **ISO facilitation skill build** | New Claude skill scaffolding Simon's facilitated sessions; candidate consumer of [[whisperflow]] for voice capture. | [[jehad-altoutou]] | In definition. |
| **ISO compliance gate enforcement** | Automation projects can't begin until ISO documentation for the relevant scope is complete. | [[michael-bruck]] | Policy active. |

## Roles

- **Sponsor:** [[bonaventure-wong]] — top priority; sets bar alongside Simon for ISO interpretation.
- **Programme owner:** [[michael-bruck]] — coordinates across tracks; recurring follow-up with Simon.
- **Working partner / ISO facilitator:** [[simon-tarskih]] — facilitates documentation sessions.
- **Engineering:** [[jehad-altoutou]] — builds the ISO facilitation skill, advances standup skill v3.x toward ISO alignment.

## Cross-references

- Tools / vendors implicated: [[whisperflow]] (voice capture for facilitation), [[claude-code]] (skill substrate), [[notion]] (Operations Notebook journal), [[fireflies]] (transcripts of facilitated sessions).
- Adjacent process: AI Policy gate — separate but adjacent governance gate; ISO is foundational, AI Policy gate is operational.

## Open / pending

- Get the ISO documentation references from Simon (recurring blocker on AIO standups).
- Confirm Wispr Flow Gate 1 outcome — voice-capture readiness for the ISO facilitation skill.
- Scope which Janus processes need ISO-aligned documentation first; surface order from Simon + Bonaventure agreement.

## Watch for

- Bonaventure's expectations on ISO interpretation alignment with Simon's interpretation — divergence here is the key risk.
- ai-tool-evaluation framework version that incorporates ISO-aligned dossier requirements.
- Standup skill v3.x reaching ISO-aligned production state.
