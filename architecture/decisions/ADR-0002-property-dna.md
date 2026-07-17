# ADR-0002: Property DNA as the Core Property Model

**Status:** Accepted

**Date:** 2026-07-17

**Decision Makers:** Guava Networks Architecture Team

---

# Context

Traditional property platforms represent properties as flat records containing an address, price and a small collection of attributes.

This approach limits intelligent reasoning, historical analysis and future extensibility.

guavacheck requires a richer representation capable of supporting valuation, construction planning, investment analysis, digital twins and government-scale planning.

---

# Decision

Every property shall be represented by a persistent Property DNA.

Property DNA represents the complete digital identity of a property.

The identity evolves over time while preserving historical information.

Property DNA may include:

- Identity
- Location
- Ownership
- Legal Status
- Construction
- Architecture
- Media
- Documents
- Valuation History
- Market Activity
- Investment Profile
- Community Context
- Environmental Factors
- Infrastructure
- Historical Timeline
- Austin Confidence Score

---

# Consequences

Positive

- Richer property intelligence.
- Better AI reasoning.
- Better historical analysis.
- Digital twin compatibility.
- Government-ready architecture.

Trade-offs

- Larger data model.
- Increased processing requirements.
- More sophisticated synchronization.

These trade-offs are acceptable because they establish a long-term foundation.

---

# Alternatives Considered

## Flat Listing Model

Rejected.

Reason:

Insufficient for intelligent reasoning.

---

## Independent Property Modules

Rejected.

Reason:

Would fragment property intelligence across multiple systems.

---

# Selected Approach

Every property has a single evolving digital identity.

---

# Guiding Principle

Every property should possess a persistent digital identity rather than a temporary listing.