---
type: source
source_type: laptop
title: client_row
slug: client-row
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/client_portal/admin/partials/client_row.html
original_size: 2986
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:38Z"
project: brightbean-studio

---

# client_row

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/client_portal/admin/partials/client_row.html` on 2026-05-14._

<div id="client-{{ client.membership.id }}"
class="px-6 py-4 flex items-center gap-4"
style="border-bottom: 1px solid var(--border);">

<div class="w-9 h-9 rounded-full flex items-center justify-center flex-shrink-0 text-sm font-semibold"
style="background: var(--neutral-200); color: var(--text-secondary);">

{{ client.user.display_name\|first\|upper }}

</div>

<div class="flex-1 min-w-0">

<div class="text-sm font-medium truncate"
style="color: var(--text-primary);">

{{ client.user.display_name }}

</div>

<div class="text-xs truncate" style="color: var(--text-tertiary);">

{{ client.user.email }}

</div>

</div>

<div class="flex-shrink-0">

{% if client.token %}
<span class="text-xs font-medium px-2.5 py-1 rounded-full"
style="background: #DCFCE7; color: #166534;"> Link active </span> {%
else %} <span class="text-xs font-medium px-2.5 py-1 rounded-full"
style="background: var(--neutral-100); color: var(--text-tertiary);"> No
link sent </span> {% endif %}

</div>

<div class="flex-shrink-0 flex items-center gap-2">

{% csrf_token %}

{% if client.token %}Resend Link{% else %}Send Portal Link{% endif %}

{% csrf_token %}

Remove

</div>

</div>
