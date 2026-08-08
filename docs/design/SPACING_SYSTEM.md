\# Guava Spacing System



> The official spacing specification for the Guava platform.



\---



\# Overview



Spacing is one of the strongest indicators of interface quality.



The Guava Spacing System establishes a consistent rhythm that governs every layout, component, form, table, dashboard, and Austin interaction.



Rather than treating spacing as decoration, Guava uses spacing to create hierarchy, readability, and visual balance.



\---



\# Philosophy



Whitespace is intentional.



Every gap should communicate structure.



Users should never feel overwhelmed by crowded interfaces.



Equally, excessive whitespace should not make interfaces feel disconnected.



Balance is the goal.



\---



\# Base Unit



The Guava design system is based on an \*\*8-point spacing grid\*\*.



Primary spacing increments:



```

4

8

16

24

32

40

48

56

64

80

96

128

```



Avoid arbitrary spacing values whenever possible.



\---



\# Spacing Tokens



| Token | Value |

|--------|------:|

| space-0 | 0 px |

| space-1 | 4 px |

| space-2 | 8 px |

| space-3 | 12 px |

| space-4 | 16 px |

| space-5 | 20 px |

| space-6 | 24 px |

| space-8 | 32 px |

| space-10 | 40 px |

| space-12 | 48 px |

| space-14 | 56 px |

| space-16 | 64 px |

| space-20 | 80 px |

| space-24 | 96 px |

| space-32 | 128 px |



Tokens should be referenced throughout design and engineering.



\---



\# Page Margins



Desktop



32 px



Tablet



24 px



Mobile



16 px



Margins remain consistent across every page.



\---



\# Section Spacing



Large page sections:



64–96 px



Medium sections:



48 px



Small sections:



32 px



Subsections:



24 px



Section spacing should create clear visual grouping.



\---



\# Card Spacing



Outer spacing:



24 px



Internal padding:



24 px



Compact card padding:



16 px



Large feature card padding:



32 px



Cards should maintain consistent internal rhythm.



\---



\# Dashboard Rhythm



Austin Hero



↓



48 px



↓



KPI Cards



↓



48 px



↓



Activity



↓



48 px



↓



District Cards



↓



48 px



↓



Insights



↓



48 px



↓



Partners



↓



64 px



↓



Footer



The dashboard should breathe naturally.



\---



\# Sidebar



Navigation items:



8 px vertical gap



Section groups:



24 px



Profile area:



32 px



Footer spacing:



24 px



The sidebar should remain calm and uncluttered.



\---



\# Navigation



Top navigation:



24 px horizontal padding



Button spacing:



16 px



Search spacing:



24 px



Notification spacing:



16 px



\---



\# Forms



Field spacing:



20 px



Label to input:



8 px



Helper text:



4 px



Section spacing:



32 px



Primary button:



32 px above



Forms should guide users naturally from top to bottom.



\---



\# Buttons



Horizontal padding:



24 px



Vertical padding:



12 px



Button groups:



12–16 px



Icon spacing:



8 px



Maintain consistent touch targets.



\---



\# Tables



Header padding:



16 px



Row padding:



16 px



Column spacing:



24 px



Toolbar spacing:



24 px



Filters:



16 px



Pagination:



24 px



Tables should remain readable even with dense information.



\---



\# Dialogs



Padding:



32 px



Section spacing:



24 px



Button group:



24 px



Title spacing:



16 px



Dialogs should feel spacious despite their smaller footprint.



\---



\# Austin Chat



Message spacing:



16 px



Bubble padding:



16 px



Conversation spacing:



24 px



Input spacing:



16 px



Attachment spacing:



12 px



Austin conversations should feel relaxed and easy to read.



\---



\# Lists



Item spacing:



12 px



Grouped lists:



24 px



Nested lists:



16 px



Maintain clear separation between items.



\---



\# Icons



Icon to label:



8 px



Icon groups:



12 px



Toolbar icons:



16 px



Icons should never crowd surrounding content.



\---



\# Charts



Chart title:



16 px



Legend:



24 px



Chart to controls:



24 px



Chart to summary:



32 px



Analytics pages should remain visually balanced.



\---



\# Empty States



Illustration



↓



24 px



↓



Title



↓



12 px



↓



Description



↓



24 px



↓



Primary Action



↓



Austin Suggestion



Empty states should encourage the next action.



\---



\# Mobile



Reduce spacing proportionally.



Do not compress below usability standards.



Touch targets remain a minimum of 44 × 44 px.



\---



\# Responsive Behaviour



Large desktop



Generous spacing



Desktop



Standard spacing



Tablet



Slightly reduced



Mobile



Compact while preserving readability



Hierarchy should remain identical across breakpoints.



\---



\# Figma Variables



Create spacing variables for every spacing token.



Examples:



space-1



space-2



space-4



space-6



space-8



space-12



space-16



All Auto Layout components should reference these variables.



\---



\# CSS Variables



```css

\--space-0

\--space-1

\--space-2

\--space-3

\--space-4

\--space-5

\--space-6

\--space-8

\--space-10

\--space-12

\--space-16

\--space-20

\--space-24

\--space-32

```



\---



\# Tailwind Mapping



Align spacing tokens with Tailwind's spacing scale wherever possible.



Avoid custom spacing unless there is a clear design justification.



\---



\# Engineering Rules



Never hard-code spacing values into components.



Components should consume spacing tokens.



Layout consistency depends on shared spacing definitions.



\---



\# Spacing Principles



Spacing should be:



Consistent



Predictable



Generous



Balanced



Responsive



Scalable



Purposeful



\---



\# Spacing Statement



Spacing is the invisible structure that gives Guava its calm and professional character.



By following a consistent spatial rhythm, every interface feels intentional, readable, and trustworthy.



\---



\*\*Spacing System\*\*



\*Order through rhythm.\*

