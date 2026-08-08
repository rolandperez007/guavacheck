\# Guava Color Tokens



> The official color specification for the Guava platform.



\---



\# Overview



Color in Guava is used to communicate meaning, establish hierarchy, and reinforce trust.



The palette should feel calm, modern, and premium.



Color is never decorative without purpose.



\---



\# Color Philosophy



The interface should be dominated by neutral surfaces.



Accent colors should guide attention rather than compete for it.



Users should notice information before they notice color.



\---



\# Brand Colors



\## Primary Green



Purpose:



Primary actions



Primary buttons



Navigation highlights



Austin interaction states



Suggested value:



```

\#16A34A

```



\---



\## Secondary Green



Purpose:



Hover states



Supporting accents



Success emphasis



Suggested value:



```

\#22C55E

```



\---



\## Austin Accent



Purpose:



Austin hero



Conversation highlights



AI indicators



Subtle glows



Suggested value:



```

\#10B981

```



\---



\# Neutral Palette



\## Background



```

\#F8FAFC

```



\---



\## Surface



```

\#FFFFFF

```



\---



\## Border



```

\#E5E7EB

```



\---



\## Divider



```

\#D1D5DB

```



\---



\## Shadow Overlay



```

rgba(15,23,42,0.08)

```



\---



\# Text Colors



\## Primary Text



```

\#111827

```



\---



\## Secondary Text



```

\#4B5563

```



\---



\## Muted Text



```

\#6B7280

```



\---



\## Disabled Text



```

\#9CA3AF

```



\---



\# Semantic Colors



\## Success



```

\#22C55E

```



Used for:



\- Verification complete

\- Payments received

\- Successful uploads



\---



\## Warning



```

\#F59E0B

```



Used for:



\- Expiring documents

\- Attention required

\- Pending review



\---



\## Error



```

\#EF4444

```



Used for:



\- Failed verification

\- Validation errors

\- Critical problems



\---



\## Information



```

\#3B82F6

```



Used for:



\- Tips

\- Informational banners

\- Status messages



\---



\# District Accent Colors



Each district may use a subtle accent while remaining within the Guava visual language.



Marketplace



Green



Property Passport



Blue



Construction



Orange



Finance



Emerald



Investor



Purple



Knowledge



Indigo



These accents support recognition but should never overpower the interface.



\---



\# Interactive States



Primary Button



Default



↓



Hover



↓



Pressed



↓



Disabled



Every interactive component should define:



\- Default

\- Hover

\- Focus

\- Active

\- Disabled



Avoid inventing one-off color variations.



\---



\# Charts



Use restrained palettes.



Prefer:



Green



Blue



Purple



Orange



Gray



Avoid highly saturated rainbow charts.



\---



\# Notifications



Success



Green



Warning



Amber



Error



Red



Information



Blue



Status colors should remain consistent throughout the application.



\---



\# Accessibility



All text and UI colors must meet WCAG AA contrast requirements.



Never rely on color alone to communicate meaning.



Pair colors with icons or labels where appropriate.



\---



\# Dark Mode Readiness



Color tokens should be semantic rather than hard-coded.



Example:



Surface



Background



Text Primary



Text Secondary



Border



This allows future dark mode support without redesigning components.



\---



\# Design Tokens



Create reusable tokens for:



\- Brand colors

\- Surface colors

\- Text colors

\- Borders

\- Semantic states

\- District accents



Avoid embedding raw hex values directly into components.



\---



\# CSS Variables



```css

\--color-primary

\--color-primary-hover

\--color-background

\--color-surface

\--color-border

\--color-text-primary

\--color-text-secondary

\--color-success

\--color-warning

\--color-error

\--color-info

```



\---



\# Tailwind Mapping



Map semantic tokens to Tailwind configuration rather than using arbitrary colors throughout the codebase.



\---



\# Figma Variables



Create color variables for every semantic token.



Components should reference variables instead of fixed color values.



\---



\# Color Principles



Every color should be:



Intentional



Consistent



Accessible



Reusable



Semantic



Scalable



\---



\# Color Statement



Color in Guava exists to clarify, not decorate.



A restrained palette strengthens trust, improves readability, and ensures that important actions stand out naturally.



\---



\*\*Color Tokens\*\*



\*Meaning through color. Confidence through consistency.\*

