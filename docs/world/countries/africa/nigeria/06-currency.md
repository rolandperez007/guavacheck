# Nigeria — Currency

# Purpose

This document defines Nigeria's monetary system, currency standards, payment ecosystem, exchange-rate behaviour, and financial conventions for the Guava World Engine.

It powers:

- Finance District
- Commerce Market
- Mortgage Engine
- Currency Engine
- Investor District
- Austin AI
- Payment Engine
- Analytics Engine

---

# Official Currency

| Property | Value |
|----------|-------|
| Currency Name | Nigerian Naira |
| ISO Code | NGN |
| ISO Numeric | 566 |
| Symbol | ₦ |
| Subunit | Kobo |
| Subunits per Unit | 100 |
| Decimal Places | 2 |

---

# Monetary Authority

Institution

Central Bank of Nigeria (CBN)

Responsibilities

- Monetary Policy
- Currency Issuance
- Inflation Control
- Foreign Exchange Regulation
- Banking Supervision
- Payment System Oversight

---

# Legal Tender

The Nigerian Naira is the sole legal tender recognised within Nigeria.

Transactions are commonly denominated in:

- Naira
- Kobo

---

# Currency Denominations

## Coins

- 50 Kobo
- ₦1
- ₦2

## Banknotes

- ₦5
- ₦10
- ₦20
- ₦50
- ₦100
- ₦200
- ₦500
- ₦1000

---

# Exchange Rate

Exchange rate regime

Managed Float

Common Reference Currencies

- USD
- GBP
- EUR
- CNY

Austin should always retrieve live exchange rates through the Currency Engine rather than relying on static values.

---

# Inflation

Nigeria experiences periodic inflationary cycles.

Austin should:

- Estimate purchasing power
- Adjust construction costs
- Forecast investment returns
- Calculate inflation-adjusted valuations

---

# Payment Ecosystem

Major Payment Types

- Cash
- Bank Transfer
- Debit Card
- Credit Card
- USSD
- QR Payments
- Mobile Wallets
- Instant Payments

---

# Payment Networks

Major Networks

- NIBSS
- Nigeria Inter-Bank Settlement System

Card Schemes

- Verve
- Visa
- Mastercard

---

# Major Payment Providers

Examples

- Paystack
- Flutterwave
- Moniepoint
- Interswitch
- PalmPay
- Opay
- Kuda

Guava should support integration through modular payment providers.

---

# Digital Banking

Nigeria has one of Africa's fastest-growing digital banking ecosystems.

Major Digital Banks

- Kuda
- VFD
- Sparkle
- Rubies

---

# Foreign Exchange

Austin should recognise multiple FX environments including:

- Official Market
- Authorised Dealer Market
- Market-derived reference rates

Historical exchange-rate data should be maintained separately by the Currency Engine.

---

# Currency Formatting

Display Examples

₦1,000

₦15,250

₦250,000.50

Formatting Rules

- Comma thousands separator
- Two decimal places where applicable
- Currency symbol precedes value

---

# Guava Currency Engine

The Currency Engine should support:

- Live FX conversion
- Historical FX lookup
- Multi-currency pricing
- Inflation adjustments
- Mortgage calculations
- International comparisons

---

# Austin Intelligence

Austin references this document to:

- Convert currencies
- Price international properties
- Estimate affordability
- Calculate investment returns
- Compare markets globally

---

# Related Engines

Currency Engine

Finance District

Commerce Market

Mortgage Engine

Investor District

Austin Tower

---

# Status

Reference Currency Profile

Production Ready

Version 1.0