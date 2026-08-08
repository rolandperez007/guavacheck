\# Guava Grid System



> The mathematical framework that governs alignment, spacing, and responsive layout throughout the Guava platform.



\---



\# Overview



The Guava Grid System provides a consistent spatial framework for every interface.



Rather than positioning elements arbitrarily, every component aligns to a shared grid, ensuring visual rhythm, balance, and scalability across the platform.



This grid system applies to:



\- Dashboard

\- District pages

\- Austin Workspace

\- Reports

\- Tables

\- Forms

\- Dialogs

\- Mobile layouts

\- Future modules



\---



\# Design Goals



The grid system should provide:



\- Consistent alignment

\- Predictable spacing

\- Responsive behaviour

\- Easy component composition

\- Clean visual hierarchy

\- Enterprise-level polish



The grid should be invisible to users while guiding every design decision.



\---



\# Desktop Grid



Guava uses a \*\*12-column responsive grid\*\*.



```

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 |11 |12 |

```



This allows flexible layouts while maintaining alignment.



\---



\# Maximum Content Width



Desktop content container:



\*\*1440 px\*\*



Content should remain centered on larger displays.



Avoid stretching layouts across extremely wide monitors.



\---



\# Margins



Desktop:



\- Left Margin: 32 px

\- Right Margin: 32 px



Tablet:



\- 24 px



Mobile:



\- 16 px



Margins should remain consistent across the application.



\---



\# Gutters



Desktop gutter:



\*\*24 px\*\*



Tablet gutter:



\*\*20 px\*\*



Mobile gutter:



\*\*16 px\*\*



Gutters should never collapse below their minimum values.



\---



\# Sidebar Width



Desktop:



\*\*280 px\*\*



Collapsed (future):



\*\*88 px\*\*



Sidebar width should remain constant across desktop pages.



\---



\# Top Navigation



Height:



\*\*72 px\*\*



The top navigation should maintain a fixed height to preserve consistency.



\---



\# Austin Workspace



Default width:



\*\*440 px\*\*



Minimum width:



\*\*400 px\*\*



Maximum width:



\*\*520 px\*\*



Future versions may allow resizing within these limits.



\---



\# Dashboard Alignment



The dashboard should align all major sections to the same grid.



Example:



Austin Hero



↓



KPI Cards



↓



Activity



↓



District Cards



↓



Insights



↓



Partner Logos



↓



Footer



No section should break grid alignment.



\---



\# KPI Cards



All KPI cards should have:



Equal height



Equal spacing



Aligned baselines



Consistent internal padding



Cards should resize proportionally across breakpoints.



\---



\# District Cards



Every district card should align to the grid.



Maintain:



Equal width



Equal height



Consistent spacing



Uniform image proportions



Uniform typography alignment



\---



\# Card Padding



Standard card padding:



\*\*24 px\*\*



Compact cards:



\*\*16 px\*\*



Large feature cards:



\*\*32 px\*\*



Padding should remain consistent across all components.



\---



\# Vertical Rhythm



Preferred spacing scale:



\- 8 px

\- 16 px

\- 24 px

\- 32 px

\- 48 px

\- 64 px

\- 96 px



Avoid arbitrary spacing values.



Every vertical distance should follow the spacing scale.



\---



\# Responsive Breakpoints



Mobile



0–767 px



Tablet



768–1023 px



Desktop



1024–1439 px



Large Desktop



1440 px and above



Layouts should adapt while preserving hierarchy.



\---



\# Mobile Grid



Use a \*\*4-column grid\*\*.



Margins:



16 px



Gutters:



16 px



Maintain generous touch targets.



\---



\# Tablet Grid



Use an \*\*8-column grid\*\*.



Margins:



24 px



Gutters:



20 px



The layout should remain visually close to the desktop experience.



\---



\# Alignment Rules



Every major element should align to the grid.



Avoid:



Random offsets



Uneven spacing



Misaligned cards



Inconsistent padding



Visual alignment is more important than mathematical perfection when minor adjustments improve readability.



\---



\# Component Widths



Components should occupy logical column spans.



Examples:



Search Bar



6 columns



Austin Hero



12 columns



KPI Card



3 columns



Activity Panel



6 columns



District Card



4 columns



The same proportions should repeat consistently throughout the platform.



\---



\# White Space



Whitespace is intentional.



Do not fill empty space simply because it exists.



Breathing room improves comprehension.



\---



\# Figma Guidelines



Enable layout grids on every frame.



Use Auto Layout for all reusable components.



Snap elements to the defined grid.



Avoid manual pixel adjustments unless absolutely necessary.



\---



\# Engineering Guidelines



Frontend implementation should mirror the design grid.



Use responsive layout systems rather than fixed positioning.



Maintain consistent spacing tokens.



Avoid hard-coded dimensions where responsive values are appropriate.



\---



\# Grid Principles



The grid should be:



Invisible



Consistent



Flexible



Responsive



Scalable



Balanced



Professional



\---



\# Grid Statement



The Guava Grid System provides the invisible structure that gives every screen consistency and rhythm.



By aligning all interfaces to a common mathematical framework, Guava maintains a premium, enterprise-quality experience as the platform grows.



\---



\*\*Grid System\*\*



\*Precision beneath every pixel.\*

