---
type: source
source_type: laptop
title: docker-compose
slug: docker-compose
created: 2026-04-27
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/docker-compose.yml
original_size: 426
original_ext: .yml
category: config
extracted_with: config-fenced
extracted_at: "2026-05-14T09:51:32Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# docker-compose

_Extracted from `[[assessify|assessify]]/docker-compose.yml` on 2026-05-14._

```yaml
services:
  app:
    build: .
    ports:
      - "3000:3000"
    env_file:
      - .env
    environment:
      - DATABASE_URL=file:./data/dev.db
      - NODE_ENV=production
    volumes:
      - assessify_data:/app/data
    healthcheck:
      test: ["CMD", "wget", "-q", "--spider", "http://127.0.0.1:3000/api/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 60s

volumes:
  assessify_data:

```