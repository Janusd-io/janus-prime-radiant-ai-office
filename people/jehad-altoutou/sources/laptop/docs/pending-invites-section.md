---
type: source
source_type: laptop
title: pending_invites_section
slug: pending-invites-section
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/client_portal/admin/partials/pending_invites_section.html
original_size: 3493
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:38Z"
---

# pending_invites_section

_Extracted from `brightbean-studio/templates/client_portal/admin/partials/pending_invites_section.html` on 2026-05-14._

{% if pending_invites %}

<div style="background: var(--surface-0); border: 1px solid var(--border); border-radius: var(--radius-xl); overflow: hidden;">

<div class="px-6 py-4" style="border-bottom: 1px solid var(--border);">

### Pending Invitations

</div>

<div id="client-invitations-list">

{% for invite in pending_invites %}

<div id="client-invite-{{ invite.id }}"
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

<span class="text-xs font-medium px-2.5 py-1 rounded-full"
style="background: #FEF3C7; color: #92400E;">Client</span>

</div>

<div class="flex-shrink-0 flex items-center gap-2">

{% csrf_token %}

Resend

{% csrf_token %}

Revoke

</div>

</div>

{% endfor %}

</div>

</div>

{% endif %}
