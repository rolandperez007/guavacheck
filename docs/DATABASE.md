# DATABASE.md

# guavacheck Data Doctrine

Version: 1.0

Status: Living Document

Owner: Guava Inc.

Classification: Internal Engineering

---

# Purpose

The database is the permanent memory of guavacheck.

Applications may change.

Frameworks may evolve.

Interfaces may be redesigned.

Data must endure.

This document defines the principles governing every piece of information stored by guavacheck.

---

# Philosophy

Data is not merely stored.

Data represents:

People.

Homes.

Land.

Businesses.

Communities.

Projects.

Investments.

Knowledge.

Trust.

Every record represents a real-world commitment.

Treat every record accordingly.

---

# Data Principles

Principle One

Data belongs to the user.

Guava Inc. protects it.

It does not own it.

---

Principle Two

Store Once.

Reference Everywhere.

Duplicate Nowhere.

---

Principle Three

Relationships are more valuable than isolated records.

---

Principle Four

Every important change should be traceable.

---

Principle Five

Historical information is valuable.

Deletion should be rare.

Archiving is preferred.

---

Principle Six

Every database should remain recoverable.

---

# Database Responsibilities

The database exists to provide:

Persistence

Integrity

Consistency

Availability

Recoverability

Scalability

Auditability

Performance

---

# Primary Database

Primary relational database:

PostgreSQL

Managed by Supabase.

Future database technologies may coexist.

PostgreSQL remains the source of truth.

---

# Data Categories

Identity

Users

Organizations

Professionals

Roles

Permissions

Authentication

---

Property

Properties

Land

Buildings

Addresses

Coordinates

Ownership

Titles

Media

Verification

---

Engineering

Projects

Drawings

Materials

Calculations

Measurements

Cost Estimates

Construction Phases

Specifications

---

Community

Posts

Comments

Groups

Events

Messages

Notifications

Reputation

---

Marketplace

Listings

Orders

Products

Manufacturers

Suppliers

Inventory

Transactions

---

Investment

Investment Opportunities

Financial Models

Cash Flow

Risk Analysis

Portfolio Data

Performance

---

Austin

Conversation Context

Engine Decisions

Reasoning Metadata

Memory References

Learning Signals

Operational Context

Austin never stores sensitive reasoning that should remain private.

Austin stores useful context.

---

Operations

Logs

Deployments

Monitoring

Incidents

Audit Trails

System Health

Backups

---

# Source of Truth

Every entity should have exactly one authoritative source.

Example:

User Identity

↓

Users Table

Not duplicated elsewhere.

Every other service references the original record.

---

# Data Relationships

Relationships should reflect reality.

Users own projects.

Projects contain drawings.

Drawings generate estimates.

Estimates create budgets.

Budgets create investments.

Investments generate communities.

Communities create knowledge.

Knowledge improves Austin.

The database mirrors the ecosystem.

---

# Identifiers

Every important entity should have:

Internal UUID

Human-readable identifier where appropriate

Creation timestamp

Modification timestamp

Status

Ownership

Audit information

Identifiers never change.

---

# Soft Deletes

Permanent deletion should be exceptional.

Most business entities should support:

Active

Archived

Restored

Deleted

History matters.

---

# Versioning

Important records should preserve history.

Examples:

Architectural drawings

Cost estimates

Property documents

Verification reports

Contracts

Users should be able to understand how information evolved.

---

# Constraints

Every table should define:

Primary Keys

Foreign Keys

Unique Constraints

Validation Rules

Relationships

The database should reject invalid states.

---

# Indexing

Indexes exist to improve retrieval.

Indexes should support:

Property Search

Geographic Search

Verification

Marketplace

Community

Austin Memory

Performance should improve naturally as the platform grows.

---

# Transactions

Critical operations should be atomic.

Examples:

Payments

Ownership Transfer

Verification Approval

Subscriptions

Property Publication

Either every step succeeds.

Or none do.

---

# Audit Trails

Every important action should record:

Who

When

Where

What

Why (where applicable)

Audit history strengthens trust.

---

# Data Security

Sensitive information should be:

Encrypted

Access Controlled

Audited

Backed Up

Verified

Protected throughout its lifecycle.

---

# Data Retention

Retention policies should be documented.

Examples:

Audit Logs

Operational Logs

Messages

Notifications

Backups

Deleted Records

Retention balances compliance with operational needs.

---

# AI Memory

Austin's memory is separate from business data.

Austin stores:

Context

Preferences

Conversation continuity

Engine references

Austin should never modify authoritative business records directly.

Business records remain governed by platform services.

---

# Search

The platform supports:

Structured Search

Full-text Search

Geospatial Search

Semantic Search

Vector Search

Future search technologies should enhance—not replace—the primary data model.

---

# Scalability

The data architecture should support:

Millions of users

Millions of properties

Billions of records

Multiple regions

Distributed storage

Future data growth should not require redesign.

---

# Migration Philosophy

Schema changes should be:

Reviewed

Versioned

Tested

Reversible

Documented

Production migrations should preserve data integrity.

---

# Backup Integration

Every database participates in:

Scheduled backups

Restore verification

Operational monitoring

Disaster recovery

Backups are governed by BACKUP_STRATEGY.md.

---

# Austin Guardian Integration

Guardian continuously verifies:

Database Health

Replication Status

Storage Capacity

Connection Health

Backup Success

Migration Status

Integrity Checks

Austin should always understand the condition of the platform's memory.

---

# Final Principle

The database is more than storage.

It is the living memory of guavacheck.

Applications may be rewritten.

Servers may be replaced.

Technologies may change.

The trust represented by the data must remain intact.

Every schema decision made today should still make sense decades from now.