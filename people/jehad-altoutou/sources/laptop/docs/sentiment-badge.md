---
type: source
source_type: laptop
title: _sentiment_badge
slug: sentiment-badge
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/inbox/partials/_sentiment_badge.html
original_size: 720
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:38Z"
project: brightbean-studio

---

# _sentiment_badge

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/inbox/partials/_sentiment_badge.html` on 2026-05-14._

<span class="badge-pill badge-sentiment-{{ message.sentiment }}"> {% if
message.sentiment == 'positive' %} <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0yLjUgaC0yLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMyI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNMTQuODI4IDE0LjgyOGE0IDQgMCAwMS01LjY1NiAwTTkgMTBoLjAxTTE1IDEwaC4wMU0yMSAxMmE5IDkgMCAxMS0xOCAwIDkgOSAwIDAxMTggMHoiIC8+PC9zdmc+"
class="w-2.5 h-2.5" /> {% elif message.sentiment == 'negative' %} <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0yLjUgaC0yLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMyI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNOS4xNzIgMTYuMTcyYTQgNCAwIDAxNS42NTYgME05IDEwaC4wMU0xNSAxMGguMDFNMjEgMTJhOSA5IDAgMTEtMTggMCA5IDkgMCAwMTE4IDB6IiAvPjwvc3ZnPg=="
class="w-2.5 h-2.5" /> {% endif %} {{ message.get_sentiment_display }}
</span>
