# ENVIRONMENT VARIABLES

**Project:** guavacheck

**Organization:** Guava Networks Inc.

**Purpose:** Central reference for environment configuration.

---

# Philosophy

Environment variables contain deployment-specific configuration and secrets.

They must **never** be committed to version control.

Each deployment environment (Development, Staging, Production) should maintain its own values.

---

# Required Variables

## Application

```env
NODE_ENV=
NEXT_PUBLIC_APP_NAME=guavacheck
NEXT_PUBLIC_APP_URL=
NEXT_PUBLIC_API_URL=
PORT=
```

---

## Authentication

```env
NEXTAUTH_URL=
NEXTAUTH_SECRET=
JWT_SECRET=
SESSION_SECRET=
```

---

## Database

```env
DATABASE_URL=
DATABASE_HOST=
DATABASE_PORT=
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_SSL=
```

---

## Austin AI

```env
OPENAI_API_KEY=
OPENAI_MODEL=
OPENAI_EMBEDDING_MODEL=

ANTHROPIC_API_KEY=
GOOGLE_API_KEY=

AUSTIN_DEFAULT_MODEL=
AUSTIN_TEMPERATURE=
AUSTIN_MAX_TOKENS=
```

---

## Redis / Cache

```env
REDIS_URL=
REDIS_HOST=
REDIS_PORT=
REDIS_PASSWORD=
```

---

## Storage

```env
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION=
AWS_BUCKET=
```

Alternative providers may use equivalent variables.

---

## Email

```env
SMTP_HOST=
SMTP_PORT=
SMTP_USER=
SMTP_PASSWORD=
SMTP_FROM=
```

---

## SMS / Notifications

```env
TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
TWILIO_PHONE_NUMBER=
```

---

## Maps & Geolocation

```env
GOOGLE_MAPS_API_KEY=
MAPBOX_API_KEY=
```

---

## Payments

```env
STRIPE_SECRET_KEY=
STRIPE_WEBHOOK_SECRET=

PAYSTACK_SECRET_KEY=
PAYSTACK_PUBLIC_KEY=

FLUTTERWAVE_SECRET_KEY=
```

Only configure the providers in active use.

---

## Media

```env
MAX_UPLOAD_SIZE=
ALLOWED_FILE_TYPES=
IMAGE_PROCESSOR=
VIDEO_PROCESSOR=
```

---

## Logging

```env
LOG_LEVEL=
SENTRY_DSN=
```

---

## Feature Flags

```env
ENABLE_AUSTIN=
ENABLE_BUILDING_PASSPORT=
ENABLE_DISTRESS_ENGINE=
ENABLE_AI_COUNCIL=
ENABLE_MARKET_ENGINE=
ENABLE_MEDIA_ANALYSIS=
```

---

## Deployment

```env
VERCEL_URL=
VERCEL_ENV=
```

---

# Local Development

Create:

```text
.env.local
```

Never commit this file.

---

# Production

Store secrets using your hosting platform's secure secret management system.

Avoid hardcoding credentials.

Rotate secrets periodically.

---

# Validation

Application startup should verify that required variables are present and fail fast with clear error messages if mandatory configuration is missing.

---

# Security Guidelines

* Never expose server-only secrets to client-side code.
* Use the `NEXT_PUBLIC_` prefix only for values intended to be accessible in the browser.
* Rotate credentials regularly.
* Grant services the minimum permissions they require.
* Audit access to secrets where supported by the deployment platform.

---

# Maintenance

Whenever a new service is added to the platform:

1. Document its required environment variables.
2. Update `.env.example`.
3. Update deployment documentation.
4. Validate configuration during application startup.

---

**Maintained By:** Guava Networks Inc.

**Status:** Living Configuration Reference

**Last Updated:** June 2026
