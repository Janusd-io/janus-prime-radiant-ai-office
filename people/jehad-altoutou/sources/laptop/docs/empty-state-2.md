---
type: source
source_type: laptop
title: _empty_state
slug: empty-state-2
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/media_library/_empty_state.html
original_size: 2293
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:40Z"
---

# _empty_state

_Extracted from `brightbean-studio/templates/media_library/_empty_state.html` on 2026-05-14._

{% comment %}Empty state when no assets match. Expects: query
(optional){% endcomment %}

<div class="flex flex-col items-center justify-center py-20 text-center">

<div class="w-20 h-20 rounded-2xl flex items-center justify-center mb-5"
style="background: var(--primary-soft, #FFF7ED);">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0xMCBoLTEwIiBzdHlsZT0iY29sb3I6IHZhcigtLXByaW1hcnksICNGOTczMTYpOyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+CiAgICAgIDxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik00IDE2bDQuNTg2LTQuNTg2YTIgMiAwIDAxMi44MjggMEwxNiAxNm0tMi0ybDEuNTg2LTEuNTg2YTIgMiAwIDAxMi44MjggMEwyMCAxNG0tNi02aC4wMU02IDIwaDEyYTIgMiAwIDAwMi0yVjZhMiAyIDAgMDAtMi0ySDZhMiAyIDAgMDAtMiAydjEyYTIgMiAwIDAwMiAyeiIgLz4KICAgIDwvc3ZnPg=="
class="w-10 h-10" />

</div>

{% if query %}

### No media matches your search

Try adjusting your search terms or filters.

<a
href="%7B%%20url%20&#39;media_library:index&#39;%20workspace_id=workspace.id%20%%7D"
class="inline-flex items-center gap-1.5 px-4 py-2 text-sm font-semibold rounded-full border transition-colors"
style="border-color: var(--border, #E7E5E4); color: var(--text-secondary, #57534E);"
onmouseenter="this.style.background=&#39;var(--surface-1)&#39;"
onmouseleave="this.style.background=&#39;transparent&#39;">Clear
search</a> {% else %}

### No media uploaded yet

Upload images and videos to organize and reuse across your posts.

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik03IDE2YTQgNCAwIDAxLS44OC03LjkwM0E1IDUgMCAxMTE1LjkgNkwxNiA2YTUgNSAwIDAxMSA5LjlNMTUgMTNsLTMtM20wIDBsLTMgM20zLTN2MTIiIC8+PC9zdmc+"
class="w-4 h-4" /> Upload media

{% endif %}

</div>
