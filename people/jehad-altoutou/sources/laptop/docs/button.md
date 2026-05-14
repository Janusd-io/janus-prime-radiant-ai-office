---
type: source
source_type: laptop
title: button
slug: button
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/allauth/elements/button.html
original_size: 1561
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:39Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# button

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/allauth/elements/button.html` on 2026-05-14._

{% load allauth %} {% comment %} djlint:off {% endcomment %} {% if
"link" in attrs.tags or "cancel" in attrs.tags %} \<{% if attrs.href %}a
href="{{ attrs.href }}"{% else %}button{% endif %} class="btn-link" {%
if attrs.form %}form="{{ attrs.form }}"{% endif %} {% if attrs.id
%}id="{{ attrs.id }}"{% endif %} {% if attrs.name %}name="{{ attrs.name
}}"{% endif %} {% if attrs.value %}value="{{ attrs.value }}"{% endif %}
{% if attrs.type %}type="{{ attrs.type }}"{% endif %}\> {% slot %}{%
endslot %} {% elif "outline" in attrs.tags or "secondary" in attrs.tags
%} \<{% if attrs.href %}a href="{{ attrs.href }}"{% else %}button{%
endif %} class="btn-outline" {% if attrs.form %}form="{{ attrs.form
}}"{% endif %} {% if attrs.id %}id="{{ attrs.id }}"{% endif %} {% if
attrs.name %}name="{{ attrs.name }}"{% endif %} {% if attrs.value
%}value="{{ attrs.value }}"{% endif %} {% if attrs.type %}type="{{
attrs.type }}"{% endif %}\> {% slot %}{% endslot %} {% else %} \<{% if
attrs.href %}a href="{{ attrs.href }}"{% else %}button{% endif %}
class="btn-brand" {% if attrs.form %}form="{{ attrs.form }}"{% endif %}
{% if attrs.id %}id="{{ attrs.id }}"{% endif %} {% if attrs.name
%}name="{{ attrs.name }}"{% endif %} {% if attrs.value %}value="{{
attrs.value }}"{% endif %} {% if attrs.type %}type="{{ attrs.type }}"{%
endif %}\> {% slot %}{% endslot %} {% endif %}
