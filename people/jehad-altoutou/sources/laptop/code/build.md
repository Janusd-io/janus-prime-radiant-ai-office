---
type: source
source_type: laptop
title: build
slug: build
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/build.sh
original_size: 4017
original_ext: .sh
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# build

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/build.sh` on 2026-05-14._

```bash
#!/usr/bin/env bash
# Builds Nomi.app from Command Line Tools (no full Xcode required).
#
# Signing behavior:
#   - If the "Nomi Local Dev" identity exists (installed by
#     ./scripts/install-dev-cert.sh), signs with it. Stable identity →
#     TCC permission grants persist across rebuilds.
#   - Otherwise falls back to ad-hoc signing. App runs, but macOS will
#     re-prompt for Mic / Speech / Screen Recording after every rebuild.
#
# Usage:
#   ./build.sh           # build + open
#   ./build.sh --no-open # build only

set -euo pipefail

cd "$(dirname "$0")"

APP="build/Nomi.app"
BIN_DIR="$APP/Contents/MacOS"
RES_DIR="$APP/Contents/Resources"
SDK="$(xcrun --sdk macosx --show-sdk-path)"
IDENTITY_NAME="Nomi Local Dev"
SIGNING_KEYCHAIN="$HOME/Library/Keychains/nomi-signing.keychain-db"
SIGNING_KEYCHAIN_PASS="nomi-local-dev"

HAVE_IDENTITY=false
if security find-identity -v -p codesigning 2>/dev/null | grep -q "$IDENTITY_NAME"; then
    HAVE_IDENTITY=true
    # Keep the dedicated keychain unlocked for this session
    if [ -f "$SIGNING_KEYCHAIN" ]; then
        security unlock-keychain -p "$SIGNING_KEYCHAIN_PASS" "$SIGNING_KEYCHAIN" 2>/dev/null || true
    fi
fi

echo "→ Cleaning build dir"
rm -rf build
mkdir -p "$BIN_DIR" "$RES_DIR"

echo "→ Generating Info.plist"
cat > "$APP/Contents/Info.plist" <<'PLIST'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleDevelopmentRegion</key><string>en</string>
    <key>CFBundleExecutable</key><string>Nomi</string>
    <key>CFBundleIdentifier</key><string>com.antigravity.nomi</string>
    <key>CFBundleInfoDictionaryVersion</key><string>6.0</string>
    <key>CFBundleName</key><string>Nomi</string>
    <key>CFBundlePackageType</key><string>APPL</string>
    <key>CFBundleShortVersionString</key><string>1.0</string>
    <key>CFBundleVersion</key><string>1</string>
    <key>LSMinimumSystemVersion</key><string>14.0</string>
    <key>LSUIElement</key><true/>
    <key>NSPrincipalClass</key><string>NSApplication</string>
    <key>NSMicrophoneUsageDescription</key><string>Nomi uses the microphone to listen to your voice commands.</string>
    <key>NSSpeechRecognitionUsageDescription</key><string>Nomi uses neural transcription to process your spoken instructions.</string>
    <key>NSAppleEventsUsageDescription</key><string>Nomi uses System Events to execute actions on your behalf.</string>
    <key>CFBundleURLTypes</key>
    <array>
        <dict>
            <key>CFBundleURLName</key><string>com.antigravity.nomi.oauth</string>
            <key>CFBundleURLSchemes</key><array><string>com.antigravity.nomi</string></array>
        </dict>
        <dict>
            <key>CFBundleURLName</key><string>com.antigravity.nomi.oauth.google</string>
            <key>CFBundleURLSchemes</key><array><string>com.googleusercontent.apps.373646355615-7ads5hesbv2qcmsnub3rtekohhp3o00g</string></array>
        </dict>
    </array>
</dict>
</plist>
PLIST

echo "→ Compiling Swift sources"
swiftc \
    -O \
    -target arm64-apple-macos14.0 \
    -sdk "$SDK" \
    -parse-as-library \
    -module-name Nomi \
    -swift-version 5 \
    -framework AppKit \
    -framework SwiftUI \
    -framework AVFoundation \
    -framework Speech \
    -framework AuthenticationServices \
    -framework CryptoKit \
    -framework Carbon \
    -framework ScreenCaptureKit \
    -framework Security \
    $(find Sources -name '*.swift') \
    -o "$BIN_DIR/Nomi"

if $HAVE_IDENTITY; then
    echo "→ Signing with '$IDENTITY_NAME' (stable TCC identity)"
    codesign --force --deep --options runtime \
        --keychain "$SIGNING_KEYCHAIN" \
        --sign "$IDENTITY_NAME" "$APP"
else
    echo "→ Signing ad-hoc (run ./scripts/install-dev-cert.sh once to stop TCC resets)"
    codesign --force --deep --sign - "$APP"
fi

echo "✓ Built $APP"

if [[ "${1:-}" != "--no-open" ]]; then
    echo "→ Launching"
    open "$APP"
fi

```