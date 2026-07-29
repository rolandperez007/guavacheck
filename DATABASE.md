# Guava Database Architecture

Version: 1.0

---

# Philosophy

The database is organised around domain ownership.

Every engine owns its own tables.

Shared data is referenced through identifiers rather than duplicated.

The Property Passport acts as the central identity layer.

---

# Core Entities

Property

Property Passport

Twin Studio

Owner

Trust Exchange

Finance

Commerce

Construction

Investor

Wallet

Notifications

Users

---

# Entity Relationships

User

↓

Property

↓

Property Passport

↓

Twin Studio

↓

Trust Exchange

↓

Finance

↓

Commerce

↓

Construction

↓

Investor

---

# Core Tables

users

properties

property_passports

twins

twin_versions

twin_components

twin_assets

ownership_history

transactions

offers

escrow_accounts

wallets

payments

construction_projects

milestones

contractors

suppliers

products

property_services

maintenance_records

inspection_reports

valuations

investments

notifications

audit_logs

events

---

# Database Rules

Every property references exactly one Property Passport.

Every Property Passport references exactly one Twin.

Every Twin may have many versions.

Every ownership change creates a new ownership history record.

Every financial transaction creates an immutable audit record.

Every important action generates an event.

---

# Soft Deletes

The following entities are never physically deleted:

Property Passport

Twin

Ownership History

Transactions

Audit Logs

Events

Instead:

status = archived

---

# Versioning

Twin Versions

Inspection Versions

Passport Versions

Agreement Versions

API Versions

---

# Audit

Every table includes:

created_at

updated_at

created_by

updated_by

status

version

---

# Scaling Strategy

UUID primary keys

Indexes on frequently searched fields

Partition large event tables

Separate storage for media

Redis caching

Read replicas

Background workers

---

# Security

Encrypted sensitive fields

Role-based access

Audit logging

Immutable transaction history

Secure backups

Disaster recovery

---

# Future

Sharding

Multi-region replication

Time-series analytics

Data warehouse integration

AI feature store