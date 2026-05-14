---
type: source
source_type: laptop
title: vite.config
slug: vite-config
created: 2026-04-07
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Form Request/vite.config.js
original_size: 464
original_ext: .js
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---

# vite.config

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Form Request/vite.config.js` on 2026-05-14._

```javascript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

// https://vite.dev/config/
export default defineConfig({
  base: '/janus-internal/',
  plugins: [react()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  server: {
    proxy: {
      '/webhook': {
        target: 'https://n8n.srv1086109.hstgr.cloud',
        changeOrigin: true,
        secure: false,
      }
    }
  }
})

```