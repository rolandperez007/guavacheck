\# Guava Card System



> The official specification for all card components within the Guava platform.



\---



\# Overview



Cards are the primary content containers throughout Guava.



Every major feature is presented through cards that organize information into clear, digestible sections.



Cards create hierarchy, improve scanning, and establish a predictable visual rhythm across the platform.



A user should immediately recognize a Guava card regardless of where it appears.



\---



\# Design Philosophy



Cards should feel:



Professional



Lightweight



Organized



Elegant



Trustworthy



Spacious



Cards separate information without isolating it.



They should never feel like floating boxes.



\---



\# Card Architecture



Every card follows the same structure.



```

┌──────────────────────────────┐



Header



\------------------------------



Body



\------------------------------



Supporting Content



\------------------------------



Actions



└──────────────────────────────┘

```



Not every card requires every section, but the hierarchy remains consistent.



\---



\# Card Types



The platform uses several standard card categories.



\---



\## Information Card



Displays static information.



Examples:



Property Summary



User Profile



Mortgage Overview



Construction Overview



\---



\## Action Card



Encourages a specific action.



Examples:



Verify Property



Estimate Cost



Generate Passport



Continue Project



\---



\## Metric Card



Displays a single KPI.



Examples:



Total Listings



Portfolio Value



Construction Progress



Mortgage Balance



Verification Status



Metric cards should emphasize the number rather than supporting text.



\---



\## Dashboard Widget



Interactive dashboard component.



Examples:



Market Trends



Recent Activity



Notifications



Austin Suggestions



Calendar



Widgets are movable in future versions.



\---



\## Property Card



Displays:



Photo



Address



Price



Features



Status



Verification



Primary CTA



Property cards should remain visually consistent regardless of listing source.



\---



\## Austin Recommendation Card



Contains:



Austin insight



Reasoning summary



Confidence indicator



Suggested action



Expand explanation



Ask follow-up



These cards should clearly communicate AI-generated recommendations.



\---



\## Report Card



Displays report summaries.



Examples:



Verification Report



Mortgage Report



Construction Estimate



Investment Analysis



Each report card links to a detailed workspace.



\---



\## Notification Card



Displays:



Status



Priority



Timestamp



Action



Notifications should be immediately actionable.



\---



\# Header



A card header may contain:



Title



Subtitle



Status Badge



Menu



Avatar



Icon



Timestamp



Headers establish context without overwhelming the content.



\---



\# Body



The body contains the primary information.



Maintain generous spacing.



Avoid long uninterrupted paragraphs.



Prefer lists where appropriate.



\---



\# Footer



The footer contains:



Actions



Links



Metadata



Secondary information



Footers should not compete with the body.



\---



\# Padding



Default:



24 px



Compact:



16 px



Large:



32 px



Padding should remain consistent throughout the platform.



\---



\# Border Radius



Use the global radius token.



Cards should visually align with:



Buttons



Inputs



Dialogs



Tables



\---



\# Elevation



Cards should use subtle elevation.



Prefer soft shadows over strong borders.



Elevation communicates hierarchy, not decoration.



\---



\# Borders



Default:



Light border token.



Avoid heavy outlines.



Use borders only when necessary for separation.



\---



\# Card Width



Cards should remain responsive.



Avoid fixed widths unless required by the layout.



Use the Grid System for alignment.



\---



\# Card Heights



Cards within the same collection should maintain equal heights whenever practical.



Consistent height improves scanability.



\---



\# Images



Property cards should maintain a consistent aspect ratio.



Images should never distort.



Rounded corners should match the card radius.



\---



\# Typography



Use typography tokens.



Typical structure:



Title



↓



Subtitle



↓



Body



↓



Metadata



↓



Actions



Avoid introducing custom font styles.



\---



\# Interactive Cards



Clickable cards should:



Display hover feedback.



Maintain keyboard accessibility.



Provide clear focus indicators.



Never hide primary actions.



\---



\# Card States



Every interactive card supports:



Default



Hover



Focus



Selected



Loading



Disabled



Empty



Error



Success



State changes should remain subtle.



\---



\# Loading Cards



Loading cards use skeleton placeholders.



Maintain final layout dimensions to prevent layout shifts.



\---



\# Empty Cards



Empty cards should contain:



Illustration



Title



Description



Primary action



Austin suggestion



Never leave empty containers unexplained.



\---



\# Error Cards



Display:



Problem summary



Explanation



Suggested action



Retry option



Austin assistance (where appropriate)



\---



\# Austin Integration



Austin may appear within cards as:



Recommendations



Insights



Warnings



Summaries



Suggested actions



Austin should complement the content rather than dominate it.



\---



\# Dashboard Cards



Dashboard cards should be concise.



One primary objective per card.



Avoid combining unrelated information.



\---



\# Accessibility



Cards must support:



Keyboard navigation



Screen readers



Logical focus order



Visible focus indicators



Sufficient contrast



\---



\# Responsive Behaviour



Desktop



Multi-column layouts.



Tablet



Two-column layouts where appropriate.



Mobile



Single-column stacking.



Maintain readable spacing across breakpoints.



\---



\# Motion



Hover:



Soft elevation.



Selection:



Border or accent change.



Loading:



Skeleton animation.



Expansion:



Smooth height transition.



Avoid exaggerated motion.



\---



\# Design Tokens



Cards consume:



Color Tokens



Typography Tokens



Spacing Tokens



Radius Tokens



Elevation Tokens



Motion Tokens



No visual values should be hard-coded.



\---



\# Figma



Each card should exist as:



Published component



Variants



Auto Layout



Variables



Responsive constraints



Interactive prototype



\---



\# Engineering



Recommended React API



```tsx

<Card

&#x20; variant="property"

&#x20; interactive

&#x20; loading={false}

>

&#x20; ...

</Card>

```



Supported variants include:



\- information

\- action

\- metric

\- property

\- dashboard

\- report

\- notification

\- austin



\---



\# Testing



Each card requires:



Unit tests



Accessibility tests



Visual regression tests



Responsive tests



Interaction tests



Performance tests



\---



\# Usage Principles



Each card should communicate one primary idea.



If a card attempts to solve multiple unrelated problems, it should be divided into separate cards.



\---



\# Card System Statement



Cards are the structural building blocks of the Guava interface.



By providing a consistent container for information and actions, the Card System creates a calm, organized, and scalable experience across every district, dashboard, and Austin-powered workflow.



\---



\*\*Card System\*\*



\*Organizing complexity into clarity.\*

