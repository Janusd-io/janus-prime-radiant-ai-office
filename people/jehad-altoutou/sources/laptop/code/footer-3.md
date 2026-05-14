---
type: source
source_type: laptop
title: Desktop Captures — Footer
slug: footer-3
created: 2026-04-07
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Form Request copy/src/components/layout/Footer.jsx
original_size: 438
original_ext: .jsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# Footer

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Form Request copy/src/components/layout/Footer.jsx` on 2026-05-14._

```jsx
import { cn } from '../../lib/utils';

export const Footer = () => {
    return (
        <footer className="w-full border-t border-gray-200 bg-white py-6 mt-12">
            <div className="container mx-auto px-4 text-center">
                <p className="text-xs text-gray-400">
                    &copy; {new Date().getFullYear()} Janus Digital. Internal Use Only.
                </p>
            </div>
        </footer>
    );
};

```