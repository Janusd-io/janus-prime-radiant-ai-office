---
type: source
source_type: laptop
title: client_list
slug: client-list
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/client_portal/admin/client_list.html
original_size: 2748
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:38Z"
---

# client_list

_Extracted from `brightbean-studio/templates/client_portal/admin/client_list.html` on 2026-05-14._

{% extends "layouts/workspace_settings.html" %} {% block title %}Client
Portal - {{ request.workspace.name }} - Brightbean{% endblock %} {%
block content %}

<div x-data="{ showInviteModal: false }">

<div class="flex items-center justify-between mb-6">

<div>

## Client Portal

Invite external clients to review and approve posts.

</div>

Invite Client

</div>

<div class="mb-8"
style="background: var(--surface-0); border: 1px solid var(--border); border-radius: var(--radius-xl); overflow: hidden;">

<div class="px-6 py-4" style="border-bottom: 1px solid var(--border);">

### Clients ({{ clients_data\|length }})

</div>

<div id="clients-list">

{% for client in clients_data %} {% include
"client_portal/admin/partials/client_row.html" %} {% empty %}

<div id="no-clients-placeholder" class="px-6 py-12 text-center">

<div class="w-12 h-12 mx-auto mb-3 rounded-full flex items-center justify-center"
style="background: var(--neutral-100);">

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0eWxlPSJjb2xvcjogdmFyKC0tdGV4dC10ZXJ0aWFyeSk7Ij48cGF0aCBkPSJNMTcgMjF2LTJhNCA0IDAgMDAtNC00SDVhNCA0IDAgMDAtNC00djIiIC8+PGNpcmNsZSBjeD0iOSIgY3k9IjciIHI9IjQiPjwvY2lyY2xlPjxwYXRoIGQ9Ik0yMyAyMXYtMmE0IDQgMCAwMC0zLTMuODciIC8+PHBhdGggZD0iTTE2IDMuMTNhNCA0IDAgMDEwIDcuNzUiIC8+PC9zdmc+)

</div>

No clients yet

Invite a client to give them portal access for reviewing and approving
posts.

</div>

{% endfor %}

</div>

</div>

<div id="pending-invites-section">

{% include "client_portal/admin/partials/pending_invites_section.html"
%}

</div>

{% include "client_portal/admin/partials/invite_client_modal.html" %}

</div>

{% endblock %}
