# SERVICE_BOUNDARIES.md

**Version:** 2.0  
**Platform:** guavacheck  
**Classification:** Platform Service Architecture  
**Status:** Canonical Specification

---

# Overview

This document defines the architectural boundaries between every platform domain.

The objective is to ensure every service has:

- Clear ownership
- Well-defined responsibilities
- Stable public interfaces
- Explicit dependencies
- Independent evolution

No service may access another service's internal implementation.

Communication occurs exclusively through:

- Public APIs
- Domain Events
- Shared Contracts

---

# Architecture Philosophy

A service boundary is a contract.

Everything inside the boundary belongs exclusively to that service.

Everything outside the boundary is accessed through published interfaces.

```
              Internal

    Business Logic

    Data Models

    Repositories

    Validation

    Domain Rules

-------------------------------

        PUBLIC API

-------------------------------

Other Platform Domains
```

---

# Dependency Hierarchy

Dependencies always flow downward.

```
Platform Core

↓

IRONGATE

↓

Platform Services

↓

Applications

↓

Clients
```

No upward dependency is allowed.

---

# Platform Core

## Owns

- Configuration
- Dependency Injection
- Health
- Startup
- Workers
- Registry
- Environment
- Shared Utilities

## Exposes

```
Configuration API

Health API

Registry API

Worker API
```

## Publishes

```
platform.started

platform.stopped

health.updated
```

## Never Depends On

Business services.

---

# IRONGATE

## Owns

- Authentication
- Authorization
- Policies
- Sessions
- Audit
- Security Context
- Threat Detection
- Risk Engine
- Encryption
- Secrets

## Public APIs

```
Authenticate()

Authorize()

ValidateToken()

BuildSecurityContext()

EvaluatePolicy()

ValidateAPIKey()

CreateSession()

TerminateSession()
```

## Publishes

```
user.authenticated

user.denied

session.created

session.expired

policy.evaluated

risk.updated

threat.detected
```

## Consumes

Platform Core only.

---

# Austin

## Owns

- Planning
- Reasoning
- Recommendations
- Workflow
- Automation
- AI Orchestration
- Simulations

Austin never owns business data.

---

## Public APIs

```
AskAustin()

GenerateRecommendation()

RunSimulation()

GenerateReport()

ExecuteWorkflow()
```

---

## Publishes

```
recommendation.generated

simulation.completed

workflow.executed

analysis.completed

report.generated
```

---

## Consumes

Property Events

Knowledge Events

Institution Events

Billing Events

Analytics Events

Search Events

---

# Property Intelligence

## Owns

- Properties
- Property Passport
- Digital Twin
- Ownership
- Verification
- Valuation
- Inspection

---

## Public APIs

```
RegisterProperty()

UpdateProperty()

VerifyProperty()

GeneratePassport()

GenerateTwin()

CalculateValuation()

PropertyTimeline()
```

---

## Publishes

```
property.created

property.updated

passport.generated

property.verified

valuation.completed

inspection.completed
```

---

## Consumes

Geo

Media

Knowledge

---

# Institution Platform

## Owns

Institution Registry

Institution Verification

Partner APIs

Offer Engine

Partner Dashboard

Institution Analytics

Partner Marketplace

---

## Public APIs

```
RegisterInstitution()

VerifyInstitution()

PublishOffer()

SearchOffers()

InstitutionProfile()

InstitutionDashboard()
```

---

## Publishes

```
institution.registered

institution.verified

offer.created

offer.updated

application.submitted

application.approved
```

---

## Consumes

Billing

Property

Austin

Analytics

---

# Marketplace

## Owns

Listings

Discovery

Recommendations

Professionals

Advertising

Reviews

Featured Content

---

## Public APIs

```
CreateListing()

SearchListings()

RecommendListings()

SearchProfessionals()

SubmitReview()
```

---

## Publishes

```
listing.created

listing.updated

listing.deleted

review.created
```

---

## Consumes

Property

Austin

Analytics

---

# Billing

## Owns

Payments

Wallet

Credits

Subscriptions

Invoices

Checkout

Revenue

Refunds

---

## Public APIs

```
CreateCheckout()

VerifyPayment()

Refund()

WalletBalance()

SubscriptionStatus()

InvoiceHistory()
```

---

## Publishes

```
payment.completed

payment.failed

subscription.created

subscription.cancelled

invoice.generated
```

---

## Consumes

IRONGATE

Institution

Analytics

---

# Knowledge

## Owns

Construction Knowledge

Building Codes

Learning

Articles

AI Knowledge

Regulations

---

## Public APIs

```
SearchKnowledge()

RetrieveArticle()

BuildingCode()

ConstructionGuide()
```

---

## Publishes

```
knowledge.created

knowledge.updated

article.published
```

---

# Search

## Owns

Indexes

Ranking

Autocomplete

Semantic Search

Geo Search

---

## Public APIs

```
Search()

Autocomplete()

Nearby()

SemanticSearch()
```

---

## Consumes

Property

Knowledge

Marketplace

Institution

---

# Analytics

## Owns

Dashboards

KPIs

Forecasting

Reporting

Business Intelligence

AI Metrics

Institution Metrics

---

## Public APIs

```
Dashboard()

KPI()

Report()

Forecast()

Metrics()
```

---

## Consumes

Events from every platform domain.

Analytics does not own operational data.

---

# Geo

## Owns

Countries

Cities

Coordinates

Maps

GIS

Geocoding

Spatial Queries

---

## Public APIs

```
Geocode()

ReverseGeocode()

Nearby()

SpatialSearch()
```

---

# Localization

## Owns

Languages

Currencies

Units

Translations

Regional Policies

---

## Public APIs

```
Translate()

ConvertCurrency()

RegionalSettings()

SupportedLanguages()
```

---

# Communication

## Owns

Email

SMS

WhatsApp

Push

Templates

Notification Queue

---

## Public APIs

```
SendEmail()

SendSMS()

SendPush()

Notify()
```

---

# Media

## Owns

Images

Videos

OCR

Documents

Compression

Metadata

Storage

---

## Public APIs

```
Upload()

Compress()

OCR()

GenerateThumbnail()

Metadata()
```

---

# Developer Platform

## Owns

Public APIs

SDKs

API Keys

Sandbox

Webhooks

Developer Portal

---

## Public APIs

```
GenerateAPIKey()

RegisterWebhook()

WebhookHistory()

DeveloperDashboard()
```

---

# Operations

## Owns

Monitoring

Deployment

Scaling

Recovery

Logging

Observability

Incident Response

---

## Public APIs

```
Health()

Metrics()

Logs()

Alerts()

DeploymentStatus()
```

---

# Shared Contracts

Every service exposes contracts rather than internal models.

Example

Instead of

```
Property SQL Model
```

Expose

```
PropertyDTO
```

Services never exchange ORM objects.

---

# API Design Rules

Every public API must:

- Be versioned
- Be documented
- Return consistent errors
- Produce audit events
- Respect SecurityContext
- Support tracing
- Be idempotent where applicable

---

# Event Design Rules

Every service publishes only its own events.

Never publish another domain's events.

Events are immutable.

Events are versioned.

Events contain correlation IDs.

---

# Database Rules

Each service owns its own tables.

No service performs direct SQL queries against another service's tables.

Cross-domain communication occurs through APIs or events.

---

# Security Rules

Every API request must pass through IRONGATE.

Every event inherits SecurityContext.

Every privileged action produces an audit record.

Every external integration is authenticated.

Every webhook is signed and verified.

---

# Versioning Policy

Public APIs use semantic versioning.

```
/api/v1/

↓

/api/v2/

↓

/api/v3/
```

Breaking changes never modify existing versions.

---

# Observability

Every service emits:

- Logs
- Metrics
- Traces
- Health Status
- Audit Events

Every request receives:

- Request ID
- Correlation ID

This enables end-to-end tracing.

---

# Engineering Principles

Every platform service must:

- Own exactly one business capability.
- Expose stable interfaces.
- Publish domain events.
- Consume events responsibly.
- Never bypass IRONGATE.
- Never directly access another domain's database.
- Be independently testable.
- Be independently deployable.
- Be fully documented.
- Support future horizontal scaling.

---

# Future Direction

The service boundary architecture allows guavacheck to evolve from a modular monolith into distributed services without changing business contracts.

Because APIs, events, and ownership boundaries are defined independently of deployment, services can later be extracted into microservices, serverless workloads, or dedicated infrastructure with minimal disruption.

---

# Vision

Service boundaries define the architectural integrity of guavacheck.

Every platform domain is autonomous, secure, observable, and independently evolvable while remaining part of a cohesive Property Intelligence Platform.

This separation of concerns ensures that as new capabilities, institutions, AI services, and global deployments are introduced, the platform remains maintainable, scalable, and resilient without compromising consistency or trust.