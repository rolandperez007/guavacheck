# Property Passport API

Version: 1.0

---

# Purpose

The Property Passport API provides the canonical interface for creating, querying and maintaining Property Passports.

Every property on the platform is represented by exactly one Property Passport.

---

# Core Endpoints

POST /passport

Create Property Passport

---

GET /passport/{passport_id}

Retrieve Passport

---

PUT /passport/{passport_id}

Update Passport

---

DELETE /passport/{passport_id}

Archive Passport

---

GET /passport/{passport_id}/history

Retrieve Property Timeline

---

GET /passport/{passport_id}/dna

Retrieve Property DNA

---

GET /passport/{passport_id}/twin

Retrieve Twin Studio Reference

---

GET /passport/search

Search Property Passports

---

# Validation

Unique Passport ID

Valid Ownership

Verified Coordinates

Document Validation

Government Reference Validation

---

# Security

JWT Authentication

Role-Based Access Control

Audit Logging

Permission Validation

---

# Events

PassportCreated

PassportUpdated

PassportArchived

PassportTransferred