---
type: source
source_type: laptop
title: project
slug: project
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/project.yml
original_size: 1276
original_ext: .yml
category: config
extracted_with: config-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---

# project

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/project.yml` on 2026-05-14._

```yaml
name: Nomi
options:
  bundleIdPrefix: com.antigravity
  deploymentTarget:
    macOS: 14.0
targets:
  Nomi:
    type: application
    platform: macOS
    info:
      path: Info.plist
      properties:
        LSUIElement: true
        NSPrincipalClass: NSApplication
        NSMicrophoneUsageDescription: "Nomi uses the microphone to listen to your voice commands."
        NSSpeechRecognitionUsageDescription: "Nomi uses neural transcription to process your spoken instructions."
        NSAppleEventsUsageDescription: "Nomi uses System Events to execute actions on your behalf."
        CFBundleURLTypes:
          - CFBundleURLName: com.antigravity.nomi.oauth
            CFBundleURLSchemes:
              - com.antigravity.nomi
          - CFBundleURLName: com.antigravity.nomi.oauth.google
            CFBundleURLSchemes:
              - com.googleusercontent.apps.373646355615-7ads5hesbv2qcmsnub3rtekohhp3o00g
    sources:
      - path: Sources
    resources:
      - path: Resources
        optional: true
    settings:
      PRODUCT_BUNDLE_IDENTIFIER: com.antigravity.nomi
      CODE_SIGN_IDENTITY: "-"
      CODE_SIGN_STYLE: Automatic
      GENERATE_INFOPLIST_FILE: NO
      LSMinimumSystemVersion: "14.0"
      ENABLE_HARDENED_RUNTIME: YES
      SWIFT_VERSION: "5.9"

```