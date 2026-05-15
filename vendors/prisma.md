---
type: vendor
title: Prisma
slug: prisma
air_id: AIR-75
status: Backlog
labels: [Functional, Technology]
departments: []
url: https://linear.app/janusd/issue/AIR-75/prisma
created: 2026-04-09
updated: 2026-04-09
captured_by: jehad-altoutou
audience: department
sensitivity: dept
sensitivity_confidence: 0.9
---

# Prisma

> AI Registry entry [AIR-75](https://linear.app/janusd/issue/AIR-75/prisma) — status **Backlog** as of 2026-04-09. Departments: —.

**Category:** Database ORM / Backend Development Tool
**Status:** Backlog
**Cost:** Free (open source); Accelerate/Pulse paid add-ons
**Departments:** Technology

## Overview

Next-gen open-source ORM for Node.js and TypeScript. Type-safe database client, schema management, migration tooling. Currently in use by Jehad for candidate assessment platform ("Assessify") backend. Runs locally in Docker; intended for company server deployment.

## Current Usage

* Backend database layer for assessment platform
* Schema definition via Prisma Schema
* Typed database queries and relations

## Considerations

* Open-source core — no licensing concerns for self-hosted
* Prisma Accelerate (cloud connection pooling) raises data residency questions
* Should be installed on company infrastructure (not external hosting)
* Compare against Supabase, raw SQL, Firebase Firestore for stack consistency

*Backlog. Functional tier. Currently in use by Jehad's assessment platform.*
