# Provenance Intelligence

## Purpose

Provenance Intelligence provides the traceability layer for GuavaCheck's
construction intelligence.

Every significant AI, rule, calculation, quantity, assembly, pricing and
BOQ decision should be traceable to its source.

---

# Core Principle

Every intelligent result should answer:

What produced this?

What source was used?

Which rule was applied?

Which version was active?

When was it produced?

How confident are we?

---

# Provenance Chain

Source
→
Knowledge
→
Rule
→
Engine
→
Calculation
→
Result
→
Consumer

---

# Provenance Identity

A provenance record may contain:

- provenance_id
- source_id
- source_type
- source_uri
- source_version
- source_date
- source_provider
- engine
- engine_version
- rule_id
- rule_version
- input_hash
- output_hash
- created_at
- confidence

---

# Source Types

Sources may include:

- structured database
- government data
- standards
- district profile
- building model
- user input
- uploaded document
- CAD/BIM geometry
- AI-generated inference
- pricing provider
- market data
- internal knowledge
- manual override

---

# Confidence

Confidence must be associated with the relevant decision.

Confidence is not proof of correctness.

The system should distinguish:

- source confidence
- rule confidence
- geometry confidence
- calculation confidence
- pricing confidence
- final result confidence

---

# Human Overrides

Human modifications must preserve:

- original result
- modified result
- actor
- timestamp
- reason
- affected field
- previous version

---

# Versioning

Provenance records must support reproducibility.

Given the same:

- source versions
- rule versions
- engine versions
- input data
- configuration

the system should be able to identify the version of the result that
was produced.

---

# Cross-Domain Provenance

Provenance must connect:

District
→
Building
→
Interior
→
Assembly
→
Quantity
→
BOQ
→
Pricing
→
Estimate

This allows Austin to explain not only the final estimate but the
reasoning and source chain behind it.

---

# Canonical Ownership

Provenance Intelligence owns:

- provenance records
- source references
- version references
- calculation lineage
- audit metadata
- confidence metadata
- override history

It does not own the underlying domain knowledge.

---

# Architectural Principle

Provenance is cross-cutting infrastructure.

It must not be duplicated independently inside every engine.

Individual domains produce provenance metadata.

The provenance layer stores and resolves the lineage.

---

# Canonical Principle

If a construction result cannot be traced, it should not be treated as
fully auditable intelligence.
