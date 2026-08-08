\# Guava Form System



> The official specification for all forms and data entry experiences within the Guava platform.



\---



\# Overview



Forms are the primary mechanism through which users provide information to the Guava platform.



Every form should reduce friction, improve accuracy, and build user confidence.



Forms are not simply collections of fields—they are guided conversations between the user and the platform.



Austin serves as an intelligent assistant throughout this process.



\---



\# Design Philosophy



Every form should be:



Simple



Predictable



Progressive



Accessible



Forgiving



Recoverable



Professional



The platform should always help users complete forms rather than merely validate them.



\---



\# Form Architecture



Every form follows a consistent hierarchy.



```

Page Title



↓



Purpose



↓



Progress Indicator (optional)



↓



Sections



↓



Fields



↓



Validation



↓



Primary Action



↓



Secondary Actions



↓



Austin Assistance

```



This structure should remain consistent across all workflows.



\---



\# Form Types



\## Single-Page Form



Used for:



\- Login

\- Contact

\- Search

\- Quick Actions



\---



\## Multi-Step Wizard



Used for:



\- Property Registration

\- Property Passport

\- Mortgage Application

\- Investor Onboarding

\- Construction Projects



Users should complete one logical section at a time.



\---



\## Austin Guided Form



Austin actively assists users.



Capabilities include:



\- Field suggestions

\- Auto-completion

\- Error explanation

\- Contextual guidance

\- Follow-up questions



Austin should feel like a knowledgeable assistant, not an interruption.



\---



\# Form Sections



Large forms should be divided into meaningful sections.



Example:



Property Details



↓



Ownership



↓



Location



↓



Documents



↓



Verification



↓



Review



Avoid presenting excessively long, uninterrupted forms.



\---



\# Field Categories



Support the following field types:



\- Text

\- Number

\- Currency

\- Percentage

\- Date

\- Time

\- Phone

\- Email

\- URL

\- Password

\- Address

\- GPS Coordinates

\- Dropdown

\- Multi-select

\- Radio

\- Checkbox

\- Toggle

\- File Upload

\- Image Upload

\- Video Upload

\- Rich Text

\- Signature

\- Search

\- Tags



Field behavior should remain consistent across all modules.



\---



\# Labels



Every field must include:



Clear label



Optional helper text



Required indicator (if applicable)



Placeholder text should never replace labels.



\---



\# Validation



Validation should occur progressively.



Prefer inline validation over end-of-form validation.



Validation messages should explain:



\- What went wrong

\- Why

\- How to fix it



Never display vague messages such as:



"Invalid input."



\---



\# Required Fields



Clearly indicate required fields.



Minimize mandatory inputs.



Request only information that is genuinely necessary.



\---



\# Auto Save



Long forms should automatically save progress.



Users should never lose work because of:



Browser refresh



Connection issues



Timeouts



Unexpected closure



\---



\# Draft Recovery



If a draft exists:



Offer to restore it automatically.



Clearly display:



Last saved time



Progress



Resume option



\---



\# Conditional Logic



Fields should appear only when relevant.



Example:



Mortgage Type



↓



Fixed



↓



Show Interest Options



↓



Variable



↓



Show Rate Options



Conditional forms reduce cognitive load.



\---



\# Dynamic Forms



Austin may generate additional questions based on previous answers.



Generated fields should:



Appear naturally



Include explanations



Remain visually consistent



\---



\# File Uploads



Support:



Images



PDF



CAD files



Contracts



Certificates



Identity documents



Videos



Display:



Upload progress



Preview



File size



Status



Retry option



\---



\# Property Media



Support:



Multiple images



Floor plans



360° tours



Drone footage



Videos



Maintain consistent upload behaviour.



\---



\# Address Entry



Support:



Country



State



City



District



Street



Coordinates



Autocomplete should be available where supported.



\---



\# Currency Inputs



Display:



Currency symbol



Thousands separators



Consistent decimal precision



Support future multi-currency workflows.



\---



\# Measurement Inputs



Support:



Square metres



Square feet



Acres



Hectares



Metres



Feet



Unit conversion should be available where appropriate.



\---



\# Austin Assistance



Every major form should include:



Ask Austin



Explain this field



Suggest a value



Complete from documents



Review before submission



Austin should reduce effort, not add complexity.



\---



\# Progress Indicators



Multi-step forms should display:



Current step



Completed steps



Remaining steps



Estimated completion



Users should always know where they are.



\---



\# Review Screen



Before submission:



Summarize entered information.



Highlight missing or inconsistent values.



Allow editing without restarting the workflow.



\---



\# Error Handling



Errors should:



Be specific



Remain close to the relevant field



Suggest corrective action



Never erase valid user input.



\---



\# Success State



After successful submission:



Display confirmation



Summarize the completed action



Suggest logical next steps



Allow returning to previous records



\---



\# Accessibility



Forms must support:



Keyboard navigation



Logical tab order



Screen readers



Visible focus states



Error announcements



High contrast



Touch accessibility



\---



\# Mobile Behaviour



Use single-column layouts.



Large touch targets.



Sticky primary action buttons where appropriate.



Reduce typing through:



Dropdowns



Date pickers



Autocomplete



Austin suggestions



\---



\# Responsive Behaviour



Desktop



Multi-column sections.



Tablet



Two-column layouts where practical.



Mobile



Single-column flow.



Maintain consistent spacing across all breakpoints.



\---



\# Motion



Use subtle animations for:



Section transitions



Validation feedback



Progress updates



File uploads



Austin suggestions



Motion should improve understanding without slowing users down.



\---



\# Design Tokens



Forms consume:



Typography Tokens



Spacing Tokens



Color Tokens



Radius Tokens



Elevation Tokens



Motion Tokens



Never introduce isolated styling.



\---



\# Figma



Each form element should exist as:



Published component



Variants



Auto Layout



Variables



Interactive prototype



Validation examples



\---



\# Engineering



Recommended React API



```tsx

<Form

\&#x20; autoSave

\&#x20; validation="inline"

\&#x20; austinEnabled

\&#x20; multiStep

>

\&#x20; ...

</Form>

```



Supported capabilities:



\- Auto-save

\- Draft recovery

\- Validation

\- Conditional fields

\- File uploads

\- Austin assistance

\- Progress tracking



\---



\# Testing



Every form requires:



Unit tests



Accessibility tests



Validation tests



Responsive tests



Keyboard interaction tests



File upload tests



Auto-save tests



Draft recovery tests



\---



\# Usage Principles



A form should guide users toward success rather than test their patience.



Every interaction should reduce uncertainty.



Every validation message should teach.



Every completed form should leave users confident that their information has been captured correctly.



\---



\# Form System Statement



The Guava Form System transforms data entry into a guided, intelligent workflow.



By combining thoughtful design with Austin's assistance, forms become faster, more accurate, and significantly less intimidating, regardless of their complexity.



\---



\*\*Form System\*\*



\*From data entry to guided collaboration.\*

