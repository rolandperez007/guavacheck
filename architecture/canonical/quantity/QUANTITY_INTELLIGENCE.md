# Quantity Intelligence

## Purpose

Quantity Intelligence converts building elements and construction assemblies
into measurable quantities.

It is responsible for measurement.

It does not determine market prices and does not generate the final BOQ.

---

# Core Responsibility

Quantity Intelligence resolves:

Building Geometry
+
Assembly
+
Quantity Rule
→
Measured Quantity

---

# Measurement Types

Supported measurement concepts include:

- count
- length
- area
- volume
- weight
- capacity
- duration
- formula-derived quantity

---

# Quantity Identity

Every calculated quantity should contain:

- quantity_id
- project_id
- building_id
- element_id
- assembly_id
- component_id
- quantity
- unit
- raw_quantity
- waste_factor
- adjusted_quantity
- calculation_method
- source_geometry
- confidence
- version

---

# Geometry Inputs

Quantity Intelligence may consume:

- length
- width
- height
- thickness
- radius
- diameter
- perimeter
- surface area
- volume
- opening areas
- floor areas
- room dimensions
- element counts

---

# Quantity Rules

Quantity rules must be explicit.

Examples:

Area:
length × width

Volume:
length × width × thickness

Wall area:
wall length × wall height − openings

Linear quantity:
element length

Count:
number of elements

---

# Raw Quantity

Raw quantity represents the directly calculated quantity before
applicable waste or adjustment.

Raw quantity must remain auditable.

---

# Waste Adjustment

Adjusted quantity is derived from:

Raw Quantity
+
Applicable Waste Rule
→
Adjusted Quantity

Waste must be associated with its originating rule.

---

# Units

Canonical units must be normalized.

Typical units include:

- m
- m²
- m³
- kg
- tonne
- item
- set
- lot
- litre
- hour
- day

Unit conversion must be explicit and traceable.

---

# Quantity Validation

Quantity Intelligence should validate:

- missing dimensions
- impossible dimensions
- negative quantities
- incompatible units
- missing assembly
- missing quantity rule
- invalid geometry
- duplicate measurement
- unsupported measurement method

---

# Precision

Quantities must preserve sufficient precision internally.

Presentation rounding must occur at the presentation boundary.

The calculation engine must not prematurely round intermediate values.

---

# Provenance

Every quantity must be traceable to:

- source geometry
- source element
- assembly
- quantity rule
- calculation
- waste rule
- version

---

# Output Contract

Quantity Intelligence produces measurable quantity records.

These records become inputs to BOQ Intelligence.

---

# Canonical Ownership

Quantity Intelligence owns:

- measurement
- quantity calculation
- unit normalization
- waste application
- quantity validation

It does not own:

- construction assemblies
- market pricing
- currency conversion
- BOQ presentation
- commercial totals

---

# Canonical Flow

Building Element
↓
Assembly Component
↓
Quantity Rule
↓
Raw Quantity
↓
Waste Rule
↓
Adjusted Quantity
↓
BOQ Line Candidate
