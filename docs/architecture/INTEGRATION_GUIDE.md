# Integration Guide

Modules must never depend directly on another module's persistence layer.

Preferred integration order:

1. Domain Service
2. Published Event
3. Workflow Action
4. External Integration

Avoid:

- Cross-module model mutations.
- Direct repository access across domains.
- Circular imports.
- Shared mutable state.

All integrations should be observable through events and analytics.