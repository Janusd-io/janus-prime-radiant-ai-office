---
type: source
source_type: laptop
title: apps
slug: apps-7
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/publisher/apps.py
original_size: 1093
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
---

# apps

_Extracted from `brightbean-studio/apps/publisher/apps.py` on 2026-05-14._

```python
import logging

from django.apps import AppConfig

logger = logging.getLogger(__name__)


class PublisherConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.publisher"
    verbose_name = "Publishing Engine"

    def ready(self):
        from django.db.models.signals import post_migrate

        post_migrate.connect(self._register_publish_task, sender=self)

    @staticmethod
    def _register_publish_task(sender, **kwargs):
        """Register the recurring publish-cycle task after migrations are applied."""
        try:
            from background_task.models import Task

            from apps.publisher.tasks import run_publish_cycle

            if not Task.objects.filter(verbose_name="run_publish_cycle").exists():
                run_publish_cycle(
                    repeat=15,
                    verbose_name="run_publish_cycle",
                )
                logger.info("Registered recurring publish task (every 15s)")
        except Exception:
            logger.debug("Skipping publish task registration (database not ready)")

```