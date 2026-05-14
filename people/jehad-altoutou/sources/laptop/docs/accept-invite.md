---
type: source
source_type: laptop
title: accept_invite
slug: accept-invite
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/members/accept_invite.html
original_size: 4672
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:40Z"
---

# accept_invite

_Extracted from `brightbean-studio/templates/members/accept_invite.html` on 2026-05-14._

<div class="card">

<div class="logo">

Brightbean

</div>

# Join {{ invitation.organization.name }}

{{ invitation.invited_by.display_name }} invited you to join their team
on Brightbean.

{% if error %}

{{ error }}

{% endif %}

<div class="info-box">

<div class="info-label">

Organization

</div>

<div class="info-value" style="margin-bottom: 12px;">

{{ invitation.organization.name }}

</div>

<div class="info-label">

Role

</div>

<div class="info-value"
style="margin-bottom: 12px; text-transform: capitalize;">

{{ invitation.org_role }}

</div>

{% if ws_display %}

<div class="info-label">

Workspaces

</div>

- {% for ws in ws_display %}
- {{ ws.name }} <span class="role">{{ ws.role }}</span>
  {% endfor %}

{% endif %}

</div>

{% if user.is_authenticated %}

{% csrf_token %}

Join {{ invitation.organization.name }}

{% else %} <a href="/accounts/signup/?next=%7B%7B%20accept_url%20%7D%7D"
class="btn btn-primary">Sign Up to Join</a>

<div class="or-divider">

or

</div>

<a href="/accounts/login/?next=%7B%7B%20accept_url%20%7D%7D"
class="btn btn-secondary">Log In to Join</a> {% endif %}

</div>
