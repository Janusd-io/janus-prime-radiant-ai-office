---
type: source
source_type: laptop
title: Container
slug: container-2
created: 2026-02-11
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Form Request copy/src/components/layout/Container.jsx
original_size: 237
original_ext: .jsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---

# Container

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Form Request copy/src/components/layout/Container.jsx` on 2026-05-14._

```jsx
import { cn } from '../../lib/utils';

export const Container = ({ children, className }) => {
    return (
        <div className={cn('container mx-auto px-4 py-8 max-w-3xl', className)}>
            {children}
        </div>
    );
};

```