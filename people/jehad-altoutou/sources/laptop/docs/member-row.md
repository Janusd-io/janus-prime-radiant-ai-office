---
type: source
source_type: laptop
title: member_row
slug: member-row
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/members/partials/member_row.html
original_size: 8250
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:40Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# member_row

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/members/partials/member_row.html` on 2026-05-14._

<div id="member-{{ member.membership.id }}" class="px-6 py-4 group"
style="border-bottom: 1px solid var(--border);"
x-data="{ showActions: false, showWorkspaces: false }">

<div class="flex items-center gap-4">

<div class="w-9 h-9 rounded-full flex items-center justify-center flex-shrink-0 text-sm font-semibold"
style="background: var(--neutral-200); color: var(--text-secondary);">

{{ member.user.display_name\|first\|upper }}

</div>

<div class="flex-1 min-w-0">

<div class="flex items-center gap-2">

<span class="text-sm font-medium truncate"
style="color: var(--text-primary);"> {{ member.user.display_name }}
</span> {% if member.user.id == current_user.id %}
<span class="text-xs px-1.5 py-0.5 rounded"
style="background: var(--neutral-100); color: var(--text-tertiary);">you</span>
{% endif %}

</div>

<div class="text-xs truncate" style="color: var(--text-tertiary);">

{{ member.user.email }}

</div>

</div>

<div class="flex-shrink-0">

{% if member.membership.org_role == "owner" %}
<span class="text-xs font-medium px-2.5 py-1 rounded-full"
style="background: #FEF3C7; color: #92400E;">Owner</span> {% elif
member.membership.org_role == "admin" %}
<span class="text-xs font-medium px-2.5 py-1 rounded-full"
style="background: #DBEAFE; color: #1E40AF;">Admin</span> {% else %}
<span class="text-xs font-medium px-2.5 py-1 rounded-full"
style="background: var(--neutral-100); color: var(--text-secondary);">Member</span>
{% endif %}

</div>

{% if is_admin and member.user.id != current_user.id %}

<div class="flex-shrink-0 relative">

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0Ij48Y2lyY2xlIGN4PSIxMiIgY3k9IjUiIHI9IjIiPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjEyIiBjeT0iMTIiIHI9IjIiPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjEyIiBjeT0iMTkiIHI9IjIiPjwvY2lyY2xlPjwvc3ZnPg==)

<div class="absolute right-0 top-full mt-1 w-52 py-1 rounded-lg shadow-lg z-10"
x-show="showActions" @click.outside="showActions = false"
x-transition=""
style="background: var(--surface-0); border: 1px solid var(--border);">

{% csrf_token %} Organization Role

<div class="flex gap-2">

{% for value, label in org_role_choices %} {{ label }} {% endfor %}

Save

</div>

Manage Workspaces

{% csrf_token %}

Remove from Organization

</div>

</div>

{% endif %}

</div>

{% if member.workspace_memberships %}

<div class="flex items-center justify-start flex-wrap gap-2 mt-2">

{% for wm in member.workspace_memberships %}
<span class="inline-flex items-center gap-1.5 text-xs px-2 py-0.5 rounded-full"
style="background: var(--neutral-100); color: var(--text-secondary);"
title="{{ wm.workspace.name }} ({{ wm.workspace_role }})"> {% if
wm.workspace.icon %} <img src="%7B%7B%20wm.workspace.icon.url%20%7D%7D"
class="w-4 h-4 rounded-full object-cover" /> {% else %}
<span class="w-4 h-4 rounded-full flex items-center justify-center text-[10px] font-semibold"
style="background: var(--neutral-200); color: var(--text-tertiary);">{{
wm.workspace.name\|first\|upper }}</span> {% endif %} {{
wm.workspace.name }} </span> {% endfor %}

</div>

{% endif %} {% if is_admin and member.user.id != current_user.id %}

<div class="fixed inset-0 z-50 flex items-center justify-center"
x-show="showWorkspaces" x-transition.opacity=""
style="background: rgba(0,0,0,0.4);">

<div class="w-full max-w-md rounded-xl shadow-xl p-6"
@click.outside="showWorkspaces = false"
style="background: var(--surface-0);">

<div class="flex items-center justify-between mb-4">

### Workspaces - {{ member.user.display_name }}

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48bGluZSB4MT0iMTgiIHkxPSI2IiB4Mj0iNiIgeTI9IjE4Ij48L2xpbmU+PGxpbmUgeDE9IjYiIHkxPSI2IiB4Mj0iMTgiIHkyPSIxOCI+PC9saW5lPjwvc3ZnPg==)

</div>

<div id="ws-modal-content">

Loading...

</div>

</div>

</div>

{% endif %}

</div>
