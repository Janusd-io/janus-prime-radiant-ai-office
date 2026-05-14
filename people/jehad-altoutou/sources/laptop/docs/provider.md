---
type: source
source_type: laptop
title: provider
slug: provider
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/allauth/elements/provider.html
original_size: 878
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:39Z"
---

# provider

_Extracted from `brightbean-studio/templates/allauth/elements/provider.html` on 2026-05-14._

{% load allauth %}
<a href="%7B%7B%20attrs.href%20%7D%7D" class="btn-social"
title="{{ attrs.name }}">{% if attrs.id == "google" %} <img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSI+PHBhdGggZD0iTTIyLjU2IDEyLjI1YzAtLjc4LS4wNy0xLjUzLS4yLTIuMjVIMTJ2NC4yNmg1LjkyYTUuMDYgNS4wNiAwIDAxLTIuMiAzLjMydjIuNzdoMy41N2MyLjA4LTEuOTIgMy4yOC00Ljc0IDMuMjgtOC4xeiIgZmlsbD0iIzQyODVGNCIgLz48cGF0aCBkPSJNMTIgMjNjMi45NyAwIDUuNDYtLjk4IDcuMjgtMi42NmwtMy41Ny0yLjc3Yy0uOTguNjYtMi4yMyAxLjA2LTMuNzEgMS4wNi0yLjg2IDAtNS4yOS0xLjkzLTYuMTYtNC41M0gyLjE4djIuODRDMy45OSAyMC41MyA3LjcgMjMgMTIgMjN6IiBmaWxsPSIjMzRBODUzIiAvPjxwYXRoIGQ9Ik01Ljg0IDE0LjA5Yy0uMjItLjY2LS4zNS0xLjM2LS4zNS0yLjA5cy4xMy0xLjQzLjM1LTIuMDlWNy4wN0gyLjE4QTEwLjk2IDEwLjk2IDAgMDAxIDEyYzAgMS43Ny40MiAzLjQ1IDEuMTggNC45M2wyLjg1LTIuMjIuODEtLjYyeiIgZmlsbD0iI0ZCQkMwNSIgLz48cGF0aCBkPSJNMTIgNS4zOGMxLjYyIDAgMy4wNi41NiA0LjIxIDEuNjRsMy4xNS0zLjE1QzE3LjQ1IDIuMDkgMTQuOTcgMSAxMiAxIDcuNyAxIDMuOTkgMy40NyAyLjE4IDcuMDdsMy42NiAyLjg0Yy44Ny0yLjYgMy4zLTQuNTMgNi4xNi00LjUzeiIgZmlsbD0iI0VBNDMzNSIgLz48L3N2Zz4=" />
{% endif %} <span>Continue with {{ attrs.name }}</span></a>
