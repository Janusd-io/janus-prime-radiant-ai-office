---
type: source
source_type: laptop
title: _sla_badge
slug: sla-badge
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/inbox/partials/_sla_badge.html
original_size: 233
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:38Z"
project: brightbean-studio

---

# _sla_badge

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/inbox/partials/_sla_badge.html` on 2026-05-14._

{% if sla_config and sla_config.is_active %}
<span class="sla-countdown badge-pill"
:class="getSlaClass('{{ message.received_at|date:'c' }}')"
x-text="formatSla('{{ message.received_at|date:'c' }}')"> </span> {%
endif %}
