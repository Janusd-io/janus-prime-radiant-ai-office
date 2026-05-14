---
type: source
source_type: laptop
title: _delete_blocked
slug: delete-blocked
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/media_library/_delete_blocked.html
original_size: 1338
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:40Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# _delete_blocked

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/media_library/_delete_blocked.html` on 2026-05-14._

{% comment %}Shown when delete is blocked by post references. Expects:
asset, referencing_posts, workspace{% endcomment %}

<div class="p-4 rounded-xl border"
style="background: var(--warning-50, #FEFCE8); border-color: rgba(234,179,8,0.2);">

<div class="flex items-start gap-3">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSBmbGV4LXNocmluay0wIG10LTAuNSIgc3R5bGU9ImNvbG9yOiB2YXIoLS13YXJuaW5nLTUwMCwgI0VBQjMwOCk7IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0Ij4KICAgICAgPHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xMiA5djJtMCA0aC4wMW0tNi45MzggNGgxMy44NTZjMS41NCAwIDIuNTAyLTEuNjY3IDEuNzMyLTIuNUwxMy43MzIgNGMtLjc3LS44MzMtMS45NjQtLjgzMy0yLjczMiAwTDQuMDgyIDE2LjVjLS43Ny44MzMuMTkyIDIuNSAxLjczMiAyLjV6IiAvPgogICAgPC9zdmc+"
class="w-5 h-5 flex-shrink-0 mt-0.5" />

<div>

#### Cannot delete this asset

This media is referenced by {{ referencing_posts\|length }} scheduled
post{{ referencing_posts\|pluralize }}. Remove it from those posts
first.

{% if referencing_posts %}

- {% for post in referencing_posts %}
- • {{ post.caption\|truncatechars:60 }}
  {% endfor %}

{% endif %}

</div>

</div>

</div>
