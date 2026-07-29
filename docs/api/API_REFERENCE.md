# Guava Platform API Reference

Version: 1.0

---

# Overview

The Guava Platform API provides secure access to every platform engine through a unified REST interface.

Every request is authenticated and authorised before reaching the target engine.

---

# API Categories

Authentication

Users

Property Passport

Twin Studio

Construction

Commerce

Finance

Investor

Trust Exchange

Distress

Knowledge

Community

Government

Wallet

Payments

Notifications

Austin AI

Search

Analytics

Administration

---

# API Principles

RESTful

Versioned

Secure

Stateless

JSON Responses

Consistent Naming

Audit Logged

Permission Aware

---

# Base URL

/api/v1

---

# Authentication

JWT Bearer Tokens

OAuth (Future)

API Keys

Organisation Tokens

---

# Response Format

Success

Status

Message

Data

Pagination

Metadata

Correlation ID

---

# Error Format

Error Code

Message

Details

Timestamp

Correlation ID

---

# API Versioning

v1

v2 (Future)

Backwards Compatible

Deprecation Notices

---

# Rate Limiting

Authenticated Users

Organisation Limits

Partner Limits

Developer Limits

---

# Common HTTP Codes

200 OK

201 Created

204 No Content

400 Bad Request

401 Unauthorized

403 Forbidden

404 Not Found

409 Conflict

422 Validation Error

429 Too Many Requests

500 Internal Server Error

503 Service Unavailable

---

# Platform Services

Authentication

Authorisation

Event Bus

Notifications

Audit Logs

Billing

Search

Storage

AI Services

Monitoring