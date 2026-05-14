---
type: source
source_type: laptop
title: 0015_per_account_status
slug: 0015-per-account-status
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/composer/migrations/0015_per_account_status.py
original_size: 4133
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
project: brightbean-studio

---

# 0015_per_account_status

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/apps/composer/migrations/0015_per_account_status.py` on 2026-05-14._

```python
"""Move editorial status from Post onto PlatformPost.

After this migration each ``PlatformPost`` owns its own ``status`` field and
flows through the full editorial state machine independently. ``Post.status``
becomes a derived Python property (see ``apps.composer.status``) so list and
dashboard rendering still works unchanged.

Existing rows are backfilled so every PlatformPost inherits its parent's
current status — zero behavioural change for in-flight posts on day one.
"""

from django.db import migrations, models

_STATUS_CHOICES = [
    ("draft", "Draft"),
    ("pending_review", "Pending Review"),
    ("pending_client", "Pending Client"),
    ("approved", "Approved"),
    ("changes_requested", "Changes Requested"),
    ("rejected", "Rejected"),
    ("scheduled", "Scheduled"),
    ("publishing", "Publishing"),
    ("published", "Published"),
    ("failed", "Failed"),
]


# Old → new value mapping. ``partially_published`` was a post-level aggregate
# that can't exist on a single PlatformPost; fall it through to publishing so
# the publisher's retry logic can re-evaluate each child individually.
_AGGREGATE_REMAP = {"partially_published": "publishing"}


def forwards(apps, schema_editor):
    PlatformPost = apps.get_model("composer", "PlatformPost")
    for pp in PlatformPost.objects.select_related("post").iterator():
        parent_status = getattr(pp.post, "status", None) or "draft"
        pp.status = _AGGREGATE_REMAP.get(parent_status, parent_status)
        # Previously-successful publishes kept their timestamp on Post only;
        # copy it down so per-account UI reflects reality.
        if pp.status == "published" and not pp.published_at and pp.post.published_at:
            pp.published_at = pp.post.published_at
        pp.save(update_fields=["status", "published_at"])


def backwards(apps, schema_editor):
    """Re-create ``Post.status`` from the aggregate of its children."""
    # Import at call time so this module is safe to load under the new schema.
    from apps.composer.status import derive_post_status

    Post = apps.get_model("composer", "Post")
    for post in Post.objects.prefetch_related("platform_posts").iterator():
        statuses = [pp.status for pp in post.platform_posts.all()]
        post.status = derive_post_status(statuses)
        post.save(update_fields=["status"])


class Migration(migrations.Migration):
    dependencies = [
        ("composer", "0014_add_platform_post_platform_extra"),
    ]

    operations = [
        # 1. Add the new PlatformPost.status column (nullable default so the
        #    backfill step can populate it without tripping NOT NULL).
        migrations.AddField(
            model_name="platformpost",
            name="status",
            field=models.CharField(
                choices=_STATUS_CHOICES,
                default="draft",
                max_length=30,
                db_index=True,
            ),
        ),
        # 2. Backfill from Post.status (reverse rebuilds Post.status from
        #    children via derive_post_status).
        migrations.RunPython(forwards, backwards),
        # 3. Drop the old PlatformPost.publish_status field and its index.
        migrations.RemoveIndex(
            model_name="platformpost",
            name="idx_pp_status_sched",
        ),
        migrations.RemoveField(
            model_name="platformpost",
            name="publish_status",
        ),
        # 4. Re-add the index using the new field.
        migrations.AddIndex(
            model_name="platformpost",
            index=models.Index(
                fields=["status", "scheduled_at"],
                name="idx_pp_status_sched",
            ),
        ),
        # 5. Drop Post.status and its indexes now that the data lives on the
        #    child rows.
        migrations.RemoveIndex(
            model_name="post",
            name="idx_post_status_sched",
        ),
        migrations.RemoveIndex(
            model_name="post",
            name="idx_post_ws_status",
        ),
        migrations.RemoveField(
            model_name="post",
            name="status",
        ),
    ]

```