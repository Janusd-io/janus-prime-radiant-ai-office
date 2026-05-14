---
type: source
source_type: laptop
title: _message_list
slug: message-list
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/inbox/partials/_message_list.html
original_size: 215
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:38Z"
project: brightbean-studio

---

# _message_list

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/inbox/partials/_message_list.html` on 2026-05-14._

{% load humanize %} {% if messages %} {% for msg in messages %} {%
include "inbox/partials/\_message_row.html" with message=msg %} {%
endfor %} {% else %} {% include "inbox/partials/\_empty_state.html" %}
{% endif %}
