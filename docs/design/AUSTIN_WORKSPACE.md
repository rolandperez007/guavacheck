\# Austin Workspace



> The official specification for the Austin Workspace throughout the Guava ecosystem.



\---



\# Overview



The Austin Workspace is Guava's persistent AI collaboration environment.



Users begin interacting with Austin naturally from the Guava City dashboard and may expand the conversation into a dedicated workspace whenever deeper analysis or longer tasks are required.



The workspace is not a chat window.



It is a professional environment where users collaborate with Austin on property intelligence, construction planning, verification, financial analysis, document review, and strategic decision-making.



Austin remembers the active task throughout the session, allowing users to move across different parts of the platform without losing context.



\---



\# Design Philosophy



Austin should feel like:



Knowledgeable



Professional



Calm



Trustworthy



Proactive



Transparent



Austin should guide work without dominating it.



The platform remains user-driven.



\---



\# Entry Points



Users may open Austin from:



Dashboard City Scene



Property Card



Property Passport



Map View



Construction Workspace



Mortgage Workspace



Investor Dashboard



Verification Workspace



Analytics



Global Search



Keyboard Shortcut



Notification Center



Every entry point connects to the same persistent workspace.



\---



\# Dashboard Experience



The Guava City dashboard is the primary introduction to Austin.



Austin appears as an active presence within the city.



Examples:



• Floating assistant



• Animated office



• Interactive AI hub



• City beacon



Selecting Austin opens a lightweight conversation directly on the dashboard.



Users may ask questions immediately without leaving their current view.



\---



\# Conversation Modes



Austin supports multiple modes.



\## Quick Conversation



Small overlay.



Fast questions.



Fast answers.



No interruption.



Ideal for:



Search



Navigation



Clarification



Recommendations



Definitions



\---



\## Docked Sidebar



The conversation expands into a persistent right-hand sidebar.



The user may continue working elsewhere while Austin remains available.



The sidebar supports:



Scrolling history



Suggested actions



Pinned responses



File references



Task progress



\---



\## Full Workspace



For complex work.



The workspace becomes a dedicated productivity environment.



Suitable for:



Property Verification



Construction Planning



Investment Analysis



Mortgage Modeling



Passport Generation



Document Review



Government Record Analysis



Large Reports



Long-running AI tasks



\---



\# Workspace Layout



```

+------------------------------------------------------+



Toolbar



\--------------------------------------------------------



Conversation



\--------------------------------------------------------



Austin Reasoning



\--------------------------------------------------------



Documents



\--------------------------------------------------------



Suggested Actions



\--------------------------------------------------------



Task Timeline



\--------------------------------------------------------



Status



+------------------------------------------------------+

```



Panels may be collapsed or resized.



\---



\# Persistent Context



Austin maintains:



Current property



Selected map location



Active passport



Construction project



Mortgage scenario



Uploaded documents



Open reports



Conversation history



Users should never need to repeat information unnecessarily during the same session.



\---



\# Conversation Features



Support:



Markdown



Tables



Charts



Property Cards



Maps



Images



Documents



Code (internal tools)



References



Pinned messages



Message editing



Conversation search



Message export



\---



\# Suggested Actions



Austin continuously proposes relevant next steps.



Examples:



Verify ownership



Generate Property Passport



Estimate construction cost



Compare nearby properties



Request mortgage options



Review uploaded survey



Open map



Create report



Suggestions should remain optional.



\---



\# Task Management



Austin can manage long-running activities.



Each task displays:



Status



Progress



Estimated completion



Dependencies



Output



Completion notification



Users may continue using Guava while tasks execute.



\---



\# Multi-Document Analysis



Users may upload multiple documents simultaneously.



Examples:



Survey Plan



Certificate of Occupancy



Building Plan



Title Document



Engineering Report



Valuation



Austin compares documents, identifies inconsistencies, and summarizes findings.



\---



\# Workspace Tabs



Support multiple concurrent workspaces.



Examples:



Property Verification



↓



Construction Estimate



↓



Mortgage Comparison



↓



Investor Report



↓



Return to Verification



without losing progress.



\---



\# Austin Memory



Within the active workspace Austin remembers:



Recent instructions



Current objectives



Referenced documents



Generated reports



Reasoning chain



Pinned decisions



This memory is session-based unless explicitly saved by the user.



\---



\# Explainability



Austin should explain conclusions.



Users may ask:



Why?



Show reasoning.



Show assumptions.



Show references.



Compare alternatives.



Confidence should always be visible where appropriate.



\---



\# Collaboration



Future capability.



Users may invite collaborators.



Examples:



Estate Agents



Surveyors



Lawyers



Banks



Developers



Government Officials



Shared workspaces preserve comments and task history.



\---



\# Notifications



Austin informs users when:



Tasks complete



Reports finish



Verification changes



New government records appear



Construction milestones update



Mortgage offers change



Notifications should link directly back into the workspace.



\---



\# Search



Workspace search includes:



Messages



Documents



Reports



Generated content



Properties



Tasks



References



Austin suggestions



\---



\# Responsive Behaviour



Desktop



Persistent sidebar



Docked panels



Multiple tabs



Tablet



Reduced panels



Collapsible workspace



Mobile



Bottom sheet



Expandable conversation



Task view



Document preview



Conversation continuity should remain intact.



\---



\# Accessibility



Support:



Keyboard navigation



Screen readers



Logical focus



High contrast



Reduced motion



Voice input (future)



Touch accessibility



\---



\# Motion



Use subtle transitions for:



Opening workspace



Docking



Panel resizing



Task completion



Austin suggestions



Avoid excessive animation.



\---



\# Design Tokens



The workspace consumes:



Typography Tokens



Spacing Tokens



Color Tokens



Elevation Tokens



Radius Tokens



Motion Tokens



No isolated styling is permitted.



\---



\# Figma



Provide reusable components for:



Conversation



Message Bubble



Suggested Action



Task Card



Document Panel



Reasoning Panel



Timeline



Workspace Toolbar



Dock Button



Expand Button



Status Indicator



Austin Presence



All components should support Auto Layout, Variables, and Interactive Variants.



\---



\# Engineering



Recommended React API



```tsx

<AustinWorkspace

&#x20;   mode="sidebar"

&#x20;   context={activeContext}

&#x20;   documents={documents}

&#x20;   tasks={tasks}

&#x20;   conversation={conversation}

&#x20;   persistent

/>

```



Capabilities include:



\- Persistent conversations

\- Docking

\- Expand / Collapse

\- Document analysis

\- Property intelligence

\- Map integration

\- Report generation

\- Task management

\- Session context

\- Suggested actions



\---



\# Testing



The workspace requires:



Unit Tests



Accessibility Tests



Conversation Tests



Document Upload Tests



Task Management Tests



Persistence Tests



Responsive Tests



Performance Tests



Austin Integration Tests



Multi-tab Tests



\---



\# Integration Points



Austin Workspace integrates directly with:



Dashboard



Global Search



Property Cards



Property Passport



Map System



Construction Engine



Mortgage Engine



Verification Engine



Investor Engine



Analytics



World Engine



ACOS Runtime



Austin Tower



This is the primary orchestration interface for AI-powered workflows.



\---



\# Guiding Principles



Austin should always:



Reduce effort



Increase understanding



Preserve user control



Explain recommendations



Maintain context



Support long-running work



Respect transparency



The user remains the decision-maker.



\---



\# Austin Workspace Statement



The Austin Workspace is the cognitive center of the Guava platform.



It transforms AI from a simple conversational assistant into a persistent professional collaborator capable of reasoning across properties, documents, maps, construction, finance, and verification while maintaining continuity throughout the user's workflow.



\---



\*\*Austin Workspace\*\*



\*One conversation. One workspace. Every decision supported.\*

