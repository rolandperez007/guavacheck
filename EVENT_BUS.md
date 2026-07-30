# EVENT_BUS.md

Version: 2.0

Platform: guavacheck

Classification: Platform Messaging Architecture

Status: Canonical Specification

---

# Overview

The guavacheck platform is designed around an event-driven architecture.

Business domains do not communicate through direct database access.

Instead, domains exchange immutable events through the Platform Event Bus.

This architecture enables:

- Loose coupling
- Horizontal scalability
- Reliable processing
- Independent deployment
- AI orchestration
- Analytics
- Auditing
- Real-time updates
- Event replay
- Future microservice migration

---

# Philosophy

Events represent facts.

Commands represent intentions.

Queries retrieve information.

Example

Command

↓

Create Property

↓

Property Service

↓

Property Created Event

↓

Analytics

↓

Search

↓

Austin

↓

Notifications

↓

Institution Platform

Every consumer receives the same event.

---

# Event Lifecycle

```text
User

↓

API

↓

IRONGATE

↓

Platform Service

↓

Business Logic

↓

Database Transaction

↓

Publish Event

↓

Event Bus

↓

Subscribers

↓

Background Processing

↓

Completion
```

No subscriber may modify the original event.

---

# Event Structure

Every event follows the same contract.

```json
{
  "event_id": "uuid",
  "event_name": "property.created",
  "version": "1.0",
  "occurred_at": "timestamp",
  "source": "property-service",
  "actor_id": "user-id",
  "tenant_id": "organization-id",
  "correlation_id": "request-id",
  "payload": {}
}
```

This schema applies to every domain.

---

# Event Categories

## Identity Events

Examples

user.registered

user.logged_in

user.logged_out

password.changed

session.created

session.expired

permission.granted

permission.revoked

api_key.created

api_key.revoked

---

## Property Events

property.created

property.updated

property.deleted

property.verified

property.published

property.archived

property.sold

passport.generated

twin.updated

valuation.completed

inspection.completed

---

## Institution Events

institution.registered

institution.verified

institution.suspended

offer.created

offer.updated

offer.published

offer.expired

application.submitted

application.approved

application.rejected

---

## Billing Events

checkout.created

payment.completed

payment.failed

payment.refunded

subscription.created

subscription.cancelled

wallet.credited

wallet.debited

invoice.generated

---

## Austin Events

conversation.started

recommendation.generated

simulation.completed

workflow.executed

automation.completed

analysis.finished

report.generated

---

## Knowledge Events

knowledge.created

knowledge.updated

knowledge.deleted

article.published

regulation.updated

---

## Marketplace Events

listing.created

listing.updated

listing.deleted

review.created

review.updated

professional.registered

---

## Notification Events

email.sent

sms.sent

push.sent

notification.failed

---

## Analytics Events

dashboard.updated

metric.calculated

forecast.completed

---

# Event Naming Convention

Every event follows:

```
domain.action
```

Examples

property.created

billing.payment_completed

institution.verified

Avoid generic names like:

created

updated

deleted

---

# Event Versioning

Events are immutable.

Breaking changes require a new version.

Examples

property.created.v1

property.created.v2

Subscribers choose which version to consume.

---

# Event Ordering

Ordering is guaranteed only within a single aggregate.

Example

Property

↓

Created

↓

Updated

↓

Verified

↓

Published

↓

Sold

Ordering is not guaranteed across unrelated aggregates.

---

# Delivery Guarantees

The Event Bus guarantees:

At-Least-Once Delivery

Consumers must therefore be idempotent.

Duplicate processing must never create duplicate business results.

---

# Retry Strategy

Failed events enter a retry queue.

Default policy:

Retry 1

Retry 2

Retry 3

Retry 5

Retry 8

Dead Letter Queue

Permanent failures are preserved for investigation.

---

# Dead Letter Queue

Events that repeatedly fail processing are moved to:

Dead Letter Queue

Reasons include:

Invalid Payload

Unknown Subscriber

Database Failure

Timeout

Schema Mismatch

Unexpected Exception

No event is discarded.

---

# Event Replay

The platform supports replaying historical events.

Use cases include:

Search Re-indexing

Analytics Rebuild

Austin Memory Reconstruction

Institution Synchronization

Recovery After Failure

Replay must never duplicate business actions.

---

# Event Subscribers

Each domain subscribes only to events it needs.

Example

Property Created

↓

Search

Index Property

↓

Analytics

Update Metrics

↓

Austin

Generate Insights

↓

Notifications

Notify Followers

↓

Institution Platform

Evaluate Mortgage Offers

Each subscriber remains independent.

---

# Event Ownership

Only the owning domain may publish its events.

Examples

Billing publishes:

payment.completed

Property publishes:

property.created

Austin publishes:

recommendation.generated

Analytics never publishes Property events.

---

# Correlation IDs

Every request receives:

Request ID

Correlation ID

Every emitted event carries both.

This enables complete request tracing.

---

# Event Security

Events inherit SecurityContext.

Every event contains:

Tenant

Organization

User

Permissions

Timestamp

Risk Score

Correlation ID

Sensitive payloads must be encrypted where required.

---

# Event Monitoring

Metrics include:

Published Events

Consumed Events

Failed Events

Retry Count

Dead Letters

Average Processing Time

Subscriber Latency

Queue Depth

Replay Duration

---

# Event Storage

Events may optionally be persisted for:

Audit

Compliance

Analytics

Replay

Disaster Recovery

Future Event Sourcing

---

# Austin Integration

Austin is primarily an event consumer.

Austin listens for:

Property Created

Passport Generated

Institution Verified

Payment Completed

Listing Published

Knowledge Updated

Austin produces:

Recommendations

Reports

Insights

Automation

Austin never bypasses domain ownership.

---

# Institution Integration

Institutions consume events through secure subscriptions.

Examples

Mortgage Bank

↓

Property Verified

↓

Offer Generated

↓

Customer Notified

Insurance Company

↓

Property Registered

↓

Risk Assessment

↓

Premium Generated

Every integration remains loosely coupled.

---

# Engineering Rules

1. Events are immutable.
2. Events represent facts.
3. Commands change state.
4. Queries never publish events.
5. Domains publish only their own events.
6. Consumers are idempotent.
7. Events are versioned.
8. Every event has a correlation ID.
9. Failed events are preserved.
10. Replay is a first-class capability.

---

# Future Evolution

The Event Bus is designed to support:

Kafka

RabbitMQ

Redis Streams

Google Pub/Sub

AWS EventBridge

Azure Service Bus

NATS

Current implementation details may evolve without changing the event contracts.

---

# Vision

The Event Bus is the communication backbone of guavacheck.

Rather than tightly coupling services together, every platform domain communicates through durable, versioned, secure, and observable events.

This architecture allows guavacheck to evolve from a modular monolith into a distributed platform without requiring changes to business domains, enabling long-term scalability, resilience, and institutional-grade reliability.