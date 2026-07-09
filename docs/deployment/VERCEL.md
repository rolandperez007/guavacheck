# Vercel Deployment Guide

Version: 1.0

Status: Living Document

Owner: Guava Inc.

Classification: Frontend Infrastructure

---

# Purpose

This document defines the official deployment strategy for the guavacheck frontend on Vercel.

It covers:

- Project configuration
- Build process
- Environment variables
- Domain management
- Monitoring
- Rollback
- Production best practices

---

# Overview

The guavacheck frontend is built with:

- Next.js
- React
- TypeScript

Production hosting is provided by Vercel.

Vercel is responsible for:

- Building the application
- CDN distribution
- Edge optimization
- HTTPS
- Preview deployments
- Production deployments

---

# Repository

Official Repository

guavacheck

Primary Branch

main

Development Branch

develop

Feature Branches

feature/*

Bug Fixes

bugfix/*

Hotfixes

hotfix/*

---

# Deployment Flow

Developer

↓

Git Commit

↓

GitHub

↓

GitHub Actions

↓

Quality Checks

↓

Vercel Build

↓

Preview Deployment

↓

Approval

↓

Production Deployment

↓

Austin Health Verification

↓

Platform Online

---

# Build Command

```bash
npm run build
```

---

# Development Command

```bash
npm run dev
```

---

# Install Command

```bash
npm install
```

---

# Output

Next.js Production Build

---

# Environment Variables

Production variables should never be committed.

Examples include:

NEXT_PUBLIC_SUPABASE_URL

NEXT_PUBLIC_SUPABASE_ANON_KEY

OPENAI_API_KEY

SUPABASE_SERVICE_ROLE_KEY

DATABASE_URL

JWT_SECRET

PAYMENT_PROVIDER_KEY

GOOGLE_MAPS_KEY

SMTP_CONFIGURATION

Secrets should only exist inside:

- Vercel Environment Variables
- Secure Secret Managers

---

# Environment Separation

Development

Independent configuration.

---

Preview

Testing environment.

Safe for reviewers.

---

Production

Live user environment.

Highest security level.

---

# Domains

Primary Domain

guavacheck.com

Future Regional Domains

africa.guavacheck.com

eu.guavacheck.com

us.guavacheck.com

asia.guavacheck.com

Additional domains may be introduced as the platform expands.

---

# HTTPS

HTTPS is mandatory.

HTTP should automatically redirect.

TLS certificates should remain managed through Vercel.

---

# Build Validation

Every deployment should verify:

Next.js compilation

TypeScript compilation

Static generation

Dynamic routes

Image optimization

Asset integrity

Environment configuration

---

# Performance

Monitor:

Core Web Vitals

Largest Contentful Paint

Interaction to Next Paint

Cumulative Layout Shift

JavaScript bundle size

Image optimization

Font loading

Route performance

---

# Preview Deployments

Every Pull Request should automatically create:

Preview URL

Build Logs

Deployment Summary

Performance Metrics

Preview deployments should never affect production data.

---

# Rollback

Production rollback should occur immediately if:

Critical frontend failure

Authentication failure

Broken routing

Austin unavailable

Environment misconfiguration

Rollback should restore the previous healthy deployment.

---

# Monitoring

Monitor:

Deployment success

Build duration

Edge performance

Traffic

Error rate

API latency

Austin availability

Authentication

User sessions

Frontend uptime

---

# Austin Integration

The frontend should verify Austin availability during startup.

If Austin is unavailable:

Display a graceful fallback.

Provide clear messaging.

Allow non-AI functionality where possible.

Austin should never fail silently.

---

# Security

Never expose:

Private API keys

Service role keys

Database credentials

Internal endpoints

Secrets

Only NEXT_PUBLIC variables may be exposed to the browser.

---

# Deployment Checklist

Before Production

✅ Build successful

✅ Tests passing

✅ Environment variables verified

✅ Documentation updated

✅ Austin healthy

✅ API healthy

✅ Database healthy

✅ Monitoring active

---

# Disaster Recovery

If deployment fails:

Pause deployment

Restore previous release

Verify database

Verify authentication

Verify Austin

Verify monitoring

Resume only after validation.

---

# Long-Term Vision

Future deployment capabilities include:

Multi-region deployment

Edge AI inference

Geo-routing

Feature flags

Canary releases

Blue-green deployment

Automatic rollback

Traffic shaping

Global CDN optimization

---

# Engineering Principle

A successful deployment is measured by the user experience after deployment—not merely by a successful build.

Reliability is a feature.

Trust is earned with every release.

---

© 2026 Guava Inc.

Intelligence with integrity.

Technology with purpose.

Trust above everything.