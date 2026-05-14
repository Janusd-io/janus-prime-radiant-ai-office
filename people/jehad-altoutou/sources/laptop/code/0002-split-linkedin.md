---
type: source
source_type: laptop
title: 0002_split_linkedin
slug: 0002-split-linkedin
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/social_accounts/migrations/0002_split_linkedin.py
original_size: 1297
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
---

# 0002_split_linkedin

_Extracted from `brightbean-studio/apps/social_accounts/migrations/0002_split_linkedin.py` on 2026-05-14._

```python
from django.db import migrations, models

NEW_CHOICES = [
    ("facebook", "Facebook"),
    ("instagram", "Instagram"),
    ("linkedin_personal", "LinkedIn (Personal Profile)"),
    ("linkedin_company", "LinkedIn (Company Page)"),
    ("tiktok", "TikTok"),
    ("youtube", "YouTube"),
    ("pinterest", "Pinterest"),
    ("threads", "Threads"),
    ("bluesky", "Bluesky"),
    ("google_business", "Google Business Profile"),
    ("mastodon", "Mastodon"),
]


def rename_linkedin_to_company(apps, schema_editor):
    SocialAccount = apps.get_model("social_accounts", "SocialAccount")
    SocialAccount.objects.filter(platform="linkedin").update(platform="linkedin_company")


def rename_company_to_linkedin(apps, schema_editor):
    SocialAccount = apps.get_model("social_accounts", "SocialAccount")
    SocialAccount.objects.filter(platform="linkedin_company").update(platform="linkedin")


class Migration(migrations.Migration):
    dependencies = [
        ("social_accounts", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(rename_linkedin_to_company, rename_company_to_linkedin),
        migrations.AlterField(
            model_name="socialaccount",
            name="platform",
            field=models.CharField(choices=NEW_CHOICES, max_length=30),
        ),
    ]

```