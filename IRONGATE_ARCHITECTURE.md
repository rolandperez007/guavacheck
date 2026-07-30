# IRONGATE_ARCHITECTURE.md

> Version: 2.0
> Platform: guavacheck
> Component: IRONGATE
> Status: Platform Security Foundation
> Classification: Core Platform Architecture

---

# Overview

IRONGATE is the centralized security platform that protects every service, API, AI workflow, institution integration, and user interaction within guavacheck.

Unlike traditional middleware that simply authenticates requests, IRONGATE functions as a complete Security Operating System responsible for identity, trust, authorization, auditing, threat detection, compliance, and platform-wide governance.

Every request entering the platform passes through IRONGATE before reaching any business service.

---

# Mission

Build the most trusted property technology security platform by providing:

- Zero Trust Architecture
- Centralized Identity
- Policy-Based Authorization
- Enterprise Audit Trails
- AI Security
- Institution Security
- API Protection
- Threat Intelligence
- Compliance by Design

---

# Core Principles

## Security First

Security is never optional.

Every request is validated.

Every action is authorized.

Every event is audited.

---

## Zero Trust

Trust nothing.

Verify everything.

Authentication never implies authorization.

---

## Platform Wide

IRONGATE protects:

- Web Application
- Mobile Applications
- Public APIs
- Internal APIs
- Austin AI
- Institution Platform
- Billing
- Marketplace
- Property Engine
- Analytics
- Administration
- Developer Platform

---

## Policy Driven

Business logic never performs authorization.

Services ask IRONGATE.

Example:

Property Service

↓

Can user modify this property?

↓

IRONGATE

↓

Yes / No

---

## Event Driven

Every security decision produces an event.

Nothing happens silently.

---

# Platform Position

                         Users

                           │

                    Mobile / Web

                           │

                    API Gateway

                           │

                    IRONGATE

──────────────────────────────────────────

Identity

Authentication

Authorization

Policy Engine

Permissions

Threat Engine

Audit

Monitoring

Encryption

Secrets

Compliance

Session Management

──────────────────────────────────────────

Austin

Property Engine

Institutions

Marketplace

Billing

Analytics

Search

Knowledge

Notifications

---

# Responsibilities

IRONGATE owns every security concern.

No other module should implement independent security logic.

---

# Identity

Responsible for identifying actors within the platform.

Supported identities include:

- Buyer
- Seller
- Agent
- Developer
- Surveyor
- Institution
- Government
- Administrator
- Austin AI
- Service Account
- Guest
- API Client

Every identity receives a globally unique identifier.

---

# Authentication

Supported authentication methods:

- JWT
- OAuth
- Bearer Tokens
- Refresh Tokens
- API Keys
- Institution Tokens
- Service Tokens
- Device Sessions

Future:

- Passkeys
- Enterprise SSO
- Hardware Keys

---

# Authorization

Authorization is policy-based.

Instead of:

if role == "admin"

Use:

Property.Read

Property.Edit

Property.Delete

Property.Verify

Passport.Generate

Mortgage.Apply

Institution.Publish

Institution.Manage

Analytics.Read

Billing.Manage

Austin.Execute

Developer.API

Policies remain independent from roles.

---

# Roles

Example platform roles:

Guest

Registered User

Verified User

Property Owner

Agent

Agency Admin

Institution User

Institution Admin

Government Officer

Support

Platform Administrator

Austin

Service Account

---

# Security Context

Every request carries a SecurityContext.

SecurityContext

User ID

Organization ID

Institution ID

Tenant ID

Role

Permissions

Country

Subscription

Risk Score

Device

Session

API Key

Request ID

Correlation ID

Authentication Method

IP Address

User Agent

Timestamp

Every downstream service receives the same context.

---

# Policy Engine

The Policy Engine evaluates permissions.

Example

Austin

↓

Can user publish mortgage products?

↓

Policy Engine

↓

Verified Institution

Institution Admin

Mortgage.Publish

Approved

↓

Return TRUE

No service should contain authorization logic.

---

# Session Manager

Responsible for:

Session Creation

Session Expiry

Refresh

Logout

Session Revocation

Concurrent Session Limits

Trusted Devices

Session Analytics

---

# API Security

Every API request passes through:

Authentication

↓

Authorization

↓

Rate Limiting

↓

Schema Validation

↓

Threat Analysis

↓

Logging

↓

Business Logic

---

# API Key Management

Each API Key contains:

Identifier

Owner

Scopes

Environment

Expiry

Status

Usage Statistics

Last Used

Rotation Schedule

---

# Encryption

IRONGATE owns cryptography.

Responsibilities include:

Password Hashing

Document Encryption

Secret Encryption

Webhook Signature Validation

Checksums

Digital Signatures

Random Generation

Key Rotation

Future:

Property Passport Signatures

Institution Certificates

---

# Secrets Management

Central storage for:

Stripe

Paystack

Flutterwave

OpenAI

Supabase

Google

AWS

Twilio

Institution Credentials

Webhook Secrets

Secrets must never be hardcoded.

---

# Audit Engine

Every critical action produces an immutable audit record.

Examples:

User Login

Logout

Password Change

Permission Granted

Permission Revoked

Role Changed

Institution Connected

Institution Verified

Property Created

Property Modified

Passport Generated

Mortgage Requested

Payment Completed

Austin Request

API Key Created

Secret Rotated

Security Alert

Audit entries are immutable.

---

# Threat Engine

Detects platform threats.

Examples:

Impossible Travel

Credential Stuffing

Replay Attack

Token Abuse

Brute Force

Bot Traffic

Spam Listings

Fake Institutions

Fraudulent Payments

Prompt Injection

AI Abuse

Institution Abuse

High Risk Documents

Threat events generate risk scores.

---

# Risk Engine

Every user receives a dynamic risk score.

Factors include:

Device History

IP Reputation

Behavior

Velocity

Location

Failed Logins

Institution Reputation

Document Confidence

Austin can consume risk scores but never modify them.

---

# Security Simulator

Purpose:

Validate security assumptions before production.

Supported simulations:

Cross Tenant Access

Role Escalation

Privilege Escalation

Replay Attack

Expired Tokens

Permission Bypass

API Abuse

Webhook Forgery

Institution Isolation

Prompt Injection

Austin Sandbox Escape

Secret Exposure

The simulator becomes part of CI/CD.

---

# Compliance

Designed to support:

OWASP Top 10

OWASP ASVS

GDPR

NDPR

SOC 2 Readiness

ISO 27001 Alignment

PCI DSS

Compliance mappings should link every requirement to one or more IRONGATE controls.

---

# Monitoring

Metrics collected include:

Authentication Success Rate

Authentication Failure Rate

Permission Denials

Threat Count

Blocked Requests

Average Authentication Time

API Key Usage

Institution Activity

Austin Security Events

Audit Volume

Security Score

---

# Dashboard

The IRONGATE Dashboard provides real-time visibility.

Displays:

Platform Health

Threat Level

Active Sessions

Failed Logins

Blocked Requests

Institution Security

Austin Activity

Audit Events

Policy Decisions

Security Score

---

# Events

IRONGATE publishes standardized events.

UserAuthenticated

AuthenticationFailed

SessionCreated

SessionExpired

PermissionGranted

PermissionDenied

ThreatDetected

RiskScoreChanged

PolicyEvaluated

AuditRecorded

InstitutionVerified

SecretRotated

APIKeyCreated

APIKeyRevoked

AustinAuthorized

AustinDenied

These events are consumed by Analytics, Monitoring, Notifications, and Austin.

---

# Integration Rules

Every module integrates with IRONGATE.

Property Engine

↓

Authenticate

Authorize

Audit

Proceed

Institution Platform

↓

Authenticate

Authorize

Threat Check

Audit

Proceed

Billing

↓

Authenticate

Permission Check

Fraud Check

Audit

Proceed

Austin

↓

Security Context

Policy Evaluation

Threat Check

Audit

Execute

---

# Architectural Rules

1. No service authenticates users independently.

2. No service performs authorization internally.

3. No service stores security secrets.

4. No module bypasses IRONGATE.

5. Every privileged action is audited.

6. Every security decision is reproducible.

7. SecurityContext is immutable during request execution.

8. Policies replace hardcoded role checks.

9. Threat intelligence is centralized.

10. Cryptography is centralized.

11. Audit logs are immutable.

12. Security events are event-driven.

13. Every platform capability inherits security from IRONGATE.

---

# Future Roadmap

IRONGATE v2

✓ Platform Consolidation

✓ Unified Policy Engine

✓ Central Security Context

✓ Standard Audit Events

✓ Threat Intelligence

✓ Security Simulator

---

IRONGATE v3

- Adaptive Risk Scoring
- AI-assisted Threat Detection
- Device Trust
- Passkeys
- Behavioral Biometrics
- Institution Trust Framework
- Property Passport Signatures
- Continuous Authorization
- Security Analytics Dashboard
- Automated Compliance Reporting

---

# Vision

IRONGATE is not a middleware component.

It is the trust layer of guavacheck.

Every user, every institution, every AI interaction, every payment, every property passport, and every future platform capability depends upon IRONGATE to establish identity, enforce policy, protect data, detect threats, and preserve trust.

As guavacheck evolves into a global property intelligence platform, IRONGATE remains the foundation that guarantees every interaction is secure, auditable, compliant, and trustworthy.