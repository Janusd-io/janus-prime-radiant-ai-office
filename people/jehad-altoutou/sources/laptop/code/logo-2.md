---
type: source
source_type: laptop
title: Logo
slug: logo-2
created: 2026-04-08
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Form Request copy/src/components/ui/Logo.jsx
original_size: 225
original_ext: .jsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# Logo

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Form Request copy/src/components/ui/Logo.jsx` on 2026-05-14._

```jsx
import React from 'react';

const basePath = import.meta.env.BASE_URL;

export const Logo = ({ className }) => (
    <img
        src={`${basePath}logo.png`}
        alt="Company Logo"
        className={className}
    />
);

```