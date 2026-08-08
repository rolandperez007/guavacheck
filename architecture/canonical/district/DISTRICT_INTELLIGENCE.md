# Canonical District Intelligence

## Purpose

Define districts as structured intelligence rather than bespoke application
logic.

---

# District Profile

A district profile may contain:

- identity
- geography
- planning
- zoning
- land use
- density
- height
- setbacks
- plot constraints
- infrastructure
- flood risk
- wind exposure
- seismic exposure
- market positioning
- architectural character
- interior character
- construction standards
- finish standards
- material preferences
- security expectations
- landscape expectations
- cost tier

---

# District Intelligence Pipeline

Location
→ District Resolver
→ District Profile
→ Applicable Rules
→ Building Constraints
→ Architectural Profile
→ Interior Profile
→ Construction Profile
→ Pricing Profile

---

# District Must Not Become Application Code

District-specific intelligence should preferably be represented through:

- structured data
- profiles
- rules
- mappings
- constraints
- standards
- material preferences
- finish profiles

rather than large conditional code blocks.

---

# Interior Relationship

Districts may provide an interior profile.

Example:

District
→ Interior Character
→ Quality Tier
→ Finish Profile
→ Material Profile
→ Room Specifications

---

# Construction Relationship

Districts may influence:

- construction standards
- materials
- environmental requirements
- foundation requirements
- structural requirements
- roof requirements
- external works
- drainage
- flood mitigation

---

# BOQ Relationship

District intelligence should influence BOQ indirectly.

Correct:

District
→ Profile
→ Building/Interior Specification
→ Assembly
→ Quantity
→ BOQ

Incorrect:

BOQ Engine
→ if district == X
→ hard-coded price/design logic

---

# Canonical Rule

Districts provide context and constraints.

They do not become duplicated BOQ engines.