# District Intelligence

## Purpose

District Intelligence provides the structured geographic, planning,
environmental, architectural, construction and market context required
to determine how a property should be designed, evaluated and costed.

District Intelligence does not directly generate a BOQ.

It provides structured constraints, preferences and applicable rules that
downstream intelligence can consume.

---

# Core Responsibility

District Intelligence resolves:

Location
→ District
→ District Profile
→ Applicable Rules
→ Building Constraints
→ Architectural Profile
→ Interior Profile
→ Construction Profile

---

# District Identity

A district profile may contain:

- district_id
- district_name
- city
- state_or_region
- country
- latitude
- longitude
- administrative_area
- neighbourhood
- zone
- profile_version
- effective_date
- source
- confidence

---

# Planning Intelligence

District profiles may define:

- zoning
- permitted land use
- density
- plot coverage
- floor area ratio
- maximum height
- minimum setbacks
- frontage requirements
- parking requirements
- access requirements
- building orientation
- subdivision constraints
- development restrictions

---

# Environmental Intelligence

District profiles may contain:

- flood exposure
- seismic exposure
- wind exposure
- soil characteristics
- drainage conditions
- climate
- rainfall
- temperature
- coastal exposure
- erosion risk
- environmental constraints

Environmental intelligence must remain structured and versioned.

---

# Architectural Intelligence

District profiles may describe:

- architectural character
- building typology
- preferred massing
- facade character
- roof character
- material preferences
- external finish standards
- window expectations
- security expectations
- landscape expectations

These characteristics are recommendations or constraints depending on
their rule classification.

---

# Interior Intelligence Inputs

District Intelligence may influence:

- interior quality tier
- preferred materials
- finish standards
- fixture expectations
- lighting expectations
- security systems
- climate-control expectations
- local market preferences

District Intelligence must not directly hard-code individual room designs.

---

# Construction Intelligence Inputs

District Intelligence may influence:

- applicable construction standards
- foundation considerations
- structural requirements
- drainage requirements
- material availability
- local construction methods
- labour conditions
- equipment requirements
- environmental protection requirements

---

# Cost Intelligence Inputs

District Intelligence may provide:

- cost tier
- market tier
- regional pricing zone
- labour market
- material market
- logistics conditions
- contractor market
- escalation context

District cost intelligence is an input to Pricing Intelligence.

It must not become a duplicate pricing engine.

---

# Rule Classification

Every district rule should be classified as one of:

- Requirement
- Restriction
- Recommendation
- Preference
- Market Signal
- Environmental Condition
- Informational

---

# Output Contract

District Intelligence should produce a structured district profile containing:

- identity
- geography
- planning
- environmental conditions
- architectural profile
- interior profile
- construction profile
- market profile
- cost profile
- applicable rules
- sources
- confidence
- version

---

# Architectural Principle

Districts are data.

District rules are explicit rules.

District engines execute those rules.

District APIs expose resolved intelligence.

Application code must not contain large collections of district-specific
hard-coded decisions.

---

# Downstream Flow

District Profile
→ Building Constraints
→ Interior Constraints
→ Construction Constraints
→ Assembly Selection
→ Quantity Context
→ Pricing Context

---

# Canonical Ownership

District Intelligence owns:

- district identity
- district profiles
- district rules
- district classifications
- geographic context
- district-level recommendations

It does not own:

- room calculations
- assembly definitions
- quantity calculations
- BOQ generation
- pricing calculation

---

# Versioning

District profiles and rules must be versioned.

Changes must preserve:

- previous version
- effective date
- source
- reason for change
- confidence
- compatibility information

---

# Auditability

Every resolved district decision should be traceable to:

District Profile
+
Rule
+
Source
+
Version
+
Resolution

---

# Canonical Principle

District Intelligence establishes the context in which construction
intelligence operates.

It provides constraints and signals.

It does not perform downstream construction calculations.
