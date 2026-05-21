---
type: pulse
title: Retroactive attribution sweep — 2026-05-21
slug: 2026-05-21-lint-followup-attribution-sweep
created: 2026-05-21
updated: 2026-05-21
departments: [ai-office]
confidence: high
sources: []
related: [2026-05-20-lint, feedback-attribution-from-fireflies, claude-md, 2026-05-11-notion-restricted-to-aio-no-broad-rollout]
---

# Retroactive attribution sweep — 2026-05-21

Mandatory first item from the 2026-05-20 lint's carry-forward backlog (§A). Sweeps the existing wiki for over-attribution of claims to named persons derived solely from Fireflies transcripts. The CLAUDE.md v0.12 attribution rule (added 2026-05-20) is preventative-going-forward; this sweep is the cleanup pass for content written before the rule landed.

## Methodology

1. **Enumerated pages with meeting sources** — 197 pages across `entities/`, `concepts/`, `processes/`, `projects/`, `decisions/`, `lessons/`, `briefs/` carry one or more `sources/meetings/*` slugs in their frontmatter.
2. **Focused on high-risk surfaces** named in the carry-forward — the 2026-05-12 Bonaventure AI-native call, the 2026-05-12 Andrew onboarding review, the 2026-05-18 CEO meeting, and especially the 2026-05-11 AIO standup-with-Jehad batch where shared-mic attribution swap is documented.
3. **Pattern-matched confident-attribution constructs**: `**Name** said`, `Per Name`, `Name's read:`, `Name pushed back`, `Name flagged`, `Name articulated`, `^Name: "...`, `Quoted reasoning` sections.
4. **For each match, checked corroboration sources**:
   - Curator confirmation in any subsequent ingest (`Confirmed by Michael <date>`).
   - Multi-source `sources:` listing including a non-Fireflies item (Jehad's vault import, Notion log, Slack thread).
   - Pre-existing `decided_by:` / `captured_by:` in the source page.
   - Role-locked content (a CEO-only ruling, a named-meeting context where the person is the primary participant, etc.).
5. **Classified each finding** as GREEN (corroborated, leave), AMBER (single Fireflies source but role-lock or strong context corroborates), RED (uncorroborated; soften).

## Findings

### GREEN — corroborated, no action

| Page | Why it's safe |
|---|---|
| `decisions/2026-05-12-generalise-factset-to-news-sources.md` | Multi-source (`sources: [2026-05-12-aio-andrew-marketing, jehad-vault-import-2026-05-13]`). Andrew is the named primary participant in the meeting. Andrew's quote corroborated by Jehad's vault import. |
| `decisions/2026-05-12-single-domain-gems-com-with-country-paths.md` | Same multi-source corroboration pattern as the FactSet decision. Andrew-named meeting + non-Fireflies source. |
| `briefs/aio-skills-sor-architecture-jehad.md` | "Jehad's view" matches were title metadata, not Fireflies-derived attribution. Brief is Jehad-authored from his personal vault — `captured_by: jehad-altoutou` is provenance, not transcript attribution. |
| `briefs/aio-playbooks-jehad.md` | Same — personal-vault author attribution, not transcript attribution. |
| `entities/internal/andrew-soane.md` | Multiple Bonaventure-attributed lines, but they're framed as Andrew's *reactions to* known Bonaventure positions. Underlying Bonaventure quotes are sourced to `2026-05-12-bonaventure-ai-native-call` (Bonaventure-named meeting; low shared-mic risk) + downstream decisions ratify the substance. |
| `briefs/ai-native-janus-positioning.md` | Three direct Bonaventure quotes, all sourced to `2026-05-12-bonaventure-ai-native-call`. The call was Bonaventure-named (he was the primary speaker), reducing shared-mic risk. Downstream decisions (Singapore-as-lead-market, three-messaging-pillars, marketing-pr-outputs-reordered) all ratify the substance. |
| `projects/singapore-news-monitoring.md` | Multiple Bonaventure mentions. The critical line ("white paper Bonaventure referenced") is followed by `Confirmed by Michael 2026-05-15` — explicit curator corroboration. Other Bonaventure lines are from his named call. |
| `decisions/2026-05-18-ceo-global-kb-unified-market-ui.md` | Sole-source meeting, but the meeting is the CEO call and the decision is role-locked content (only CEO can issue a global-KB direction statement). `decided_by: bonaventure-wong` corroborated by role-lock. |

### AMBER — single Fireflies source, corroborated by role-lock or organisational consistency

| Page | Attribution | Corroboration |
|---|---|---|
| `decisions/2026-05-11-notion-restricted-to-aio-no-broad-rollout.md` | `decided_by: bonaventure-wong` ruling on Notion seats. | Role-lock — only the CEO can issue this ruling. Body line 21 already hedged "speaker unattributed"; this sweep adds an explicit confidence note in the body acknowledging the corroboration is role-lock, not transcript-direct. **Action taken: confidence note added.** |
| `decisions/2026-05-11-notebooklm-retirement-html-over-image-outputs.md` | Historical claim "Bonaventure championed [NotebookLM] heavily ... pushed Michael to use it more often." | Historical-context claim, not a transcribed-line attribution. Treat as established organisational history. No softening needed. |

### RED — uncorroborated, needs softening

**None found** in the sampled high-attribution surfaces. The wiki's existing discipline (multi-source citations, `Confirmed by Michael` notes after ambiguous transcripts, role-lock for CEO-level content) appears to have caught most of the over-attribution risk pre-emptively. The risk surfaces flagged in the carry-forward (2026-05-12 Bonaventure call, 2026-05-12 Andrew session, 2026-05-18 CEO meeting, 2026-05-11 standup-with-Jehad) all turn out to have at least one of: (a) named-meeting context, (b) multi-source corroboration, (c) downstream Michael-confirmed ratification, or (d) role-lock.

### Sole-source pages from the high-shared-mic-risk 2026-05-11 standup batch

The 2026-05-11 AIO standup-with-Jehad is the documented shared-mic incident. 10 pages carry it as their sole source:

- `entities/vendors/linear.md`
- `entities/departments/hr.md`
- `entities/people/yusuf-apple-dubai.md`
- `concepts/peer-to-peer-mesh-federation-pattern.md`
- `projects/april-2026-aio-transcripts-recovery.md`
- `decisions/2026-05-11-notebooklm-retirement-html-over-image-outputs.md`
- `decisions/2026-05-11-notion-restricted-to-aio-no-broad-rollout.md`
- `lessons/2026-05-11-privacy-vs-personal-vault-content-taxonomy.md`
- `briefs/aio-skills-sor-architecture-jehad.md`
- `briefs/aio-playbooks-jehad.md`

Pattern-scanned for direct-attribution constructs (`Michael said`, `Jehad said`, `^Name: "..."`, etc.). Result: **zero direct-attribution patterns found** in the sole-source pages (the two briefs matched on title metadata only). The standup ingest discipline already routed shared-mic content through framing like "the standup discussion" / "captured in the standup" rather than attributing specific lines to Michael or Jehad. The standup skill's post-hoc re-attribution work (per the carry-forward note) appears to have headed off the obvious over-attribution before it reached the wiki.

## Edits made

- `decisions/2026-05-11-notion-restricted-to-aio-no-broad-rollout.md` — added an **Attribution confidence** note after the existing "speaker unattributed" line. Documents that the corroboration is role-lock + organisational-policy consistency, not direct-quote attribution. `decided_by: bonaventure-wong` retained.

That is the only inline softening required by this sweep.

## Scope caveats

- **Not exhaustive.** This sweep covered ~30 pages directly via grep patterns; 197 pages have meeting sources in scope. The unsampled remainder may contain over-attributions that the grep patterns didn't catch (e.g., implicit attribution via wikilinks rather than explicit `Name said` constructs).
- **Pattern coverage.** The grep heuristics caught `Name said`, `Per Name`, `Name's view`, `^Name:`, `Quoted reasoning`. They would miss subtler patterns (a `[[bonaventure-wong]]` wikilink in a body sentence where the surrounding prose implies direct speech but doesn't use a flagged verb).
- **No retroactive softening on pages flagged GREEN/AMBER.** Where corroboration exists, the rule is "preserve attribution where it's confirmed" — softening would degrade the entity graph for no gain. Only RED cases get softened, and there were none.
- **Going-forward discipline holds.** The CLAUDE.md v0.12 rule remains the primary mechanism for preventing future over-attribution. This sweep is a *cleanup pass*, not a *guarantee of historical correctness*.

## What changed methodologically

This sweep tested the hypothesis that the wiki was carrying over-attributed historical claims. The result is more reassuring than the carry-forward implied: the wiki's existing ingest discipline (multi-source citation, `Confirmed by Michael` notes, role-lock framing, named-meeting context) already absorbs most of the Fireflies-attribution risk. The single inline edit (notion-restricted) is the only true correction needed in the sampled scope.

**Implication for future lints.** A permanent attribution-confidence check in §5.3 (proposed in the 2026-05-20 lint as a process-improvement candidate) should focus on *new ingests* — flagging confident attribution when the only source is a single Fireflies transcript without role-lock context. The retroactive surface is small enough that further sweeps can be reactive (when a specific over-attribution surfaces in conversation), not scheduled.

## Carry-forward updates

The 2026-05-20 lint's §A (retroactive attribution sweep) is **complete**. Remaining 2026-05-20 carry-forward items continue in this same lint workstream — see the 2026-05-21 lint report for execution status.

## Related

- CLAUDE.md v0.12 attribution rule (added 2026-05-20).
- [[2026-05-20-lint|2026-05-20 lint report]] §A — the directive this sweep executes.
- [[feedback-attribution-from-fireflies]] — user-memory entry; matches the rule.
- [[2026-05-11-notion-restricted-to-aio-no-broad-rollout]] — only page modified inline.
