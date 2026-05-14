---
type: source
source_type: laptop
title: departments
slug: departments
created: 2026-05-14
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Documents/janus-brain-bootstrap/skills/janus-brain/config/departments.yaml
original_size: 2511
original_ext: .yaml
category: config
extracted_with: config-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# departments

_Extracted from `Documents/janus-brain-bootstrap/skills/janus-brain/config/departments.yaml` on 2026-05-14._

```yaml
# Janus department vocabulary — single-vault model (rewrite 2026-05-14).
# Each dept has one GitHub repo at Janusd-io/janus-prime-radiant-<slug>.
# Every employee in that dept clones it as their single Obsidian vault.
# Do not invent new departments here; propose additions via questions/ in
# the relevant dept instance.

departments:
  - slug: ai-office
    name: AI Office
    repo: Janusd-io/janus-prime-radiant-ai-office
    curator: michael-bruck
    status: live
  - slug: marketing
    name: Marketing
    repo: Janusd-io/janus-prime-radiant-marketing
    curator: andrew-soane
    status: scaffolding   # kicked off 2026-05-08
  - slug: hr
    name: HR
    repo: Janusd-io/janus-prime-radiant-hr
    curator: theresa-wong
    status: queued
  - slug: it-ops
    name: IT / Operations
    repo: Janusd-io/janus-prime-radiant-it-ops
    curator: euclid-wong
    status: queued
  - slug: finance
    name: Finance
    repo: Janusd-io/janus-prime-radiant-finance
    curator: ann-greed
    status: queued
  - slug: office-of-ceo
    name: Office of CEO
    repo: Janusd-io/janus-prime-radiant-office-of-ceo
    curator: bonaventure-wong
    status: queued
  - slug: iso
    name: ISO
    repo: Janusd-io/janus-prime-radiant-iso
    curator: simon-tarskih
    status: queued
  - slug: pm
    name: PM
    repo: Janusd-io/janus-prime-radiant-pm
    curator: ""
    status: queued
  - slug: engineering
    name: Engineering
    repo: Janusd-io/janus-prime-radiant-engineering
    curator: ""
    status: queued
  - slug: training
    name: Training
    repo: Janusd-io/janus-prime-radiant-training
    curator: ""
    status: queued

# Per-person department mapping (extend on install for new employees)
people:
  - slug: jehad-altoutou
    name: Jehad Altoutou
    departments: [ai-office]
  - slug: michael-bruck
    name: Michael Bruck
    departments: [ai-office]
  - slug: andrew-soane
    name: Andrew Soane
    departments: [marketing]
  - slug: bonaventure-wong
    name: Bonaventure Wong
    departments: [office-of-ceo]
  - slug: theresa-wong
    name: Theresa Wong
    departments: [hr]
  - slug: mariam-mahmood
    name: Mariam Mahmood
    departments: [hr]
  - slug: euclid-wong
    name: Euclid Wong
    departments: [it-ops]
  - slug: andrey-timokhov
    name: Andrey Timokhov
    departments: [it-ops]
  - slug: ann-greed
    name: Ann Greed
    departments: [finance]
  - slug: simon-tarskih
    name: Simon Tarskih
    departments: [ai-office]   # ISO programme facilitator; AIO adjacent

```