# Repository Contract

Version: 1.0

---

## Purpose

Repositories are the exclusive persistence interface between domain services
and storage providers.

Business logic must never communicate directly with databases.

Every domain owns its repositories.

---

## Responsibilities

Load

Create

Update

Delete

Archive

Restore

Search

Filter

Aggregate

Paginate

Bulk Operations

Versioning

---

## Repository Rules

Stateless

Dependency Injectable

Testable

Transaction Aware

Tenant Isolated

Async Compatible

Observable

Auditable

---

## Naming Convention

InstitutionRepository

PassportRepository

WorkflowRepository

BillingRepository

SimulationRepository

CommunityRepository

AnalyticsRepository

NotificationRepository

AustinRepository

VisionRepository

TwinRepository

TrustRepository

GeoRepository

CurrencyRepository

---

## Return Types

Entity

Collection

Optional

Cursor

Paged Result

Statistics

Aggregate

Projection

DTO

---

## Transaction Rules

Begin

Commit

Rollback

Retry

Deadlock Recovery

Timeout

Compensation

---

## Performance

Lazy Loading

Streaming

Chunk Reads

Batch Writes

Optimistic Locking

Caching

Indexes

Partition Awareness

---

## Audit

Created By

Updated By

Timestamp

Version

Correlation ID

Workflow ID

Institution ID

Tenant ID
