---
type: source
source_type: laptop
title: install-dev-cert
slug: install-dev-cert
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/scripts/install-dev-cert.sh
original_size: 3166
original_ext: .sh
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---

# install-dev-cert

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/scripts/install-dev-cert.sh` on 2026-05-14._

```bash
#!/usr/bin/env bash
# One-time setup: installs a self-signed "Nomi Local Dev" code-signing
# identity in a dedicated keychain so every build of Nomi carries the
# same stable signature. With a stable signature, macOS TCC (Microphone,
# Speech Recognition, Screen Recording) stops forgetting your permission
# grants between rebuilds.
#
# Run this ONCE:
#     ./scripts/install-dev-cert.sh
#
# Then ./build.sh automatically picks it up. If this script isn't run,
# ./build.sh falls back to ad-hoc signing (permissions reset every build).
#
# This script is interactive — macOS may show one or two dialogs asking
# you to allow codesign to access the new keychain. Click "Always Allow"
# on each.

set -euo pipefail

IDENTITY_NAME="Nomi Local Dev"
SIGNING_KEYCHAIN="$HOME/Library/Keychains/nomi-signing.keychain-db"
SIGNING_KEYCHAIN_PASS="nomi-local-dev"

if security find-identity -v -p codesigning 2>/dev/null | grep -q "$IDENTITY_NAME"; then
    echo "✓ Identity '$IDENTITY_NAME' is already installed."
    exit 0
fi

echo "→ Creating dedicated keychain at $SIGNING_KEYCHAIN"
if [ -f "$SIGNING_KEYCHAIN" ]; then
    security delete-keychain "$SIGNING_KEYCHAIN" 2>/dev/null || true
fi
security create-keychain -p "$SIGNING_KEYCHAIN_PASS" "$SIGNING_KEYCHAIN"
security set-keychain-settings -u "$SIGNING_KEYCHAIN"
security unlock-keychain -p "$SIGNING_KEYCHAIN_PASS" "$SIGNING_KEYCHAIN"

echo "→ Adding to keychain search list"
OLD_LIST="$(security list-keychains -d user | sed -e 's/^[[:space:]]*//;s/\"//g' | tr '\n' ' ')"
# shellcheck disable=SC2086
security list-keychains -d user -s $OLD_LIST "$SIGNING_KEYCHAIN"

echo "→ Generating self-signed code-signing certificate"
T="$(mktemp -d)"
trap "rm -rf '$T'" EXIT

cat > "$T/cert.conf" <<EOF
[req]
distinguished_name = dn
prompt = no
x509_extensions = ext
[dn]
CN = $IDENTITY_NAME
[ext]
basicConstraints = CA:FALSE
keyUsage = digitalSignature
extendedKeyUsage = codeSigning
EOF

openssl req -x509 -nodes -days 3650 -newkey rsa:2048 \
    -keyout "$T/key.pem" -out "$T/cert.pem" \
    -config "$T/cert.conf"

openssl pkcs12 -export -legacy \
    -inkey "$T/key.pem" -in "$T/cert.pem" \
    -out "$T/identity.p12" \
    -name "$IDENTITY_NAME" \
    -passout pass:"$SIGNING_KEYCHAIN_PASS"

echo "→ Importing identity (macOS may prompt — click Always Allow)"
security import "$T/identity.p12" \
    -k "$SIGNING_KEYCHAIN" \
    -P "$SIGNING_KEYCHAIN_PASS" \
    -T /usr/bin/codesign \
    -A

echo "→ Granting codesign access without future prompts"
security set-key-partition-list \
    -S apple-tool:,apple:,codesign: \
    -s -k "$SIGNING_KEYCHAIN_PASS" \
    "$SIGNING_KEYCHAIN" >/dev/null 2>&1 || \
    echo "  (set-key-partition-list prompt may appear; accept it)"

echo ""
if security find-identity -v -p codesigning 2>/dev/null | grep -q "$IDENTITY_NAME"; then
    echo "✓ Success. ./build.sh will now sign with '$IDENTITY_NAME'."
    echo "  After the next build, grant TCC permissions once and they'll stick."
else
    echo "✗ Install appears incomplete. Run Keychain Access.app and look for"
    echo "  '$IDENTITY_NAME' — if missing, please report back what went wrong."
    exit 1
fi

```