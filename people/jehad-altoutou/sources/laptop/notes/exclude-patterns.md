---
type: source
source_type: laptop
title: exclude-patterns
slug: exclude-patterns
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-brain-bootstrap/skills/janus-brain/config/exclude-patterns.txt
original_size: 2656
original_ext: .txt
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.95
sensitivity_reason: "Public basename-glob exclusion list shipped in the skill repo — describes privacy categories but contains no actual secrets."
---

# exclude-patterns

_Extracted from `Documents/janus-brain-bootstrap/skills/janus-brain/config/exclude-patterns.txt` on 2026-05-14._

# Privacy + noise exclusion patterns for /janus-brain
# One pattern per line. Lines starting with # are comments.
# Matched against the *basename* of every file and directory.
# Patterns use fnmatch globbing (case-insensitive).
#
# Do NOT remove anything from this file. To override, edit user-exclude.txt instead.

# ── Credentials, secrets, keys ─────────────────────────────────────────────
*.env
*.env.*
.env*
*.pem
*.key
*.p12
*.pfx
*.crt
*.cer
*.der
*.jks
*.keystore
id_rsa*
id_ed25519*
id_ecdsa*
id_dsa*
*.ppk
*secret*
*credential*
*password*
*passwd*
*token*
.netrc
.npmrc
.pypirc
.aws*
.gcp*
.azure*
.kube*
.dockercfg
.docker
authorized_keys
known_hosts

# ── Wallets, finance, identity ────────────────────────────────────────────
*.kdbx
*.kdb
*.1password
*.opvault
*.wallet
*.dat
*wallet.json
mnemonic*
seedphrase*
*tax*return*.pdf
*passport*.pdf
*passport*.jpg
*passport*.png
*national*id*.pdf
*emirates*id*.pdf

# ── VCS and package noise ─────────────────────────────────────────────────
.git
.gitignore
.gitattributes
.gitmodules
.svn
.hg
.bzr
node_modules
bower_components
vendor
__pycache__
*.pyc
*.pyo
.venv
venv
env
.virtualenv
.tox
.mypy_cache
.pytest_cache
.ruff_cache
.nox
.eggs
*.egg-info
.next
.nuxt
.svelte-kit
.parcel-cache
.cache
.turbo
.angular
dist
build
target
out
.gradle
.idea
.vscode
.vs
*.code-workspace
.DS_Store
Thumbs.db
desktop.ini
.Spotlight-V100
.Trashes
.fseventsd
.TemporaryItems
.AppleDouble
.LSOverride

# ── Browser data / app profiles ──────────────────────────────────────────
Cookies
Cookies-journal
History
History-journal
Login Data
Login Data-journal
Web Data
Web Data-journal
*.sqlite
*.sqlite3
*.db-journal
*.db-wal
*.db-shm
*Profile*
*default-release*
storage.json

# ── Media that adds noise (skip from text enrichment) ────────────────────
*.dmg
*.iso
*.img
*.vmdk
*.vdi
*.qcow2
*.zip
*.tar
*.tar.gz
*.tgz
*.7z
*.rar
*.gz
*.bz2
*.xz
*.lz4
*.zst
*.bin
*.exe
*.msi
*.deb
*.rpm
*.pkg
*.app
*.lock

# ── Lockfiles, build artifacts, generated ─────────────────────────────────
package-lock.json
yarn.lock
pnpm-lock.yaml
Cargo.lock
poetry.lock
Pipfile.lock
go.sum
composer.lock
Gemfile.lock
*.min.js
*.min.css
*.map
