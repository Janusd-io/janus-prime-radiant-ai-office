---
type: source
source_type: laptop
title: privacy-filter
slug: privacy-filter
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-brain-bootstrap/skills/janus-brain/references/privacy-filter.md
original_size: 4145
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.95
sensitivity_reason: "Documentation of the three-layer privacy filter — by design about secrets, but the filter itself is non-secret"
---

# privacy-filter

_Extracted from `Documents/janus-brain-bootstrap/skills/janus-brain/references/privacy-filter.md` on 2026-05-14._

# Privacy Filter — What's Excluded and Why

The bootstrap is allowed to scan `$HOME` excluding hidden directories and `~/Library`. Even within that scope, three layers of filtering keep secrets and personal data out of the vault.

## Layer 1 — Hard-skip path segments

Defence in depth. Even if a user accidentally clears `exclude-paths.txt`, anything whose path contains one of these segments is never touched:

```
.ssh   .aws   .gnupg   .gcp   .azure   .kube   .docker
.password-store   .config/gcloud   .config/gh
Library/Keychains   Library/Mail   Library/Messages
```

Implemented in `walk-and-filter.py:HARD_SKIP_SEGMENTS`.

## Layer 2 — Path prefix exclusion (`exclude-paths.txt`)

`$HOME`-relative prefixes that are skipped wholesale. Edit only via the config file, never inline:

- `Library` — macOS app data, keychains, mail, messages
- `.ssh`, `.aws`, `.gcp`, `.gnupg`, `.azure`, `.kube`, `.docker` — credentials
- `.npm`, `.yarn`, `.pnpm-store`, `.cargo`, `.rustup` — package caches
- `.config/gcloud`, `.config/gh`, `.config/git` — service auth
- `Pictures/Photos Library.photoslibrary`, `Photo Booth Library` — photo libraries (huge + sensitive)
- `Movies`, `Music` — media
- `Library/Containers`, `Library/Caches`, `Library/Application Support`, `Library/Group Containers`, `Library/Mobile Documents` — app sandboxes
- `go/pkg`, `go/src`, `.rbenv`, `.pyenv`, `.nvm` — language runtimes

## Layer 3 — Basename pattern exclusion (`exclude-patterns.txt`)

Fnmatch globs (case-insensitive) applied to every file and directory name. Categories:

**Credentials:**
`*.env *.env.* .env* *.pem *.key *.p12 *.pfx *.crt *.cer *.der *.jks *.keystore id_rsa* id_ed25519* id_ecdsa* id_dsa* *.ppk *secret* *credential* *password* *passwd* *token* .netrc .npmrc .pypirc .aws* .gcp* .azure* .kube* .dockercfg .docker authorized_keys known_hosts`

**Wallets, finance, identity:**
`*.kdbx *.kdb *.1password *.opvault *.wallet *.dat *wallet.json mnemonic* seedphrase* *tax*return*.pdf *passport*.pdf *passport*.jpg *passport*.png *national*id*.pdf *emirates*id*.pdf`

**VCS / build / package noise:** `.git node_modules vendor __pycache__ dist build target .venv .next .turbo .DS_Store ...`

**Browser / app data:** `Cookies History "Login Data" "Web Data" *.sqlite *Profile* ...`

**Archive / binary noise:** `*.dmg *.iso *.zip *.tar.gz *.pkg *.app *.exe ...`

**Lockfiles:** `package-lock.json yarn.lock Cargo.lock poetry.lock go.sum ...`

## Layer 4 — User additions (`user-exclude.txt`)

Anything the user added at bootstrap time or via `/janus-brain exclude <pattern>`. Same basename-glob syntax. The walker treats these identically to layer 3.

## Layer 5 — Hidden-path rule

Any path with **any segment** starting with `.` (relative to `$HOME`) is excluded. This is enforced separately from `exclude-paths.txt` so that even if the user adds a dotfolder back to the include list, the walker still refuses.

The only way to scan a dotfolder is to add an explicit override to `user-exclude.txt` *negating* the pattern — currently not supported, by design. Talk to ops if you have a legitimate need.

## Per-note privacy ([[federation|federation]] gate)

Even if a file passes all five layers and gets enriched, the enrichment subagent can mark it private (`"private": true` in the record, `#private` tag in frontmatter). Private notes:

- **Are** written to the personal vault — the user wants their own brain to include them
- **Are NOT** federated to the CompanyBrain — `sync-to-company.py` checks frontmatter `private: true` and the `#private` tag, skips both

The subagent prompt instructs: "when in doubt, set private: true". The user can promote a note to public later by editing frontmatter — the next sync will pick up the change.

## Sanity check

After a bootstrap, sanity-check the result with:

```bash
grep -rl "BEGIN RSA PRIVATE KEY" "<vault>"
grep -rl "aws_access_key_id" "<vault>"
grep -rl "Bearer " "<vault>"
```

If any of these return hits, **stop and report** — a filter has failed and we need to patch `exclude-patterns.txt` or `HARD_SKIP_SEGMENTS`. This is a security regression, not a normal issue.
