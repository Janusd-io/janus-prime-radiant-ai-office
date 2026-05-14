---
type: source
source_type: laptop
title: render
slug: render
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/render.yaml
original_size: 1320
original_ext: .yaml
category: config
extracted_with: config-fenced
extracted_at: "2026-05-14T09:51:36Z"
project: brightbean-studio

---

# render

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/render.yaml` on 2026-05-14._

```yaml
services:
  - type: web
    name: brightbean-web
    runtime: docker
    dockerfilePath: ./Dockerfile
    healthCheckPath: /health/
    preDeployCommand: "python manage.py migrate"
    envVars:
      - key: DJANGO_SETTINGS_MODULE
        value: config.settings.production
      - key: SECRET_KEY
        generateValue: true
      - key: ENCRYPTION_KEY_SALT
        generateValue: true
      - key: DATABASE_URL
        fromDatabase:
          name: brightbean-db
          property: connectionString
      - key: ALLOWED_HOSTS
        value: "*"
      - key: STORAGE_BACKEND
        value: s3

  - type: worker
    name: brightbean-worker
    runtime: docker
    dockerfilePath: ./Dockerfile
    dockerCommand: python manage.py process_tasks
    envVars:
      - key: DJANGO_SETTINGS_MODULE
        value: config.settings.production
      - key: SECRET_KEY
        fromService:
          name: brightbean-web
          type: web
          envVarKey: SECRET_KEY
      - key: ENCRYPTION_KEY_SALT
        fromService:
          name: brightbean-web
          type: web
          envVarKey: ENCRYPTION_KEY_SALT
      - key: DATABASE_URL
        fromDatabase:
          name: brightbean-db
          property: connectionString
      - key: STORAGE_BACKEND
        value: s3

databases:
  - name: brightbean-db
    plan: free

```