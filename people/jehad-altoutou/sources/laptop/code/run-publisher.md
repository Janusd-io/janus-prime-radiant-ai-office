---
type: source
source_type: laptop
title: run_publisher
slug: run-publisher
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/publisher/management/commands/run_publisher.py
original_size: 1833
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
---

# run_publisher

_Extracted from `brightbean-studio/apps/publisher/management/commands/run_publisher.py` on 2026-05-14._

```python
"""Management command to run the publishing engine worker.

Usage:
    python manage.py run_publisher
    python manage.py run_publisher --interval 15
"""

import signal
import time

from django.core.management.base import BaseCommand

from apps.publisher.engine import PublishEngine


class Command(BaseCommand):
    help = "Run the publishing engine worker that polls for scheduled posts."

    def add_arguments(self, parser):
        parser.add_argument(
            "--interval",
            type=int,
            default=15,
            help="Poll interval in seconds (default: 15).",
        )
        parser.add_argument(
            "--once",
            action="store_true",
            help="Run a single poll cycle and exit.",
        )

    def handle(self, *args, **options):
        interval = options["interval"]
        run_once = options["once"]
        engine = PublishEngine()

        self.stdout.write(self.style.SUCCESS(f"Publishing engine started (poll interval: {interval}s)"))

        # Handle graceful shutdown
        running = True

        def signal_handler(signum, frame):
            nonlocal running
            self.stdout.write(self.style.WARNING("\nShutting down publisher..."))
            running = False

        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)

        while running:
            try:
                published = engine.poll_and_publish()
                if published:
                    self.stdout.write(self.style.SUCCESS(f"Published {published} post(s)"))
            except Exception as e:
                self.stderr.write(self.style.ERROR(f"Publisher error: {e}"))

            if run_once:
                break

            time.sleep(interval)

        self.stdout.write(self.style.SUCCESS("Publisher stopped."))

```