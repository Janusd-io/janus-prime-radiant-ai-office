---
type: source
source_type: laptop
title: KeychainManager
slug: keychainmanager
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/Security/KeychainManager.swift
original_size: 736
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# KeychainManager

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/Security/KeychainManager.swift` on 2026-05-14._

```swift
import Foundation

/// Deprecated shim. All secret storage now flows through `KeychainHelper`.
/// This file exists only to avoid breaking existing imports during the migration.
@available(*, deprecated, message: "Use KeychainHelper.shared directly.")
public final class KeychainManager {
    public static let shared = KeychainManager()
    private init() {}

    public func save(token: String, forService service: String) throws {
        KeychainHelper.shared.save(token, for: service)
    }

    public func getToken(forService service: String) -> String? {
        KeychainHelper.shared.read(key: service)
    }

    public func deleteToken(forService service: String) {
        KeychainHelper.shared.delete(key: service)
    }
}

```