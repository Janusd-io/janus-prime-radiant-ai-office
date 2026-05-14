---
type: source
source_type: laptop
title: ActivityLogger
slug: activitylogger
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/Services/ActivityLogger.swift
original_size: 1508
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---

# ActivityLogger

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/Services/ActivityLogger.swift` on 2026-05-14._

```swift
import Foundation

public final class ActivityLogger {
    public static let shared = ActivityLogger()
    
    private let logURL: URL
    
    public init() {
        let directoryMap = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first!
        let appDir = directoryMap.appendingPathComponent("NomiData")
        try? FileManager.default.createDirectory(at: appDir, withIntermediateDirectories: true)
        logURL = appDir.appendingPathComponent("nomi_activity.json")
        
        if !FileManager.default.fileExists(atPath: logURL.path) {
            try? "[]".write(to: logURL, atomically: true, encoding: .utf8)
        }
    }
    
    public func record(action: String, target: String, status: String) {
        let entry: [String: String] = [
            "timestamp": ISO8601DateFormatter().string(from: Date()),
            "action": action,
            "target": target,
            "status": status
        ]
        
        Task(priority: .background) {
            do {
                let data = try Data(contentsOf: self.logURL)
                var logs = try JSONSerialization.jsonObject(with: data) as? [[String: String]] ?? []
                logs.append(entry)
                let newData = try JSONSerialization.data(withJSONObject: logs, options: .prettyPrinted)
                try newData.write(to: self.logURL, options: .atomic)
            } catch {
                print("Failed to append to ActivityLog: \(error)")
            }
        }
    }
}

```