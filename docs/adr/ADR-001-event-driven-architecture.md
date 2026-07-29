# ADR-001

## Title

Adopt Event-Driven Architecture

---

## Status

Accepted

---

## Context

The Guava Platform contains many specialised engines.

Direct engine-to-engine communication would increase coupling, reduce scalability and complicate maintenance.

---

## Decision

All engines communicate primarily through published events.

Each engine subscribes only to events relevant to its domain.

Austin coordinates workflows but does not replace event communication.

---

## Consequences

Benefits

• Loose coupling

• Independent deployment

• Easier testing

• Better scalability

• Easier observability

Trade-offs

• Event ordering must be managed.

• Retry mechanisms are required.

• Event versioning becomes important.

---

## Related Documents

SYSTEM_ARCHITECTURE.md

EVENTS.md

EVENT_CONTRACTS.md