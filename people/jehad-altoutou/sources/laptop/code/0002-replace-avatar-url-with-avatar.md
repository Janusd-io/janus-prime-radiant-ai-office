---
type: source
source_type: laptop
title: 0002_replace_avatar_url_with_avatar
slug: 0002-replace-avatar-url-with-avatar
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/accounts/migrations/0002_replace_avatar_url_with_avatar.py
original_size: 530
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
---

# 0002_replace_avatar_url_with_avatar

_Extracted from `brightbean-studio/apps/accounts/migrations/0002_replace_avatar_url_with_avatar.py` on 2026-05-14._

```python
# Generated migration to replace avatar_url URLField with avatar ImageField

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="avatar_url",
        ),
        migrations.AddField(
            model_name="user",
            name="avatar",
            field=models.ImageField(blank=True, upload_to="avatars/%Y/%m/"),
        ),
    ]

```