---
type: source
source_type: laptop
title: dashboard
slug: dashboard-2
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/accounts/dashboard.html
original_size: 2708
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:40Z"
---

# dashboard

_Extracted from `brightbean-studio/templates/accounts/dashboard.html` on 2026-05-14._

{% extends "base.html" %} {% block page_title %}Dashboard{% endblock %}
{% block content %}

<div style="display: flex; align-items: center; justify-content: center; min-height: calc(100vh - 200px);">

<div style="text-align: center; max-width: 480px; padding: 0 24px;">

<div style="
            width: 64px; height: 64px; margin: 0 auto 24px;
            background: var(--primary-soft);
            border: 1.5px solid var(--primary-muted);
            border-radius: var(--radius-xl);
            display: flex; align-items: center; justify-content: center;
        ">

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjgiIGhlaWdodD0iMjgiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tcHJpbWFyeSkiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+CiAgICAgICAgICAgICAgICA8cGF0aCBkPSJNNCA2YTIgMiAwIDAxMi0yaDJhMiAyIDAgMDEyIDJ2MmEyIDIgMCAwMS0yIDJINmEyIDIgMCAwMS0yLTJWNnptMTAgMGEyIDIgMCAwMTItMmgyYTIgMiAwIDAxMiAydjJhMiAyIDAgMDEtMiAyaC0yYTIgMiAwIDAxLTItMlY2ek00IDE2YTIgMiAwIDAxMi0yaDJhMiAyIDAgMDEyIDJ2MmEyIDIgMCAwMS0yIDJINmEyIDIgMCAwMS0yLTJ2LTJ6bTEwIDBhMiAyIDAgMDEyLTJoMmEyIDIgMCAwMTIgMnYyYTIgMiAwIDAxLTIgMmgtMmEyIDIgMCAwMS0yLTJ2LTJ6IiAvPgogICAgICAgICAgICA8L3N2Zz4=)

</div>

## No workspaces yet

Create a workspace to start scheduling posts, managing content, and
collaborating with your team.

{% csrf_token %} Workspace name

Create Workspace

</div>

</div>

{% endblock %}
