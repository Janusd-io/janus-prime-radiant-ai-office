---
type: source
source_type: laptop
title: invite_modal
slug: invite-modal
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/members/partials/invite_modal.html
original_size: 7403
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:40Z"
---

# invite_modal

_Extracted from `brightbean-studio/templates/members/partials/invite_modal.html` on 2026-05-14._

<div class="fixed inset-0 z-50 flex items-center justify-center"
x-show="showInviteModal" x-transition.opacity=""
style="background: rgba(0,0,0,0.4);">

<div class="w-full max-w-lg rounded-xl shadow-xl flex flex-col max-h-[90vh]"
@click.outside="showInviteModal = false" x-show="showInviteModal"
x-transition="" style="background: var(--surface-0);">

<div class="flex items-center justify-between px-6 py-4 flex-shrink-0"
style="border-bottom: 1px solid var(--border);">

### Invite Team Member

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48bGluZSB4MT0iMTgiIHkxPSI2IiB4Mj0iNiIgeTI9IjE4Ij48L2xpbmU+PGxpbmUgeDE9IjYiIHkxPSI2IiB4Mj0iMTgiIHkyPSIxOCI+PC9saW5lPjwvc3ZnPg==)

</div>

{% csrf_token %}

<div class="mb-5">

Email Address

</div>

<div class="mb-5">

Organization Role

<div class="flex gap-4">

{% for value, label in org_role_choices %}

<div class="flex items-center">

{{ label }}

</div>

{% endfor %}

</div>

</div>

<div class="mb-5">

Assign to Workspaces

Select workspaces and roles for this team member.

<div class="space-y-2 max-h-48 overflow-y-auto">

{% for ws in org_workspaces %}

<div class="flex items-center gap-3 py-2 px-3 rounded-lg"
style="background: var(--neutral-50);">

{{ ws.name }} {% for value, label in workspace_role_choices %} {{ label
}} {% endfor %}

</div>

{% endfor %}

</div>

Tip: For external clients who only need portal access, use the Client
Portal invite from workspace settings instead.

</div>

<div id="invite-error" class="mb-3">

</div>

<div class="flex justify-end gap-3">

Cancel

Send Invitation

</div>

</div>

</div>
