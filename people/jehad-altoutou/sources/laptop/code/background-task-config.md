---
type: source
source_type: laptop
title: background_task_config
slug: background-task-config
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/background_task_config.py
original_size: 168
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
project: brightbean-studio

---

# background_task_config

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/apps/background_task_config.py` on 2026-05-14._

```python
from background_task.apps import BackgroundTasksAppConfig


class BackgroundTaskConfig(BackgroundTasksAppConfig):
    default_auto_field = "django.db.models.AutoField"

```