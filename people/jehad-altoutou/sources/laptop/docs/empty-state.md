---
type: source
source_type: laptop
title: Brightbean Studio — _empty_state
slug: empty-state
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/inbox/partials/_empty_state.html
original_size: 2073
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:38Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# _empty_state

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/inbox/partials/_empty_state.html` on 2026-05-14._

<div class="flex flex-col items-center justify-center py-16 px-6 text-center">

<div class="w-16 h-16 rounded-2xl flex items-center justify-center mb-4"
style="background: var(--surface-2);">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy04IGgtOCIgc3R5bGU9ImNvbG9yOiB2YXIoLS10ZXh0LWdob3N0KTsiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPgogICAgICAgICAgICA8cGF0aCBkPSJNMjEgMTVhMiAyIDAgMDEtMiAySDdsLTQgNFY1YTIgMiAwIDAxMi0yaDE0YTIgMiAwIDAxMiAyeiIgLz4KICAgICAgICA8L3N2Zz4="
class="w-8 h-8" />

</div>

### Your inbox is empty

{% if social_accounts %}

Comments, mentions, and DMs from your connected accounts will appear
here. Messages are synced every 5 minutes.

{% else %}

Connect your social accounts to start receiving messages in your inbox.

<a
href="%7B%%20url%20&#39;social_accounts:connect&#39;%20workspace_id=workspace.id%20%%7D"
class="inline-flex items-center gap-1.5 px-4 py-1.5 text-[13px] font-semibold text-orange-600 bg-orange-50 border border-orange-200 rounded-full hover:bg-orange-100 hover:border-orange-300 active:bg-orange-100 transition-all duration-150"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xMiA0djE2bTgtOEg0IiAvPjwvc3ZnPg=="
class="w-4 h-4" /> Connect Accounts</a> {% endif %} {% if
active_filters.q or active_filters.platform or active_filters.type or
active_filters.status or active_filters.sentiment %}

<div class="mt-4 pt-4 border-t border-stone-100">

No messages match your current filters.

<a
href="%7B%%20url%20&#39;inbox:feed&#39;%20workspace_id=workspace.id%20%%7D"
class="text-[12px] font-semibold hover:underline"
style="color: var(--primary);">Clear all filters</a>

</div>

{% endif %}

</div>
