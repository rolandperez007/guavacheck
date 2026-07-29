# ADR-005

## Title

Austin Coordinates Rather Than Owns

---

## Status

Accepted

---

## Context

Business logic should remain inside specialised engines.

---

## Decision

Austin orchestrates.

Austin never duplicates engine logic.

Austin queries engines.

Austin combines results.

Austin recommends actions.

---

## Consequences

Cleaner architecture

Reduced duplication

Simpler maintenance

Independent engine evolution

---

## Related Documents

AUSTIN_PROTOCOL.md

ENGINES.md