# Canonical Intelligence Architecture

## Purpose

This directory defines the canonical architecture connecting GuavaCheck's
construction, district, interior, assembly, BOQ and pricing intelligence.

The canonical intelligence layer does not replace existing engines immediately.

Instead, it defines the contracts and relationships that existing engines must
eventually conform to.

---

# Core Intelligence Pipeline

Location
→ District Profile
→ District Rules
→ Building Model
→ Building Elements
→ Interior Specification
→ Construction Assemblies
→ Quantity Rules
→ BOQ Line Items
→ Regional Pricing
→ Estimate

---

# Canonical Domains

## 1. District Intelligence

Determines:

- planning characteristics
- zoning
- density
- height
- setbacks
- environmental exposure
- infrastructure
- market positioning
- architectural character
- interior character
- construction standards
- finish standards
- material preferences
- cost tier

---

## 2. Interior Intelligence

Determines:

- room type
- room specification
- finishes
- flooring
- walls
- ceilings
- doors
- joinery
- furniture
- lighting
- electrical requirements
- plumbing requirements
- fixtures
- appliances
- materials
- style
- quality tier

---

## 3. Construction Assembly Intelligence

Converts design specifications into measurable construction work.

Assembly
→ Components
→ Materials
→ Labour
→ Equipment
→ Quantity Rules
→ Waste
→ Units
→ Rates

---

## 4. Quantity Intelligence

Converts building elements and assemblies into measurable quantities.

Examples:

- area
- length
- volume
- count
- weight
- capacity
- linear measurement

---

## 5. BOQ Intelligence

Converts quantities into structured BOQ line items.

Each BOQ line must retain:

- project
- element
- assembly
- component
- material
- description
- quantity
- unit
- waste
- adjusted quantity
- unit rate
- amount
- currency
- region
- source
- confidence
- version

---

## 6. Pricing Intelligence

Determines applicable:

- material rates
- labour rates
- equipment rates
- contractor rates
- regional adjustments
- market adjustments
- currency
- taxes
- escalation
- contingency

---

# Canonical Principle

The BOQ engine must not invent construction knowledge.

It consumes structured intelligence from:

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

and produces an auditable BOQ.

---

# Existing Implementations

Existing implementations may remain during migration.

Every implementation must eventually be classified as:

- Canonical
- Supporting
- Duplicate
- Legacy
- Documentation
- Test
- Unknown

No duplicate engine should be created merely because an existing implementation
is difficult to locate or integrate.

---

# Architectural Rule

Knowledge should primarily exist as structured data.

Rules should primarily exist as explicit rule definitions.

Engines should primarily execute those rules.

Services should orchestrate engines.

APIs should expose capabilities.

UI should consume the resulting intelligence.

---

# Migration Strategy

1. Inventory
2. Classify
3. Define canonical contracts
4. Map existing implementations
5. Select canonical implementations
6. Introduce adapters where necessary
7. Migrate incrementally
8. Validate
9. Deprecate duplicates
10. Freeze canonical architecture