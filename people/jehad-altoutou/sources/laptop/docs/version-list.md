---
type: source
source_type: laptop
title: _version_list
slug: version-list
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/media_library/_version_list.html
original_size: 2510
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:40Z"
project: brightbean-studio

---

# _version_list

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/media_library/_version_list.html` on 2026-05-14._

{% comment %}Version history list. Expects: asset, versions, workspace{%
endcomment %} {% if versions %}

<div class="space-y-2">

{% for version in versions %}

<div class="flex items-start gap-3 p-2.5 rounded-lg transition-colors"
style="background: var(--surface-1, #FAFAF9);">

<div class="w-10 h-10 rounded-lg overflow-hidden flex-shrink-0"
style="background: var(--surface-2, #F5F5F4);">

{% if version.thumbnail %}
<img src="%7B%7B%20version.thumbnail.url%20%7D%7D"
class="w-full h-full object-cover"
alt="v{{ version.version_number }}" /> {% else %}

<div class="w-full h-full flex items-center justify-center">

<span class="text-xs font-bold" style="color: var(--text-ghost);">v{{
version.version_number }}</span>

</div>

{% endif %}

</div>

<div class="flex-1 min-w-0">

<div class="flex items-center gap-2">

<span class="text-xs font-bold"
style="color: var(--text-primary, #1C1917);">Version {{
version.version_number }}</span> {% if asset.current_version_id ==
version.id %}
<span class="text-xs px-1.5 py-0.5 rounded-full font-semibold"
style="background: var(--success-50, #F0FDF4); color: var(--success-700, #15803D);">Current</span>
{% endif %}

</div>

{% if version.change_description %}

{{ version.change_description }}

{% endif %}

{{ version.created_at\|date:"M j, Y g:i A" }}

</div>

{% if asset.current_version_id != version.id and not asset.is_shared %}

Restore

{% endif %}

</div>

{% endfor %}

</div>

{% else %}

No version history yet. Edits will appear here.

{% endif %}
