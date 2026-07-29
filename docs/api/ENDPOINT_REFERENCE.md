# Platform Endpoint Reference

Version: 1.0

---

# Authentication

POST   /auth/register

POST   /auth/login

POST   /auth/logout

POST   /auth/refresh

GET    /auth/me

---

# Users

GET    /users

GET    /users/{id}

PUT    /users/{id}

DELETE /users/{id}

---

# Property Passport

POST   /passport

GET    /passport/{id}

PUT    /passport/{id}

DELETE /passport/{id}

GET    /passport/search

GET    /passport/{id}/history

GET    /passport/{id}/dna

---

# Twin Studio

POST   /twin

GET    /twin/{id}

PUT    /twin/{id}

POST   /twin/{id}/publish

POST   /twin/{id}/assets

DELETE /twin/{id}/assets/{asset}

GET    /twin/{id}/versions

POST   /twin/{id}/restore

---

# Construction

POST   /construction/project

GET    /construction/project/{id}

PUT    /construction/project/{id}

POST   /construction/milestone

POST   /construction/inspection

---

# Commerce

GET    /commerce/catalogue

GET    /commerce/suppliers

POST   /commerce/orders

GET    /commerce/orders/{id}

POST   /commerce/installations

---

# Finance

GET    /finance/products

POST   /finance/prequalification

POST   /finance/mortgage

POST   /finance/construction-loan

POST   /finance/escrow

---

# Investor

GET    /investor/dashboard

GET    /investor/opportunities

POST   /investor/watchlist

GET    /investor/portfolio

---

# Trust Exchange

POST   /trust/verify

POST   /trust/offer

POST   /trust/accept

POST   /trust/transfer

GET    /trust/history

---

# Distress

POST   /distress/listing

GET    /distress/listings

POST   /distress/offer

POST   /distress/accept

---

# Knowledge

GET    /knowledge/articles

GET    /knowledge/courses

GET    /knowledge/search

---

# Community

GET    /community/posts

POST   /community/posts

POST   /community/comments

GET    /community/events

---

# Government

GET    /government/registry

GET    /government/permits

GET    /government/compliance

---

# Wallet

GET    /wallet

POST   /wallet/deposit

POST   /wallet/withdraw

GET    /wallet/history

---

# Billing & Payments

POST   /billing/checkout

POST   /billing/webhook/stripe

POST   /billing/webhook/paystack

POST   /billing/webhook/flutterwave

GET    /billing/history

---

# Notifications

GET    /notifications

POST   /notifications/read

POST   /notifications/preferences

---

# Austin AI

POST   /austin/chat

POST   /austin/workflow

POST   /austin/recommendations

POST   /austin/property-analysis

POST   /austin/investment-analysis

POST   /austin/construction-analysis

---

# Search

GET    /search

GET    /search/properties

GET    /search/commerce

GET    /search/investors

---

# Administration

GET    /admin/dashboard

GET    /admin/analytics

GET    /admin/system-health

POST   /admin/jobs

GET    /admin/events