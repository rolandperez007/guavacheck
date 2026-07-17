# ADR-0006: Layered Platform Architecture

**Status:** Accepted

**Date:** 2026-07-17

---

# Context

As guavacheck grows, concerns such as user experience, intelligence, business logic, shared services and infrastructure must remain separated.

Mixing these concerns increases coupling and reduces maintainability.

---

# Decision

The platform shall adopt a layered architecture.

```
Vision & Principles

↓

Core Platform

↓

Business Domains

↓

Shared Services

↓

Experience Layer

↓

Infrastructure
```

Each layer has clearly defined responsibilities.

Higher layers depend on lower layers through stable interfaces.

Lower layers should not depend on presentation concerns.

---

# Consequences

Positive

- Clear separation of concerns.
- Easier testing.
- Independent deployment.
- Long-term maintainability.

Trade-offs

- More interfaces.
- Additional coordination between layers.

---

# Guiding Principle

Every responsibility belongs to exactly one architectural layer.