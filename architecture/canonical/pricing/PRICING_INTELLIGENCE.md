# Canonical Pricing Intelligence

## Purpose

Define the pricing layer consumed by BOQ intelligence.

---

# Pricing Is Separate From Quantity

Quantity determines:

WHAT
HOW MUCH
UNIT

Pricing determines:

HOW MUCH IT COSTS
IN WHICH MARKET
IN WHICH CURRENCY
AT WHICH TIME

---

# Pricing Inputs

Pricing may consider:

- material
- labour
- equipment
- location
- region
- currency
- supplier
- contractor tier
- market condition
- date
- escalation
- tax
- logistics

---

# Pricing Pipeline

BOQ Quantity
→ Applicable Rate
→ Regional Adjustment
→ Currency
→ Taxes
→ Line Amount

---

# Regional Pricing

A material must not have one universal hard-coded price.

Example conceptual structure:

Material
→ Market
→ Region
→ Currency
→ Effective Date
→ Unit Rate
→ Source

---

# Auditability

Every rate should have provenance.

The system should be able to answer:

- Where did this rate originate?
- When was it valid?
- What currency was used?
- What region was applied?
- What supplier or source was used?