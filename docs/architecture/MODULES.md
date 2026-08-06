# Module Responsibilities

Every module follows the same architectural pattern.

```
Module
├── api/
├── analytics/
├── events/
├── integrations/
├── jobs/
├── models/
├── permissions/
├── repositories/
├── schemas/
├── services/
├── validators/
└── workflows/
```

## Responsibilities

### Models

Persist business entities.

### Repositories

Handle persistence.

### Services

Contain business logic.

### Managers

Coordinate multiple services when required.

### APIs

Expose application functionality.

### Events

Publish domain events.

### Analytics

Measure business outcomes.

### Validators

Validate business rules.

### Integrations

Communicate with external systems.