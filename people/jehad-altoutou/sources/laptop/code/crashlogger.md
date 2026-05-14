---
type: source
source_type: laptop
title: CrashLogger
slug: crashlogger
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/Core/CrashLogger.swift
original_size: 1030
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# CrashLogger

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/Core/CrashLogger.swift` on 2026-05-14._

```swift
import Foundation

public final class CrashLogger {
    public static func setup() {
        NSSetUncaughtExceptionHandler { exception in
            let logPath = (NSHomeDirectory() as NSString).appendingPathComponent("Desktop/NomiCrashLog.txt")
            let stack = exception.callStackSymbols.joined(separator: "\n")
            let message = """
            
            --- NOMI FATAL CRASH REPORT ---
            Date: \(Date())
            Name: \(exception.name.rawValue)
            Reason: \(exception.reason ?? "Unknown")
            
            Call Stack:
            \(stack)
            -------------------------------
            
            """
            if let handle = FileHandle(forWritingAtPath: logPath) {
                handle.seekToEndOfFile()
                if let data = message.data(using: .utf8) { handle.write(data) }
                handle.closeFile()
            } else {
                try? message.write(toFile: logPath, atomically: true, encoding: .utf8)
            }
        }
    }
}

```