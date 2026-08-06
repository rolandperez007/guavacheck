# GuavaCheck Platform Event Catalog

Version: 1.0

Status: Approved Architecture

Owner: Platform Engineering

---

# Purpose

GuavaCheck is an event-driven platform.

Every meaningful action performed by a user, institution, workflow, AI engine, or external integration produces a platform event.

Events are the primary communication mechanism between independent modules.

Rather than modules calling each other directly, modules publish events describing what has happened. Other modules subscribe only to the events they require.

This architecture provides:

- Loose coupling
- Horizontal scalability
- Fault tolerance
- Complete auditability
- Workflow orchestration
- Real-time synchronization
- Analytics
- AI context awareness

---

# Event Philosophy

An event always describes something that has already happened.

Examples

✓ Property Created

✓ Passport Verified

✓ Payment Received

✓ Simulation Completed

✓ Institution Activated

An event never represents an instruction.

Incorrect

Create Property

Approve Passport

Charge Payment

Correct

PropertyCreated

PassportApproved

PaymentCaptured

---

# Event Naming Convention

Events use the format

```
Domain.Action
```

Examples

```
property.created

property.updated

passport.verified

billing.payment_received

institution.branch_created

workflow.completed

austin.recommendation_generated
```

Past-tense naming is mandatory.

---

# Universal Event Envelope

Every event published on the platform follows a common envelope.

```json
{
  "event_id": "uuid",
  "event_name": "property.created",
  "version": "1.0",
  "timestamp": "2026-08-01T12:00:00Z",
  "tenant_id": "...",
  "institution_id": "...",
  "actor_id": "...",
  "correlation_id": "...",
  "trace_id": "...",
  "source": "property-service",
  "payload": {},
  "metadata": {}
}
```

---

# Standard Metadata

Every event contains:

Event ID

Unique identifier.

Correlation ID

Groups related events together.

Trace ID

Distributed tracing.

Tenant ID

Supports multi-tenancy.

Institution ID

Institution context.

Actor ID

Authenticated user or system.

Workflow ID

Optional.

Session ID

Optional.

Device ID

Optional.

IP Address

Optional.

Locale

Optional.

Currency

Optional.

Timezone

Optional.

---

# Event Versioning

Events never break consumers.

Rules

Major

Breaking change.

Minor

Backward compatible.

Patch

Metadata only.

Example

```
property.created.v1

property.created.v2
```

Older consumers remain supported during migration.

---

# Event Categories

The platform currently recognizes the following event domains.

---

## Authentication

```
auth.user_registered

auth.login_success

auth.login_failed

auth.logout

auth.password_changed

auth.password_reset_requested

auth.password_reset_completed

auth.mfa_enabled

auth.mfa_verified

auth.account_locked

auth.account_unlocked

auth.token_refreshed
```

---

## User Events

```
user.created

user.updated

user.deleted

user.avatar_updated

user.preferences_updated

user.subscription_changed

user.language_changed

user.currency_changed

user.location_updated
```

---

## Property Events

```
property.created

property.updated

property.deleted

property.submitted

property.review_requested

property.review_completed

property.verified

property.rejected

property.archived

property.restored

property.published

property.unpublished

property.viewed

property.saved

property.shared

property.bookmarked

property.flagged

property.price_updated

property.owner_changed

property.documents_uploaded

property.images_updated

property.virtual_tour_created
```

---

## Property Passport

```
passport.created

passport.generated

passport.verified

passport.reissued

passport.signed

passport.expired

passport.transferred

passport.revoked

passport.archived

passport.downloaded

passport.shared
```

---

## Institution Platform

```
institution.created

institution.updated

institution.deleted

institution.verified

institution.activated

institution.suspended

institution.branch_created

institution.branch_updated

institution.branch_deleted

institution.subscription_started

institution.subscription_cancelled

institution.subscription_renewed

institution.user_invited

institution.user_removed

institution.role_changed

institution.permissions_updated
```

---

## Billing

```
billing.checkout_created

billing.payment_pending

billing.payment_received

billing.payment_failed

billing.payment_refunded

billing.invoice_created

billing.invoice_paid

billing.invoice_overdue

billing.subscription_created

billing.subscription_active

billing.subscription_expired

billing.subscription_cancelled

billing.wallet_funded

billing.commission_paid
```

---

## Workflow

```
workflow.created

workflow.started

workflow.paused

workflow.resumed

workflow.waiting

workflow.cancelled

workflow.completed

workflow.failed

workflow.timeout

workflow.retry

workflow.compensated
```

---

## Austin AI

```
austin.session_started

austin.session_ended

austin.context_updated

austin.intent_detected

austin.recommendation_generated

austin.report_generated

austin.workflow_suggested

austin.workflow_executed

austin.market_analysis_completed

austin.learning_cycle_completed
```

Austin subscribes to nearly every domain event but publishes only AI-specific events.

---

## Simulation

```
simulation.created

simulation.started

simulation.completed

simulation.failed

simulation.cached

simulation.invalidated

simulation.exported

simulation.approved
```

---

## Community

```
community.post_created

community.post_updated

community.post_deleted

community.comment_added

community.comment_deleted

community.reaction_added

community.reaction_removed

community.report_created

community.badge_awarded
```

---

## Notifications

```
notification.created

notification.sent

notification.delivered

notification.read

notification.dismissed

notification.failed

notification.retry
```

---

## Analytics

```
analytics.metric_recorded

analytics.dashboard_updated

analytics.report_generated

analytics.export_completed
```

---

## Projects

```
project.created

project.updated

project.archived

project.task_created

project.task_completed

project.member_added

project.member_removed

project.milestone_completed
```

---

## Geo Engine

```
geo.location_resolved

geo.geofence_entered

geo.geofence_exited

geo.address_verified

geo.coordinates_updated
```

---

## Currency Engine

```
currency.rate_updated

currency.conversion_completed

currency.base_changed
```

---

## Vision Engine

```
vision.analysis_started

vision.analysis_completed

vision.defect_detected

vision.floorplan_processed
```

---

## Decision Engine

```
decision.started

decision.completed

decision.approved

decision.rejected
```

---

## Digital Twin

```
twin.created

twin.updated

twin.synchronized

twin.snapshot_created
```

---

# Event Lifecycle

Every event passes through the same lifecycle.

```
Created

↓

Validated

↓

Published

↓

Delivered

↓

Acknowledged

↓

Archived
```

---

# Delivery Guarantees

Platform events are delivered using:

- At least once delivery
- Retry on transient failures
- Idempotent consumers
- Ordered delivery within a partition
- Correlation-aware processing

---

# Event Security

Every event is protected by:

- Tenant isolation
- Institution boundaries
- Permission validation
- Audit logging
- Immutable event history
- Signed internal messages (future)
- Encryption in transit

Consumers only receive events they are authorized to access.

---

# Event Replay

Authorized administrators may replay historical events for:

- Disaster recovery
- Workflow reconstruction
- Analytics regeneration
- AI model retraining
- Audit investigations
- Integration testing

Replayed events preserve their original Event ID, Timestamp, and Correlation ID while being flagged as replayed.

---

# Event Retention

Default retention policy:

- Operational events: 90 days
- Billing events: 7 years
- Audit events: Permanent
- Workflow events: 3 years
- Analytics aggregates: Configurable
- AI telemetry: Configurable with privacy controls

---

# Future Expansion

The catalog is designed to grow without breaking consumers.

Future domains include:

- Insurance
- Government Registries
- Land Registry APIs
- Construction Monitoring
- Drone Operations
- IoT Sensors
- Smart Buildings
- Carbon Accounting
- ESG Reporting
- Blockchain Ownership
- Digital Identity
- Open Banking
- International Payment Networks

Each new domain follows the same event naming, metadata, versioning, and security standards.

---

# Architecture Summary

The Event Catalog is the canonical language of the GuavaCheck platform.

Every workflow, AI interaction, dashboard update, institutional integration, mobile notification, and analytics pipeline begins with an event.

By treating events as first-class citizens, GuavaCheck remains modular, observable, scalable, and ready for future integrations while maintaining a consistent platform-wide contract.