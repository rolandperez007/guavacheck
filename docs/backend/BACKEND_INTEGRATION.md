# Backend Integration

## Overview

GuavaCheck is composed of multiple independent platforms.

Every platform owns:

- Models
- Services
- Repositories
- Events
- APIs

No platform accesses another platform's database objects directly.

Communication occurs through:

- Services
- Workflow Adapters
- Events

---

# Core Platforms

Austin AI

Institution

Property

Passport

Simulation

Billing

Community

Notifications

Analytics

Geo

Currency

Vision

Trust

Decision

Twin

Projects

Documents

Search

Knowledge

Marketplace

Finance

Identity

Authentication

Permissions

Workflow

---

# Integration Rules

Platform

↓

Service

↓

Adapter

↓

Workflow

↓

Events

↓

Analytics

Never the opposite.

---

# Shared Components

Execution Context

Correlation ID

Tenant ID

Audit Trail

Permissions

Notification Queue

Analytics Events

Workflow History
