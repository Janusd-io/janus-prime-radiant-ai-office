---
type: source
source_type: laptop
title: app
slug: app
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/app.json
original_size: 1628
original_ext: .json
category: config
extracted_with: config-fenced
extracted_at: "2026-05-14T09:51:36Z"
project: brightbean-studio

---

# app

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/app.json` on 2026-05-14._

```json
{
  "name": "Brightbean",
  "description": "Open-source social media management platform",
  "repository": "https://github.com/brightbeanxyz/brightbean-studio",
  "keywords": ["django", "social-media", "management"],
  "formation": {
    "web": {
      "quantity": 1,
      "size": "basic"
    },
    "worker": {
      "quantity": 1,
      "size": "basic"
    }
  },
  "addons": [
    {
      "plan": "heroku-postgresql:essential-0"
    }
  ],
  "env": {
    "SECRET_KEY": {
      "generator": "secret"
    },
    "ENCRYPTION_KEY_SALT": {
      "generator": "secret"
    },
    "DJANGO_SETTINGS_MODULE": {
      "value": "config.settings.production"
    },
    "ALLOWED_HOSTS": {
      "description": "Comma-separated list of allowed hostnames",
      "value": "*"
    },
    "APP_URL": {
      "description": "Public URL of the application (e.g., https://your-app.herokuapp.com). Can be set after first deploy.",
      "required": false
    },
    "STORAGE_BACKEND": {
      "description": "Storage backend: 'local' or 's3'",
      "value": "local"
    },
    "S3_ENDPOINT_URL": {
      "description": "S3-compatible endpoint URL",
      "required": false
    },
    "S3_ACCESS_KEY_ID": {
      "description": "S3 access key",
      "required": false
    },
    "S3_SECRET_ACCESS_KEY": {
      "description": "S3 secret key",
      "required": false
    },
    "S3_BUCKET_NAME": {
      "description": "S3 bucket name",
      "required": false
    }
  },
  "scripts": {
    "postdeploy": "python manage.py migrate"
  },
  "buildpacks": [
    {
      "url": "heroku/nodejs"
    },
    {
      "url": "heroku/python"
    }
  ]
}

```