---
type: source
source_type: laptop
title: workspace_card
slug: workspace-card
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/organizations/partials/workspace_card.html
original_size: 3337
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:37Z"
project: brightbean-studio

---

# workspace_card

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/organizations/partials/workspace_card.html` on 2026-05-14._

<div class="flex items-center gap-3">

{% if item.workspace.icon %}
<img src="%7B%7B%20item.workspace.icon.url%20%7D%7D"
class="w-10 h-10 rounded-full object-cover flex-shrink-0" /> {% else %}

<div class="w-10 h-10 rounded-full flex items-center justify-center flex-shrink-0 text-sm font-semibold"
style="background: var(--neutral-200); color: var(--text-secondary);">

{{ item.workspace.name\|first\|upper }}

</div>

{% endif %}

<div class="flex-1 min-w-0">

<div class="flex items-center gap-2">

<span class="text-sm font-medium truncate"
style="color: var(--text-primary);"> {{ item.workspace.name }} </span>
{% if item.workspace.is_archived %}
<span class="text-xs px-2 py-0.5 rounded-full"
style="background: #FEF3C7; color: #92400E;">Archived</span> {% endif %}

</div>

<div class="text-xs" style="color: var(--text-tertiary);">

{{ item.member_count }} member{{ item.member_count\|pluralize }}

</div>

</div>

{% if item.can_manage %} <a
href="%7B%%20url%20&#39;workspaces:settings&#39;%20workspace_id=item.workspace.id%20%%7D"
class="inline-flex items-center gap-1.5 text-xs font-medium px-3 py-1.5 rounded-full transition-colors"
style="background: var(--neutral-100); color: var(--text-secondary);"
onmouseenter="this.style.background=&#39;var(--neutral-200)&#39;"
onmouseleave="this.style.background=&#39;var(--neutral-100)&#39;"><img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIzIj48L2NpcmNsZT48cGF0aCBkPSJNMTkuNCAxNWExLjY1IDEuNjUgMCAwMC4zMyAxLjgybC4wNi4wNmEyIDIgMCAwMTAgMi44MyAyIDIgMCAwMS0yLjgzIDBsLS4wNi0uMDZhMS42NSAxLjY1IDAgMDAtMS44Mi0uMzMgMS42NSAxLjY1IDAgMDAtMSAxLjUxVjIxYTIgMiAwIDAxLTQgMHYtLjA5QTEuNjUgMS42NSAwIDAwOSAxOS40YTEuNjUgMS42NSAwIDAwLTEuODIuMzNsLS4wNi4wNmEyIDIgMCAwMS0yLjgzLTIuODNsLjA2LS4wNkExLjY1IDEuNjUgMCAwMDQuNjggMTVhMS42NSAxLjY1IDAgMDAtMS41MS0xSDNhMiAyIDAgMDEwLTRoLjA5QTEuNjUgMS42NSAwIDAwNC42IDlhMS42NSAxLjY1IDAgMDAtLjMzLTEuODJsLS4wNi0uMDZhMiAyIDAgMDEyLjgzLTIuODNsLjA2LjA2QTEuNjUgMS42NSAwIDAwOSA0LjY4YTEuNjUgMS42NSAwIDAwMS0xLjUxVjNhMiAyIDAgMDE0IDB2LjA5YTEuNjUgMS42NSAwIDAwMSAxLjUxIDEuNjUgMS42NSAwIDAwMS44Mi0uMzNsLjA2LS4wNmEyIDIgMCAwMTIuODMgMi44M2wtLjA2LjA2QTEuNjUgMS42NSAwIDAwMTkuMzIgOWExLjY1IDEuNjUgMCAwMDEuNTEgMUgyMWEyIDIgMCAwMTAgNGgtLjA5YTEuNjUgMS42NSAwIDAwLTEuNTEgMXoiIC8+PC9zdmc+" />
Settings</a> {% endif %}

</div>

{% if item.members %}

<div class="flex items-center flex-wrap gap-2 mt-3">

{% for membership in item.members %}
<span class="inline-flex items-center gap-1.5 text-xs px-2 py-0.5 rounded-full"
style="background: var(--neutral-100); color: var(--text-secondary);"
title="{{ membership.user.display_name }} ({{ membership.get_workspace_role_display }})">
<span class="w-4 h-4 rounded-full flex items-center justify-center text-[10px] font-semibold flex-shrink-0"
style="background: var(--neutral-200); color: var(--text-tertiary);"> {{
membership.user.display_name\|first\|upper }} </span> {{
membership.user.display_name }} </span> {% endfor %}

</div>

{% else %}

<div class="mt-3 text-xs" style="color: var(--text-tertiary);">

No members assigned

</div>

{% endif %}
