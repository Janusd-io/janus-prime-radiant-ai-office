---
type: source
source_type: laptop
title: field
slug: field
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/allauth/elements/field.html
original_size: 2994
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:39Z"
project: brightbean-studio

---

# field

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/allauth/elements/field.html` on 2026-05-14._

{% load allauth %} {% if attrs.errors %}

<div class="mb-1">

- {% for error in attrs.errors %}
- {{ error }}
  {% endfor %}

</div>

{% endif %}

<div class="mb-4">

{% if attrs.type == "textarea" %} {% slot label %}{% endslot %}

{% elif attrs.type == "checkbox" or attrs.type == "radio" %} {% slot
label %}{% endslot %} {% else %} {% slot label %}{% endslot %} {% endif
%} {% if slots.help_text %}

{% slot help_text %}{% endslot %}

{% endif %}

</div>
