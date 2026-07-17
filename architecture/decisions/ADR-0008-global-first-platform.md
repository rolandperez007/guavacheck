# ADR-0008: Global-First Platform

**Status:** Accepted

**Date:** 2026-07-17

---

# Context

guavacheck is intended to operate internationally rather than being designed for a single country and expanded later.

Global support must therefore be foundational rather than an afterthought.

---

# Decision

Every platform capability shall support global operation by design.

Examples include:

- Multiple countries.
- Multiple currencies.
- Multiple languages.
- Multiple measurement systems.
- Regional regulations.
- Localized market intelligence.

Country-specific functionality should extend the platform without changing its architecture.

---

# Consequences

Positive

- Easier international expansion.
- Consistent platform architecture.
- Better localization.

Trade-offs

- Increased initial complexity.
- Larger reference datasets.

---

# Alternatives Considered

Country-first expansion.

Rejected.

Reason:

Would require repeated architectural changes during international growth.

---

# Guiding Principle

Design globally.

Localize intelligently.