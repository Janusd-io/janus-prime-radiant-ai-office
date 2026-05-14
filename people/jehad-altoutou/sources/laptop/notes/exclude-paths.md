---
type: source
source_type: laptop
title: exclude-paths
slug: exclude-paths
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-brain-bootstrap/skills/janus-brain/config/exclude-paths.txt
original_size: 791
original_ext: .txt
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.95
sensitivity_reason: "Public path-prefix exclusion list shipped in the skill repo."
project: janus-brain-bootstrap

---
<!-- jb:project-callout -->
> Part of [[janus-brain-bootstrap|Janus Brain Bootstrap]] — automatically linked by /janus-brain.


# exclude-paths

> Part of [[janus-brain-bootstrap|Janus Brain Bootstrap]] — captured by /janus-brain.

_Extracted from `Documents/janus-brain-bootstrap/skills/janus-brain/config/exclude-paths.txt` on 2026-05-14._

# Absolute path prefixes (relative to $HOME) that are never scanned.
# One path per line, no globbing, no comments inline.
# Patterns starting with / are absolute. Otherwise treated as $HOME/<pattern>.

Library
.ssh
.aws
.gcp
.gnupg
.config/gcloud
.config/gh
.config/git
.docker
.kube
.minikube
.terraform.d
.azure
.npm
.yarn
.pnpm-store
.cargo
.rustup
.cache
.local/share/keyrings
.password-store
.gpg
.openvpn
Pictures/Photos Library.photoslibrary
Pictures/Photo Booth Library
Library/Containers
Library/Caches
Library/Application Support
Library/Group Containers
Library/Keychains
Library/Mobile Documents
Library/Mail
Library/Messages
Library/Safari
Movies
Music
Public

# Common code-host clones we want graphified separately, not folded into the brain
go/pkg
go/src
.rbenv
.pyenv
.nvm
