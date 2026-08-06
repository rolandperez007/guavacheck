# GuavaCheck Platform State Machine

Version: 1.0

Status: Approved Architecture

Owner: Platform Engineering

Related Documents

- EVENT_CATALOG.md
- MESSAGE_BUS.md
- WORKFLOW_ENGINE.md
- PROPERTY_PASSPORT.md
- SUPABASE_INTEGRATION.md

---

# Vision

Everything in GuavaCheck has a lifecycle.

Nothing simply "exists."

Properties evolve.

Institutions mature.

Users subscribe.

Passports transfer ownership.

Payments complete.

Austin learns.

Workflows execute.

Simulations expire.

Every domain object progresses through clearly defined states.

This document defines those transitions.

---

# Why State Machines?

Without a state machine:

• invalid transitions become possible

• duplicate operations occur

• workflows become unpredictable

• UI becomes inconsistent

• analytics become unreliable

• AI loses context

State Machines ensure every module speaks the same language.

---

# State Machine Principles

Every state machine contains:

Initial State

↓

Allowed States

↓

Transition Rules

↓

Entry Actions

↓

Exit Actions

↓

Events

↓

Audit Records

↓

Permissions

↓

Notifications

↓

Analytics

↓

Austin Awareness

---

# Universal Transition Rules

Every transition must satisfy:

✓ Permission Validation

✓ Business Rule Validation

✓ Workflow Validation

✓ Audit Logging

✓ Event Publication

✓ Notification Hooks

✓ Analytics Recording

✓ AI Context Update

No transition bypasses validation.

---

# PROPERTY LIFECYCLE

```
Draft

↓

Submitted

↓

Pending Review

↓

Verified

↓

Published

↓

Reserved

↓

Under Negotiation

↓

Sold

↓

Archived
```

---

## Draft

Meaning

Property exists but is incomplete.

Allowed Actions

Save

Upload Images

Edit

Delete

Cannot

Publish

Sell

Verify

Events

property.created

---

## Submitted

Meaning

Owner requests verification.

Events

property.submitted

Allowed

Withdraw

Update Documents

---

## Pending Review

Platform review begins.

Austin performs:

Image analysis

Metadata validation

Location verification

Fraud detection

Duplicate detection

Possible Outcomes

Verified

Rejected

Needs Information

---

## Verified

Meaning

Property passes platform verification.

Events

property.verified

UI Badge

Verified

Austin Confidence

Updated

---

## Published

Visible to:

Marketplace

Institutions

Austin

Investors

Search Engine

Community

Events

property.published

---

## Reserved

Temporary reservation.

Reservation timer begins.

Expiration policy applies.

---

## Under Negotiation

Buyer

Seller

Institution

Lawyers

Austin

become active participants.

---

## Sold

Ownership transfer begins.

Passport updates.

Analytics update.

Institution notified.

Workflow initiated.

---

## Archived

Historical record.

Read-only.

---

# PROPERTY PASSPORT

```
Requested

↓

Generating

↓

Generated

↓

Verified

↓

Signed

↓

Transferred

↓

Archived
```

---

## Requested

Created after verification workflow.

---

## Generating

Austin compiles:

Property data

Ownership

History

Images

Documents

Valuation

Location

Geo information

Risk score

---

## Generated

Digital Passport produced.

---

## Verified

Integrity confirmed.

Hash recorded.

---

## Signed

Owner signs.

Institution may countersign.

---

## Transferred

Ownership changes.

Passport history preserved.

---

## Archived

Historical snapshot.

Never deleted.

---

# INSTITUTION LIFECYCLE

```
Registered

↓

Verification Pending

↓

Verified

↓

Active

↓

Suspended

↓

Expired

↓

Archived
```

---

## Registered

Institution profile created.

---

## Verification Pending

Compliance

Licensing

Identity

Corporate documents

are checked.

---

## Verified

Institution approved.

---

## Active

Institution may

Issue mortgages

Offer insurance

Publish products

Create branches

Access APIs

Receive leads

Run simulations

---

## Suspended

Temporary restriction.

Reasons

Compliance

Billing

Fraud

Manual review

---

## Expired

Subscription expired.

Access reduced.

---

## Archived

Historical institution.

---

# USER ACCOUNT

```
Registered

↓

Email Verified

↓

Active

↓

Restricted

↓

Suspended

↓

Deleted
```

---

Restrictions preserve data.

Deletion follows retention policy.

---

# BILLING

```
Created

↓

Pending

↓

Authorized

↓

Captured

↓

Paid

↓

Refunded

↓

Cancelled
```

---

Created

Invoice exists.

---

Pending

Awaiting payment.

---

Authorized

Provider approved.

Funds reserved.

---

Captured

Money collected.

---

Paid

Platform activated.

---

Refunded

Financial reversal.

---

Cancelled

Workflow terminated.

---

# SUBSCRIPTIONS

```
Trial

↓

Active

↓

Past Due

↓

Grace Period

↓

Suspended

↓

Cancelled

↓

Expired
```

Grace period supports payment recovery.

---

# WORKFLOW

```
Created

↓

Queued

↓

Running

↓

Waiting

↓

Paused

↓

Resumed

↓

Completed

↓

Failed

↓

Compensated

↓

Archived
```

---

Waiting

External dependency.

Institution

Payment

Document

Government API

---

Compensated

Rollback completed.

---

# SIMULATION

```
Requested

↓

Preparing

↓

Running

↓

Completed

↓

Cached

↓

Expired
```

Simulation cache avoids unnecessary computation.

---

# AUSTIN AI

```
Idle

↓

Listening

↓

Understanding

↓

Retrieving Context

↓

Planning

↓

Reasoning

↓

Generating

↓

Executing Workflow

↓

Learning

↓

Idle
```

---

Listening

Input received.

---

Understanding

Intent classification.

Language detection.

User context.

---

Retrieving Context

Property

Institution

Workflow

History

Knowledge

Conversation

Analytics

---

Planning

Austin chooses:

Search

Workflow

Simulation

Recommendation

Institution

Passport

Community

---

Reasoning

Internal decision process.

No database mutations occur.

---

Generating

Produces

Advice

Explanation

Summary

Recommendations

Insights

---

Executing Workflow

Only approved workflows execute.

Austin never bypasses permissions.

---

Learning

Conversation metrics.

Feedback.

Performance.

Embeddings.

Knowledge updates.

---

# COMMUNITY

```
Draft

↓

Published

↓

Trending

↓

Pinned

↓

Archived
```

---

Moderation may interrupt progression.

---

# NOTIFICATIONS

```
Created

↓

Queued

↓

Sent

↓

Delivered

↓

Read

↓

Archived
```

Failures return to retry queue.

---

# ANALYTICS REPORT

```
Requested

↓

Generating

↓

Completed

↓

Exported

↓

Archived
```

---

# PROJECTS

```
Planning

↓

Active

↓

Blocked

↓

Completed

↓

Archived
```

---

# DIGITAL TWIN

```
Created

↓

Synchronizing

↓

Current

↓

Snapshot

↓

Archived
```

---

# DECISION ENGINE

```
Requested

↓

Evaluating

↓

Approved

or

Rejected

↓

Archived
```

---

# Transition Validation

Every transition executes:

Permission Validation

↓

Business Rules

↓

Workflow Validation

↓

Database Transaction

↓

Event Publication

↓

Notification

↓

Analytics

↓

Austin Context Update

↓

Commit

No transition skips this pipeline.

---

# Illegal Transitions

Examples

Published → Draft

Sold → Pending Review

Refunded → Pending

Transferred → Generated

These transitions are rejected automatically.

---

# Timeout Rules

Some states expire automatically.

Examples

Reservation

48 hours

Verification

14 days

Workflow Wait

30 days

Simulation Cache

24 hours

Austin Context

Session configurable

---

# Audit Trail

Every transition records:

Previous State

Next State

Timestamp

Actor

Workflow

Institution

Tenant

Reason

Correlation ID

Trace ID

No state change occurs without an audit record.

---

# State Events

Every successful transition publishes a platform event.

Example

```
Draft

↓

Published
```

Produces:

property.submitted

property.review_started

property.verified

property.published

Each event flows through the Message Bus.

---

# Dashboard Integration

The Dashboard visualizes state progression using:

Progress timelines

Status badges

Workflow indicators

Real-time updates

Activity feeds

Institution dashboards

Austin recommendations

Every state has a corresponding visual representation.

---

# Future Expansion

Additional state machines will be introduced for:

Insurance Policies

Construction Projects

Inspection Reports

Drone Missions

Smart Building Sensors

Carbon Credits

Land Registry Records

Government Workflows

International Transactions

Digital Identity

Blockchain Ownership

Each new domain follows the same lifecycle principles established in this document.

---

# Architecture Summary

The State Machine is the behavioral contract of the GuavaCheck platform.

While the Event Catalog defines what happens and the Message Bus defines how information moves, the State Machine defines how every entity evolves over time.

Together, these three documents establish a consistent operational language across backend services, frontend applications, Austin AI, mobile clients, analytics, institutional integrations, and future platform extensions.

Every workflow, dashboard component, notification, and AI recommendation ultimately derives its behavior from these defined state transitions, ensuring that GuavaCheck remains predictable, auditable, scalable, and maintainable as the platform grows.