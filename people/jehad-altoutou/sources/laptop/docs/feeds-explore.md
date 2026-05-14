---
type: source
source_type: laptop
title: feeds_explore
slug: feeds-explore
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/composer/partials/feeds_explore.html
original_size: 3941
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:39Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# feeds_explore

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/composer/partials/feeds_explore.html` on 2026-05-14._

<div class="p-6">

## Explore Feeds

<div class="flex items-center justify-center gap-2 flex-wrap mb-6">

{% for cat in categories %}

{{ cat.label }}

{% endfor %}

</div>

<div class="grid grid-cols-1 sm:grid-cols-2 gap-3 max-h-[400px] overflow-y-auto">

{% for feed in curated_feeds %}

<div class="flex items-center gap-3 px-4 py-3 border border-stone-200 rounded-xl">

<div class="w-10 h-10 rounded-full bg-stone-100 flex items-center justify-center flex-shrink-0">

{% if feed.favicon %} <img src="%7B%7B%20feed.favicon%20%7D%7D"
class="w-5 h-5 rounded object-contain" loading="lazy"
onerror="this.style.display=&#39;none&#39;; this.nextElementSibling.classList.remove(&#39;hidden&#39;);" />
{% endif %} <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCB0ZXh0LXN0b25lLTQwMCB7JSBpZiBmZWVkLmZhdmljb24gJX1oaWRkZW57JSBlbmRpZiAlfSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PHBhdGggZD0iTTQgMTFhOSA5IDAgMDE5IDkiIC8+PHBhdGggZD0iTTQgNGExNiAxNiAwIDAxMTYgMTYiIC8+PGNpcmNsZSBjeD0iNSIgY3k9IjE5IiByPSIxIj48L2NpcmNsZT48L3N2Zz4="
class="w-4 h-4 text-stone-400 {% if feed.favicon %}hidden{% endif %}" />

</div>

<div class="flex-1 min-w-0">

<div class="text-sm font-semibold text-stone-800 truncate">

{{ feed.name }}

</div>

<div class="text-xs text-stone-400 truncate">

{{ feed.rss }}

</div>

</div>

{% if feed.subscribed %}

<div class="flex items-center justify-center w-8 h-8 flex-shrink-0">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSB0ZXh0LWdyZWVuLTUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwb2x5bGluZSBwb2ludHM9IjIwIDYgOSAxNyA0IDEyIj48L3BvbHlsaW5lPjwvc3ZnPg=="
class="w-5 h-5 text-green-500" />

</div>

{% else %}

{% csrf_token %}

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGQ9Ik0xMiA1djE0TTUgMTJoMTQiIC8+PC9zdmc+"
class="w-5 h-5" />

{% endif %}

</div>

{% endfor %}

</div>

</div>
