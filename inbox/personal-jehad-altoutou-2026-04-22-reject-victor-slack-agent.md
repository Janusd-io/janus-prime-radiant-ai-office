---
type: decision
title: Reject Victor Slack agent over RBAC failure
slug: 2026-04-22-reject-victor-slack-agent
created: 2026-04-22
updated: 2026-04-22
departments: [ai-office]
status: resolved
owner: michael-bruck
decided_by: michael-bruck
sources: [2026-04-22-it-team-meeting]
related: []
audience: department
captured_by: jehad-altoutou
confidence: high
---

# Reject Victor Slack agent over RBAC failure

## Decision

Victor (a Slack-resident open-cloud agent) is rejected from the AI tool registry because it executes any request from any user in a channel, regardless of role.

## Why

If a finance user runs Victor in an open Slack channel, anyone in that channel inherits their access. With no role-based access control, the tool violates the segregation Janus needs before broader AI rollout.

## Evidence

> Speaker 3: We decided today to cancel it to not go with it... if anybody in this channel asks you a question, you'll do it? He goes, Yes.

## When

2026-04-22 · meeting [[2026-04-22-it-team-meeting]] · decided by [[michael-bruck]]

## Implications

- (to be populated by the owner)
