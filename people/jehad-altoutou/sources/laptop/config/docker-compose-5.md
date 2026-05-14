---
type: source
source_type: laptop
title: docker-compose
slug: docker-compose-5
created: 2026-02-11
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Form Request copy/docker-compose.yml
original_size: 878
original_ext: .yml
category: config
extracted_with: config-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# docker-compose

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Form Request copy/docker-compose.yml` on 2026-05-14._

```yaml
services:
  psi-form-request:
    build:
      context: .
      args:
        VITE_N8N_WEBHOOK_URL: ${VITE_N8N_WEBHOOK_URL}
        VITE_WEBHOOK_SECRET: ${VITE_WEBHOOK_SECRET}
    container_name: psi-form-request
    ports:
      - "8080:80"
    restart: always
    environment:
      # Pass build-time variables if needed, or runtime envs (Nginx serves static files, so runtime envs for JS need special handling if dynamic)
      # Since Vite bakes env vars at build time, we ensure they are present during build if running local dev mode, 
      # but for this production build, we assume .env is available in context or we need to pass ARGS.
      # For a simple static site, environment variables are embedded in the JS bundle.
      # To "pull updates", user rebuilds.
      - VITE_N8N_WEBHOOK_URL=${VITE_N8N_WEBHOOK_URL}
      - VITE_WEBHOOK_SECRET=${VITE_WEBHOOK_SECRET}

```