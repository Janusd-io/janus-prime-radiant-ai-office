---
type: source
source_type: laptop
title: sla_config
slug: sla-config
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/inbox/sla_config.html
original_size: 4169
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:37Z"
project: brightbean-studio

---

# sla_config

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/inbox/sla_config.html` on 2026-05-14._

{% extends "base.html" %} {% block title %}SLA Settings - {{
workspace.name }} - Brightbean{% endblock %} {% block content %}

<div class="max-w-lg">

<div class="flex items-center gap-3 mb-6">

<a
href="%7B%%20url%20&#39;inbox:feed&#39;%20workspace_id=workspace.id%20%%7D"
class="text-stone-400 hover:text-stone-600 transition-colors"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwb2x5bGluZSBwb2ludHM9IjE1IDE4IDkgMTIgMTUgNiI+PC9wb2x5bGluZT48L3N2Zz4="
class="w-5 h-5" /></a>

<div>

## SLA Settings

Set response time targets for your inbox.

</div>

</div>

<div class="bg-white border border-stone-200 rounded-xl p-6"
style="box-shadow: var(--shadow-xs);">

{% csrf_token %}

<div class="space-y-5">

<div class="flex items-center justify-between">

<div>

Enable SLA Timer

Show countdown timers and overdue badges on unresolved messages.

</div>

<div class="w-9 h-5 bg-stone-200 rounded-full peer peer-checked:bg-orange-500 transition-colors after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:after:translate-x-full">

</div>

</div>

<div>

Target Response Time (minutes) {{ form.target_response_minutes }}

Messages exceeding this time will show an "Overdue" badge.

</div>

<div class="flex items-center justify-between pt-2 border-t border-stone-100">

<div>

Auto-resolve on Reply

Automatically mark messages as resolved when a reply is sent.

</div>

<div class="w-9 h-5 bg-stone-200 rounded-full peer peer-checked:bg-orange-500 transition-colors after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:after:translate-x-full">

</div>

</div>

</div>

<div class="flex items-center gap-3 mt-8 pt-5 border-t border-stone-100">

Save Settings

<a
href="%7B%%20url%20&#39;inbox:feed&#39;%20workspace_id=workspace.id%20%%7D"
class="text-[13px] font-medium text-stone-500 hover:text-stone-700 transition-colors">Cancel</a>

</div>

</div>

</div>

{% endblock %}
