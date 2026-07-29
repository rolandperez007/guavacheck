# ADR-006

## Title

Strict Engine Ownership

---

## Status

Accepted

---

## Decision

Each engine owns one business domain.

Examples

Twin Studio

↓

3D Data

Finance

↓

Money

Commerce

↓

Suppliers

Trust

↓

Ownership

Passport

↓

Identity

Austin

↓

Coordination

No engine modifies another engine's private data.

Communication occurs through APIs and Events.

---

## Consequences

Clear ownership

Reduced technical debt

Simpler testing

Improved scalability