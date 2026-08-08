\# Guava Input System



> The official specification for all input components within the Guava platform.



\---



\# Overview



Input components are the primary interface between users and the Guava platform.



Every search, property registration, mortgage application, construction estimate, Austin conversation, and verification workflow begins with an input.



Inputs should feel intelligent, forgiving, and responsive.



Austin should enhance data entry rather than interrupt it.



\---



\# Design Philosophy



Inputs should be:



Clear



Fast



Accessible



Predictable



Helpful



Intelligent



Consistent



Users should always understand:



• what is expected



• what has been entered



• whether the value is valid



• how to fix mistakes



\---



\# Input Architecture



Every input follows the same structure.



```

Label



↓



Helper Text



↓



Input Field



↓



Validation Message



↓



Austin Suggestions (optional)

```



\---



\# Supported Input Types



The platform supports:



Text



Email



Password



Phone



Search



Address



Country



State



City



GPS Coordinates



Currency



Percentage



Number



Measurement



Date



Time



Date Range



Dropdown



Autocomplete



Tags



Rich Text



Textarea



Checkbox



Switch



Radio



Slider



Rating



Color Picker (future)



File Upload



Image Upload



Video Upload



CAD Upload



Document Upload



Signature



Voice Input (future)



Austin Prompt Input



\---



\# Standard Heights



Small



36 px



Medium



44 px



Large



52 px



Extra Large



60 px



Medium is the default.



\---



\# Width Behaviour



Inputs should support:



Auto width



Container width



Full width



Responsive resizing



Never rely on fixed widths.



\---



\# Labels



Every field requires a permanent label.



Placeholder text is supplementary.



Never use placeholder text as the only field identifier.



\---



\# Helper Text



Helper text explains:



Expected format



Examples



Constraints



Units



Austin recommendations



Helper text should remain concise.



\---



\# Placeholder Text



Placeholder text demonstrates examples.



Example:



```

Enter property address

```



Avoid vague placeholders.



\---



\# Validation



Validation should occur progressively.



Display success and error states inline.



Every validation message should explain:



What happened



Why



How to correct it



\---



\# Input States



Every input supports:



Default



Hover



Focus



Typing



Filled



Success



Warning



Error



Disabled



Read Only



Loading



These states should be visually distinct while remaining subtle.



\---



\# Search Inputs



Search fields should support:



Instant suggestions



Recent searches



Saved searches



Austin suggestions



Voice search (future)



Global search



Search is a core feature of Guava.



\---



\# Austin Smart Inputs



Austin-enabled inputs may provide:



Auto-completion



Field prediction



Suggested values



Document extraction



Context awareness



Error explanation



Natural language input



Austin suggestions should appear below the active field without disrupting layout.



\---



\# Currency Inputs



Display:



Currency symbol



Thousands separators



Optional decimals



Negative values (where appropriate)



Future multi-currency support is required.



\---



\# Measurement Inputs



Support:



Square Metres



Square Feet



Acres



Hectares



Metres



Feet



Miles



Kilometres



Conversions should be available where appropriate.



\---



\# Address Inputs



Support:



Country



State



City



District



Street



Building Number



Postal Code



Coordinates



Map Selection



Autocomplete should reduce typing whenever possible.



\---



\# Property Search Input



Support:



Natural language



Structured filters



Austin suggestions



Location lookup



Recent searches



Examples:



```

3-bedroom duplex in Lekki under ₦250M



Commercial land in Victoria Island



Verified apartments with mortgage

```



Austin should understand conversational queries.



\---



\# Password Inputs



Support:



Show / Hide



Strength indicator



Requirements



Confirmation



Password managers



\---



\# Upload Inputs



Support:



Images



Videos



PDF



CAD



DWG



DOCX



XLSX



ZIP



Display:



Preview



Upload progress



Retry



Replace



Remove



Status



\---



\# Read Only Inputs



Read-only fields should remain selectable for copying.



Avoid making them appear disabled.



\---



\# Accessibility



Inputs must support:



Keyboard navigation



Logical tab order



Visible focus



Screen readers



ARIA attributes



Touch accessibility



High contrast



\---



\# Mobile Behaviour



Use:



Large touch targets



Native keyboards



Autocomplete



Appropriate input modes



Date pickers



Austin suggestions



Reduce unnecessary typing.



\---



\# Motion



Animations should support:



Focus



Validation



Suggestions



Autocomplete



Uploads



Never distract from the task.



\---



\# Typography



Use the Typography System.



Input text:



16 px



Weight:



400



Labels:



14 px



Weight:



500



Validation:



13 px



Weight:



400–500



\---



\# Design Tokens



Inputs consume:



Color Tokens



Spacing Tokens



Typography Tokens



Radius Tokens



Elevation Tokens



Motion Tokens



\---



\# Figma



Every input should exist as:



Published component



Variants



Interactive states



Auto Layout



Variables



Validation examples



Austin-enabled examples



\---



\# Engineering



Recommended React API



```tsx

<Input

&#x20;   type="text"

&#x20;   label="Property Address"

&#x20;   helperText="Start typing to search"

&#x20;   austinEnabled

&#x20;   validation="inline"

/>

```



Supported properties include:



\- type

\- size

\- disabled

\- readOnly

\- required

\- placeholder

\- helperText

\- validation

\- icon

\- prefix

\- suffix

\- autocomplete

\- austinEnabled



\---



\# Testing



Every input requires:



Unit tests



Accessibility tests



Validation tests



Autocomplete tests



Responsive tests



Keyboard tests



Upload tests



Austin suggestion tests



\---



\# Usage Principles



Inputs should minimize effort while maximizing accuracy.



Typing should never feel like unnecessary work.



Whenever possible, Austin should reduce manual data entry through intelligent assistance.



\---



\# Input System Statement



The Guava Input System transforms data entry into an intelligent interaction.



By combining clear design, progressive validation, and Austin-assisted completion, every input becomes faster, more accurate, and easier to use across the entire platform.



\---



\*\*Input System\*\*



\*Every field is an opportunity to reduce effort.\*

