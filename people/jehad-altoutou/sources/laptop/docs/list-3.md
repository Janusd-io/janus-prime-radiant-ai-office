---
type: source
source_type: laptop
title: list
slug: list-3
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/members/list.html
original_size: 2516
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:40Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# list

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/members/list.html` on 2026-05-14._

{% extends "layouts/settings.html" %} {% block title %}Team Members -
Settings - Brightbean{% endblock %} {% block content %}

<div x-data="{ showInviteModal: false }">

<div class="flex items-center justify-between mb-6">

## Team Members

{% if is_admin %}

Invite Team Member

{% endif %}

</div>

<div class="mb-8"
style="background: var(--surface-0); border: 1px solid var(--border); border-radius: var(--radius-xl); overflow: hidden;">

<div class="px-6 py-4" style="border-bottom: 1px solid var(--border);">

### Members ({{ members_data\|length }})

</div>

<div id="members-list">

{% for member in members_data %} {% include
"members/partials/member_row.html" %} {% empty %}

<div class="px-6 py-8 text-center">

No team members yet.

</div>

{% endfor %}

</div>

</div>

{% if is_admin %}

<div style="background: var(--surface-0); border: 1px solid var(--border); border-radius: var(--radius-xl); overflow: hidden;">

<div class="px-6 py-4" style="border-bottom: 1px solid var(--border);">

### Pending Invitations

</div>

<div id="invitations-list">

{% for invite in pending_invites %} {% include
"members/partials/invitation_row.html" %} {% empty %}

<div id="no-invites-placeholder" class="px-6 py-8 text-center">

No pending invitations.

</div>

{% endfor %}

</div>

</div>

{% endif %} {% if is_admin %} {% include
"members/partials/invite_modal.html" %} {% endif %}

</div>

{% endblock %}
