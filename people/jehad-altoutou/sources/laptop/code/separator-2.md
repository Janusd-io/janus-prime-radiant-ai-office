---
type: source
source_type: laptop
title: separator
slug: separator-2
created: 2026-02-11
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Form Request/src/components/ui/separator.jsx
original_size: 702
original_ext: .jsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# separator

_Extracted from `Desktop/Form Request/src/components/ui/separator.jsx` on 2026-05-14._

```jsx
import * as React from "react"
import * as SeparatorPrimitive from "@radix-ui/react-separator"

import { cn } from "../../lib/utils"

const Separator = React.forwardRef(
    ({ className, orientation = "horizontal", decorative = true, ...props }, ref) => (
        <SeparatorPrimitive.Root
            ref={ref}
            decorative={decorative}
            orientation={orientation}
            className={cn(
                "shrink-0 bg-gray-200",
                orientation === "horizontal" ? "h-[1px] w-full" : "h-full w-[1px]",
                className
            )}
            {...props}
        />
    )
)
Separator.displayName = SeparatorPrimitive.Root.displayName

export { Separator }

```