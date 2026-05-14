---
type: source
source_type: laptop
title: nginx
slug: nginx
created: 2026-02-11
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Form Request/nginx.conf
original_size: 392
original_ext: .conf
category: config
extracted_with: config-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---

# nginx

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Form Request/nginx.conf` on 2026-05-14._

```conf
server {
    listen 80;
    
    location / {
        root /usr/share/nginx/html;
        index index.html index.htm;
        try_files $uri $uri/ /psi-internal/index.html;
    }

    # Optional: Cache static assets
    location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg)$ {
        root /usr/share/nginx/html;
        expires 1y;
        add_header Cache-Control "public, no-transform";
    }
}

```