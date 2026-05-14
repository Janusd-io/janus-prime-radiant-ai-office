---
type: source
source_type: laptop
title: webhook_urls
slug: webhook-urls
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/inbox/webhook_urls.py
original_size: 311
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
project: brightbean-studio

---

# webhook_urls

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/apps/inbox/webhook_urls.py` on 2026-05-14._

```python
"""Webhook URL patterns - not auth-protected, CSRF-exempt."""

from django.urls import path

from . import webhooks

app_name = "inbox_webhooks"

urlpatterns = [
    path("facebook/", webhooks.facebook_webhook, name="webhook_facebook"),
    path("youtube/", webhooks.youtube_webhook, name="webhook_youtube"),
]

```