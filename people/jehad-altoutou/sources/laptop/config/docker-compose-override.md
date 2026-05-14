---
type: source
source_type: laptop
title: docker-compose.override
slug: docker-compose-override
created: 2026-04-20
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/docker-compose.override.yml
original_size: 439
original_ext: .yml
category: config
extracted_with: config-fenced
extracted_at: "2026-05-14T09:51:36Z"
project: brightbean-studio

---

# docker-compose.override

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/docker-compose.override.yml` on 2026-05-14._

```yaml
services:
  app:
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    environment:
      - DJANGO_SETTINGS_MODULE=config.settings.development
      - DATABASE_URL=postgres://postgres:postgres@postgres:5432/brightbean

  worker:
    volumes:
      - .:/app
    environment:
      - DJANGO_SETTINGS_MODULE=config.settings.development
      - DATABASE_URL=postgres://postgres:postgres@postgres:5432/brightbean

```