---
type: source
source_type: laptop
title: testCal
slug: testcal
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/testCal.swift
original_size: 1130
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---

# testCal

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/testCal.swift` on 2026-05-14._

```swift
import Foundation

let token = "ya29.a0Aa7MYioEvM08p_G9rjCwLx-X3pxPreRxUpjMzlGnbYNWv5CI1RoeZrg2TrRoUv_FEV0nyM5e9SVJMOTrdWLJLzXxoElIHGHuAHCgdDSldcaeeR4N5Wpu4CEMY4_7RnXcIdI5z3hT2dO3h47whgpWj1ZyRP9Ul6jFGSXgiAPJ440kEbbHVeoPrpcobCjJN9qUlJ1uBzYaCgYKARoSARMSFQHGX2MieDcXDkT9XK0mGBuj08zkfA0206"

var components = URLComponents(string: "https://www.googleapis.com/calendar/v3/calendars/primary/events")!
components.queryItems = [
    URLQueryItem(name: "timeMin", value: ISO8601DateFormatter().string(from: Date())),
    URLQueryItem(name: "maxResults", value: "5"),
    URLQueryItem(name: "singleEvents", value: "true"),
    URLQueryItem(name: "orderBy", value: "startTime")
]

var req = URLRequest(url: components.url!)
req.httpMethod = "GET"
req.addValue("Bearer \(token)", forHTTPHeaderField: "Authorization")

let sem = DispatchSemaphore(value: 0)
URLSession.shared.dataTask(with: req) { data, response, error in 
    guard let data = data else { sem.signal(); return }
    print("STATUS: \((response as? HTTPURLResponse)?.statusCode ?? 0)")
    print(String(data: data, encoding: .utf8) ?? "")
    sem.signal()
}.resume()
sem.wait()

```