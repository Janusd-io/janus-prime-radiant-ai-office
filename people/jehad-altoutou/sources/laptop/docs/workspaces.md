---
type: source
source_type: laptop
title: workspaces
slug: workspaces
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/organizations/workspaces.html
original_size: 1526
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:37Z"
project: brightbean-studio

---

# workspaces

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/organizations/workspaces.html` on 2026-05-14._

{% extends "layouts/settings.html" %} {% block title %}Workspaces -
Settings - Brightbean{% endblock %} {% block content %}

<div>

## Workspaces

{% if workspace_data %}

<div style="background: var(--surface-0); border: 1px solid var(--border); border-radius: var(--radius-xl);">

{% for item in workspace_data %}

<div class="px-6 py-4{% if not forloop.last %}"
style="border-bottom: 1px solid var(--border);" {%="" else="" %}"{%=""
endif="" %}="">

{% include "organizations/partials/workspace_card.html" with item=item
%}

</div>

{% endfor %}

</div>

{% else %}

<div class="px-6 py-12 text-center rounded-xl"
style="background: var(--surface-0); border: 1px solid var(--border);">

No workspaces yet.

</div>

{% endif %} {% if archived_data %}

### Archived

<div style="background: var(--surface-0); border: 1px solid var(--border); border-radius: var(--radius-xl); opacity: 0.75;">

{% for item in archived_data %}

<div class="px-6 py-4{% if not forloop.last %}"
style="border-bottom: 1px solid var(--border);" {%="" else="" %}"{%=""
endif="" %}="">

{% include "organizations/partials/workspace_card.html" with item=item
%}

</div>

{% endfor %}

</div>

{% endif %}

</div>

{% endblock %}
