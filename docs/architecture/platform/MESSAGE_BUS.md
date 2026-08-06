# GuavaCheck Platform Message Bus

Version: 1.0

Status: Approved Architecture

Owner: Platform Engineering

Related Documents

- EVENT_CATALOG.md
- REALTIME_SYNCHRONIZATION.md
- WORKFLOW_ENGINE.md
- STATE_MACHINE.md
- SUPABASE_INTEGRATION.md

---

# Vision

GuavaCheck is an event-driven platform.

Every module communicates through a unified Message Bus rather than directly invoking another module whenever possible.

The Message Bus acts as the platform's nervous system, carrying events safely, reliably, and efficiently between services.

This architecture enables:

• Loose Coupling

• Independent Deployments

• Horizontal Scaling

• Real-time Updates

• Workflow Automation

• AI Context Synchronization

• Analytics

• Observability

• Fault Recovery

---

# Core Philosophy

Modules own business logic.

The Message Bus owns communication.

Instead of this:

```
Billing

↓

Notification Service

↓

Austin

↓

Analytics
```

The platform operates like this:

```
Billing

↓

Publish Event

↓

Message Bus

↓

Subscribers

↓

Notification

Austin

Analytics

Workflow

Dashboard
```

Publishers never need to know who consumes their events.

Subscribers never need to know who produced them.

---

# Responsibilities

The Message Bus is responsible for:

Publishing

Routing

Filtering

Ordering

Retrying

Dead Letter Handling

Replay

Monitoring

Metrics

Tracing

Security

Version Compatibility

---

# Architecture

```
                    User

                      │

                REST / GraphQL

                      │

               Domain Services

                      │

               Domain Events

                      │

              Message Bus Core

──────────────────────────────────────────

        Router

        Queues

        Retry Manager

        Event Store

        Metrics

        Security

        Replay

──────────────────────────────────────────

                      │

        Workflow Engine

        Austin AI

        Dashboard

        Notifications

        Billing

        Passport

        Community

        Simulation

        Analytics

        Mobile

        External APIs
```

---

# Event Flow

Every event follows the same pipeline.

```
Event Created

↓

Validation

↓

Serialization

↓

Message Bus

↓

Queue Selection

↓

Subscriber Resolution

↓

Delivery

↓

Acknowledgement

↓

Audit

↓

Archive
```

---

# Queue Categories

The platform separates workloads into dedicated queues.

---

## Immediate Queue

Purpose

User-facing actions requiring very low latency.

Examples

Login

Dashboard refresh

Notifications

Austin chat

Target latency

<100 ms

---

## Workflow Queue

Purpose

Business orchestration.

Examples

Institution onboarding

Mortgage workflow

Verification

Construction approval

Property transfer

Target latency

<1 second

---

## Billing Queue

Purpose

Financial consistency.

Examples

Invoices

Subscriptions

Refunds

Wallets

Payments

Priority

High

Ordering

Strict

---

## Simulation Queue

Purpose

Long-running calculations.

Examples

Investment simulations

Building cost estimation

Property valuation

Market forecasting

Risk scoring

Processing

Asynchronous

---

## Austin Queue

Purpose

AI execution.

Examples

Recommendations

Summaries

Insights

Report generation

Natural language tasks

Context updates

---

## Analytics Queue

Purpose

Metrics.

Examples

User activity

Reports

Dashboards

KPIs

Aggregations

---

## Notification Queue

Purpose

Deliver communication.

Email

SMS

Push

WhatsApp

In-App

---

## Community Queue

Purpose

Social activity.

Posts

Comments

Likes

Mentions

Moderation

---

## Institution Queue

Purpose

Enterprise lifecycle.

Institution onboarding

Branch creation

Permission changes

Subscription updates

Compliance

---

## Passport Queue

Purpose

Identity operations.

Passport generation

Verification

Transfer

Revocation

Signature

---

# Priority Levels

```
Critical

High

Normal

Background

Low
```

Critical

Payments

Identity

Security

Verification

High

Notifications

Workflow

Austin

Normal

Analytics

Community

Background

Reporting

Indexing

Synchronization

---

# Routing

Routing is based on:

Event Name

Tenant

Institution

Priority

Workflow

Permissions

Subscriber

Example

```
billing.payment_received

↓

Billing Queue

↓

Workflow Engine

↓

Notification

↓

Austin

↓

Analytics
```

---

# Subscriber Model

Each module subscribes only to events it needs.

Austin

Subscribes to

Property

Billing

Passport

Institution

Simulation

Community

Workflow

Notifications

Dashboard

Subscribes to

Property

Workflow

Analytics

Institution

Billing

Simulation

Notification

Subscribes to

Billing

Workflow

Institution

Community

---

# Delivery Guarantees

The Message Bus guarantees:

✓ Ordered delivery per partition

✓ Retry on transient failures

✓ Idempotent processing

✓ Correlation preservation

✓ Event persistence

✓ Replay support

---

# Retry Policy

Retry schedule

Attempt 1

Immediate

Attempt 2

5 seconds

Attempt 3

30 seconds

Attempt 4

2 minutes

Attempt 5

10 minutes

After maximum attempts

↓

Dead Letter Queue

---

# Dead Letter Queue

Failed events are never discarded.

Instead they enter:

```
DLQ

↓

Investigation

↓

Repair

↓

Replay
```

Reasons

Malformed payload

Timeout

Permission failure

External API unavailable

Validation failure

Unexpected exception

---

# Replay Engine

Replay allows administrators to republish historical events.

Used for

Disaster recovery

Workflow reconstruction

Analytics rebuilding

AI retraining

Migration

Debugging

Replay never changes the original Event ID.

A replay marker is attached instead.

---

# Idempotency

Consumers must safely process duplicate events.

Each event carries

Event ID

Correlation ID

Version

Timestamp

Consumers maintain processed-event records to prevent duplicate side effects.

---

# Ordering

Ordering is guaranteed within logical partitions.

Example

Property

```
Created

↓

Verified

↓

Published

↓

Sold
```

The Message Bus prevents

Sold

↓

Created

which would violate business rules.

---

# Correlation IDs

Every workflow shares one Correlation ID.

Example

Mortgage Request

```
User Applies

↓

Workflow Started

↓

Documents Uploaded

↓

Simulation Completed

↓

Institution Approved

↓

Payment Received

↓

Passport Updated
```

All events belong to one correlation chain.

---

# Security

Every message includes

Tenant ID

Institution ID

Permissions

Signature (future)

Timestamp

Trace ID

Unauthorized consumers never receive restricted events.

---

# Observability

Every event records

Publisher

Subscribers

Queue

Latency

Retries

Execution Time

Worker

Trace ID

Correlation ID

Status

These metrics feed the Analytics Platform.

---

# Worker Pools

Each queue uses dedicated workers.

```
Workflow Workers

Billing Workers

Austin Workers

Notification Workers

Simulation Workers

Analytics Workers

Community Workers
```

Workers scale independently.

---

# Horizontal Scaling

The Message Bus supports

Multiple Publishers

Multiple Consumers

Consumer Groups

Partitioned Queues

Load Balancing

Automatic Failover

---

# External Integrations

Future connectors

Banks

Government

Insurance

Land Registry

Drone Systems

IoT

Construction Platforms

Payment Providers

Open Banking APIs

Blockchain Networks

External systems publish and consume events through secured gateway adapters rather than direct database access.

---

# Monitoring Dashboard

Platform operators can observe:

Queue depth

Processing rate

Worker utilization

Retry counts

Dead Letter Queue size

Average latency

Peak throughput

Failed deliveries

Replay activity

Subscriber health

This dashboard becomes part of the Operations Center.

---

# Disaster Recovery

If a consumer fails:

Events remain persisted.

Another worker resumes processing.

No committed event is lost.

Critical domains (Billing, Passport, Identity) use stricter acknowledgement policies before marking events as complete.

---

# Future Evolution

The Message Bus is designed to support:

Redis Streams

RabbitMQ

Apache Kafka

NATS

Google Pub/Sub

Azure Service Bus

AWS SQS

Hybrid multi-region deployments

Cross-region event replication

Edge processing

AI-native event routing

---

# Architecture Summary

The Message Bus is the communication backbone of GuavaCheck.

Every event generated anywhere in the platform flows through this shared infrastructure before reaching interested services.

By separating communication from business logic, the platform gains scalability, resilience, observability, and the flexibility to evolve without tightly coupling modules.

Together with the Event Catalog, the Message Bus forms the foundation upon which Workflows, Austin AI, the Dashboard, Mobile Applications, Institutions, and future third-party integrations operate as a single intelligent ecosystem.