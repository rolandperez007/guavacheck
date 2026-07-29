# Guava API Guide

Version: 1.0

---

# API Philosophy

REST-first

Versioned

Secure

Predictable

Documented

Event-aware

---

# Base URL

/api/v1

---

# Authentication

JWT

OAuth

API Keys

Role-based permissions

---

# Standard Response

Success

{
    success,
    data,
    metadata
}

Failure

{
    success,
    error,
    message,
    correlation_id
}

---

# Core APIs

Authentication

/auth

Users

/users

Properties

/properties

Property Passport

/passports

Twin Studio

/twins

Trust Exchange

/trust

Finance

/finance

Commerce

/commerce

Construction

/construction

Investor

/investor

Wallet

/wallet

Austin

/austin

Notifications

/notifications

Events

/events

---

# API Standards

GET

Retrieve resources

POST

Create resources

PUT

Replace resources

PATCH

Partial updates

DELETE

Archive resources

---

# Pagination

page

page_size

total

next

previous

---

# Filtering

status

country

city

price

date

owner

property_type

verification_status

---

# Security

JWT validation

Permission checks

Rate limiting

Audit logging

Input validation

Request signing

---

# Versioning

/api/v1

/api/v2

Deprecated versions remain supported during transition periods.

---

# Documentation

Every endpoint includes:

Purpose

Parameters

Authentication

Responses

Examples

Events Published

Errors

---

# Future

GraphQL Gateway

Streaming APIs

WebSocket APIs

AI APIs

SDKs