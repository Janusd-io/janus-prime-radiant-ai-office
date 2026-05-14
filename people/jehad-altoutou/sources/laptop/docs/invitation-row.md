---
type: source
source_type: laptop
title: invitation_row
slug: invitation-row
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/members/partials/invitation_row.html
original_size: 3298
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:40Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# invitation_row

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/members/partials/invitation_row.html` on 2026-05-14._

<div id="invite-{{ invite.id }}"
class="px-6 py-4 flex items-center gap-4"
style="border-bottom: 1px solid var(--border);">

<div class="w-9 h-9 rounded-full flex items-center justify-center flex-shrink-0"
style="background: var(--neutral-100); color: var(--text-tertiary);">

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cGF0aCBkPSJNNCA0aDE2YzEuMSAwIDIgLjkgMiAydjEyYzAgMS4xLS45IDItMiAySDRjLTEuMSAwLTItLjktMi0yVjZjMC0xLjEuOS0yIDItMnoiIC8+PHBvbHlsaW5lIHBvaW50cz0iMjIsNiAxMiwxMyAyLDYiPjwvcG9seWxpbmU+PC9zdmc+)

</div>

<div class="flex-1 min-w-0">

<div class="text-sm font-medium truncate"
style="color: var(--text-primary);">

{{ invite.email }}

</div>

<div class="text-xs" style="color: var(--text-tertiary);">

Invited by {{ invite.invited_by.display_name }} · Expires {{
invite.expires_at\|timesince }} from now

</div>

</div>

<div class="flex-shrink-0">

{% if invite.org_role == "admin" %}
<span class="text-xs font-medium px-2.5 py-1 rounded-full"
style="background: #DBEAFE; color: #1E40AF;">Admin</span> {% else %}
<span class="text-xs font-medium px-2.5 py-1 rounded-full"
style="background: var(--neutral-100); color: var(--text-secondary);">Member</span>
{% endif %}

</div>

<div class="flex-shrink-0 flex items-center gap-1 max-w-[150px] overflow-hidden">

{% for assignment in invite.workspace_assignments %}
<span class="text-xs px-2 py-0.5 rounded-full truncate"
style="background: var(--neutral-100); color: var(--text-secondary);">
{{ assignment.role }} </span> {% endfor %}

</div>

{% if is_admin %}

<div class="flex-shrink-0 flex items-center gap-2">

{% csrf_token %}

Resend

{% csrf_token %}

Revoke

</div>

{% endif %}

</div>
