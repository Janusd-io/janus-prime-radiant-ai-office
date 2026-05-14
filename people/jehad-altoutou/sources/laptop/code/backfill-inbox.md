---
type: source
source_type: laptop
title: backfill_inbox
slug: backfill-inbox
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/inbox/management/commands/backfill_inbox.py
original_size: 2577
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
---

# backfill_inbox

_Extracted from `brightbean-studio/apps/inbox/management/commands/backfill_inbox.py` on 2026-05-14._

```python
"""Management command to backfill historical inbox messages."""

from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from apps.inbox.tasks import InboxSyncEngine
from apps.social_accounts.models import SocialAccount
from providers import get_provider


class Command(BaseCommand):
    help = "Backfill historical inbox messages for connected accounts."

    def add_arguments(self, parser):
        parser.add_argument(
            "--days",
            type=int,
            default=7,
            help="Number of days to backfill (default: 7).",
        )
        parser.add_argument(
            "--platform",
            type=str,
            default=None,
            help="Only backfill a specific platform (e.g., youtube, linkedin, tiktok).",
        )
        parser.add_argument(
            "--account-id",
            type=str,
            default=None,
            help="Only backfill a specific account by UUID.",
        )

    def handle(self, *args, **options):
        days = options["days"]
        platform_filter = options["platform"]
        account_id = options["account_id"]
        since = timezone.now() - timedelta(days=days)
        engine = InboxSyncEngine()

        accounts = SocialAccount.objects.filter(
            connection_status=SocialAccount.ConnectionStatus.CONNECTED,
        ).select_related("workspace")

        if platform_filter:
            accounts = accounts.filter(platform=platform_filter)
        if account_id:
            accounts = accounts.filter(id=account_id)

        self.stdout.write(f"Backfilling {days} days of messages for {accounts.count()} account(s)...")

        for account in accounts:
            try:
                provider = get_provider(account.platform)
                messages = provider.get_messages(
                    access_token=account.oauth_access_token,
                    since=since,
                )
                count = 0
                for msg in messages:
                    engine._upsert_message(account, msg)
                    count += 1
                self.stdout.write(self.style.SUCCESS(f"  {account.platform}/{account.account_name}: {count} messages"))
            except NotImplementedError:
                self.stdout.write(f"  {account.platform}/{account.account_name}: skipped (not supported)")
            except Exception as e:
                self.stderr.write(f"  {account.platform}/{account.account_name}: ERROR - {e}")

        self.stdout.write(self.style.SUCCESS("Backfill complete."))

```