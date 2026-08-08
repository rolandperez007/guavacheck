# Canonical BOQ Intelligence

## Purpose

Define the canonical responsibility of the Bill of Quantities intelligence
layer.

The BOQ layer converts measurable construction information into an auditable
Bill of Quantities.

---

# BOQ Does Not Design the Building

The BOQ engine does not independently determine:

- architectural design
- district character
- room design
- structural design
- material preferences
- interior style
- construction methodology

Those decisions originate upstream.

---

# BOQ Input

The BOQ engine consumes:

- project
- site
- district
- building
- levels
- spaces
- building elements
- interior specifications
- construction assemblies
- quantity rules
- materials
- labour definitions
- equipment definitions
- regional pricing
- waste rules

---

# BOQ Processing

Building Element
→ Assembly
→ Component
→ Quantity Rule
→ Raw Quantity
→ Waste Adjustment
→ BOQ Quantity
→ Unit Rate
→ Line Amount

---

# BOQ Line Item

Every canonical BOQ line item should be capable of representing:

- id
- project_id
- building_id
- element_id
- assembly_id
- component_id
- material_id
- code
- description
- category
- specification
- quantity
- waste_factor
- adjusted_quantity
- unit
- unit_rate
- currency
- amount
- region
- source
- confidence
- version
- created_at
- updated_at

---

# Provenance

Every generated quantity should be traceable.

Example:

Room
→ Floor Finish
→ Assembly
→ Tile Component
→ Area Quantity
→ Waste Factor
→ BOQ Line

Austin must be able to explain where the number came from.

---

# Versioning

BOQs are versioned.

A change to:

- building geometry
- room dimensions
- interior specification
- assembly
- quantity rule
- material
- waste factor
- regional rate

must be capable of producing a new BOQ version.

Previous versions remain auditable.

---

# District Awareness

The BOQ engine may receive district-derived intelligence.

Example:

District
→ Luxury Finish Profile
→ Premium Flooring Assembly
→ Tile Quantity
→ BOQ

The BOQ engine itself should not contain hard-coded district-specific design
logic.

---

# Interior Awareness

Interior specifications resolve into assemblies.

Example:

Master Bedroom
→ Premium Floor Finish
→ Porcelain Tile Assembly
→ Floor Area × Tile Quantity Rule
→ BOQ

---

# Structural Awareness

Structural elements resolve through assemblies.

Example:

Column
→ Reinforced Concrete Column Assembly
→ Concrete
→ Reinforcement
→ Formwork
→ Labour
→ Equipment
→ BOQ

---

# Non-Goals

The BOQ engine should not become:

- a CAD engine
- an architectural design engine
- an interior style engine
- a district database
- a pricing database
- a rendering engine

It is the measurable commercial construction layer connecting those systems.