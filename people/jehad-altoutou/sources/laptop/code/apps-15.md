---
type: source
source_type: laptop
title: apps
slug: apps-15
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/notifications/apps.py
original_size: 198
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
project: brightbean-studio

---

# apps

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/apps/notifications/apps.py` on 2026-05-14._

```python
from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.notifications"
    verbose_name = "Notifications"

```