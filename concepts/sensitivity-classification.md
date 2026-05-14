---
type: concept
title: Sensitivity classification
slug: sensitivity-classification
created: 2026-05-14
updated: 2026-05-14
departments: [ai-office, it-ops]
status: active
confidence: high
sources: [rewrite-spec, skill-3, readme-12, enrollment, readme-11]
related: [janus-brain-bootstrap, prime-radiant, claude-md-rulebook, role-based-access-control, zero-trust-security]
captured_by: jehad-altoutou
audience: department
---

# Sensitivity classification

The routing key the [[janus-brain-bootstrap]] skill applies to every source it ingests, so that personal items never reach the dept-shared GitHub repo. Per [[rewrite-spec]] (signed 2026-05-14), every page filed under `people/<slug>/sources/` or `people/<slug>/meetings/` carries two fields in frontmatter:

- `sensitivity`: one of `dept`, `self`, `confidential`
- `sensitivity_confidence`: a float in `[0.0, 1.0]`

The Phase 6 applier moves anything classified `self` or `confidential` — or `dept` with confidence `< 0.7` — to the gitignored `people/<slug>/private/`. Items below `0.7` confidence are also appended to `people/<slug>/.review-queue.md` so the user can confirm or promote them.

## Heuristics (first match wins)

Per the enrichment subagent prompt:

| Pattern | sensitivity | typical confidence |
| --- | --- | --- |
| credentials, API keys, passwords, `.env`, `id_rsa`, AWS keys | `confidential` | 0.95+ |
| HR / salary / performance / legal / health / family / personal finance | `confidential` | 0.85+ |
| 1:1 manager meeting, performance discussion about the user | `self` | 0.8+ |
| Personal journal entries, private notes-to-self | `self` | 0.7+ |
| Bank statements, tax docs, identity documents | `confidential` | 0.95+ (also escalate) |
| Default — work content, vendor evals, project notes, public meetings | `dept` | 0.8+ |

When confidence is below 0.7, the subagent errs toward the more private bucket (`self` over `dept`, `confidential` over `self`) and lets the applier surface it to `.review-queue.md` for human review.

## Defence in depth

Classification is the third layer, not the first. The earlier two — capture-time `exclude-patterns.txt` + `exclude-paths.txt`, then file-extension allowlisting — already drop the highest-risk artefacts (credential files, browser profiles, identity documents) before they ever reach a subagent. Classification handles the long tail: notes whose privacy can only be inferred from content.

## See also

- [[janus-brain-bootstrap]] — the project that built the classifier
- [[prime-radiant]] — vault architecture this routing protects
- [[zero-trust-security]] — the broader principle the classifier inherits
