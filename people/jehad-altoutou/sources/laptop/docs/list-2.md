---
type: source
source_type: laptop
title: Brightbean Studio — list
slug: list-2
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/workspaces/list.html
original_size: 3103
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:39Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# list

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/workspaces/list.html` on 2026-05-14._

{% extends "base.html" %} {% block page_title %}Workspaces{% endblock %}
{% block content %}

<div style="max-width: 720px;">

<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 24px;">

## Workspaces

</div>

{% if workspaces %}

<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 12px; margin-bottom: 24px;">

{% for workspace in workspaces %} <a
href="%7B%%20url%20&#39;calendar:calendar&#39;%20workspace_id=workspace.id%20%%7D"
style="
            display: block;
            background: var(--surface-0);
            border: 1px solid var(--border);
            border-radius: var(--radius-xl);
            padding: 20px;
            text-decoration: none;
            transition: all var(--dur-base) var(--ease-out);
        "
onmouseover="this.style.boxShadow=&#39;var(--shadow-lg)&#39;;this.style.borderColor=&#39;transparent&#39;;this.style.transform=&#39;translateY(-2px)&#39;"
onmouseout="this.style.boxShadow=&#39;none&#39;;this.style.borderColor=&#39;var(--border)&#39;;this.style.transform=&#39;none&#39;"></a>

<div style="font-size: 0.9375rem; font-weight: 600; color: var(--text-primary); margin-bottom: 4px;">

{{ workspace.name }}

</div>

{% if workspace.description %}

<div style="font-size: 0.8125rem; color: var(--text-secondary); line-height: 1.6;">

{{ workspace.description\|truncatechars:80 }}

</div>

{% endif %} {% endfor %}

</div>

{% else %}

<div style="
        text-align: center;
        padding: 48px 24px;
        background: var(--surface-0);
        border: 1px solid var(--border);
        border-radius: var(--radius-xl);
        margin-bottom: 24px;
    ">

No workspaces yet. Create your first workspace to get started.

</div>

{% endif %}

<div style="
        background: var(--surface-0);
        border: 1px solid var(--border);
        border-radius: var(--radius-xl);
        padding: 24px;
        box-shadow: var(--shadow-xs);
    ">

### New workspace

{% csrf_token %}

<div style="flex: 1;">

</div>

Create

</div>

</div>

{% endblock %}
