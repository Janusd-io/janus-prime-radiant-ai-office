---
type: source
source_type: laptop
title: templates_list
slug: templates-list
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/composer/templates_list.html
original_size: 4266
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:38Z"
project: brightbean-studio

---

# templates_list

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/composer/templates_list.html` on 2026-05-14._

{% extends "base.html" %} {% block title %}Post Templates - {{
workspace.name }} - Brightbean{% endblock %} {% block page_header %}

<div class="flex items-center justify-between mb-6">

<div>

# Post Templates

Reusable templates to speed up content creation.

</div>

<a
href="%7B%%20url%20&#39;composer:compose&#39;%20workspace_id=workspace.id%20%%7D"
class="text-sm text-stone-500 hover:text-stone-700 flex items-center gap-1"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGQ9Ik0xNSAxOGwtNi02IDYtNiIgLz48L3N2Zz4="
class="w-4 h-4" /> Back to Composer</a>

</div>

{% endblock %} {% block content %}

<div id="templates-container" class="max-w-3xl"
hx-get="{% url 'composer:template_list' workspace_id=workspace.id %}"
hx-trigger="templateChanged from:body" hx-select="#templates-grid"
hx-target="#templates-grid" hx-swap="outerHTML">

<div id="templates-grid" class="grid grid-cols-1 sm:grid-cols-2 gap-4">

{% for tpl in templates %}

<div class="bg-white rounded-xl border border-stone-200 p-4 hover:border-stone-300 transition-colors group">

<div class="flex items-start justify-between mb-2">

### {{ tpl.name }}

<div class="flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-all flex-shrink-0 ml-2">

{% csrf_token %}

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNMTkgN2wtLjg2NyAxMi4xNDJBMiAyIDAgMDExNi4xMzggMjFINy44NjJhMiAyIDAgMDEtMS45OTUtMS44NThMNSA3bTUgNHY2bTQtNnY2bTEtMTBWNGExIDEgMCAwMC0xLTFoLTRhMSAxIDAgMDAtMSAxdjNNNCA3aDE2IiAvPjwvc3ZnPg=="
class="w-3.5 h-3.5" />

</div>

</div>

{% if tpl.description %}

{{ tpl.description }}

{% endif %} {% if tpl.template_data.caption %}

{{ tpl.template_data.caption\|truncatechars:120 }}

{% endif %}

<div class="flex items-center justify-between">

<span class="text-[11px] text-stone-400"> {% if tpl.created_by %}by {{
tpl.created_by.name\|default:tpl.created_by.email }}{% endif %} </span>
<a
href="%7B%%20url%20&#39;composer:use_template&#39;%20workspace_id=workspace.id%20template_id=tpl.id%20%%7D"
class="text-xs font-semibold py-1.5 px-3 rounded-full border border-stone-200 hover:border-stone-300 text-stone-700 hover:text-stone-900 transition-colors">Use
Template</a>

</div>

</div>

{% empty %}

<div class="col-span-2 text-center py-16">

<div class="w-12 h-12 rounded-full bg-stone-100 flex items-center justify-center mx-auto mb-3">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy02IGgtNiB0ZXh0LXN0b25lLTQwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTE5LjUgMTQuMjV2LTIuNjI1YTMuMzc1IDMuMzc1IDAgMDAtMy4zNzUtMy4zNzVoLTEuNUExLjEyNSAxLjEyNSAwIDAxMTMuNSA3LjEyNXYtMS41YTMuMzc1IDMuMzc1IDAgMDAtMy4zNzUtMy4zNzVIOC4yNW0wIDEyLjc1aDcuNW0tNy41IDNIMTJNMTAuNSAyLjI1SDUuNjI1Yy0uNjIxIDAtMS4xMjUuNTA0LTEuMTI1IDEuMTI1djE3LjI1YzAgLjYyMS41MDQgMS4xMjUgMS4xMjUgMS4xMjVoMTIuNzVjLjYyMSAwIDEuMTI1LS41MDQgMS4xMjUtMS4xMjVWMTEuMjVhOSA5IDAgMDAtOS05eiIgLz48L3N2Zz4="
class="w-6 h-6 text-stone-400" />

</div>

No templates yet

Save a post as a template from the composer to get started.

</div>

{% endfor %}

</div>

</div>

{% endblock %}
