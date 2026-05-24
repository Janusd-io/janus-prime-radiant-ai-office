---
type: brief
title: "NanoClaude wiring as of 2026-05-24 — Slack-fronted Prime Radiant reader, why the personal-brain pattern unblocks cross-dept rollout"
slug: nanoclaw-prime-radiant-wiring
created: 2026-05-24
updated: 2026-05-24
departments: [ai-office]
countries: [ae, sg]
status: active
confidence: high
sources: [2026-05-18-ai-native-ceo, 2026-05-19-aio-standup, 2026-05-20-aio-standup, 2026-05-21-aio-standup, 2026-05-22-aio-standup]
related: [nanoclaw, 2026-05-18-nanoclaw-as-personal-ai-coa-candidate, 2026-04-22-per-user-data-control-hard-requirement-agent-platforms, janus-prime-radiant-build, slack, hostinger, andrew-soane, michael-bruck, jehad-altoutou, claude-code, github]
---

# NanoClaude wiring as of 2026-05-24

NanoClaude — Janus's instance of [[nanoclaw|NanoClaw v2.0.64]] — has been running on Michael's MacBook since the 2026-05-21 demo and is now in daily dogfooding use. Slack-DM Q&A, scheduled 7AM news digest, HTML deck generation, and Chrome MCP first-run capabilities are all live. The deployment is N=1 (Michael only); Andrew's NanoClaude onboarding was confirmed verbally on 2026-05-21 but has not materialised in this install. AIR-103 still reads "Evaluating" in Linear; the Linear status has not been moved forward to reflect that the personal-brain pattern is now operating in dogfood.

## Why this matters to AIO bets

The [[janus-prime-radiant-build]] cross-department rollout has a hidden dependency that this deployment now resolves: **every contributor needs a low-friction read surface for their department's vault, because Obsidian is for curators**. NanoClaude is that surface. It validates the personal-brain pattern end-to-end: per-container Docker isolation + per-agent [[onecli|OneCLI Agent Vault]] secret allow-list + Slack-fronted Q&A + vault read-only by policy. That stack satisfies [[2026-04-22-per-user-data-control-hard-requirement-agent-platforms]] as a *configuration*, not a *promise*.

Three concrete unlocks:

1. **The originating decision is now testable, not aspirational.** [[2026-05-18-nanoclaw-as-personal-ai-coa-candidate]] proposed NanoClaw as the resolution for Slack-bot sprawl. Six days later the bot is in a Slack DM answering vault questions. The slack-bot-sprawl framing was correct.
2. **Cross-dept rollout can scale by replicating `dm-with-<handle>` agent groups.** The architecture is per-user agent groups on a per-machine host process. As Andrew, Joyce, Bonaventure, etc. come online, each gets their own NanoClaw install on their own machine pulling the same vault repo from [[github|`Janusd-io/janus-prime-radiant-ai-office`]] — no shared-state coupling, no multi-tenant complexity.
3. **The personal-brain layer is still consume-only.** The CLAUDE.local.md in `groups/dm-with-michaelb/` explicitly defers write-back: "If you draft a brief, decision, or pulse entry in response to a request, return it in the chat reply for him to file manually." This is the right floor for v0 — establishing trust before opening write paths. The brief-writing-via-Slack and conversational-query-filed-back flows referenced in the user prompt are *not yet open*.

## Deployment specifics (paths cited live in `~/Code/nanoclaw-v2/`)

### 1. Hosting & runtime

- **Single Node host process** orchestrates per-session Bun-runtime Docker containers. No docker-compose, no k8s — orchestration is bespoke in `src/container-runner.ts` (per `~/Code/nanoclaw-v2/CLAUDE.md` §"Quick Context" / §"Container Restart"). One Docker container per active session.
- **macOS launchd service.** Template at `~/Code/nanoclaw-v2/launchd/com.nanoclaw.plist` (substituted into `~/Library/LaunchAgents/com.nanoclaw.plist` at setup). `RunAtLoad=true`, `KeepAlive=true`. Logs to `logs/nanoclaw.log` and `logs/nanoclaw.error.log`. Service control: `launchctl kickstart -k gui/$(id -u)/com.nanoclaw`.
- **Public Slack reachability via Ngrok tunnel** (free tier — URL rotates on reconnect, breaks the webhook). [[hostinger|Hostinger]] VPS + Caddy reverse proxy migration is planned (Monday item 2931866304, owner Jehad; AIR-79 Hostinger, AIR-133 Caddy created 2026-05-22) but not yet executed. No Caddyfile in the install tree.
- **Version pinned to NanoClaw v2.0.64** (`package.json:3`). Upstream `nanocoai/nanoclaw`. Channels and providers live on `channels` / `providers` long-lived branches; installed via `/add-<channel>` skills, not bundled in trunk (`CLAUDE.md` §"Channels and Providers").

### 2. Authentication

Four env vars total in `.env`: `ONECLI_URL`, `SLACK_BOT_TOKEN`, `SLACK_SIGNING_SECRET`, `TZ`. That's it — `.env.example` is one line by design. Everything else is in OneCLI.

- **Slack auth: HTTP webhook mode, not Socket Mode.** `SLACK_BOT_TOKEN` (`xoxb-…`) for outbound, `SLACK_SIGNING_SECRET` for request validation. No `SLACK_APP_TOKEN` (the `xapp-…` Socket Mode token is absent), which is why Ngrok is required as a public webhook receiver. Adapter: `@chat-adapter/slack@4.26.0` (`package.json:31`).
- **Anthropic auth: via OneCLI gateway.** No `ANTHROPIC_API_KEY` in `.env`. Per-container requests proxy through the local OneCLI gateway, which injects credentials at request time. The container agent gets host pattern matching against the OneCLI vault; secrets never appear in container env vars or chat context (`CLAUDE.md` §"Secrets / Credentials / OneCLI", L152–190).
- **Known OneCLI gotcha:** newly-created agents start in `selective` secret mode with **zero secrets assigned**, even if vault host patterns would match. Symptom is `401 Unauthorized` from APIs whose credentials *are* in the vault. Fix is CLI-only (the SDK doesn't expose `setSecretMode`): `onecli agents set-secret-mode --id <agent-id> --mode all`, or `onecli agents set-secrets --secret-ids <id1>,<id2>`. Web UI at `http://127.0.0.1:10254`.

### 3. Vault access — read-only, via a separate clone refreshed by the host

This is the load-bearing detail most likely to be misunderstood downstream:

- The Prime Radiant vault is mounted into NanoClaude containers at `/workspace/agent/vault`, but the source on the host is **not** `~/janus/prime-radiant/ai-office/` (the canonical curator clone Obsidian edits). It is a **separate git clone** at `~/Code/nanoclaw-v2/groups/dm-with-michaelb/vault/` of the same `Janusd-io/janus-prime-radiant-ai-office` repo. Latest commit on disk as of inspection: `8cb4b70` (2026-05-20). The NanoClaude clone is a *snapshot* refreshed manually.
- **Sync model:** host-side `git pull` is what refreshes NanoClaude's vault. The container's network egress is OneCLI-gated and explicitly does not trust `github.com`'s TLS chain — so the container *cannot* run `git pull`, `git fetch`, or any network git operation. The CLAUDE.local.md instructs the agent to ask Michael for a host-side refresh if the vault looks stale (`groups/dm-with-michaelb/CLAUDE.local.md:7–9`).
- **Read-only by policy, not just by mount.** CLAUDE.local.md L20–24 explicitly: "Do not write to the vault yet. Writes, commits, and pushes are deferred to a later milestone — Michael will say when. … Do not run `git commit` or `git push` in the vault directory. `git pull --ff-only` only."
- **No MCP — direct filesystem.** Vault is just a mounted directory; the agent uses ordinary file tools. No obsidian-MCP, no filesystem-MCP wrapper.

### 4. Slack surface

- **One agent group wired:** `dm-with-michaelb` (agent group ID `ag-1779283681855-gu6whc`, per `groups/dm-with-michaelb/container.json`). Wired to Michael's Slack DM. The agent identifies as **"Nano"** (`container.json` `assistantName: "Nano"`; "NanoClaude" is the colloquial name from standups, "Andy" is the env-var default in the plist template that container config overrides).
- **`groups/main/` exists but is unwired** — it has a `CLAUDE.local.md` and nothing else, no `container.json`. `groups/_ping-test/` is empty. The 2026-05-22-standup-planned **AI eval Slack bot for the AIO channel** (monitor for tool suggestions → first-pass evaluation → reply + Monday task) has **not been wired into either** as of inspection. Either Michael's prototype attempt happened on this install and is incomplete, or the work hasn't started.
- **No multi-workspace setup.** One Slack workspace (Michael's `xoxb-…` bot token). Channel/DM scoping lives in the `messaging_groups` table inside `data/v2.db` — not in flat config — so without running `ncl messaging-groups list` it's not legible from files alone.

### 5. Skills inventory

NanoClaw has four skill types (`CLAUDE.md` §"Skills"). For Janus:

- **Host-side installer skills** — 50 of them in `~/Code/nanoclaw-v2/.claude/skills/`. These are how Michael (or whoever) extends the install. Notable available-but-not-yet-run installers: `add-linear`, `add-gmail-tool`, `add-gcal-tool`, `add-github`, `add-resend`, `add-mnemon`, `add-opencode`, `add-karpathy-llm-wiki`. Not in the available installer set: Notion, Monday, Fireflies — those would need custom MCP wiring.
- **Container skills** — 7 baked-in for every agent session: `agent-browser`, `frontend-engineer`, `onecli-gateway`, `self-customize`, `slack-formatting`, `vercel-cli`, `welcome` (`~/Code/nanoclaw-v2/container/skills/`).
- **Per-group CLAUDE.md fragments** composed into the agent's system prompt: `module-agents`, `module-cli`, `module-core`, `module-interactive`, `module-scheduling`, `module-self-mod`, `skill-onecli-gateway` (`groups/dm-with-michaelb/.claude-fragments/`).
- **Janus Prime Radiant skills (`/standup`, `/ai-registry`, `/ai-tool-evaluation`, lint) are NOT wired into NanoClaude.** These remain Claude Code skills invoked from Michael's terminal / Cowork session. NanoClaude can read the vault and reason over it; it cannot invoke the curation skills. This is a deliberate posture given the vault-read-only policy — invocation rights without write rights would be incoherent.

### 6. Connectors / MCP servers — none

`mcpServers: {}` in **both** the root `~/Code/nanoclaw-v2/.mcp.json` and the per-group `groups/dm-with-michaelb/container.json`. **Zero MCP connectors wired.** Linear, Notion, Monday, Fireflies, Gmail, GCal — none. Per-group config materialises out of the `container_configs` table in `data/v2.db` at spawn (`CLAUDE.md` §"Container Config"); the empty state is current ground truth, not stale serialisation.

What the agent reaches today: the mounted vault, the OneCLI-proxied Anthropic API, the built-in container skills (`agent-browser` Chromium, `slack-formatting`, etc.), and SQLite-backed working memory (per-session `inbound.db` / `outbound.db`, central `data/v2.db`).

### 7. OneCLI Agent Vault — deployed and active

Active local service. URL in `.env`'s `ONECLI_URL`, web UI at `http://127.0.0.1:10254`. SDK dep `@onecli-sh/sdk@^0.5.0` (`package.json:34`). All non-Slack secrets (Anthropic key, any future connector OAuth tokens) live here.

Approval-gating credentialed actions is a two-sided flow that is **not currently configured for Janus**: server-side approval policies must be set via the OneCLI web UI (the `onecli` CLI only supports `block` / `rate_limit`, not `approve`, as of `onecli@1.3.0`); host-side delivery routes through `src/modules/approvals/onecli-approvals.ts` against the `user_roles` table. If/when Janus wants human-in-the-loop on credentialed actions (e.g., Linear writes from NanoClaude), both sides need configuration.

### 8. Per-person isolation — three nested layers

The architecture supports three isolation tiers (`docs/isolation-model.md`); Janus's deployment uses the strongest:

| Layer | Mechanism | Janus today |
|---|---|---|
| **Per-machine** | Each user runs their own NanoClaw host on their own laptop | N=1 (Michael's MacBook). Andrew's Windows install planned. |
| **Per-user agent group** | One `dm-with-<handle>` agent group per user inside the host; modeled in `agent_groups` + `user_roles` tables | N=1 group (`dm-with-michaelb`) on Michael's host. |
| **Per-session container** | Each session gets its own Docker container with private `inbound.db`/`outbound.db` under `data/v2-sessions/<group>/<session>/` | 1 session active. |

Because users get their own machines, the per-machine layer naturally collapses into per-user isolation — the multi-tenant agent-group model becomes redundant in the dominant Janus topology, which is *one user per host*. The agent-group abstraction matters more when one host serves multiple users (e.g., a shared workspace install), which Janus doesn't have today.

Privilege model: owner / global admin / scoped admin / member, persisted in `user_roles`. CLI scope (`disabled` / `group` / `global`) controls what the agent itself can do via the `ncl` admin CLI from inside its container — Michael's group will be `global` (set automatically by `init-first-agent`), Andrew's should be `group`-scoped.

### 9. New ingest flows that NanoClaude opens (or doesn't, yet)

Live as of 2026-05-24:
- **Slack-DM vault Q&A** — operational since the 2026-05-21 demo. Read-only.
- **Daily 7AM news digest** — `groups/dm-with-michaelb/newsbot-seen.json` shows 75 Google-News article URLs tracked with timestamps; most recent 2026-05-21T03:01Z. Scheduled job (per `module-scheduling` CLAUDE fragment) pulls news, dedupes against `newsbot-seen.json`, posts interest-profiled digest to Slack.
- **HTML deck generation** — `nano-capabilities.html` (56KB) sits in the group dir as the first-run demonstration artefact. The capability is real; productionising it as a callable workflow is the next-step.
- **Conversation persistence** — `groups/dm-with-michaelb/conversations/` has 2 markdown transcripts from 2026-05-20 and 2026-05-21.

**Not yet open:**
- **Slack-as-inbox.** No flow where a Slack message becomes a vault `pulse/` or `briefs/` entry. The read-only policy precludes it until vault writes are unblocked.
- **Conversational queries filed back as briefs.** Drafts return to chat for Michael to file manually (per `groups/dm-with-michaelb/CLAUDE.local.md:22`).
- **AIO-channel AI eval bot** (planned in 2026-05-22 standup). No wired agent group for the channel as of inspection.

### 10. AIR-103 Gate 2 status

**Per evidence in this vault, no Gate 2 (Technical Qualification) assessment has been started.** AIR-103 remains in **Evaluating** despite the install being well past prototype — the Linear status hasn't been advanced to reflect that the personal-brain pattern is operating in daily dogfood. Per the [[ai-tool-evaluation-framework]] pipeline stages, the appropriate status is Sandbox now.

Candidate G2 findings already evident from this install (the install itself is the evidence):

- **G2.1 MCP-compatible architecture.** Per-group MCP server config is first-class in `container_configs`; container CLAUDE.md fragments include MCP-tool instructions (`module-self-mod` covers `add_mcp_server`).
- **G2.x security model.** Per-container Docker isolation + per-agent OneCLI secret allow-list (`selective`/`all` modes) + vault read-only by policy + OneCLI-gated container network egress (container does not trust `github.com` TLS). The supply-chain rule `minimumReleaseAge: 4320` (3 days) in `pnpm-workspace.yaml` is an additional defense-in-depth signal.
- **G2.x deployability.** Single Node host + Docker, launchd / systemd service unit, idempotent installer skills (`/setup`, `/init-onecli`, `/add-slack`), explicit v1→v2 migration path (`migrate-v2.sh` + `/migrate-from-v1` skill).
- **G2.x observability.** Structured logs at `logs/nanoclaw.log` + `logs/nanoclaw.error.log` + `logs/setup-steps/*.log`; session DBs (`messages_in`, `messages_out`) are inspectable post-hoc.

Recommended next: trigger `/ai-tool-evaluation` to walk G2.x against the live install rather than against the GitHub README. The install is the artefact under test now, not the project.

## What this brief is not

This is the *as-of-2026-05-24 wiring snapshot* — what's running, where, secured how. It is **not** a strategic Gate 2 dossier (that's the `/ai-tool-evaluation` skill's job) and it is **not** a rollout plan for the other departments (that belongs in [[janus-prime-radiant-build]]). When Andrew's install comes online, when the Hostinger+Caddy migration ships, or when vault writes get unblocked, this brief gets updated rather than appended-to — the snapshot shape is the point.

## Cross-references

- Originating decision: [[2026-05-18-nanoclaw-as-personal-ai-coa-candidate]].
- Vendor entity: [[nanoclaw]] (Janus deployment section updated in lockstep with this brief).
- Hard requirement satisfied: [[2026-04-22-per-user-data-control-hard-requirement-agent-platforms]].
- Program-level rollout this enables: [[janus-prime-radiant-build]].
- Substrate dependency: [[github]] (vault repo at `Janusd-io/janus-prime-radiant-ai-office`).
- Infrastructure migration in flight: [[hostinger]] (AIR-79); Caddy reverse proxy (AIR-133) — no vendor page yet.
- People referenced: [[michael-bruck]] (curator + sole user as of today), [[jehad-altoutou]] (owns the Hostinger migration), [[andrew-soane]] (second user, onboarding in flight).
