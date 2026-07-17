# ADR-0007: Modular Engine Design

**Status:** Accepted

**Date:** 2026-07-17

---

# Context

guavacheck consists of numerous intelligent capabilities that will continue to expand over time.

Embedding all business logic into large monolithic services would reduce maintainability and increase deployment risk.

---

# Decision

The platform shall be organized into modular engines.

Each engine owns a single responsibility.

Examples include:

- Valuation Engine
- Search Engine
- Matching Engine
- Reasoning Engine
- Planning Engine
- Media Engine

Engines communicate through well-defined interfaces.

Austin coordinates engine execution.

---

# Consequences

Positive

- Independent development.
- Independent testing.
- Independent scaling.
- Easier replacement.
- Improved observability.

Trade-offs

- More service interfaces.
- Greater orchestration complexity.

---

# Alternatives Considered

Monolithic business services.

Rejected.

Reason:

Reduced scalability and increased coupling.

---

# Guiding Principle

Every engine should do one thing exceptionally well.