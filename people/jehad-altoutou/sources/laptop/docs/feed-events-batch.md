---
type: source
source_type: laptop
title: feed_events_batch
slug: feed-events-batch
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/composer/partials/feed_events_batch.html
original_size: 3146
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:39Z"
---

# feed_events_batch

_Extracted from `brightbean-studio/templates/composer/partials/feed_events_batch.html` on 2026-05-14._

{% if events %} {% for event in events %} {% with
event_url=event.link\|default:event.feed_website_url\|default:'#' %}

<a href="%7B%7B%20event_url%20%7D%7D"
class="block w-[140px] h-[96px] rounded-lg overflow-hidden bg-stone-100 flex-shrink-0"
target="_blank" rel="noopener noreferrer">{% if event.image_url %} <img
src="%7B%7B%20event.image_url%20%7D%7D"
class="w-full h-full object-cover" loading="lazy" /> {% else %}</a>

<div class="w-full h-full flex items-center justify-center">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy02IGgtNiB0ZXh0LXN0b25lLTQwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PHBhdGggZD0iTTQgMTFhOSA5IDAgMDE5IDkiIC8+PHBhdGggZD0iTTQgNGExNiAxNiAwIDAxMTYgMTYiIC8+PGNpcmNsZSBjeD0iNSIgY3k9IjE5IiByPSIxIj48L2NpcmNsZT48L3N2Zz4="
class="w-6 h-6 text-stone-400" />

</div>

{% endif %}

<div class="flex-1 min-w-0">

<a href="%7B%7B%20event_url%20%7D%7D"
class="block text-lg sm:text-xl leading-snug font-semibold text-stone-800 hover:text-stone-900"
target="_blank" rel="noopener noreferrer">{{ event.title }}</a>

<div class="mt-1 flex items-center gap-1.5 text-sm text-stone-500">

{% if event.feed_favicon_url %}
<img src="%7B%7B%20event.feed_favicon_url%20%7D%7D"
class="w-4 h-4 rounded object-contain" loading="lazy"
onerror="this.style.display=&#39;none&#39;; this.nextElementSibling.classList.remove(&#39;hidden&#39;);" />
{% endif %} <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCB0ZXh0LXN0b25lLTQwMCB7JSBpZiBldmVudC5mZWVkX2Zhdmljb25fdXJsICV9aGlkZGVueyUgZW5kaWYgJX0iIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGQ9Ik00IDExYTkgOSAwIDAxOSA5IiAvPjxwYXRoIGQ9Ik00IDRhMTYgMTYgMCAwMTE2IDE2IiAvPjxjaXJjbGUgY3g9IjUiIGN5PSIxOSIgcj0iMSI+PC9jaXJjbGU+PC9zdmc+"
class="w-4 h-4 text-stone-400 {% if event.feed_favicon_url %}hidden{% endif %}" />
{{ event.feed_name }}

</div>

{% if event.summary %}

{{ event.summary\|truncatechars:220 }} {% if event_url != '#' %}
<a href="%7B%7B%20event_url%20%7D%7D"
class="text-stone-700 hover:text-stone-900" target="_blank"
rel="noopener noreferrer">View Entire Post</a> {% endif %}

{% endif %}

<div class="mt-2 text-sm text-stone-500">

{% if event.published_at %} {{ event.published_at\|timesince }} ago {%
else %} Recently {% endif %}

</div>

</div>

{% endwith %} {% endfor %} {% elif show_empty %}

<div class="py-10 text-center text-stone-500">

No events found for this feed filter.

</div>

{% endif %} {% if has_more %}

<div class="py-5 flex items-center justify-center"
hx-get="{% url 'composer:feed_list' workspace_id=workspace.id %}?append=1&amp;offset={{ next_offset }}&amp;feed_id={{ selected_feed_id }}"
hx-target="this" hx-swap="outerHTML" hx-trigger="intersect once">

<div class="animate-spin w-5 h-5 border-2 border-stone-300 border-t-orange-500 rounded-full">

</div>

</div>

{% endif %}
