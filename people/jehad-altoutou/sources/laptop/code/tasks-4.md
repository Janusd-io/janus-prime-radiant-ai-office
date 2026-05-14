---
type: source
source_type: laptop
title: tasks
slug: tasks-4
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/publisher/tasks.py
original_size: 642
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
project: brightbean-studio

---

# tasks

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/apps/publisher/tasks.py` on 2026-05-14._

```python
"""Background tasks for the publishing engine."""

import logging

from background_task import background

logger = logging.getLogger(__name__)


@background(schedule=0)
def run_publish_cycle():
    """Poll for due posts and publish them.

    Registered as a recurring task (every 15s) so that
    ``python manage.py process_tasks`` handles publishing
    without needing a separate ``run_publisher`` process.
    """
    from apps.publisher.engine import PublishEngine

    engine = PublishEngine()
    published = engine.poll_and_publish()
    if published:
        logger.info("Publish cycle completed - %d post(s) published", published)

```