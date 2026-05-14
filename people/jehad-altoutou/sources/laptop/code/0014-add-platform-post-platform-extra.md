---
type: source
source_type: laptop
title: 0014_add_platform_post_platform_extra
slug: 0014-add-platform-post-platform-extra
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/composer/migrations/0014_add_platform_post_platform_extra.py
original_size: 562
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# 0014_add_platform_post_platform_extra

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/apps/composer/migrations/0014_add_platform_post_platform_extra.py` on 2026-05-14._

```python
# Generated for YouTube-specific composer fields

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("composer", "0013_add_platform_post_scheduled_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="platformpost",
            name="platform_extra",
            field=models.JSONField(
                blank=True,
                default=dict,
                help_text="Per-platform metadata (privacy, tags, thumbnail_asset_id, etc.)",
            ),
        ),
    ]

```