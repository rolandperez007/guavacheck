\# Guava Typography System



> The official typography specification for the Guava platform.



\---



\# Overview



Typography is the primary communication layer of the Guava interface.



Every heading, paragraph, metric, label, button, table, and conversation should communicate clarity, hierarchy, and confidence.



Typography should never compete for attention.



Instead, it should quietly guide users through information.



\---



\# Typography Philosophy



Good typography is invisible.



Users should immediately understand:



\- What is important

\- What is secondary

\- What is actionable

\- What requires attention



without consciously thinking about font sizes.



\---



\# Primary Typeface



\## Primary Font



\*\*Inter Variable\*\*



Inter Variable should be used whenever variable font support is available.



Benefits:



\- Smaller bundle size

\- Smooth weight interpolation

\- Better rendering

\- Modern browser support



\---



\## Static Fallback



Inter



\---



\## System Fallback Stack



```

Inter Variable,

Inter,

SF Pro Display,

Segoe UI,

Helvetica Neue,

Arial,

sans-serif

```



Never substitute another primary font.



\---



\# Monospace Font



Used for:



\- Code

\- IDs

\- API Keys

\- Coordinates

\- JSON

\- Technical logs



Preferred stack:



```

JetBrains Mono,

SF Mono,

Consolas,

Menlo,

monospace

```



\---



\# Font Weights



| Weight | Usage |

|---------|-------|

| 300 | Rare decorative text |

| 400 | Body text |

| 500 | Labels |

| 600 | Card titles |

| 700 | Headings |

| 800 | Dashboard metrics |

| 900 | Reserved for hero numbers only |



Avoid unnecessary weight variation.



\---



\# Type Scale



| Style | Size |

|--------|------|

| Display XL | 64 px |

| Display L | 56 px |

| Display M | 48 px |

| H1 | 40 px |

| H2 | 32 px |

| H3 | 28 px |

| H4 | 24 px |

| H5 | 20 px |

| H6 | 18 px |

| Large Body | 18 px |

| Body | 16 px |

| Small Body | 14 px |

| Caption | 12 px |

| Micro | 11 px |



Maintain this scale throughout the platform.



\---



\# Line Heights



| Font Size | Line Height |

|------------|-------------|

| 64 | 72 |

| 56 | 64 |

| 48 | 56 |

| 40 | 48 |

| 32 | 40 |

| 24 | 32 |

| 20 | 28 |

| 18 | 28 |

| 16 | 24 |

| 14 | 22 |

| 12 | 18 |



Line height should maximize readability.



\---



\# Letter Spacing



Default:



```

0

```



Display headings:



```

\-0.02em

```



Captions:



```

0.02em

```



Avoid excessive tracking.



\---



\# Heading Hierarchy



H1



Platform pages



Major dashboards



\---



H2



Section titles



\---



H3



Card groups



\---



H4



Panel titles



\---



H5



Card headings



\---



H6



Widget headings



\---



\# Dashboard Metrics



Dashboard numbers should use:



Weight:



800



Large size



Tabular numerals



Examples:



```

₦245M



96%



18,234



4.8★



```



Metrics should be immediately readable.



\---



\# Austin Conversation



Austin should use:



Body



16 px



Weight 400



Generous line spacing



Replies should feel conversational.



Never compress chat text.



\---



\# Navigation Typography



Sidebar



16 px



Weight 500



Active item:



600



Muted inactive items.



\---



\# Buttons



Primary Button



16 px



600



\---



Secondary Button



15–16 px



500



\---



Small Button



14 px



500



Buttons should never use uppercase text.



\---



\# Forms



Labels



14 px



500



Input Text



16 px



400



Helper Text



13 px



400



Error Text



13 px



500



\---



\# Tables



Headers



14 px



600



Rows



14 px



400



Numeric columns



Tabular numerals



Right aligned



\---



\# Numbers



Enable:



Tabular Figures



For:



Currency



Measurements



Mortgage



Analytics



Reports



Construction costs



Financial values



Numbers should align vertically.



\---



\# Currency



Example



```

₦45,000,000



$1,250,000



€350,000

```



Always include:



Thousands separators



Consistent decimal formatting



\---



\# Text Alignment



Headings:



Left



Body:



Left



Metrics:



Usually left



Numeric tables:



Right



Avoid center alignment except in limited UI contexts.



\---



\# Text Width



Long paragraphs should not exceed:



75 characters per line



This improves readability.



\---



\# Responsive Typography



Desktop:



Full scale



Tablet:



Reduce headings by one level



Mobile:



Reduce display sizes while preserving hierarchy



Never reduce body text below:



16 px



\---



\# Accessibility



Minimum body size:



16 px



Contrast:



WCAG AA minimum



Never rely solely on color to communicate meaning.



\---



\# CSS Tokens



```css

\--font-family-base

\--font-family-mono



\--font-size-display-xl

\--font-size-display-lg

\--font-size-h1

\--font-size-h2

\--font-size-h3

\--font-size-h4

\--font-size-body

\--font-size-small



\--font-weight-regular

\--font-weight-medium

\--font-weight-semibold

\--font-weight-bold

\--font-weight-extrabold

```



\---



\# Tailwind Mapping



```

text-xs



text-sm



text-base



text-lg



text-xl



text-2xl



text-3xl



text-4xl



text-5xl



text-6xl

```



Map Guava typography to Tailwind utilities wherever possible.



\---



\# Figma Variables



Create typography variables for:



\- Font Family

\- Font Size

\- Weight

\- Line Height

\- Letter Spacing

\- Paragraph Spacing



Use text styles consistently across every component.



\---



\# Typography Principles



Typography should be:



Elegant



Readable



Consistent



Accessible



Scalable



Professional



Predictable



\---



\# Typography Statement



Typography is one of Guava's strongest visual assets.



It creates clarity without decoration, hierarchy without complexity, and confidence without distraction.



Every word should feel intentional.



Every number should feel trustworthy.



Every screen should communicate professionalism before the user reads a single sentence.



\---



\*\*Typography System\*\*



\*Clarity through consistency.\*

