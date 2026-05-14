---
type: source
source_type: laptop
title: docker-compose
slug: docker-compose-2
created: 2026-04-20
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/docker-compose.yml
original_size: 812
original_ext: .yml
category: config
extracted_with: config-fenced
extracted_at: "2026-05-14T09:51:36Z"
---

# docker-compose

_Extracted from `brightbean-studio/docker-compose.yml` on 2026-05-14._

```yaml
services:
  app:
    build: .
    volumes:
      - media_data:/app/media
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      postgres:
        condition: service_healthy

  worker:
    build: .
    command: python manage.py process_tasks
    volumes:
      - media_data:/app/media
    env_file:
      - .env
    depends_on:
      postgres:
        condition: service_healthy

  postgres:
    image: postgres:16-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: brightbean
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5

volumes:
  postgres_data:
  media_data:

```