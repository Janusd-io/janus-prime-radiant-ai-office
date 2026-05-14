---
type: source
source_type: laptop
title: docker-compose.prod
slug: docker-compose-prod
created: 2026-04-20
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/docker-compose.prod.yml
original_size: 1865
original_ext: .yml
category: config
extracted_with: config-fenced
extracted_at: "2026-05-14T09:51:36Z"
---

# docker-compose.prod

_Extracted from `brightbean-studio/docker-compose.prod.yml` on 2026-05-14._

```yaml
services:
  migrate:
    build: .
    command: python manage.py migrate --noinput
    env_file:
      - .env
    environment:
      - DJANGO_SETTINGS_MODULE=config.settings.production
      - DATABASE_URL=postgres://postgres:postgres@postgres:5432/brightbean
    depends_on:
      postgres:
        condition: service_healthy

  app:
    command: gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 4 --threads 2
    volumes:
      - media_data:/app/media
    environment:
      - DJANGO_SETTINGS_MODULE=config.settings.production
    depends_on:
      migrate:
        condition: service_completed_successfully
    restart: unless-stopped

  worker:
    volumes:
      - media_data:/app/media
    environment:
      - DJANGO_SETTINGS_MODULE=config.settings.production
    depends_on:
      migrate:
        condition: service_completed_successfully
    restart: unless-stopped

  postgres:
    restart: unless-stopped

  maintenance:
    build: .
    command: >
      sh -c "
      while true; do
        echo \"[maintenance] $$(date): Running clearsessions...\"
        python manage.py clearsessions
        echo \"[maintenance] $$(date): Running media cleanup...\"
        python manage.py cleanup_orphaned_media --once --min-age-days 14
        echo \"[maintenance] $$(date): Done. Sleeping 24h.\"
        sleep 86400
      done
      "
    volumes:
      - media_data:/app/media
    environment:
      - DJANGO_SETTINGS_MODULE=config.settings.production
    depends_on:
      migrate:
        condition: service_completed_successfully
    restart: unless-stopped

  caddy:
    image: caddy:2-alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./Caddyfile:/etc/caddy/Caddyfile
      - caddy_data:/data
      - caddy_config:/config
    depends_on:
      - app
    restart: unless-stopped

volumes:
  caddy_data:
  caddy_config:

```