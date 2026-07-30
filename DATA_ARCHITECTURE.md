# DATA_ARCHITECTURE.md

**Version:** 2.0

**Platform:** guavacheck

**Classification:** Enterprise Data Architecture

**Status:** Canonical Specification

---

# Overview

The guavacheck platform is built around a unified, domain-driven data architecture that ensures consistency, integrity, scalability, and long-term maintainability.

Every piece of data belongs to exactly one domain.

Every domain owns its own schema.

Every interaction with data is protected by IRONGATE.

Every important change becomes an immutable event.

---

# Data Philosophy

The platform follows seven core principles.

1. Single Source of Truth

Every business entity has one authoritative owner.

2. Domain Ownership

Every table belongs to one domain.

3. API First

Data is shared through APIs, not direct database access.

4. Event Driven

State changes generate immutable events.

5. Security First

Every record inherits platform security.

6. Auditability

Every critical change is traceable.

7. Future Distributed Architecture

The design supports eventual migration to independent services.

---

# Data Layers

```
                    Presentation Layer

──────────────────────────────────────────────

                  Application Layer

──────────────────────────────────────────────

                  Domain Services

──────────────────────────────────────────────

                 Domain Repositories

──────────────────────────────────────────────

               PostgreSQL + Redis + Storage

──────────────────────────────────────────────

             Backup + Analytics + Archives
```

---

# Canonical Data Domains

The platform consists of the following primary data domains.

Platform

Security

Identity

Property

Institution

Marketplace

Billing

Knowledge

Analytics

Media

Geo

Localization

Communication

Austin

Developer Platform

Operations

Each domain owns its own schema.

---

# Platform Schema

Purpose

Shared platform infrastructure.

Contains

Configuration

Feature Flags

System Metadata

Platform Settings

Service Registry

Health Records

Version Information

---

# Identity Schema

Purpose

Represent every actor in the platform.

Entities

Users

Profiles

Organizations

Institutions

Service Accounts

API Clients

Sessions

Devices

Permissions

Roles

Relationships

One user may belong to multiple organizations.

One organization may own multiple properties.

---

# Security Schema

Purpose

Owned exclusively by IRONGATE.

Contains

Authentication Records

Tokens

Audit Logs

Risk Scores

Security Events

Threat Events

Policy Decisions

API Keys

Secret Metadata

Sessions

Security Context Cache

Business domains never manipulate these tables.

---

# Property Schema

Purpose

Digital representation of every property.

Entities

Property

Address

Coordinates

Ownership

Property Passport

Digital Twin

Inspection

Valuation

Construction History

Property Media

Property Timeline

Property Risks

Property Documents

Property Metadata

Every property receives a globally unique Property ID.

---

# Institution Schema

Purpose

Represent every institutional partner.

Entities

Institution

Institution Profile

Verification

Licenses

Branches

Offers

Products

Applications

Partner Dashboard

Institution Analytics

Institution API Credentials

Institutions never directly access Property tables.

---

# Marketplace Schema

Purpose

Discovery.

Entities

Listings

Categories

Reviews

Professionals

Advertising

Featured Listings

Saved Searches

Recommendations

Marketplace Analytics

---

# Billing Schema

Purpose

Financial transactions.

Entities

Payments

Subscriptions

Invoices

Wallet

Credits

Transactions

Refunds

Provider Sessions

Billing Events

Revenue Metrics

No other domain owns payment records.

---

# Knowledge Schema

Purpose

Knowledge backbone.

Entities

Articles

Building Codes

Construction Guides

Regulations

Learning Resources

Reference Documents

Knowledge Graph

Austin Context

Knowledge Versioning

---

# Analytics Schema

Purpose

Business intelligence.

Entities

Metrics

Reports

Dashboards

Forecasts

Aggregations

Executive KPIs

Institution KPIs

AI KPIs

Growth Metrics

Analytics stores derived information rather than operational data.

---

# Search Index

Purpose

Fast discovery.

Indexes

Properties

Institutions

Knowledge

Listings

Professionals

Documents

Austin Search

Indexes are rebuilt from events.

---

# Geo Schema

Purpose

Location intelligence.

Entities

Countries

States

Cities

Coordinates

Administrative Boundaries

Road Networks

Geocoding Cache

Spatial Indexes

---

# Localization Schema

Purpose

Global deployment.

Entities

Languages

Currencies

Exchange Rates

Translations

Regional Rules

Units

Timezones

Tax Profiles

---

# Communication Schema

Purpose

Messaging.

Entities

Notifications

Email Queue

SMS Queue

Push Queue

Templates

Delivery Status

Communication Preferences

---

# Media Schema

Purpose

Digital assets.

Entities

Images

Videos

Documents

OCR Results

Metadata

Compression Jobs

Storage References

Media Versions

---

# Austin Schema

Purpose

AI orchestration.

Entities

Conversation

Planning

Recommendations

Workflow History

Simulation Results

Reasoning Logs

Prompt Templates

Memory References

Austin never duplicates operational business data.

---

# Developer Platform Schema

Purpose

External integrations.

Entities

API Keys

Webhook Registrations

SDK Versions

Usage Metrics

Developer Accounts

Sandbox Sessions

API Logs

---

# Data Ownership Rules

Each schema owns its own tables.

No schema may directly modify another schema's data.

Communication occurs through:

- Public APIs
- Domain Events
- Shared Contracts

---

# Primary Keys

Every entity uses globally unique identifiers.

Examples

UserID

PropertyID

InstitutionID

PaymentID

PassportID

ConversationID

AuditID

EventID

UUIDs are preferred for global uniqueness.

---

# Foreign Key Strategy

Relationships remain inside domain boundaries where practical.

Cross-domain relationships should prefer identifiers over deep coupling.

Example

Property

↓

OwnerID

rather than embedding user information.

---

# Data Lifecycle

Every record follows:

Create

↓

Validate

↓

Persist

↓

Publish Event

↓

Index

↓

Analyze

↓

Archive

↓

Retain

↓

Delete (where permitted)

Critical records such as audit logs may be retained indefinitely.

---

# Soft Deletes

Business records should generally support soft deletion.

Fields

deleted_at

deleted_by

reason

Hard deletion is reserved for compliance or operational requirements.

---

# Versioning

Mutable records maintain version history where appropriate.

Examples

Property Passport

Construction Records

Knowledge Articles

Institution Profiles

Version history supports auditing and rollback.

---

# Caching Strategy

Redis is used for:

Sessions

Security Context

Frequently Accessed Properties

Institution Offers

Search Suggestions

Rate Limiting

Feature Flags

Analytics Snapshots

The database remains the source of truth.

---

# File Storage

Large assets are stored outside PostgreSQL.

Examples

Images

Videos

Blueprints

Inspection Reports

PDFs

Property Documents

Only metadata is stored in relational tables.

---

# Data Security

Every sensitive record is protected by IRONGATE.

Controls include:

Authentication

Authorization

Encryption

Audit

Threat Monitoring

Risk Scoring

Security Context

Multi-tenant Isolation

---

# Multi-Tenancy

Every tenant is logically isolated.

Security Context determines visibility.

Institutions never access another institution's data.

Users never access another organization's records without authorization.

---

# Audit Strategy

Every critical modification produces:

Audit Record

Event

Timestamp

Actor

Correlation ID

Request ID

Risk Score

No privileged action occurs without traceability.

---

# Data Retention

Retention policies vary by domain.

Examples

Audit Logs

7–10 years

Payments

Financial regulations

Security Events

Compliance requirements

Notifications

Configurable retention

Media

Lifecycle policies

---

# Backup Strategy

Daily incremental backups.

Weekly full backups.

Point-in-time recovery.

Cross-region replication (future).

Regular restoration testing.

---

# Disaster Recovery

Recovery objectives should include:

Recovery Time Objective (RTO)

Recovery Point Objective (RPO)

Automated restoration

Integrity verification

Disaster recovery procedures are documented separately.

---

# Future Evolution

The architecture supports:

Data Warehousing

Lakehouse Integration

Event Sourcing

CQRS

Distributed Databases

Regional Data Residency

Machine Learning Pipelines

Real-Time Analytics

---

# Vision

Data is the foundation of guavacheck.

Every property, institution, payment, recommendation, passport, and AI interaction contributes to a trusted, auditable, and scalable Property Intelligence Platform.

By enforcing clear ownership, strong security, immutable events, and disciplined data governance, the platform can evolve from a modular monolith into a globally distributed ecosystem without compromising integrity or trust.