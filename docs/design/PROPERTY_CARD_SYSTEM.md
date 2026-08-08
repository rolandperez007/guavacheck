\# Guava Property Card System



> The official specification for every property card within the Guava ecosystem.



\---



\# Overview



The Property Card is the primary visual representation of a property throughout the Guava platform.



Unlike traditional listing cards, the Guava Property Card combines marketplace information with verified intelligence, Austin insights, construction data, financing options, and ownership confidence.



Every property card should allow users to make informed decisions without immediately opening the full property page.



\---



\# Philosophy



Every property card should answer five questions immediately.



1\. What is this property?



2\. Where is it located?



3\. Can I trust it?



4\. What can I do with it?



5\. What does Austin think?



The user should understand these answers within seconds.



\---



\# Standard Layout



```

┌───────────────────────────────────┐



Property Image



Status Badges



Verification Badge



───────────────────────────────────



Property Title



Location



Price



Property Summary



───────────────────────────────────



Key Metrics



───────────────────────────────────



Austin Insight



───────────────────────────────────



Primary Actions



└───────────────────────────────────┘

```



Every variant follows this hierarchy.



\---



\# Property Image



Display:



Primary photo



Fallback image



Image carousel (optional)



360° indicator



Video indicator



Image quality should remain consistent across listings.



\---



\# Verification Indicators



Display:



Verified



Pending Verification



Passport Available



Ownership Confirmed



Survey Available



Government Data Connected



Verification indicators should remain highly visible.



\---



\# Property Title



Examples:



Luxury 5 Bedroom Detached Duplex



Commercial Office Building



Industrial Warehouse



Residential Land



Titles should remain concise.



\---



\# Location



Display:



Country



State



City



District



Neighbourhood



Street (when appropriate)



Support clickable maps.



\---



\# Price



Display:



Currency



Primary price



Alternative currency (optional)



Mortgage availability



Price history indicator



Austin valuation comparison (optional)



Support future multi-currency features.



\---



\# Property Summary



Display concise information.



Examples:



Bedrooms



Bathrooms



Land Area



Building Area



Parking



Floors



Property Type



Year Built



Construction Status



\---



\# Key Metrics



Examples:



Verification Score



Austin Confidence



Investment Rating



Rental Yield



ROI Estimate



Market Trend



Risk Level



These metrics should be immediately scannable.



\---



\# Austin Insight



Austin provides a concise summary.



Examples:



"This property appears fairly priced based on recent comparable sales."



"Planning approval documentation is still pending."



"Rental demand in this area has increased during the past year."



Austin insights should be:



Short



Actionable



Understandable



Expandable into the Austin Workspace.



\---



\# Confidence Score



Every verified property may display:



Overall Confidence



0–100%



Derived from:



Ownership



Documents



Government Records



Survey



Location



Construction



Historical Data



Confidence should be explained on demand.



\---



\# Status Badges



Examples:



New



Featured



Verified



Exclusive



Distressed



Auction



Mortgage Eligible



Price Reduced



Construction Ready



Investor Pick



Badges should use semantic colors only.



\---



\# Marketplace Indicators



Display where applicable:



Agency



Developer



Owner Listed



Bank Listed



Government Listed



Auction



Each source should be clearly identified.



\---



\# Property Timeline



Quick timeline preview:



Listed



↓



Verified



↓



Passport Generated



↓



Ownership Updated



↓



Recent Activity



Expand for full history.



\---



\# Primary Actions



Standard actions include:



View Property



Open Passport



Ask Austin



Verify



Mortgage



Estimate Construction



Share



Save



Compare



Primary actions should adapt to user permissions.



\---



\# Secondary Actions



Examples:



Print



Export PDF



Report Issue



Contact Agent



View Documents



Generate Report



\---



\# Comparison Mode



Cards should support comparison selection.



Display:



Selected state



Comparison badge



Maximum comparison limit



\---



\# Saved Properties



Support:



Bookmark



Collections



Favorites



Investment Watchlist



Saved cards synchronize across devices.



\---



\# Mortgage Summary



Where applicable display:



Estimated Monthly Payment



Interest Rate



Loan Duration



Down Payment



Bank Offers



Users should expand for detailed financing.



\---



\# Construction Summary



Construction-enabled properties display:



Estimated Build Cost



Estimated Timeline



BOQ Availability



Material Index



Austin Build Recommendation



\---



\# Documents



Quick indicators for:



Survey



Title



Deed



Passport



Planning Approval



Building Permit



Environmental Report



Users should immediately know document availability.



\---



\# Interactive Behaviour



Hover:



Soft elevation



Quick actions appear



Austin preview expands



Focus:



Visible outline



Keyboard support



Selection:



Comparison mode



Saved state



Action highlighting



\---



\# Card Variants



Small



Marketplace Grid



Medium



Search Results



Large



Featured Listings



Horizontal



Recommendation Lists



Compact



Mobile



Dashboard Widget



Austin Recommendation



All variants share the same visual language.



\---



\# Loading State



Display:



Skeleton Image



Skeleton Title



Skeleton Metrics



Skeleton Actions



Avoid layout shifts.



\---



\# Empty State



If property data is incomplete:



Explain missing information



Offer verification



Suggest Austin review



Provide reporting option



\---



\# Accessibility



Cards support:



Keyboard navigation



Screen readers



Focus indicators



Touch accessibility



Logical reading order



\---



\# Responsive Behaviour



Desktop



Three to four cards per row



Tablet



Two cards per row



Mobile



Single-column layout



Maintain consistent proportions.



\---



\# Motion



Use subtle animations for:



Hover



Save



Compare



Verification updates



Austin insight expansion



Never distract from property information.



\---



\# Design Tokens



Consume:



Typography Tokens



Spacing Tokens



Color Tokens



Elevation Tokens



Radius Tokens



Motion Tokens



No custom styling outside shared tokens.



\---



\# Figma



Every property card should exist as:



Published Component



Variants



Interactive States



Auto Layout



Variables



Responsive Constraints



Prototype Examples



\---



\# Engineering



Recommended React API



```tsx

<PropertyCard

&#x20;   property={property}

&#x20;   variant="marketplace"

&#x20;   verification

&#x20;   mortgage

&#x20;   construction

&#x20;   austin

/>

```



Supported options:



\- verification

\- passport

\- mortgage

\- construction

\- comparison

\- favorite

\- dashboard

\- recommendation



\---



\# Testing



Every Property Card requires:



Unit Tests



Accessibility Tests



Visual Regression



Performance Tests



Responsive Tests



Austin Integration Tests



Comparison Tests



\---



\# Future Expansion



The Property Card should evolve without changing its structure.



Future capabilities may include:



Live valuation



Drone imagery



Satellite overlays



Digital Twin preview



Construction simulation



Environmental scoring



Insurance scoring



Energy efficiency



Ownership graph



Austin predictive analytics



These should extend the existing component rather than replace it.



\---



\# Property Card Statement



The Guava Property Card transforms a traditional listing into a trusted intelligence object.



By combining verified data, financial context, construction insights, and Austin-powered recommendations, every property becomes more than an advertisement—it becomes a complete decision-making asset.



\---



\*\*Property Card System\*\*



\*Every property tells a verified story.\*

