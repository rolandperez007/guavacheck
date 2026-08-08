\# Guava Button System



> The official specification for all button components within the Guava platform.



\---



\# Overview



Buttons represent user intent.



Every primary action, confirmation, submission, navigation, and Austin interaction begins with a button.



Buttons should communicate importance through hierarchy rather than excessive visual styling.



The button system ensures consistency across every Guava product.



\---



\# Design Philosophy



Buttons should be:



Clear



Predictable



Accessible



Responsive



Consistent



Professional



The user should never hesitate before clicking a button.



\---



\# Button Hierarchy



The Guava platform uses six button levels.



\---



\## Primary Button



Purpose:



The single most important action on a page.



Examples:



Save



Continue



Verify Property



Generate Passport



Estimate Cost



Ask Austin



Only one primary button should dominate a section.



\---



\## Secondary Button



Supports the primary action.



Examples:



Cancel



Back



Preview



View Details



Secondary buttons should remain visually quieter.



\---



\## Tertiary Button



Low-emphasis actions.



Examples:



Learn More



View History



Export



Show Details



These buttons should use minimal visual weight.



\---



\## Ghost Button



Background-free button.



Used inside:



Cards



Tables



Dialogs



Menus



Austin replies



Ghost buttons should never compete with primary actions.



\---



\## Icon Button



Icon-only interaction.



Examples:



Search



Settings



Close



Refresh



Filter



Every icon button must include an accessible label.



\---



\## Destructive Button



Reserved for irreversible actions.



Examples:



Delete Property



Remove User



Archive Project



Reset Workspace



These buttons should use semantic error colors.



\---



\# Standard Sizes



Extra Small



32 px



Small



36 px



Medium



44 px



Large



52 px



Extra Large



60 px



The Medium button is the default.



\---



\# Width Behaviour



Buttons may be:



Auto width



Full width



Container width



Avoid arbitrary fixed widths.



\---



\# Padding



Medium Button



Horizontal:



24 px



Vertical:



12 px



Maintain generous click targets.



\---



\# Border Radius



Use the global radius token.



Buttons should align with cards and inputs.



\---



\# Typography



Font:



Inter Variable



Size:



16 px



Weight:



600



Sentence case only.



Avoid ALL CAPS.



\---



\# Icons



Icons should be:



20 px



Spacing:



8 px from text



Icons should reinforce actions without replacing labels.



\---



\# States



Every button supports:



Default



Hover



Focus



Pressed



Loading



Disabled



Success (optional)



Error (optional)



All state transitions should be smooth and subtle.



\---



\# Loading State



During processing:



Disable repeated clicks.



Replace text with a spinner when appropriate.



Preserve button width to prevent layout shifts.



\---



\# Disabled State



Disabled buttons should:



Reduce opacity.



Remain readable.



Clearly communicate that interaction is unavailable.



Never hide disabled actions entirely when users benefit from knowing they exist.



\---



\# Accessibility



Buttons must support:



Keyboard navigation



Visible focus rings



Screen readers



Minimum touch target of 44 × 44 px



Proper ARIA labels where required



\---



\# Austin Buttons



Austin-specific buttons include:



Ask Austin



Continue Conversation



Generate Report



Explain Result



Open Workspace



Suggested Action



These should follow the Primary or Secondary styles depending on context.



\---



\# Confirmation Actions



High-risk actions should request confirmation.



Examples:



Delete



Publish



Transfer Ownership



Submit Payment



Archive



Buttons alone should not trigger irreversible actions without confirmation.



\---



\# Responsive Behaviour



Desktop



Standard sizing.



Tablet



Maintain touch targets.



Mobile



Prefer full-width primary buttons where appropriate.



\---



\# Motion



Hover:



Subtle elevation or color transition.



Pressed:



Slight scale reduction or shadow adjustment.



Loading:



Smooth spinner animation.



Avoid distracting effects.



\---



\# Design Tokens



Buttons consume:



Color Tokens



Typography Tokens



Spacing Tokens



Radius Tokens



Shadow Tokens



Motion Tokens



No visual property should be hard-coded.



\---



\# Figma



Each button should exist as:



Published component



Variants



Auto Layout



Interactive states



Variables



Documented usage



\---



\# Engineering



Recommended React API



```tsx

<Button

&#x20; variant="primary"

&#x20; size="medium"

&#x20; loading={false}

&#x20; disabled={false}

&#x20; icon={<Search />}

>

&#x20; Search Properties

</Button>

```



Supported variants:



\- primary

\- secondary

\- tertiary

\- ghost

\- icon

\- destructive



Supported sizes:



\- xs

\- sm

\- md

\- lg

\- xl



\---



\# Testing



Every button should include:



Unit tests



Accessibility tests



Keyboard interaction tests



Loading state tests



Responsive tests



Visual regression tests



\---



\# Usage Principles



Buttons should always answer:



What happens if I click this?



If the answer is unclear, the button label should be improved.



\---



\# Button System Statement



The Guava Button System provides a consistent, accessible, and predictable interaction model across every product and workflow.



Buttons communicate action with clarity, allowing users to move confidently through the platform without hesitation.



\---



\*\*Button System\*\*



\*Every click should feel intentional.\*

