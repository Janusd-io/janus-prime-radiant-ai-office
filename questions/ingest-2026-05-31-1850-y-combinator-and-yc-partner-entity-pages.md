---
type: question
title: Should Y Combinator + named YC partners (Diana Hu, Tom Blomfield, retroactively Garry Tan) get entity pages?
slug: ingest-2026-05-31-1850-y-combinator-and-yc-partner-entity-pages
created: 2026-05-31
updated: 2026-05-31
departments: [ai-office]
status: active
owner: michael-bruck
related: [recursive-self-improving-loop, 2026-05-31-yc-formalises-self-improving-company-playbook, gbrain, 2026-05-22-gbrain-yc-tan-memory-layer]
---

# Should Y Combinator + named YC partners get entity pages?

Escalation filed during the 2026-05-31 batch ingest of the two YC talks. Three intersecting decisions Michael should resolve together.

## The triggers

The 2026-05-31 ingest filed:
- [[2026-04-24-yc-diana-hu-ai-native-company-from-ground-up]] — source by **Diana Hu**, YC Partner.
- [[2026-05-21-yc-blomfield-self-improving-company]] — source by **Tom Blomfield**, YC General Partner (and co-founder of Monzo).
- [[2026-05-31-yc-formalises-self-improving-company-playbook]] — pulse that names both partners as load-bearing.
- [[recursive-self-improving-loop]] — concept that names both partners as the people who formalised the architectural primitive.

Earlier ingests have also surfaced:
- **Garry Tan** — YC President; named extensively in [[gbrain]] and [[2026-05-22-gbrain-yc-tan-memory-layer]] as the author/publisher of the open-source markdown-first agent memory layer.

**Y Combinator itself** has no entity page on this wiki.

Three named YC partners are now load-bearing on wiki content (Diana Hu, Tom Blomfield, Garry Tan). All three currently exist only as inline name-checks within source files / pulse pages, not as `entities/people/` pages.

## Why this is being escalated, not acted on

Per CLAUDE.md §5.1 trust line, *"Creating a new entity page (vendor, person, client, internal) — name collision risk, duplication risk"* is high-stakes. No prior wiki precedent for YC-organisation as an entity (YC is not a SaaS vendor; not a client; not a Janus internal team). Currently AIO has external people pages for [[andrej-karpathy]] (researcher / inspiration), [[vivian-balakrishnan]] (SG Foreign Minister / potential government advocate), [[yusuf-apple-dubai]] (potential internship candidate) — so the precedent is selective, not blanket.

## The decisions

### Decision 1 — Should YC be an entity?

If yes: **what folder?**
- Not `entities/vendors/` — YC is not a SaaS or AI tool.
- Not `entities/clients/` — Janus is not a YC portfolio company.
- Not `entities/internal/` or `entities/departments/`.
- The cleanest fit might be a new entity subtype (e.g., `entities/external-orgs/`), or a one-off precedent in `entities/people/` (treating YC as a "named external network entity"), or simply *no entity page* — track YC only through its named partners.

**Curator's call.** My recommendation: defer the YC organisation page until at least one of these conditions is met:
- Janus has direct interaction with YC (mentorship, partnership, investment relationship).
- A fourth distinct YC partner becomes load-bearing on the wiki.
- The pattern "AIO references YC org-level decisions" recurs (e.g., YC Requests For Startups; YC Demo Day signals).

### Decision 2 — Should Diana Hu and Tom Blomfield get `entities/people/` pages?

If yes:
- `entities/people/diana-hu.md` — YC Partner; engineer-turned-investor; her *"AI as operating system"* + closed-loop framing is now load-bearing on [[recursive-self-improving-loop]] and [[organisational-digital-twin]].
- `entities/people/tom-blomfield.md` — YC General Partner; co-founder of Monzo; his five-part-loop articulation is load-bearing in the same places + on [[ai-native-enterprise-restructuring]].

**My recommendation: yes for both.** Both are now structurally referenced from multiple wiki pages with concept-level claims attached to their names. Forward-references currently broken (`[[diana-hu]]` and `[[tom-blomfield]]` not used yet — inline naming only) means lint won't flag them today, but the next time either is referenced in a future ingest the same calculus repeats.

Risk: scope-creep on `entities/people/` — every notable AI commentator could end up here. Mitigation: the bar should be *"this person's specific framings are load-bearing on wiki concepts, not just quoted in passing."* Karpathy is on the wiki because of the LLM Wiki framing; Vivian Balakrishnan because of the SG-government-advocate relationship. Diana Hu and Tom Blomfield meet a similar bar.

### Decision 3 — Should Garry Tan be retroactively promoted?

[[gbrain]] currently has *"Garry Tan / YC"* inline. The vendor page is substantive and the YC-Tan-context matters for the pattern recognition (markdown-first agent memory layer co-evolving with the YC-distributed AI-native playbook).

**My recommendation: yes, but tracked under this question.** If Decision 2 lands on creating Diana Hu and Tom Blomfield pages, Garry Tan should join them in the same change for consistency. If Decision 2 defers, defer Garry Tan too.

## The "lint will flag this anyway" angle

If the decision is to create the pages, do so before the next lint pass (currently 4 ingests since last lint — well below the threshold). If the decision is to defer, the pulse + concept + brief pages currently name Diana Hu and Tom Blomfield inline without `[[wikilinks]]`, so nothing breaks today.

If the decision is "defer but use forward-references in the meantime" — that requires me to go back and edit the pulse + concept + brief to add `[[diana-hu]]` and `[[tom-blomfield]]` wikilinks that will lint as broken until the curator approves the pages. The wiki has precedent for this (per CLAUDE.md §6: *"Link liberally — a `[[name]]` that doesn't match an existing memory yet is fine; it marks something worth writing later, not an error"*).

## Proposed resolution shape (for Michael)

The cleanest single resolution:

1. **Defer YC organisation page** until either the partner-count crosses 4 or Janus has a YC interaction.
2. **Create three `entities/people/` pages**: diana-hu, tom-blomfield, garry-tan. Each minimal — role, why they're load-bearing on the wiki, links to the pages that reference them.
3. **Retroactively update** the new pulse, the new concept, and `entities/vendors/gbrain.md` to use `[[wikilinks]]` once the pages exist.

Estimated work: ~20 minutes if approved as a single change.
