# Environment Configuration

Version: 1.0

Status: Living Document

Owner: Guava Inc.

Classification: Infrastructure

---

# Purpose

This document defines every environment variable used throughout guavacheck.

Environment variables provide configuration without exposing sensitive information in source code.

No secrets should ever be committed to Git.

---

# Philosophy

Configuration belongs outside the application.

Code should remain portable.

Secrets should remain private.

Every production environment should be reproducible using environment variables alone.

---

# Environment Types

guavacheck operates using multiple environments.

## Local

Developer workstation.

Purpose:

Development

Testing

Debugging

---

## Development

Shared engineering environment.

Purpose:

Feature integration

Testing

Internal QA

---

## Staging

Production simulation.

Purpose:

Acceptance testing

Deployment validation

Performance verification

---

## Production

Live environment.

Purpose:

Real users

Real data

Maximum reliability

---

# Frontend Variables

## Supabase

```env
NEXT_PUBLIC_SUPABASE_URL=https://gxrslgddffdslvmemtqa.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imd4cnNsZ2RkZmZkc2x2bWVtdHFhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQ5ODUwMTEsImV4cCI6MjA5MDU2MTAxMX0.hJ4w6e5TgkkkF3QuRcGpIwG0cyMMCj1xImzJ-J-Bz2M
```

These variables are safe for browser access.

---

## Application

```env
NEXT_PUBLIC_APP_NAME=guavacheck

NEXT_PUBLIC_APP_URL=https://guavacheck.com

NEXT_PUBLIC_API_URL=https://api.guavacheck.com
```

---

## Analytics

```env
NEXT_PUBLIC_ANALYTICS_ENABLED=true
```

Future providers may include:

Vercel Analytics

Google Analytics

PostHog

---

# Backend Variables

## Database

```env
DATABASE_URL=
```

---

## Supabase

```env
SUPABASE_URL=https://gxrslgddffdslvmemtqa.supabase.co

SUPABASE_SERVICE_ROLE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imd4cnNsZ2RkZmZkc2x2bWVtdHFhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQ5ODUwMTEsImV4cCI6MjA5MDU2MTAxMX0.hJ4w6e5TgkkkF3QuRcGpIwG0cyMMCj1xImzJ-J-Bz2M

# OpenAI
OPENAI_API_KEY=YOUR_OPENAI_API_KEY

# Anthropic
ANTHROPIC_API_KEY=YOUR_ANTHROPIC_API_KEY

# Google Gemini
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

Never expose the Service Role Key to the frontend.

---

## Authentication

```env
JWT_SECRET=

SESSION_SECRET=
```

Secrets should be generated using cryptographically secure randomness.

---

## Austin

```env
AUSTIN_ENABLED=true

AUSTIN_MODEL=gpt-5.5

AUSTIN_MEMORY_ENABLED=true

AUSTIN_LOG_LEVEL=info
```

Austin configuration should remain centralized.

---

## OpenAI

```env
OPENAI_API_KEY=
```

Future AI providers may include:

Anthropic

Google Gemini

Azure OpenAI

Local Models

---

## Payments

```env
STRIPE_SECRET_KEY=

PAYSTACK_SECRET_KEY=

FLUTTERWAVE_SECRET_KEY=
```

Only enabled providers require configuration.

---

## Email

```env
SMTP_HOST=

SMTP_PORT=

SMTP_USERNAME=

SMTP_PASSWORD=

SMTP_FROM=
```

---

## Maps

```env
GOOGLE_MAPS_API_KEY=
```

Future mapping providers may also be supported.

---

## Storage

```env
STORAGE_PROVIDER=supabase
```

Future values:

aws

cloudflare

azure

---

## Monitoring

```env
SENTRY_DSN=

LOG_LEVEL=info

METRICS_ENABLED=true
```

---

## Feature Flags

```env
FEATURE_COMMUNITY=true

FEATURE_MARKETPLACE=true

FEATURE_INVESTMENT=true

FEATURE_VERIFICATION=true

FEATURE_AUSTIN=true
```

Feature flags allow controlled rollout of new capabilities.

---

# Security Rules

Never commit:

API Keys

Passwords

Secrets

Private Certificates

Database Credentials

Service Role Keys

Encryption Keys

JWT Secrets

These values belong only in secure environment management systems.

---

# File Naming

Recommended structure:

```
.env.example

.env.local

.env.development

.env.staging

.env.production
```

Only `.env.example` should be committed to the repository.

---

# Validation

Application startup should verify:

Required variables exist

Required formats are valid

Secrets are present

URLs are valid

Missing configuration should stop startup.

---

# Rotation

Sensitive credentials should be rotated periodically.

Rotation should include:

API Keys

JWT Secrets

Database Passwords

SMTP Credentials

Service Tokens

Compromised credentials should be replaced immediately.

---

# Disaster Recovery

Environment variables should be:

Backed up securely

Documented

Version controlled (excluding secret values)

Recoverable

Production secrets should never exist only in one location.

---

# Austin Startup Requirements

Austin should verify:

Database

Authentication

AI Provider

Storage

Monitoring

Scheduler

Environment Configuration

If any required variable is missing:

Austin should refuse startup and report the missing configuration.

---

# Engineering Principles

Environment variables should be:

Consistent

Documented

Minimal

Secure

Portable

No engineer should need to modify source code simply to change configuration.

---

# Final Principle

Configuration defines behaviour.

Behaviour defines reliability.

Reliability builds trust.

---

© 2026 Guava Inc.

Intelligence with integrity.

Technology with purpose.

Trust above everything.