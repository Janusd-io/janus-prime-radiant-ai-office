---
type: source
source_type: laptop
title: package
slug: package
created: 2026-05-06
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/package.json
original_size: 1423
original_ext: .json
category: config
extracted_with: config-fenced
extracted_at: "2026-05-14T09:51:32Z"
---

# package

_Extracted from `[[assessify|assessify]]/package.json` on 2026-05-14._

```json
{
  "name": "assessify",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "eslint",
    "test": "vitest run",
    "test:watch": "vitest",
    "test:ui": "vitest --ui"
  },
  "dependencies": {
    "@anthropic-ai/sdk": "^0.93.0",
    "@base-ui/react": "^1.3.0",
    "@libsql/client": "^0.17.2",
    "@prisma/adapter-libsql": "^7.7.0",
    "@prisma/client": "^7.7.0",
    "@react-pdf/renderer": "^4.5.1",
    "bcryptjs": "^3.0.3",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "cmdk": "^1.1.1",
    "date-fns": "^4.1.0",
    "framer-motion": "^12.38.0",
    "lucide-react": "^1.7.0",
    "nanoid": "^5.1.7",
    "next": "^16.2.4",
    "next-themes": "^0.4.6",
    "prisma": "^7.7.0",
    "react": "19.2.4",
    "react-dom": "19.2.4",
    "resend": "^6.10.0",
    "shadcn": "^4.2.0",
    "sonner": "^2.0.7",
    "tailwind-merge": "^3.5.0",
    "tw-animate-css": "^1.4.0",
    "uuid": "^13.0.0",
    "zod": "^4.3.6"
  },
  "devDependencies": {
    "@tailwindcss/postcss": "^4",
    "@types/bcryptjs": "^2.4.6",
    "@types/node": "^20.19.39",
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "@vitest/ui": "^4.1.5",
    "dotenv": "^17.4.1",
    "eslint": "^9",
    "eslint-config-next": "16.2.2",
    "tailwindcss": "^4",
    "tsx": "^4.21.0",
    "typescript": "^5",
    "vitest": "^4.1.5"
  }
}

```