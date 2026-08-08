# Construction Assembly Intelligence

## Purpose

Construction Assembly Intelligence converts design intent into repeatable,
measurable construction systems.

Assemblies are the bridge between spatial/design intelligence and
quantity/BOQ intelligence.

---

# Core Responsibility

Assembly Intelligence resolves:

Design Element
→ Assembly
→ Components
→ Materials
→ Labour
→ Equipment
→ Quantity Rules
→ Waste Rules

---

# Assembly Identity

Every assembly should have:

- assembly_id
- assembly_code
- name
- description
- category
- version
- status
- applicable_regions
- quality_tier
- applicable_standards

---

# Assembly Categories

Assemblies may include:

- site works
- earthworks
- foundations
- reinforced concrete
- structural steel
- walls
- partitions
- floors
- ceilings
- roofs
- doors
- windows
- waterproofing
- finishes
- kitchens
- bathrooms
- electrical
- plumbing
- HVAC
- fire protection
- security
- external works
- landscaping

---

# Assembly Structure

An assembly consists of:

Assembly
├── Components
├── Materials
├── Labour
├── Equipment
├── Quantity Rules
├── Waste Rules
├── Unit
├── Standards
└── Regional Applicability

---

# Components

Each component should identify:

- component_id
- description
- category
- material
- unit
- quantity_rule
- waste_factor
- optionality
- sequencing
- dependencies

---

# Material Intelligence

Materials may include:

- material_id
- material_code
- name
- specification
- grade
- size
- finish
- unit
- applicable_standards
- regional_availability
- quality_tier

---

# Labour Intelligence

Labour components may define:

- labour_type
- skill_class
- productivity_rate
- unit
- quantity_rule
- regional_applicability

Labour rates are owned by Pricing Intelligence.

Assembly Intelligence defines labour requirements, not market prices.

---

# Equipment Intelligence

Assemblies may identify required equipment:

- equipment_type
- operating_unit
- productivity
- dependency
- quantity_rule

Equipment rates are owned by Pricing Intelligence.

---

# Quantity Rules

Assemblies must define how their components become measurable.

Examples:

- area-based
- length-based
- volume-based
- count-based
- weight-based
- capacity-based
- formula-based

---

# Waste Rules

Waste must be explicit.

Each waste rule should define:

- waste_factor
- unit
- applicability
- reason
- source
- version

Waste must never be silently embedded inside arbitrary quantity values.

---

# Quality Tiers

Assemblies may support:

- basic
- standard
- premium
- luxury
- bespoke

Quality tiers may change:

- materials
- components
- labour requirements
- quantities
- specifications

They may also influence pricing through Pricing Intelligence.

---

# Regional Applicability

Assemblies may specify:

- countries
- states
- cities
- districts
- climate zones
- construction environments

An assembly should not be selected when its applicability rules fail.

---

# Assembly Selection

Assembly selection may consume:

- building element
- building type
- district profile
- construction standard
- interior specification
- quality tier
- project requirements

---

# Output Contract

Assembly Intelligence produces:

- assembly identity
- selected specification
- components
- material requirements
- labour requirements
- equipment requirements
- quantity rules
- waste rules
- applicable standards
- regional applicability
- provenance
- confidence
- version

---

# Canonical Ownership

Assembly Intelligence owns:

- assembly definitions
- component relationships
- material requirements
- labour requirements
- equipment requirements
- quantity rules
- waste rules
- applicability rules

It does not own:

- final project quantities
- BOQ line generation
- market prices
- currency conversion
- final project estimates

---

# Architectural Principle

An assembly is a reusable construction recipe.

The same assembly may be used by many projects.

Project-specific quantities are calculated downstream.

---

# Canonical Flow

Building Element
+
District Rules
+
Interior Specification
+
Quality Tier
↓
Assembly Selection
↓
Assembly Components
↓
Quantity Rules
↓
Quantity Intelligence
