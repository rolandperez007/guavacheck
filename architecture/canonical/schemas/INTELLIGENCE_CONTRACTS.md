# Intelligence Contracts

## Canonical Relationships

DistrictProfile
→ InteriorProfile

DistrictProfile
→ ConstructionProfile

Building
→ BuildingElement

Room
→ InteriorSpecification

InteriorSpecification
→ Assembly

BuildingElement
→ Assembly

Assembly
→ AssemblyComponent

AssemblyComponent
→ QuantityRule

QuantityRule
→ Quantity

Quantity
→ BOQLineItem

BOQLineItem
→ PricingRate

PricingRate
→ Cost

---

# Core Contract

The canonical construction intelligence graph is:

Location
→ District
→ Building
→ Element
→ Specification
→ Assembly
→ Component
→ Quantity
→ BOQ
→ Rate
→ Cost

---

# No Direct Shortcuts

Avoid:

District
→ BOQ

Interior
→ Price

Rendering
→ BOQ

Image
→ Final Cost

Instead all such paths resolve through canonical structured intelligence.

---

# Confidence

AI-generated intelligence should carry confidence.

Examples:

- high
- medium
- low

or a numeric confidence score.

---

# Provenance

Generated intelligence should retain provenance whenever possible.

Examples:

- user input
- architectural model
- district profile
- interior profile
- assembly definition
- quantity calculation
- pricing source
- AI inference

---

# Versioning

Canonical intelligence objects must be versionable.

Changes must not silently alter historical estimates.

---

# Austin

Austin acts as the intelligence orchestrator.

Austin may:

- interpret user intent
- select district profiles
- select interior profiles
- select assemblies
- invoke quantity calculations
- invoke BOQ generation
- invoke pricing
- explain results

Austin does not replace the domain engines.

---

# Domain Ownership

District Engine
→ District intelligence

Interior Engine
→ Interior intelligence

Assembly Engine
→ Construction assemblies

Quantity Engine
→ Quantities

BOQ Engine
→ BOQ

Pricing Engine
→ Pricing

Austin
→ Orchestration and reasoning