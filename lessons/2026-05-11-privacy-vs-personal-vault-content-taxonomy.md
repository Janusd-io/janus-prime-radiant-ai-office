---
type: lesson
title: Privacy / private / personal — three-tier vault content taxonomy
slug: 2026-05-11-privacy-vs-personal-vault-content-taxonomy
created: 2026-05-11
updated: 2026-05-11
departments: [ai-office, hr, office-of-ceo]
status: active
sources: [2026-05-11-aio-standup-with-jehad]
related: [janus-prime-radiant-build, peer-to-peer-mesh-federation-pattern, michael-bruck, jehad-altoutou, bonaventure-wong, theresa-wong]
---

# Privacy / private / personal — three-tier vault content taxonomy

A clarification that emerged in the 11 May 2026 AIO standup: the three words *public*, *private*, and *personal* sound similar in English but mean three different things in the context of Janus's Prime Radiant federation. Conflating them is the failure mode; the taxonomy below is the operating definition going forward.

## The three tiers

| Tier | Meaning | Visibility | Example |
|---|---|---|---|
| **Public** | Shared across departments — the default once content is no longer single-individual or single-department. | Visible across the mesh; flows through shared `entities/departments/<other>/` folders. | An AI tooling decision, a cross-department meeting, a strategic POV. |
| **Private** | Restricted to a defined small group; typically only CEO-level access. | Stays in a restricted Drive folder; not federated through the mesh. | HR salary discussions between [[bonaventure-wong|Bonaventure]] and [[theresa-wong|Theresa]]; an employee performance conversation. |
| **Personal** | Content that has *not yet* been promoted from an individual's personal vault to a department Prime Radiant. | Visible only to the individual whose vault it lives in. | A meeting note someone is still drafting; a brainstorm not yet shared. |

**Critical:** per Janus employment contracts, no content is "personal" in the sense of *belonging to the individual rather than the company*. Personal use of company tools for content that is not company work is explicitly forbidden. The "personal" tier in this taxonomy refers only to *operationally pre-promotion content* inside the work context — it's a workflow staging area, not a private space.

## Why this matters

The three-tier hierarchy is what makes the [[peer-to-peer-mesh-federation-pattern|mesh federation pattern]] tractable. Without the tier distinction, the mesh would either over-federate (private content leaks across the mesh) or under-federate (everything stays personal because nobody knows what's safe to promote).

Operationally:

- **Personal tier** is the individual's perception layer — every individual has their own vault where signals first land. Promotion to the department tier is the act of moving content into the department Prime Radiant.
- **Public tier** is the federation surface — the mesh moves content sideways across departments through the shared `entities/departments/<other>/` folders.
- **Private tier** is the policy escape valve — a small number of conversations need to stay outside the federation entirely (executive HR discussions, M&A, performance management).

The CEO can see all three tiers (the apex of the visibility cone). Most operators see public + their own personal. The mesh moves public, not private and not personal.

## Word-choice trap

In casual conversation it's easy to use *private* and *personal* interchangeably ("that's private — I mean, personal — well, you know what I mean"). The 11 May standup exposed the slip: a finance/CEO conversation is *private* (restricted by policy), not *personal* (which would imply non-work content, which is forbidden). Using the word correctly is part of correctly assigning the visibility tier.

Operational guidance: when in doubt, name the audience explicitly ("CEO + Theresa only", "AIO public", "my own draft pre-promotion") rather than reaching for *private* or *personal* — the words are too overloaded to carry the visibility decision on their own.

## Related

[[peer-to-peer-mesh-federation-pattern]] · [[janus-prime-radiant-build]]
