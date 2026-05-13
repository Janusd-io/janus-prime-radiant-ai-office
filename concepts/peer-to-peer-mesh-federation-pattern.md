---
type: concept
title: Peer-to-peer mesh federation pattern
slug: peer-to-peer-mesh-federation-pattern
created: 2026-05-11
updated: 2026-05-11
departments: [ai-office]
sources: [2026-05-11-aio-standup-with-jehad]
related: [janus-prime-radiant-build, prime-radiant-three-layer-architecture, llm-wiki, agent-to-agent-protocol, model-context-protocol, jehad-altoutou, michael-bruck]
---

# Peer-to-peer mesh federation pattern

A federation architecture for the [[janus-prime-radiant-build|Janus Prime Radiant]] rollout in which every department-to-department relationship gets its own *shared subfolder* inside each vault. Cross-instance signal flows peer-to-peer through the filesystem rather than top-down through a hub, and rather than through an event broker. The pattern emerged from the 11 May 2026 AIO standup discussion; this page captures the shape, its rationale (cross-pollinisation between disciplines), and its relationship to alternative federation designs.

## The shape

Each Prime Radiant instance is its own Google Shared Drive vault with its own `CLAUDE.md`, its own `inbox/`, and its own folder tree (per [[2026-05-08-marketing-prime-radiant-as-separate-vault|the separate-vault decision]]). Inside `entities/departments/`, each vault carries a folder *or* sub-vault for every other department it touches. When two departments meet — AIO with IT-Ops, AIO with Marketing, Finance with Office-of-CEO — the meeting's transcript and synthesised content land in the **shared** folder visible to *both* department vaults.

```
<AIO Prime Radiant>/entities/departments/
  it-ops/        ← shared with the IT-Ops Prime Radiant
  marketing/     ← shared with the Marketing Prime Radiant
  finance/       ← shared with the Finance Prime Radiant
  ...

<IT-Ops Prime Radiant>/entities/departments/
  ai-office/     ← same folder as AIO's it-ops, viewed from the other side
  ...
```

Both vaults see the AIO-and-IT-Ops shared folder. Both ingestion passes process the meeting. Both vaults' `CLAUDE.md` files contain the schema rules that govern what gets ingested. No central broker, no top-down hub — just mutual filesystem visibility on the cross-cutting subset of content.

The framing surfaced in the meeting was *"it's like a mesh network."* Every peer-to-peer relationship is one shared folder; the company-level digital knowledge twin emerges as the union of all the per-instance content plus the federation edges.

## Why mesh instead of hub-and-spoke

Two alternatives were considered:

- **Top-down hub.** A central Prime Radiant aggregates Signals from every department instance. Single ingest, single canonical view. Simple to design; high coupling; the hub becomes the bottleneck and the political object.
- **Event-broker / Solace-SAM-style.** Departments publish events; subscribers (other departments) pick up only what's relevant to them. This is the architecture being explored separately in AIR-97 ([[linear]] Solace SAM evaluation). Industrial-grade; cleanly decoupled; requires a broker to be standing.

The mesh pattern is the third option, solved at the **file-system / directory level** rather than at the event-broker level. Pros: no broker required; works with the existing Google Drive substrate; each cross-department relationship is concretely visible as a folder both teams can browse. Cons: cross-cutting topics that span three or more departments need explicit fan-out; deletion semantics across vaults need care; ACLs are Drive folder ACLs rather than typed permissions.

The three patterns are not exclusive. The mesh handles routine cross-team meetings and shared decisions; an event broker (if AIR-97 lands) handles real-time signal fan-out; a hub view (if useful for leadership) emerges as a read-only aggregation on top of the mesh.

## Why this matters — cross-pollinisation as the strategic rationale

The standup discussion connected the mesh pattern to a long-arc theme: **cross-pollinisation between disciplines is where the most valuable insights emerge.** The historical references that surfaced:

- **Pixar's central atrium.** Steve Jobs designed Pixar's office so people from different departments would have to meet in the middle — random encounters between animators, story, and engineering produced disproportionate creative output.
- **Bell Labs.** Famous research lab (where [[euclid-wong|Euclid]] worked, per the transcript); breakthroughs repeatedly came from researchers in unrelated fields bumping into each other at the coffee machine.
- **SRI (Stanford Research Institute).** Multiple labs across unrelated domains; cross-domain conversations were often the source of the best ideas.
- **Steve Jobs's typography course.** A single non-degree class he took shaped the design discipline of every Apple product. Pollinisation across one disciplinary boundary; durable consequences.

Companies tend to silo. The mesh federation pattern is a deliberate counter-measure: *the AI does the cross-pollinisation that previously depended on chance encounters.* Department A's Prime Radiant sees that Department B's discussion mentions something relevant; the [[claude|Claude]] processor in Department B's `CLAUDE.md` notices it relevant to Department A and links accordingly; the bee carries pollen between flowers without the bee being a human who happened to walk past at the right moment.

The vision articulated in the meeting: *"That's how we replace [[slack]]. You don't need to chase. The system tells Simon, 'By the way, you were mentioned in this discussion last week — here's the link.'"* The mesh is the substrate that makes that addressable.

## The three-level hierarchy this mesh sits inside

Mesh federation operates at one tier of a three-tier hierarchy:

1. **Personal vault** (per individual). Captures meetings, notes, decisions relevant to one person. Visible to that person only by default.
2. **Department Prime Radiant** (per department). Compounds the personal vaults of its members + department-level Signals; this is the federation peer.
3. **Company-level digital knowledge twin** (Janus-wide). Emerges from the union of department instances + their mesh edges + selective leadership-level access.

Movement upward is selective. A personal-vault decision moves into the department Prime Radiant when it's relevant beyond one individual. A department decision moves into a peer department's vault via the shared `entities/departments/<other>/` folder when both departments are implicated. A signal becomes company-level when the digital-twin layer queries across instances. This is the structural counterpart to the cross-pollinisation rationale.

## Privacy, private, and personal — the access taxonomy

The mesh assumes content has a *visibility tier* that determines which vault edges it traverses. Per the 11 May standup, three tiers were clarified:

- **Public** (shared across departments) — the default once a topic is no longer single-individual or single-department. Flows through the mesh.
- **Private** (restricted, typically only CEO-level access) — e.g., HR salary discussions between [[bonaventure-wong|Bonaventure]] and [[theresa-wong|Theresa]]. Stays in a restricted Drive folder; not federated through the mesh.
- **Personal** (single individual) — for *work-context* use, this means the individual's vault before content has been promoted to the department instance. Per Janus employment contracts, no content is "personal" in the sense of belonging to the individual rather than the company — but operationally, content that has not yet been promoted lives only in the personal vault.

The mesh handles **public** by design. **Private** is a Drive-ACL question. **Personal-as-pre-promotion** is the individual-to-department interface that the `/standup` skill, the proposed `/janus-pulse` skill, and `/ims-enrolment` are all variations on. See [[2026-05-11-privacy-vs-personal-vault-content-taxonomy]] for the lesson.

## Relationship to existing federation primitives

This pattern formalises and extends what's already in CLAUDE.md §1:

- `entities/departments/<dept-slug>.md` (currently a single page per department) is the v0.8 federation primitive. The mesh pattern proposes promoting `entities/departments/<dept-slug>/` from a single file into a *folder* with shared content beneath it.
- The schema change is non-breaking: existing `entities/departments/marketing.md` stays as the entity page; `entities/departments/marketing/` becomes a sibling subfolder for shared content. Frontmatter `[[marketing]]` resolves to the entity page; deeper paths resolve to shared documents.
- The federation linkage is bi-directional: AIO's `entities/departments/marketing/` is the same Drive folder as Marketing's `entities/departments/ai-office/`. Both vaults' CLAUDE.md ingest passes process content from it; both vaults' indexes reflect it.

A formal CLAUDE.md amendment is queued (deferred until the pattern is exercised concretely with [[andrew-soane|Andrew]] and with [[euclid-wong|Euclid]]'s project-management team — first practical tests).

## Open design questions

- **Conflict semantics.** Two ingest passes (AIO and Marketing) might process the same shared document and produce diverging downstream artifacts. Acceptable? Resolved by treating each vault's downstream as independent? Or via a "canonical owner" annotation per shared doc?
- **Three-way and N-way cross-references.** A meeting that touches AIO + Marketing + Finance — does it sit in three pair-wise shared folders, in a multi-department shared folder, or in one folder cross-linked from the other two?
- **Deletion + retention.** When a department leaves the mesh (unlikely but theoretical), what happens to the shared edges?
- **ACL granularity.** Drive folder-level ACLs are coarse; a tag-level visibility annotation (per-page `audience:` frontmatter, already in use on the federated personal-vault pages contributed from [[jehad-altoutou]]'s vault) is finer-grained but harder to enforce.

These are deferred until the first three peer relationships (AIO↔Marketing, AIO↔IT-Ops, AIO↔Office-of-CEO) are operating concretely.

## Related

[[janus-prime-radiant-build]] · [[prime-radiant-three-layer-architecture]] · [[llm-wiki]] · [[agent-to-agent-protocol]] · [[model-context-protocol]] · [[2026-05-11-privacy-vs-personal-vault-content-taxonomy]]
