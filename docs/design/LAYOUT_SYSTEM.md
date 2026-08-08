\# Guava Layout System



> The structural foundation for every interface in the Guava platform.



\---



\# Overview



The Guava Layout System defines how every screen is organized.



It establishes a consistent page structure that remains recognizable regardless of which district, module, or workflow the user is currently using.



Layouts should communicate familiarity before functionality.



Users should immediately understand where navigation, content, actions, and Austin are located.



\---



\# Layout Philosophy



Every page follows one architectural structure.



Users should never need to learn a new interface simply because they entered another district.



Consistency creates confidence.



\---



\# Core Layout



```

\---------------------------------------------------------



Top Navigation



\---------------------------------------------------------



Sidebar | Main Workspace



&#x20;       |



&#x20;       |



&#x20;       |



&#x20;       |



&#x20;       |



\---------------------------------------------------------

```



Every desktop page follows this structure.



\---



\# Sidebar



Permanent.



Never overlaps content.



Contains:



\- Primary navigation

\- District navigation

\- User profile

\- Settings

\- Austin shortcut



The sidebar remains visually stable.



\---



\# Top Navigation



Reserved for:



\- Search

\- Notifications

\- User Account

\- Global Actions



Its height remains constant throughout the application.



\---



\# Main Workspace



The workspace contains page-specific content.



Typical hierarchy:



Page Title



↓



Description



↓



Primary Actions



↓



Dashboard Widgets



↓



Supporting Panels



↓



Footer



No component should appear outside this hierarchy without strong justification.



\---



\# Dashboard Layout



The dashboard is unique.



It contains:



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



Partner Section



↓



Footer



This arrangement should remain stable.



\---



\# District Pages



Every district follows the same layout.



Header



↓



Summary



↓



Primary Tools



↓



Data



↓



Related Austin Actions



↓



History



↓



Footer



Users should recognise the structure immediately.



\---



\# Workspace Layout



When Austin Workspace opens:



Dashboard remains visible.



Workspace slides from the right.



Workspace width:



420–480 px



Resizable in future versions.



\---



\# Card Layout



Every card follows:



Header



↓



Content



↓



Actions



↓



Status



Cards should never become visually crowded.



\---



\# Forms



Forms should always follow:



Title



↓



Description



↓



Fields



↓



Validation



↓



Primary Action



↓



Secondary Actions



Users should never guess the next step.



\---



\# Tables



Tables should contain:



Header



↓



Filters



↓



Data



↓



Pagination



↓



Actions



Maintain consistent spacing throughout.



\---



\# Empty States



Every empty page should provide:



Explanation



↓



Illustration



↓



Suggested Action



↓



Austin Assistance



Never present a blank interface.



\---



\# Responsive Behaviour



Desktop



Sidebar visible.



Tablet



Collapsible sidebar.



Mobile



Bottom navigation.



Austin becomes full-screen when expanded.



The overall hierarchy remains identical.



\---



\# Visual Rhythm



Maintain generous whitespace.



Avoid crowded layouts.



Use consistent vertical spacing.



Users should feel relaxed rather than overwhelmed.



\---



\# Layout Principles



Every page should be:



Predictable



Balanced



Calm



Structured



Scalable



Professional



\---



\# Layout Statement



Guava's layout system creates a consistent workspace where users always know where information lives, regardless of the feature they are using.



The layout should disappear into the background, allowing users to focus entirely on their work.



\---



\*\*Layout System\*\*



\*A consistent structure for every experience.\*

