\# Guava Table System



> The official specification for all tabular data interfaces within the Guava platform.



\---



\# Overview



Tables present structured information throughout the Guava ecosystem.



They power:



\- Property Listings

\- Property Passports

\- Verification Records

\- Construction Estimates

\- Mortgage Applications

\- Investment Portfolios

\- Analytics

\- Government Records

\- Financial Reports

\- Austin Intelligence Results



Tables are not spreadsheets.



They are intelligent workspaces.



\---



\# Design Philosophy



Every table should be:



Readable



Fast



Searchable



Filterable



Accessible



Responsive



Scalable



Intelligent



Users should never feel overwhelmed regardless of dataset size.



\---



\# Table Structure



Every table follows a consistent structure.



Toolbar



↓



Search



↓



Filters



↓



Bulk Actions



↓



Column Controls



↓



Table



↓



Pagination



↓



Austin Insights



\---



\# Table Components



Every table contains:



Header



Rows



Columns



Actions



Selection



Status



Pagination



Summary



Austin Assistant



\---



\# Toolbar



The toolbar may contain:



Global Search



Saved Views



Filters



Export



Import



Refresh



Bulk Actions



Column Visibility



Austin Analysis



Toolbar actions should remain consistent across all modules.



\---



\# Columns



Columns should support:



Sorting



Resizing



Reordering



Visibility



Pinning



Grouping (future)



Every column should have a clear label.



\---



\# Row Selection



Support:



Single Select



Multi Select



Select Page



Select All



Clear Selection



Selected rows should expose contextual bulk actions.



\---



\# Bulk Actions



Examples:



Verify



Archive



Export



Assign



Delete



Share



Generate Report



Generate Passport



Austin Analysis



Bulk actions should appear only when relevant.



\---



\# Search



Every table should include:



Instant search



Natural language search



Austin-assisted search



Recent searches



Saved searches



Search should work across multiple columns where appropriate.



\---



\# Filters



Support:



Dropdown



Checkbox



Date Range



Status



Price



Location



Country



State



City



Property Type



Verification Status



Construction Stage



Investment Score



Mortgage Status



Filters should be combinable.



\---



\# Sorting



Columns support:



Ascending



Descending



Default



Multi-column sorting (future)



Sorting should remain stable and predictable.



\---



\# Pagination



Support:



10



25



50



100



250



500



rows per page.



Large datasets should support virtual scrolling.



\---



\# Virtualization



Very large datasets should render only visible rows.



This keeps scrolling smooth regardless of dataset size.



\---



\# Sticky Elements



Support:



Sticky Header



Sticky First Column



Sticky Action Column



This improves navigation across large datasets.



\---



\# Row Expansion



Expandable rows may reveal:



Property Summary



Timeline



Verification



Austin Notes



Construction Progress



Mortgage Details



Documents



Expansion should preserve table context.



\---



\# Status Badges



Common statuses include:



Verified



Pending



Draft



Archived



Rejected



Processing



Completed



Badges should use semantic colors.



\---



\# Property Tables



Property tables typically display:



Photo



Address



Price



Bedrooms



Bathrooms



Land Size



Owner



Verification



Passport



Status



Actions



Layouts should remain consistent across datasets.



\---



\# Financial Tables



Support:



Currency formatting



Negative values



Totals



Subtotals



Percentage changes



Trend indicators



Tabular numerals should always be used.



\---



\# Construction Tables



Support:



Material



Quantity



Unit Cost



Labour



Equipment



Supplier



Total Cost



Variance



Austin Recommendations



\---



\# Government Tables



Support:



Parcel Number



Ownership



Planning



Utilities



Survey



Title



Verification



Restrictions



Historical Records



\---



\# Austin Integration



Austin should enhance every table.



Capabilities include:



Summarize Results



Find Anomalies



Explain Trends



Suggest Filters



Generate Reports



Compare Records



Identify Missing Data



Austin appears as a contextual assistant rather than replacing the table.



\---



\# Empty State



When no records exist:



Illustration



↓



Explanation



↓



Suggested Action



↓



Austin Recommendation



Never display an empty table without guidance.



\---



\# Loading State



Use:



Skeleton Rows



Progress Indicator



Estimated Completion (where applicable)



Avoid layout shifts.



\---



\# Error State



Display:



Problem



Cause



Retry



Austin Help



Errors should preserve user context.



\---



\# Responsive Behaviour



Desktop



Full table



Tablet



Reduced columns



Horizontal scrolling where necessary



Mobile



Stacked row cards



Priority columns only



Maintain functionality across all devices.



\---



\# Accessibility



Tables must support:



Keyboard navigation



Screen readers



Focus management



High contrast



ARIA roles



Logical reading order



\---



\# Motion



Animations should support:



Sorting



Filtering



Loading



Expansion



Selection



Bulk actions



Motion should improve comprehension.



\---



\# Design Tokens



Tables consume:



Typography Tokens



Spacing Tokens



Color Tokens



Elevation Tokens



Radius Tokens



Motion Tokens



Never use isolated styling.



\---



\# Figma



Tables should exist as reusable components.



Variants include:



Compact



Comfortable



Dense



Selectable



Expandable



Loading



Empty



Error



Published with Auto Layout and Variables.



\---



\# Engineering



Recommended React API



```tsx

<DataTable

&#x20;   columns={columns}

&#x20;   rows={rows}

&#x20;   searchable

&#x20;   filterable

&#x20;   sortable

&#x20;   selectable

&#x20;   pagination

&#x20;   virtualized

&#x20;   austinEnabled

/>

```



Supported features:



\- Search

\- Filters

\- Sorting

\- Selection

\- Export

\- Import

\- Pagination

\- Virtualization

\- Austin Insights

\- Responsive Layout



\---



\# Testing



Every table requires:



Unit Tests



Accessibility Tests



Sorting Tests



Filtering Tests



Pagination Tests



Virtualization Tests



Performance Tests



Responsive Tests



Austin Integration Tests



\---



\# Usage Principles



Tables should help users discover information rather than merely display it.



Austin should augment analysis, not replace structured data.



Users should always feel in control regardless of dataset size.



\---



\# Table System Statement



The Guava Table System transforms structured data into intelligent workspaces.



By combining enterprise-grade interaction patterns with Austin-powered analysis, tables become powerful decision-making environments for property professionals, financial institutions, governments, and investors.



\---



\*\*Table System\*\*



\*Turning records into intelligence.\*

