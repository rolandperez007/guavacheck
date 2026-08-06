# Event Architecture

Every important business action generates a domain event.

Examples:

```
institution.created
institution.updated

passport.created
passport.verified
passport.transferred

workflow.started
workflow.completed
workflow.failed

billing.invoice.created
billing.payment.completed

simulation.completed

notification.sent
```

## Event Rules

- Events are immutable.
- Events represent facts that have already occurred.
- Events should never contain business logic.
- Events should contain only the data required by subscribers.
- Consumers should remain independent of publishers.

The Workflow Engine subscribes to many of these events and orchestrates long-running business processes.