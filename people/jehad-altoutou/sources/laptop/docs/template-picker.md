---
type: source
source_type: laptop
title: template_picker
slug: template-picker
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/composer/partials/template_picker.html
original_size: 1058
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:39Z"
project: brightbean-studio

---

# template_picker

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/composer/partials/template_picker.html` on 2026-05-14._

<div class="space-y-3">

{% for tpl in templates %} <a
href="%7B%%20url%20&#39;composer:use_template&#39;%20workspace_id=workspace.id%20template_id=tpl.id%20%%7D"
class="block p-3 rounded-lg border border-stone-200 hover:border-stone-300 hover:bg-stone-50 transition-colors"></a>

<div class="flex items-center justify-between mb-1">

<span class="text-sm font-semibold text-stone-800">{{ tpl.name }}</span>

</div>

{% if tpl.description %}

{{ tpl.description }}

{% endif %} {% if tpl.template_data.caption %}

{{ tpl.template_data.caption\|truncatechars:80 }}

{% endif %} {% empty %}

<div class="text-center py-8">

No templates yet.

Save a post as a template to see it here.

</div>

{% endfor %}

</div>
