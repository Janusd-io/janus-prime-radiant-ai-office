---
type: source
source_type: laptop
title: mastodon_connect
slug: mastodon-connect
created: 2026-04-20
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/social_accounts/mastodon_connect.html
original_size: 3569
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:38Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# mastodon_connect

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/social_accounts/mastodon_connect.html` on 2026-05-14._

{% extends "base.html" %} {% block page_title %}Connect Mastodon{%
endblock %} {% block content %}

<div class="max-w-lg">

<div class="mb-8">

<a
href="%7B%%20url%20&#39;social_accounts:connect&#39;%20workspace_id=workspace_id%20%%7D"
class="inline-flex items-center gap-1.5 text-sm text-stone-500 hover:text-stone-700 transition-colors mb-4"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xNSAxOWwtNy03IDctNyIgLz48L3N2Zz4="
class="w-4 h-4" /> Back</a>

<div class="flex items-center gap-3 mb-2">

<div class="w-10 h-10 rounded-xl bg-indigo-50 flex items-center justify-center text-indigo-600">

{% include "social_accounts/partials/\_platform_icon.html" with
platform="mastodon" size="5" %}

</div>

## Connect Mastodon

</div>

Mastodon is federated, enter your profile URL to begin the connection
process.

</div>

{% csrf_token %}

<div>

Profile URL

<div class="relative">

<div class="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none">

<span class="text-sm text-stone-400">https://</span>

</div>

</div>

The Mastodon instance where your account lives

</div>

<div class="p-3.5 bg-indigo-50 rounded-xl border border-indigo-100">

<div class="flex gap-2.5">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCB0ZXh0LWluZGlnby01MDAgZmxleC1zaHJpbmstMCBtdC0wLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyIiBkPSJNMTMgMTZoLTF2LTRoLTFtMS00aC4wMU0yMSAxMmE5IDkgMCAxMS0xOCAwIDkgOSAwIDAxMTggMHoiIC8+PC9zdmc+"
class="w-4 h-4 text-indigo-500 flex-shrink-0 mt-0.5" />

After entering your instance URL, you'll be redirected to your Mastodon
instance to authorize access. We request **read**, **write**, and
**follow** permissions.

</div>

</div>

<div class="flex items-center gap-3 pt-2">

Continue to Mastodon <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xNCA1bDcgN20wIDBsLTcgN203LTdIMyIgLz48L3N2Zz4="
class="w-4 h-4" />

<a
href="%7B%%20url%20&#39;social_accounts:connect&#39;%20workspace_id=workspace_id%20%%7D"
class="px-4 py-2.5 text-sm font-semibold text-stone-600 hover:text-stone-800 transition-colors">Cancel</a>

</div>

</div>

{% endblock %}
