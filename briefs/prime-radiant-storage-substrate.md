---
type: brief
title: Prime Radiant moves off Google Drive — Git as the substrate for company-wide rollout
slug: prime-radiant-storage-substrate
created: 2026-05-13
updated: 2026-05-13
departments: [ai-office, it-ops, marketing]
status: active
confidence: high
sources: [2026-05-12-prime-radiant-marketing-setup-debug]
related: [janus-prime-radiant-build, marketing-prime-radiant, llm-wiki, obsidian, peer-to-peer-mesh-federation-pattern, ai-native-janus-positioning, 2026-05-08-marketing-prime-radiant-as-separate-vault, 2026-05-07-llm-wiki-extends-to-marketing-domain, andrew-soane, jehad-altoutou, michael-bruck]
---

# Prime Radiant moves off Google Drive — Git as the substrate for company-wide rollout

The Janus Prime Radiant pattern needs a different storage substrate than the Google Shared Drive layout the AIO instance was prototyped on. Drive's stream-on-demand sync model produced the exact failure that blocked [[andrew-soane|Andrew]]'s Marketing onboarding on 2026-05-12 (Cowork couldn't reliably mount the nested vault even though Obsidian could), and the underlying problem compounds the moment a contributor's identity sits on a different Google Workspace. **Git, hosted in the existing `Janusd-io` GitHub Organization with one private repo per Prime Radiant instance, eliminates both failure classes structurally**, naturally aligns the substrate with the wiki's existing content discipline (markdown + frontmatter + atomic commits is what Git provides natively), and turns per-department rollout into a one-page runbook instead of an evening of debugging. [[jehad-altoutou|Jehad]] confirmed the move 2026-05-13; this brief captures the decision rationale and the setup runbook to get him operational.

## Why this matters to Janus

Prime Radiant is no longer internal-tooling-only — per [[ai-native-janus-positioning]] it has been reframed as a commercial-asset under the three-pillar messaging spine, and per [[janus-prime-radiant-build]] the rollout is sequenced across all nine Janus departments. The substrate decision needs to be made *once*, with a pattern that scales linearly with each new instance and tolerates the cross-Workspace identity reality (`janusd.io` ↔ `janusd.com` today; client-facing contractors and ISO auditors later). Drive can be made to work for one or two instances with sufficient debugging per onboarding; it cannot be the substrate that turns "new department" into a half-day setup.

Git already is the substrate in spirit. The template repo `janus-prime-radiant-template` (v0.9.0 at [github.com/Janusd-io/janus-prime-radiant-template](https://github.com/Janusd-io/janus-prime-radiant-template)) is the canonical seed referenced from [[janus-prime-radiant-build]], and the [[peer-to-peer-mesh-federation-pattern]] was already designed assuming GitHub backing. This brief formalises what was implicit at the program level and provides the operational handoff to start using Git as the live substrate, not just the bootstrap surface.

## Diagnosis — what actually broke on 2026-05-12

Two distinct problems were entangled in the same failed session, and only one is solvable by rearranging folders.

**Drive's stream-on-demand sync model.** Drive for Desktop (and *all* Shared Drive content — Shared Drives can only be streamed, there is no mirror option) represents files on disk as placeholders, materialising the bytes only on first access. The placeholder model is implemented by a file-provider virtual filesystem (File Provider on macOS, an equivalent driver on Windows) that sits between apps and disk. When an app reads a file, the file provider intercepts, fetches the bytes, materialises them, then returns. For a single-file open this is invisible latency. For a recursive directory walk — which is what Cowork does to build its initial vault index — it produces inconsistent state: some files materialise fast, some slow, some return "exists but bytes not yet here" responses, and nested paths inside a Shared Drive don't resolve until a parent has been "warmed" by something walking it. The Marketing vault was nested inside the AI Office Shared Drive. Obsidian opens files lazily as the user navigates and tolerated the streaming behaviour; Cowork validates the mount up front and saw an empty folder.

**Cross-Workspace identity.** [[andrew-soane|Andrew]]'s primary identity is on `janusd.com`; the AI Office Shared Drive lives on `janusd.io`. Cross-Workspace Shared Drive access via Drive for Desktop is historically unreliable — even when the web UI grants permission, the local sync client can fail to enumerate the drive correctly. This is independent of the streaming issue and would recur with every cross-Workspace contributor, which the Janus digital knowledge twin will accumulate.

The folder-level fix that emerged at the end of the 2026-05-12 session (promote each Prime Radiant instance to its own top-level Shared Drive) addresses the streaming issue partially. It does not address cross-Workspace identity, which will recur with each non-`janusd.io` contributor.

## Why Git resolves both at the root

A git clone is real files on real disk. There is no file provider, no placeholder, no lazy parent resolution. The vault Cowork sees is the vault Obsidian sees, with the same semantics as any local file the user might have created in TextEdit. The entire class of streaming-mount bugs cannot occur because the streaming layer doesn't exist.

GitHub auth is decoupled from Google Workspace identity. Permissions are GitHub Team memberships against GitHub repos; whether a contributor's email is on `.com` or `.io` is irrelevant to whether their GitHub user can pull `janus-prime-radiant-<instance>`. The `Janusd-io` GitHub Organization (already extant) becomes the federation boundary, and that boundary was built for cross-org collaboration from the start — GitHub treats external identities as first-class.

Three additional alignments matter for the scale story:

The wiki's content discipline already describes a git repo. Kebab-case slugs, frontmatter discipline, immutable `sources/`, append-only `log.md`, the `inbox/.processed/` archive, the `updated:` frontmatter bumps — several of these rules exist to *recreate* what git provides natively (commit history, atomic multi-file changes, per-line blame). The CLAUDE.md rules don't go away, but several become belt-and-suspenders rather than primary safeguards.

Federation between instances becomes mechanical. Each contributor clones the instances they're entitled to into sibling directories under a standard parent (`~/janus/prime-radiant/<instance>/`). The [[peer-to-peer-mesh-federation-pattern]] translates one-to-one to this layout — cross-vault references become cross-clone paths. When stronger federation becomes desirable (unified search, programmatic cross-vault citations), the sibling-clone layout is exactly what crawlers and link-checkers assume.

Backup and disaster recovery are implicit. Every clone is a full backup of the repo's history. If GitHub were unavailable for a day, every contributor's machine would still hold the full vault and continue working; sync resumes when GitHub comes back. Compare to Drive, where the local copy is a thin placeholder cache and the cloud is the source of truth.

## Alternatives considered

| Option | Verdict | Reasoning |
|---|---|---|
| **Git on GitHub** (recommended) | Adopt | Solves streaming + cross-Workspace identity at the root; aligns substrate with content discipline; scales linearly with departments. |
| Top-level Shared Drive per instance + "Available offline" toggle | Bridge fix only | Solves streaming issue partially; does not solve cross-Workspace identity. Repeats the same debugging per new department. |
| Stay on nested Shared Drive layout | Rejected | Contradicts [[2026-05-08-marketing-prime-radiant-as-separate-vault]] and reproduces the 2026-05-12 failure mode. |
| Dropbox Business | Fallback option | Solves cross-org identity and streaming. Gives up version-control semantics, atomic multi-file changes, and the audit/blame surface the wiki implicitly wants. Keep in reserve for "if Git proves too unfamiliar for non-AIO departments." |
| Box | Rejected | Box Drive uses the same streaming-placeholder model as Google Drive — reproduces the exact bug class in a different vendor. |
| Obsidian Sync | Niche | $10/seat/month, purpose-built for Obsidian, but doesn't address Cowork's mount surface — the load-bearing requirement. Suitable as a personal-vault tool, not the company-wide substrate. |

## Operational model

One private GitHub repo per Prime Radiant instance, in the `Janusd-io` Organization. Repo naming: `janus-prime-radiant-<instance-slug>` — e.g., `janus-prime-radiant-ai-office`, `janus-prime-radiant-marketing`. Each repo seeded from the [[janus-prime-radiant-build|janus-prime-radiant-template]] (v0.9.0) on creation.

Per-department permissions via GitHub Teams (one team per department, mapped to the corresponding repo). Members get write access; the AIO curator role gets admin. Branch protection on `main` prevents force-push and history rewriting.

Per machine: each contributor clones their entitled repos to `~/janus/prime-radiant/<instance>/`. Same path on every machine and every OS — makes troubleshooting and federation tooling reproducible. Critical rule: the local path must not be inside any other sync root (iCloud Drive, Google Drive, Dropbox). Git is the sync layer; layering another on top reliably corrupts the repo internals.

Sync model is two-channel and deliberately redundant:

1. **Cowork commits and pushes its own work** at the end of each ingest, query, lint, or standup workflow. This is the load-bearing piece — it works regardless of whether Obsidian is open. The CLAUDE.md workflows need a small extension (open item) to formalise this.
2. **The Obsidian Git community plugin** (vinzent03, v2.38.2, 2.5M+ downloads) catches direct-in-Obsidian human edits with auto-pull on open, auto-pull every 5 min, and auto-commit-and-push every 5 min. Safety net, not primary sync — it only runs while Obsidian is open.

Cowork also runs `git pull` at the start of each workflow.

## Migration sequence

1. **Now / Jehad setup (this brief).** Push the current Drive vault contents to `janus-prime-radiant-ai-office` in `Janusd-io`. Stand up [[jehad-altoutou|Jehad]]'s machine per the runbook in Appendix A. Run both substrates (Drive + Git) in parallel for one week with Git authoritative; verify no missed writes during the bridge period.
2. **Week +1.** Stand up Andrew's Marketing instance from scratch on Git (`janus-prime-radiant-marketing`), skipping Drive entirely. The 2026-05-12 onboarding failure is the precipitating event; the corrected onboarding uses Git from the first commit.
3. **Week +2 to +4.** Demote the Drive copy of the AIO vault to read-only archive. Update CLAUDE.md §1 / §2 / §3 to describe Git as the canonical substrate. Extract the generalised `processes/prime-radiant-member-setup.md` runbook from the lessons learned in steps 1–2.
4. **Ongoing.** New-department rollouts (IT-Ops project-management team, HR, Finance, ISO, …) use the generalised runbook end-to-end. Target: half a day per new instance to stand up the repo + team; ten minutes per new member to clone-and-configure.

## Open questions and risks

*Mobile editing.* The Obsidian Git plugin documentation explicitly flags mobile as unstable. Git-backed mobile editing requires Working Copy on iOS plus Obsidian mobile — a more advanced setup. For now, mobile capture should continue to route through Obsidian Web Clipper on the phone (which drops into the desktop `inbox/` once the phone syncs); direct mobile editing is deferred until someone actually asks.

*Concurrent Cowork sessions touching the same vault.* The current CLAUDE.md ingest workflow implicitly assumes one Cowork session at a time (ingest counter, `inbox/.processed/` archive, lint trigger). Git resolves file-level merges cleanly, but the workflow *logic* could double-count if Michael and Jehad both run ingests simultaneously. Not urgent (they coordinate in practice); resolve with a small lock-file convention if it becomes a real issue.

*Non-technical onboarding curve.* The Obsidian Git plugin makes git largely invisible at runtime, but first-time setup touches a terminal once. For technical members (Jehad) this is trivial. For non-technical ones (Andrew, future Mariam / Theresa / Ann) the runbook needs careful rendering and probably an IT-pre-staged machine for the first run. Tracked as a runbook polish item; not a blocker.

*PDFs and binaries.* The wiki has a small number of PDFs in `sources/articles/`. Git handles modest binary volume fine. If volume grows substantially, Git LFS is the transparent answer. Not urgent.

*CLAUDE.md schema doc needs updating.* §1 "Top-level structure" and §3 "Naming conventions" both reference the Google Drive layout. They need a v0.10 pass to describe Git as the canonical substrate and to formalise the per-machine path convention. Out of scope for this brief; queue as a schema-doc work item.

*Dropbox fallback.* If the Obsidian Git plugin's setup curve proves too steep for HR / Finance / IT-Ops members, Dropbox Business is the documented fallback. Decision deferrable until evidence emerges from the Marketing rollout (Andrew is the leading non-technical test case).

---

## Appendix A — Jehad setup runbook (2026-05-13)

Jehad-specific. The generalised version will become `processes/prime-radiant-member-setup.md` once the pattern is proven through this first run.

**Prerequisites (verify before starting):**

- GitHub user (Jehad has one)
- GitHub user added to the `Janusd-io` Organization with write access to `janus-prime-radiant-ai-office` (Michael grants this once the repo exists)
- Obsidian installed
- Cowork installed (Claude desktop with Cowork mode)
- Terminal access for one-time setup

**One-time setup steps (on Jehad's Mac):**

1. **Authenticate to GitHub.** Install the GitHub CLI if not already (`brew install gh`), then `gh auth login` — choose GitHub.com, HTTPS, "Login with a web browser." Browser dance, ~30 seconds.

2. **Create the standard local layout and clone the AIO vault.**
   ```
   mkdir -p ~/janus/prime-radiant
   cd ~/janus/prime-radiant
   gh repo clone Janusd-io/janus-prime-radiant-ai-office ai-office
   ```
   The AIO vault is now at `~/janus/prime-radiant/ai-office/` as real local files.

3. **Confirm path hygiene.** This path must NOT be inside iCloud, Google Drive, or Dropbox. By default macOS only syncs `~/Documents` and `~/Desktop` to iCloud, so `~/janus/` is safe — but verify in System Settings → Apple ID → iCloud → Drive → Options that nothing is grabbing the parent.

4. **Register as an Obsidian vault.** Obsidian → Manage Vaults → Open folder as vault → select `~/janus/prime-radiant/ai-office/`. Open it; the existing AIO content should render.

5. **Enable Community plugins.** In the new vault: Settings → Community plugins → Turn on. Accept the third-party-code disclaimer (one-time, per vault).

6. **Install the Git plugin.** Settings → Community plugins → Browse → search "Git" → install **"Git" by vinzent03** (the one with 2.5M+ downloads, repository `github.com/Vinzent03/obsidian-git`) → Enable.

7. **Configure the Git plugin.** Settings → Git, then set:
   - Auto pull interval (minutes): `5`
   - Auto pull on startup: on
   - Auto backup interval (minutes): `5` (the plugin calls auto-commit-and-push "backup")
   - Commit message template: `vault backup: {{date}} {{hostname}}`
   - Pull strategy: `rebase`
   - Disable push: off
   - Disable pull: off

8. **Point Cowork at the same folder.** In Cowork, create a project pointed at `~/janus/prime-radiant/ai-office/`. Verify the project loads — file count, folder structure visible. If it shows empty, escalate to Michael (likely a permissions issue on the GitHub side rather than anything client-local).

9. **Sanity-check the round-trip.** Edit any file slightly in Obsidian, save, wait 5 min, refresh the GitHub web UI on the repo → confirm a commit appeared with Jehad's identity. Then from a Cowork session, modify a file and run a manual `git add -A && git commit -m "cowork sanity check" && git push` in `~/janus/prime-radiant/ai-office/` — confirm it appears on GitHub.

**Daily working pattern (no further setup):**

Open Obsidian to write. Open Cowork (project already configured) for ingest / queries / workflows. The Git plugin auto-pulls on Obsidian startup and auto-pushes every 5 minutes thereafter. Cowork's workflows commit-and-push their own changes at the end (see Cowork-side responsibility below). Nothing else to do.

**Cowork-side commit responsibility (open item):**

Cowork sessions running against the vault should `git pull` at the start of each workflow and `git add -A && git commit && git push` at the end. The CLAUDE.md ingest / query / lint workflows need a small extension to formalise this — that's a schema-doc work item, not a blocker for Jehad's setup. Until that extension lands, manual `git pull` / `git push` in the vault directory before/after Cowork sessions works fine; this is documentation polish, not a correctness issue.

**If something looks wrong:**

- *Vault appears empty in Cowork or Obsidian.* `git status` and `git log` in `~/janus/prime-radiant/ai-office/`. Most likely: clone failed silently — repeat step 2.
- *Git plugin shows a conflict notice in Obsidian.* Click through; the plugin opens a small two-way diff. For the AIO instance with Michael + Jehad as the only writers, true conflicts will be rare. Escalate to Michael if unsure rather than picking arbitrarily.
- *A commit landed with the wrong author.* `git config user.name` and `git config user.email` in the repo; both should match Jehad's GitHub identity. Fix with `git config user.email "<email>"` and `git config user.name "<name>"`.
- *Anything else weird.* Escalate to Michael. Git is hard to truly break — every state is recoverable from history.

---

## Sources

[[2026-05-12-prime-radiant-marketing-setup-debug]] — Andrew + Michael, 2026-05-12 17:42 Fireflies transcript of the failed Marketing-vault setup session and the live diagnosis of Drive's behaviour. (Note: source file pending formal ingest; transcript currently in uploads/.)
