---
type: decision
title: "Global KB = one unified knowledge base with market-specific UI layer"
slug: 2026-05-18-ceo-global-kb-unified-market-ui
created: 2026-05-18
updated: 2026-05-18
status: active
departments: [ai-office, office-of-ceo]
countries: [sg, ae, gb]
owner: bonaventure-wong
decided_by: bonaventure-wong
captured_by: jehad-altoutou
sources: [2026-05-18-ai-native-ceo]
related: [janus-prime-radiant-build, joyce-woo, 2026-05-12-singapore-as-lead-market, peer-to-peer-mesh-federation-pattern]
---

# Global KB = one unified knowledge base with market-specific UI layer

**Date:** 18 May 2026
**Source:** AI Native CEO meeting ([[2026-05-18-ai-native-ceo]])
**Decided by:** Bonaventure Wong (CEO)

---

## Decision

One unified global knowledge base. Market-specific UI layer on top. Open access across departments.

Cross-department connectivity is the design goal — not siloed per-department brains that never talk to each other.

---

## Singapore two-layer model

For the Singapore market specifically, Bonaventure articulated a two-layer structure:

1. **Global KB layer:** Read access for Singapore team to the full Janus global knowledge base.
2. **Local vault layer:** Singapore-specific knowledge feeds back upward into the global KB.

This is a practical expression of the federated Prime Radiant pattern — each locale contributes rather than being walled off.

---

## Context

This direction was confirmed after the 18 May Prime Radiant demo to Bonaventure and Joyce Woo. Seeing the system in action (entity nodes auto-sourced from Joyce's white paper, Obsidian graph view, HTML deck generated from the system) prompted Bonaventure to articulate the long-arc architectural intent.

Prior work had established department-level Prime Radiant instances ([[2026-05-07-llm-wiki-extends-to-marketing-domain]], [[2026-05-08-marketing-prime-radiant-greenlit-with-andrew]]). This decision elevates the scope to a company-wide unified KB as the end-state, with department instances as intermediary build steps.

---

## Known constraint (deferred)

Obsidian's single-repo limitation blocks full cross-department connectivity at scale. This was surfaced in the meeting and explicitly deferred — the federation architecture needs further design work (see [[peer-to-peer-mesh-federation-pattern]] and [[2026-05-14-personal-vaults-shelved-pending-federation-redesign]]) before this direction is fully operationalisable.

---

## Implications

- The [[janus-prime-radiant-build]] program is now explicitly scoped toward a company-wide unified KB, not just per-department instances.
- The Singapore market rollout (Joyce Woo) is the first practical test of the two-layer model.
- Cross-department connectivity design becomes a first-class engineering requirement alongside the federation redesign work.
- The market-specific UI layer is a new requirement — the wiki's current HTML deck generation capability is a precursor; a more formalised UI layer needs design.
