# Workflow Engine

The Workflow Engine is the orchestration layer of GuavaCheck.

It does not contain business logic.

Instead, it coordinates specialized modules.

## Responsibilities

- Receive domain events.
- Select workflow templates.
- Create workflow executions.
- Track execution state.
- Invoke services from other modules.
- Record history.
- Publish workflow events.
- Collect execution analytics.

## Execution Lifecycle

```
Domain Event
      │
      ▼
Workflow Selection
      │
      ▼
Execution Created
      │
      ▼
Workflow Steps
      │
      ▼
External Services
      │
      ▼
Completion
      │
      ▼
History
Analytics
Notifications
```

Business rules remain inside the owning module.