# ENGINEERING_PLAYBOOK.md

Version: 1.0

Platform: guavacheck

Classification: Engineering Constitution

Status: Canonical Engineering Guide

---

# Introduction

This document defines the engineering culture, coding philosophy, architectural discipline, and development workflow for the guavacheck platform.

It exists to ensure that every engineer, AI coding assistant, contributor, and future team member builds software in a consistent, scalable, secure, and maintainable manner.

This is not merely a coding guide.

It is the engineering constitution of the platform.

---

# The Guavacheck Engineering Principles

Every engineering decision must satisfy the following principles.

1. Simplicity over cleverness

Simple systems survive.

Complex systems fail.

---

2. Architecture before implementation

Never ask:

"What code should I write?"

Ask:

"What domain owns this capability?"

---

3. Security by default

Security is never added later.

Authentication

Authorization

Encryption

Audit

Logging

Rate Limiting

Threat Detection

must exist before production deployment.

---

4. Documentation is code

If implementation changes,

documentation changes.

Documentation is part of the feature.

---

5. AI is a development partner

Austin

ChatGPT

Cursor

Copilot

Claude

are engineering tools.

They never replace engineering judgement.

---

6. One owner

Every capability has:

one owner

one module

one API

one responsibility

---

7. Everything observable

Every request produces

logs

metrics

traces

audit records

events

---

8. APIs are products

Every API should be usable by:

Mobile

Web

Austin

Institutions

Developers

Future systems

---

9. Long-term thinking

Never optimize for today if it damages tomorrow.

---

# Engineering Workflow

Every feature follows the same lifecycle.

Product

↓

Architecture

↓

API Design

↓

Database

↓

Security Review

↓

Implementation

↓

Testing

↓

Documentation

↓

Deployment

↓

Monitoring

↓

Feedback

↓

Iteration

---

# Development Standards

Every module contains:

README

Architecture

API

Schemas

Models

Services

Repositories

Events

Tests

Examples

Documentation

Every module should look familiar.

---

# Backend Standards

Controllers

Only HTTP.

Never business logic.

---

Services

Business rules.

No SQL.

---

Repositories

Persistence.

No HTTP.

---

Models

Storage.

No business rules.

---

Schemas

Validation.

Only validation.

---

Events

Immutable.

Versioned.

Published after successful transactions.

---

# Frontend Standards

Pages

Compose components.

No business logic.

---

Components

Reusable.

Independent.

Small.

---

Hooks

State

Data Fetching

Caching

Interaction

---

Utilities

Pure functions.

No UI.

---

# Mobile Standards

Mobile is not a smaller website.

Every API should assume:

intermittent connectivity

slow networks

offline capability

background synchronization

---

# AI Standards

Austin must:

Never own business data.

Never bypass IRONGATE.

Never call private services.

Always explain reasoning.

Always produce audit events.

---

# Institution Standards

Institutions never receive unrestricted access.

Everything flows through:

Institution API

↓

IRONGATE

↓

Permissions

↓

Business Services

↓

Events

↓

Response

---

# Database Standards

One owner.

One schema.

One migration history.

No cross-domain SQL.

---

# Logging Standards

Every log contains:

Timestamp

Service

Version

Environment

Request ID

Correlation ID

User

Institution

Duration

Status

Severity

Logs are structured JSON.

---

# Monitoring Standards

Metrics include:

Latency

Errors

Success Rate

Throughput

Memory

CPU

Database

Queue

Cache

Austin

Institutions

Billing

Search

Everything measurable.

---

# API Standards

REST first.

GraphQL optional.

Versioned.

Consistent.

Documented.

Authenticated.

Observable.

---

# Event Standards

Past tense.

Immutable.

Idempotent.

Versioned.

Example

property.created

passport.generated

institution.verified

payment.completed

---

# Git Standards

Feature branches.

Small pull requests.

Descriptive commits.

Protected main branch.

Tag releases.

Never commit secrets.

---

# Code Review Checklist

Architecture respected?

Security implemented?

Tests written?

Events emitted?

Logs added?

Metrics added?

Documentation updated?

Performance acceptable?

Backward compatibility maintained?

---

# Testing Pyramid

Unit Tests

↓

Integration Tests

↓

Contract Tests

↓

API Tests

↓

End-to-End Tests

↓

Manual Verification

Automation is preferred wherever practical.

---

# Performance Standards

Every feature should define:

Expected latency

Expected throughput

Cache strategy

Database impact

Scaling characteristics

---

# Release Process

Development

↓

Review

↓

Testing

↓

Staging

↓

Performance Validation

↓

Security Validation

↓

Production

↓

Monitoring

↓

Post Release Review

---

# Technical Debt

Technical debt is tracked.

Prioritized.

Scheduled.

Visible.

Hidden technical debt becomes operational risk.

---

# AI Coding Policy

AI-generated code is treated exactly like human-generated code.

Every change must:

Compile

Pass tests

Respect architecture

Include documentation

Follow security policies

No exceptions.

---

# Engineering Culture

Engineers optimize for:

Trust

Maintainability

Reliability

Readability

Security

Scalability

Not lines of code.

---

# Success Metrics

The engineering organization succeeds when:

New developers onboard quickly.

AI assistants generate correct code.

Features integrate predictably.

Architecture remains consistent.

Security incidents remain rare.

Deployments become routine.

Documentation remains accurate.

---

# Long-Term Vision

The engineering organization behind guavacheck should be capable of building and maintaining one of the world's most trusted Property Intelligence Platforms.

Every engineering decision should strengthen the platform's security, scalability, reliability, and long-term sustainability.