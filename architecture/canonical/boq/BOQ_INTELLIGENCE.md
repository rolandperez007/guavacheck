# BOQ Intelligence

## Purpose

BOQ Intelligence converts verified quantities and construction intelligence
into an auditable Bill of Quantities.

The BOQ engine is an orchestration and commercial-structure layer.

It must not invent construction knowledge.

---

# Core Responsibility

BOQ Intelligence resolves:

Project
+
Building Elements
+
Assemblies
+
Quantities
+
Pricing
→
Auditable BOQ

---

# BOQ Pipeline

Building Model
→
Elements
→
Assemblies
→
Quantity Intelligence
→
BOQ Line Candidates
→
Pricing Intelligence
→
BOQ Lines
→
Estimate

---

# BOQ Line Identity

Every BOQ line should contain:

- boq_line_id
- project_id
- building_id
- element_id
- assembly_id
- component_id
- material_id
- code
- description
- specification
- quantity
- unit
- waste_factor
- adjusted_quantity
- unit_rate
- amount
- currency
- region
- pricing_source
- quantity_source
- confidence
- version

---

# BOQ Sections

A BOQ may be organized into:

- preliminaries
- site preparation
- earthworks
- foundations
- structural frame
- floors
- walls
- roofs
- doors
- windows
- finishes
- ceilings
- painting
- plumbing
- electrical
- HVAC
- fire protection
- security
- external works
- landscaping
- specialist works

The section structure must remain extensible.

---

# BOQ Generation

BOQ Intelligence consumes:

- building elements
- selected assemblies
- calculated quantities
- applicable specifications
- pricing results

It should not independently calculate construction knowledge that belongs
to the upstream domains.

---

# Pricing Boundary

BOQ Intelligence requests pricing from Pricing Intelligence.

Pricing Intelligence determines:

- material rate
- labour rate
- equipment rate
- contractor rate
- regional adjustment
- market adjustment
- currency
- taxes
- escalation

BOQ Intelligence consumes those results.

---

# Amount Calculation

A BOQ amount is derived from:

Adjusted Quantity
×
Applicable Unit Rate

The source quantity and source price must remain independently auditable.

---

# Currency

Each BOQ must define:

- project currency
- pricing currency
- exchange rate
- exchange-rate source
- exchange-rate timestamp
- conversion version

Currency conversion must not overwrite the original pricing source.

---

# Confidence

BOQ lines should carry confidence information.

Confidence may reflect:

- geometry confidence
- assembly confidence
- quantity confidence
- pricing confidence
- source confidence

The final BOQ confidence must remain explainable.

---

# Provenance

Every BOQ line must be traceable to:

District Context
→
Building Element
→
Interior Specification
→
Assembly
→
Component
→
Quantity Rule
→
Calculated Quantity
→
Pricing Source
→
Unit Rate
→
BOQ Line

---

# Versioning

BOQs must support versions.

A new version may result from:

- geometry changes
- design changes
- assembly changes
- quantity changes
- pricing changes
- district-rule changes
- currency changes
- user edits

Previous versions must remain identifiable.

---

# User Editing

Users may edit BOQ values where permitted.

Editable values must preserve:

- original value
- edited value
- editor
- timestamp
- reason
- version

AI-generated values must never silently become indistinguishable from
human-entered values.

---

# Audit Trail

The BOQ must be capable of answering:

- Why does this line exist?
- Which building element created it?
- Which assembly created it?
- How was the quantity calculated?
- Which waste rule was applied?
- Where did the unit rate come from?
- Which currency was used?
- Which version generated the line?
- Was the value generated or manually edited?

---

# Canonical Ownership

BOQ Intelligence owns:

- BOQ structure
- line-item orchestration
- BOQ grouping
- BOQ versioning
- BOQ editing
- BOQ audit trail
- BOQ export representation

It does not own:

- district rules
- room design
- assembly definitions
- quantity algorithms
- market price databases

---

# Critical Principle

The BOQ engine must never become a hidden construction knowledge database.

Construction knowledge belongs upstream.

BOQ Intelligence consumes that knowledge and makes it commercially
measurable and auditable.

---

# Canonical Flow

District
+
Building
+
Interior
+
Assembly
+
Quantity
+
Pricing
↓
BOQ
↓
Estimate
