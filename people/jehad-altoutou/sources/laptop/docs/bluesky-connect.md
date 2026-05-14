---
type: source
source_type: laptop
title: bluesky_connect
slug: bluesky-connect
created: 2026-04-20
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/social_accounts/bluesky_connect.html
original_size: 3840
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:38Z"
project: brightbean-studio

---

# bluesky_connect

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/social_accounts/bluesky_connect.html` on 2026-05-14._

{% extends "base.html" %} {% block page_title %}Connect Bluesky{%
endblock %} {% block content %}

<div class="max-w-lg">

<div class="mb-8">

<a
href="%7B%%20url%20&#39;social_accounts:connect&#39;%20workspace_id=workspace_id%20%%7D"
class="inline-flex items-center gap-1.5 text-sm text-stone-500 hover:text-stone-700 transition-colors mb-4"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xNSAxOWwtNy03IDctNyIgLz48L3N2Zz4="
class="w-4 h-4" /> Back</a>

<div class="flex items-center gap-3 mb-2">

<div class="w-10 h-10 rounded-xl bg-sky-50 flex items-center justify-center text-sky-500">

{% include "social_accounts/partials/\_platform_icon.html" with
platform="bluesky" size="5" %}

</div>

## Connect Bluesky

</div>

Bluesky uses app passwords for authentication. You can create one in
your Bluesky account settings.

</div>

{% csrf_token %}

<div>

Handle

Your full Bluesky handle including domain

</div>

<div>

App Password

Generate one in Bluesky at Settings → Privacy and Security → App
Passwords

</div>

<div class="p-3.5 bg-sky-50 rounded-xl border border-sky-100">

<div class="flex gap-2.5">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCB0ZXh0LXNreS01MDAgZmxleC1zaHJpbmstMCBtdC0wLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyIiBkPSJNMTIgMTV2Mm0tNiA0aDEyYTIgMiAwIDAwMi0ydi02YTIgMiAwIDAwLTItMkg2YTIgMiAwIDAwLTIgMnY2YTIgMiAwIDAwMiAyem0xMC0xMFY3YTQgNCAwIDAwLTggMHY0aDh6IiAvPjwvc3ZnPg=="
class="w-4 h-4 text-sky-500 flex-shrink-0 mt-0.5" />

App passwords are separate from your main password. They can be revoked
at any time without affecting your Bluesky account.

</div>

</div>

<div class="flex items-center gap-3 pt-2">

Connect Bluesky <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xNCA1bDcgN20wIDBsLTcgN203LTdIMyIgLz48L3N2Zz4="
class="w-4 h-4" />

<a
href="%7B%%20url%20&#39;social_accounts:connect&#39;%20workspace_id=workspace_id%20%%7D"
class="px-4 py-2.5 text-sm font-semibold text-stone-600 hover:text-stone-800 transition-colors">Cancel</a>

</div>

</div>

{% endblock %}
