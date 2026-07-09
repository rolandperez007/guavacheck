# Supabase Infrastructure Guide

Version: 1.0

Status: Living Document

Owner: Guava Inc.

Classification: Database Infrastructure

---

# Purpose

This document defines how guavacheck uses Supabase in production.

It establishes standards for:

- PostgreSQL
- Authentication
- Storage
- Row Level Security
- Edge Functions
- Realtime
- Backups
- Disaster Recovery

The objective is simple:

Protect user data.

---

# Philosophy

Data is the most valuable asset of guavacheck.

Applications can be rebuilt.

Infrastructure can be replaced.

User trust cannot.

Every engineering decision involving data should prioritize:

Reliability

Security

Recoverability

Scalability

---

# Services Used

Current Supabase services include:

PostgreSQL Database

Authentication

Storage

Row Level Security

Realtime

Edge Functions (Future)

Cron Jobs (Future)

---

# Database Responsibilities

The database stores:

Users

Profiles

Properties

Projects

Conversations

Construction Estimates

Engineering Reports

Verification Records

Marketplace Listings

Community Content

Payments

Subscriptions

Notifications

Audit Logs

System Settings

Austin Conversations

Platform Analytics

---

# Authentication

Authentication is managed through Supabase Auth.

Supported providers include:

Email & Password

Google

Apple (Future)

Microsoft (Future)

GitHub (Developer Access)

Enterprise SSO (Future)

---

# Authorization

Every request must be authenticated.

Every resource must be authorized.

Authentication proves identity.

Authorization determines access.

---

# Row Level Security

RLS must remain enabled on every production table.

Policies should always follow least-privilege principles.

Users should only access:

Their own profile

Their own projects

Their own properties

Their own documents

Their own conversations

Administrative access must be explicitly granted.

---

# Storage

Storage contains:

Property Images

Construction Photos

Blueprints

Survey Plans

Engineering Drawings

Reports

Invoices

Generated PDFs

Media Assets

Future AI-generated content

---

# Storage Rules

Uploads should:

Validate file type

Validate file size

Validate ownership

Generate unique filenames

Reject malicious content

Private files should never be publicly accessible without authorization.

---

# Environment Variables

Examples:

NEXT_PUBLIC_SUPABASE_URL

NEXT_PUBLIC_SUPABASE_ANON_KEY

SUPABASE_SERVICE_ROLE_KEY

DATABASE_URL

Never expose service keys to the client.

Only NEXT_PUBLIC variables belong in frontend code.

---

# Database Migrations

Schema changes should always be version controlled.

Migration order:

Development

↓

Testing

↓

Staging

↓

Production

Every migration should be reversible where practical.

---

# Backup Strategy

Backups are mandatory.

Minimum backup schedule:

Daily

Weekly

Monthly

Long-term Archive

Critical deployments should trigger a backup before execution.

---

# Restore Testing

Backups have no value unless they can be restored.

Restore testing should occur regularly.

Verify:

Database integrity

Relationships

Indexes

Policies

Stored procedures

Application compatibility

---

# Disaster Recovery

Recovery objectives:

Minimal downtime

Minimal data loss

Verified restoration

Documented recovery process

Disaster recovery plans should be rehearsed—not assumed.

---

# Austin Integration

Austin depends on Supabase for:

Authentication

Memory

Conversation History

Projects

Properties

Platform State

Austin should verify database health before becoming operational.

If Supabase is unavailable:

Austin should remain offline.

---

# Monitoring

Monitor continuously:

Database Size

Storage Usage

Connection Count

Query Performance

Authentication Errors

Failed Logins

API Usage

Replication Status

Backup Status

Restore Validation

---

# Performance

Optimize:

Indexes

Foreign Keys

Query Plans

Connection Pooling

Caching

Pagination

Search

Database performance should scale with platform growth.

---

# Security

Never expose:

Service Role Keys

Database Passwords

JWT Secrets

Private Buckets

Internal Credentials

Secrets belong only in secure environment management.

---

# Scaling Strategy

Future scalability includes:

Read Replicas

Regional Databases

Connection Pooling

Partitioning

Archiving

Caching Layers

Geo-distributed Storage

---

# Engineering Principles

Every table should have:

Primary Key

Created Timestamp

Updated Timestamp

Ownership

Auditability

Appropriate Indexes

RLS Policies

Every schema decision should be intentional.

---

# Final Principle

Supabase is more than a database.

It is the trusted memory of guavacheck.

Protect it accordingly.

---

© 2026 Guava Inc.

Intelligence with integrity.

Technology with purpose.

Trust above everything.