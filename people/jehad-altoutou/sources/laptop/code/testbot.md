---
type: source
source_type: laptop
title: testBot
slug: testbot
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/testBot.swift
original_size: 544
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# testBot

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/testBot.swift` on 2026-05-14._

```swift
import Foundation

let key = UserDefaults.standard.string(forKey: "notionAPIKey") ?? ""
let url = URL(string: "https://api.notion.com/v1/users/me")!
var req = URLRequest(url: url)
req.addValue("Bearer \(key)", forHTTPHeaderField: "Authorization")
req.addValue("2022-06-28", forHTTPHeaderField: "Notion-Version")

let sema = DispatchSemaphore(value: 0)
URLSession.shared.dataTask(with: req) { data, _, _ in
    if let data = data, let str = String(data: data, encoding: .utf8) {
        print(str)
    }
    sema.signal()
}.resume()
sema.wait()

```