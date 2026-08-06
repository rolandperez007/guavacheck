# Dashboard Presentation Contract

Version: 1.0

---

## Purpose

The dashboard is not responsible for business logic.

Its responsibility is to present the current state of the Guava platform.

Every widget represents backend state.

The frontend should never compute business intelligence that already exists within backend services.

---

# Data Flow

Supabase

↓

Repository

↓

Service

↓

Workflow

↓

Austin

↓

API

↓

Frontend

↓

Dashboard Widget

---

# Widget Rules

Widgets never query multiple APIs independently.

Instead they consume Dashboard DTOs.

Example

DashboardResponse

    profile

    recommendations

    passport

    finance

    notifications

    portfolio

    analytics

    tasks

---

# Refresh Strategy

Widgets subscribe to

Passport Events

Workflow Events

Institution Events

Billing Events

Austin Events

Simulation Events

---

# Widget Categories

Navigation

Summary

Recommendations

Actions

Analytics

Community

Notifications

Finance

Property

Passport

Institution

Projects

Commerce

Settings

---

# Austin Panel

Austin is persistent.

Austin remembers conversation context.

Austin watches workflow state.

Austin watches notifications.

Austin watches institution permissions.

Austin watches current property.

Austin never loses context during navigation.

---

# Dashboard Principle

Everything is state driven.

Nothing is hardcoded.