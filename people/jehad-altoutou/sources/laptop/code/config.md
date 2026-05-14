---
type: source
source_type: laptop
title: Config
slug: config
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/Core/Config.swift
original_size: 4440
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---

# Config

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/Core/Config.swift` on 2026-05-14._

```swift
import Foundation

/// Configuration surface split into two classes of secret:
///
///   • **App secrets** — shared across every install. You (the developer) own the cost:
///     OpenAI, ElevenLabs TTS, voice selection. Hardcoded here by design; the Keychain
///     is the wrong store because every user would have to paste them individually.
///
///   • **User secrets** — per install. Each end user owns their own Linear / Notion /
///     Google Calendar / Fireflies accounts. Stored in the macOS Keychain, seeded
///     either via the in-app Connections panel or via OAuth callback.
///
/// If Nomi is ever distributed to external users, the app-secrets path must move to a
/// backend proxy — otherwise any user can extract keys from the compiled binary.
/// For an internal / personal deployment this is fine.
public enum Config {

    // MARK: - App-level secrets (shared across all installs)

    public static let openAIKey: String = "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"
    public static let elevenLabsKey: String = "5cfe684d4ab32fdb4b73b652ada5549a14d4d266cc603298246ff3c66fb18b51"
    public static let voiceID: String = "TxGi1N29NQoCaYD4fcU5"
    public static let elevenLabsModel: String = "eleven_flash_v2_5"

    // MARK: - User preferences

    public static var identity: String {
        get { KeychainHelper.shared.read(key: "identity") ?? Host.current().localizedName ?? "User" }
        set { KeychainHelper.shared.save(newValue, for: "identity") }
    }

    public static var listeningMode: ListeningMode {
        get {
            let raw = UserDefaults.standard.string(forKey: "nomi.listeningMode") ?? ListeningMode.pushToTalk.rawValue
            return ListeningMode(rawValue: raw) ?? .pushToTalk
        }
        set { UserDefaults.standard.set(newValue.rawValue, forKey: "nomi.listeningMode") }
    }

    // MARK: - User secrets (per install — Keychain-backed)

    public enum UserService: String, CaseIterable, Identifiable {
        case linear
        case notion
        case notionRootId
        case googleCalendar
        case fireflies

        public var id: String { rawValue }

        public var keychainKey: String {
            switch self {
            case .linear:          return "linearAPIKey"
            case .notion:          return "notionAPIKey"
            case .notionRootId:    return "notionTargetNotebookId"
            case .googleCalendar:  return "googleCalendarToken"
            case .fireflies:       return "firefliesAPIKey"
            }
        }

        public var displayName: String {
            switch self {
            case .linear:          return "Linear"
            case .notion:          return "Notion"
            case .notionRootId:    return "Notion — target notebook ID"
            case .googleCalendar:  return "Google Calendar"
            case .fireflies:       return "Fireflies"
            }
        }
    }

    public static func userSecret(_ service: UserService) -> String {
        KeychainHelper.shared.read(key: service.keychainKey) ?? ""
    }

    public static func setUserSecret(_ value: String, for service: UserService) {
        if value.isEmpty {
            KeychainHelper.shared.delete(key: service.keychainKey)
        } else {
            KeychainHelper.shared.save(value, for: service.keychainKey)
        }
    }

    public static func isConnected(_ service: UserService) -> Bool {
        !userSecret(service).isEmpty
    }

    // MARK: - Legacy accessors (keep existing adapters + ConnectToolCardView compiling)

    public static var linearAPIKey: String {
        get { userSecret(.linear) }
        set { setUserSecret(newValue, for: .linear) }
    }
    public static var notionAPIKey: String {
        get { userSecret(.notion) }
        set { setUserSecret(newValue, for: .notion) }
    }
    public static var notionPrivateRootId: String {
        get { userSecret(.notionRootId) }
        set { setUserSecret(newValue, for: .notionRootId) }
    }
    public static var googleCalendarToken: String {
        get { userSecret(.googleCalendar) }
        set { setUserSecret(newValue, for: .googleCalendar) }
    }
    public static var firefliesAPIKey: String {
        get { userSecret(.fireflies) }
        set { setUserSecret(newValue, for: .fireflies) }
    }
}

```