---
type: source
source_type: laptop
title: alert
slug: alert
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/allauth/elements/alert.html
original_size: 193
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:39Z"
---

# alert

_Extracted from `brightbean-studio/templates/allauth/elements/alert.html` on 2026-05-14._

{% load allauth %}

<div class="{% if 'error' in attrs.tags %}alert-error{% elif 'success' in attrs.tags %}alert-success{% else %}alert-info{% endif %} mb-4">

{% slot %}{% endslot %}

</div>
