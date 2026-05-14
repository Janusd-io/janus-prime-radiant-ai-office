---
type: source
source_type: laptop
title: workspace_assignments
slug: workspace-assignments
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/members/partials/workspace_assignments.html
original_size: 1939
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:40Z"
---

# workspace_assignments

_Extracted from `brightbean-studio/templates/members/partials/workspace_assignments.html` on 2026-05-14._

{% csrf_token %}

<div class="space-y-2 max-h-64 overflow-y-auto mb-4">

{% for wd in workspace_data %}

<div class="flex items-center gap-3 py-2 px-3 rounded-lg"
style="background: var(--neutral-50);">

{{ wd.workspace.name }} {% for value, label in workspace_role_choices %}
{{ label }} {% endfor %}

</div>

{% empty %}

No workspaces available.

{% endfor %}

</div>

<div class="flex justify-end">

Save Assignments

</div>
