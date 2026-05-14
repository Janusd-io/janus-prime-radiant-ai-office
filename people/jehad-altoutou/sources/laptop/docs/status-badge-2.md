---
type: source
source_type: laptop
title: Brightbean Studio — _status_badge
slug: status-badge-2
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/social_accounts/partials/_status_badge.html
original_size: 1362
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:38Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# _status_badge

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/social_accounts/partials/_status_badge.html` on 2026-05-14._

{% comment %} Status badge for social account connection state. Usage:
{% include "social_accounts/partials/\_status_badge.html" with
status=account.connection_status %} {% endcomment %} {% if status ==
"connected" %}
<span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-xs font-semibold bg-green-50 text-green-700 ring-1 ring-inset ring-green-600/10">
<span class="w-1.5 h-1.5 rounded-full bg-green-500"></span> Connected
</span> {% elif status == "token_expiring" %}
<span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-xs font-semibold bg-yellow-50 text-yellow-700 ring-1 ring-inset ring-yellow-600/10">
<span class="w-1.5 h-1.5 rounded-full bg-yellow-500"></span> Token
Expiring </span> {% elif status == "disconnected" %}
<span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-xs font-semibold bg-stone-100 text-stone-600 ring-1 ring-inset ring-stone-500/10">
<span class="w-1.5 h-1.5 rounded-full bg-stone-400"></span> Disconnected
</span> {% elif status == "error" %}
<span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-xs font-semibold bg-red-50 text-red-700 ring-1 ring-inset ring-red-600/10"
if="" error="" %}title="{{ error }}" {%="" endif="" %}="">
<span class="w-1.5 h-1.5 rounded-full bg-red-500"></span> Error </span>
{% endif %}
