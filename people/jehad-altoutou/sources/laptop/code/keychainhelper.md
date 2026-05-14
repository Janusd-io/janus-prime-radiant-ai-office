---
type: source
source_type: laptop
title: KeychainHelper
slug: keychainhelper
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/Core/KeychainHelper.swift
original_size: 2457
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# KeychainHelper

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/Core/KeychainHelper.swift` on 2026-05-14._

```swift
import Foundation
import Security

/// Real Keychain-backed secret storage. Tokens are stored with
/// `kSecAttrAccessibleAfterFirstUnlock` so background daemons can read them after a
/// system reboot (once the user has logged in once).
///
/// All items are stored under the service `com.antigravity.nomi.secrets`, with the
/// caller-supplied `key` as the account. Calls are synchronous but cheap — the
/// Keychain daemon handles all I/O off-process.
public final class KeychainHelper {

    public static let shared = KeychainHelper()
    private init() {}

    private let service = "com.antigravity.nomi.secrets"

    @discardableResult
    public func save(_ value: String, for key: String) -> Bool {
        guard let data = value.data(using: .utf8) else { return false }

        let base: [String: Any] = [
            kSecClass as String:       kSecClassGenericPassword,
            kSecAttrService as String: service,
            kSecAttrAccount as String: key
        ]

        // Update if present, else add.
        let attrs: [String: Any] = [
            kSecValueData as String:   data,
            kSecAttrAccessible as String: kSecAttrAccessibleAfterFirstUnlock
        ]

        let updateStatus = SecItemUpdate(base as CFDictionary, attrs as CFDictionary)
        if updateStatus == errSecSuccess { return true }
        if updateStatus != errSecItemNotFound { return false }

        var addQuery = base
        for (k, v) in attrs { addQuery[k] = v }
        return SecItemAdd(addQuery as CFDictionary, nil) == errSecSuccess
    }

    public func read(key: String) -> String? {
        let query: [String: Any] = [
            kSecClass as String:       kSecClassGenericPassword,
            kSecAttrService as String: service,
            kSecAttrAccount as String: key,
            kSecReturnData as String:  true,
            kSecMatchLimit as String:  kSecMatchLimitOne
        ]

        var result: AnyObject?
        let status = SecItemCopyMatching(query as CFDictionary, &result)
        guard status == errSecSuccess, let data = result as? Data else { return nil }
        return String(data: data, encoding: .utf8)
    }

    public func delete(key: String) {
        let query: [String: Any] = [
            kSecClass as String:       kSecClassGenericPassword,
            kSecAttrService as String: service,
            kSecAttrAccount as String: key
        ]
        SecItemDelete(query as CFDictionary)
    }
}

```