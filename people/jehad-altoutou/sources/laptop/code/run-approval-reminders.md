---
type: source
source_type: laptop
title: run_approval_reminders
slug: run-approval-reminders
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/approvals/management/commands/run_approval_reminders.py
original_size: 642
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
---

# run_approval_reminders

_Extracted from `brightbean-studio/apps/approvals/management/commands/run_approval_reminders.py` on 2026-05-14._

```python
"""Management command to run approval reminder checks.

Usage:
    python manage.py run_approval_reminders

This runs the reminder check once. Schedule it via cron or process_tasks
for periodic execution (recommended: every hour).
"""

from django.core.management.base import BaseCommand

from apps.approvals.tasks import check_approval_reminders


class Command(BaseCommand):
    help = "Check for stalled approvals and send reminder notifications."

    def handle(self, *args, **options):
        self.stdout.write("Checking approval reminders...")
        check_approval_reminders()
        self.stdout.write(self.style.SUCCESS("Done."))

```