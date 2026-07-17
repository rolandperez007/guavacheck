# ADR-0004: Domain-Driven Platform Architecture

**Status:** Accepted

**Date:** 2026-07-17

---

# Context

As guavacheck expands, features will span numerous disciplines including property, construction, finance, enterprise services and government planning.

A feature-oriented architecture would become difficult to scale and maintain.

---

# Decision

The platform shall be organized into business domains.

Each domain owns its data, services and intelligence.

Austin coordinates domains but does not replace them.

---

# Initial Domains

- Property
- Construction
- Community
- Enterprise
- Global Market
- Finance
- Identity
- Security

Additional domains may be introduced as the platform evolves.

---

# Consequences

Positive

- Independent development.
- Clear ownership.
- Easier scaling.
- Better testing.
- Improved maintainability.

Trade-offs

- Additional integration work.
- Stronger interface contracts required.

---

# Guiding Principle

Business capabilities belong to clearly defined domains with explicit ownership.