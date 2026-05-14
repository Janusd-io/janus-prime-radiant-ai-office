---
type: source
source_type: laptop
title: invite_client_modal
slug: invite-client-modal
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/client_portal/admin/partials/invite_client_modal.html
original_size: 4139
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:38Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# invite_client_modal

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/client_portal/admin/partials/invite_client_modal.html` on 2026-05-14._

<div class="fixed inset-0 z-50 flex items-center justify-center"
x-show="showInviteModal" x-transition.opacity=""
style="background: rgba(0,0,0,0.4);">

<div class="w-full max-w-md rounded-xl shadow-xl flex flex-col"
@click.outside="showInviteModal = false" x-show="showInviteModal"
x-transition="" style="background: var(--surface-0);">

<div class="flex items-center justify-between px-6 py-4 flex-shrink-0"
style="border-bottom: 1px solid var(--border);">

### Invite Client

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48bGluZSB4MT0iMTgiIHkxPSI2IiB4Mj0iNiIgeTI9IjE4Ij48L2xpbmU+PGxpbmUgeDE9IjYiIHkxPSI2IiB4Mj0iMTgiIHkyPSIxOCI+PC9saW5lPjwvc3ZnPg==)

</div>

{% csrf_token %}

<div class="mb-5">

Email Address

</div>

<div class="mb-5 px-3 py-2.5 rounded-lg text-xs"
style="background: var(--neutral-50); color: var(--text-secondary);">

The client will receive an invitation email to create an account. Once
accepted, they will have **Client** access to this workspace, allowing
them to review and approve posts via the Client Portal.

</div>

<div id="client-invite-error" class="mb-3">

</div>

<div class="flex justify-end gap-3">

Cancel

Send Invitation

</div>

</div>

</div>
