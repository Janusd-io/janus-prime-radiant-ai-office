---
type: source
source_type: laptop
title: testNotion
slug: testnotion
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/testNotion.swift
original_size: 628
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---

# testNotion

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/testNotion.swift` on 2026-05-14._

```swift
import Foundation

let key = UserDefaults.standard.string(forKey: "notionAPIKey") ?? ""
let headers = [
    "Authorization": "Bearer \(key)",
    "Notion-Version": "2022-06-28"
]

guard let url = URL(string: "https://api.notion.com/v1/blocks/335114fc090c81919a6ecd2f2cacc64a/children") else { exit(1) }
var req = URLRequest(url: url)
for (k,v) in headers { req.setValue(v, forHTTPHeaderField: k) }

let sema = DispatchSemaphore(value: 0)
URLSession.shared.dataTask(with: req) { data, response, _ in
    if let data = data {
        print(String(data: data, encoding: .utf8) ?? "")
    }
    sema.signal()
}.resume()
sema.wait()

```