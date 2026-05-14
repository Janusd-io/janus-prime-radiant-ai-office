---
type: source
source_type: laptop
title: approvals_settings
slug: approvals-settings
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/workspaces/approvals_settings.html
original_size: 3801
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:39Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# approvals_settings

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/workspaces/approvals_settings.html` on 2026-05-14._

{% extends "layouts/workspace_settings.html" %} {% block title
%}Approvals - {{ workspace.name }} - Brightbean{% endblock %} {% block
content %}

<div class="max-w-2xl">

## Approvals

Control whether posts need to be reviewed before they can be scheduled
or published.

{% csrf_token %}

<div class="flex flex-col gap-3 mb-8">

{% for value, label in approval_modes.choices %}

<div class="flex-1">

<div class="text-sm font-semibold mb-0.5"
style="color: var(--text-primary);">

{% if value == 'none' %}No approvals {% elif value == 'optional'
%}Optional approvals {% elif value == 'required_internal' %}Internal
review required {% elif value == 'required_internal_and_client'
%}Internal review + client approval {% else %}{{ label }} {% endif %}

</div>

<div class="text-xs" style="color: var(--text-secondary);">

{% if value == 'none' %} Anyone with publishing rights can schedule or
publish directly. {% elif value == 'optional' %} Creators can choose to
submit a post for review, but it's not required. {% elif value ==
'required_internal' %} Every post must be approved by a team member with
review rights before it can go out. {% elif value ==
'required_internal_and_client' %} Posts go through internal review, then
are sent to the client portal for final sign-off. {% endif %}

</div>

</div>

{% endfor %}

</div>

{% if is_owner_or_manager %}

Save Changes

{% endif %}

Reviewers are workspace members with the "Approve posts" permission.
Manage them on the
<a href="%7B%%20url%20&#39;members:list&#39;%20%%7D" class="underline"
style="color: var(--text-secondary);">Members</a> page.

</div>

{% endblock %}
