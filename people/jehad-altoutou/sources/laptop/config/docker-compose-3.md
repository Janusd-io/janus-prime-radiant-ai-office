---
type: source
source_type: laptop
title: docker-compose
slug: docker-compose-3
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/docker-compose.yml
original_size: 1665
original_ext: .yml
category: config
extracted_with: config-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# docker-compose

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/docker-compose.yml` on 2026-05-14._

```yaml
services:
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: johndoe
      POSTGRES_PASSWORD: randompassword
      POSTGRES_DB: mydb
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  app:
    build: .
    environment:
      DATABASE_URL: "postgresql://johndoe:randompassword@db:5432/mydb?schema=public"
      STRIPE_SECRET_KEY: ${STRIPE_SECRET_KEY:-}
      GMAIL_USER: ${GMAIL_USER:-}
      GMAIL_APP_PASSWORD: ${GMAIL_APP_PASSWORD:-}
      PROPOSALS_JWT_SECRET: ${PROPOSALS_JWT_SECRET:-}
      PROPOSALS_ADMIN_PASSWORD: ${PROPOSALS_ADMIN_PASSWORD:-}
    depends_on:
      - db
    networks:
      - default
      - root_infra
    labels:
      - "traefik.enable=true"
      - "traefik.docker.network=root_infra"
      - "traefik.http.routers.dubai-leads.rule=Host(`dubaipropertyleads.ae`) || Host(`www.dubaipropertyleads.ae`)"
      - "traefik.http.routers.dubai-leads.entrypoints=websecure"
      - "traefik.http.routers.dubai-leads.tls.certresolver=mytlschallenge"
      - "traefik.http.routers.dubai-leads.service=dubai-leads"
      - "traefik.http.services.dubai-leads.loadbalancer.server.port=3000"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/api/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

  ngrok:
    image: ngrok/ngrok:latest
    restart: always
    environment:
      NGROK_AUTHTOKEN: ${NGROK_AUTHTOKEN:-}
    command:
      - "http"
      - "app:3000"
      - "--pooling-enabled"
    ports:
      - "4040:4040"
    depends_on:
      - app

volumes:
  postgres_data:

networks:
  root_infra:
    external: true

```