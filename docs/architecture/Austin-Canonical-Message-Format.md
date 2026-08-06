# Austin Canonical Message Format (ACMF)

**Specification:** RFC Candidate 0016

**Status:** Draft v1.0

**Applies To:** Austin Cognitive Operating System

**Maintainer:** Guava Networks Limited

---

# Overview

The Austin Canonical Message Format (ACMF) defines the universal language spoken inside the Austin Cognitive Operating System.

Every engine communicates using ACMF.

No engine communicates directly using proprietary formats.

This guarantees interoperability across:

- Engines
- SDKs
- Languages
- Clouds
- Industries
- Decades

---

# Philosophy

Every cognitive interaction is a structured message.

Not raw JSON.

Not arbitrary payloads.

A complete cognitive envelope.

---

# Objectives

ACMF guarantees:

Identity

Intent

Context

Evidence

Confidence

Governance

Traceability

Determinism

---

# Message Lifecycle

```
Engine

↓

Create ACMF Envelope

↓

Kernel Validation

↓

Scheduler

↓

Cognitive Bus

↓

Receiving Engine

↓

Kernel Commit
```

---

# High-Level Structure

```
Envelope

├── Header

├── Identity

├── Intent

├── Context

├── Payload

├── Evidence

├── Confidence

├── Governance

├── Provenance

├── Budget

├── Metadata

└── Signature
```

---

# Header

Contains transport information.

Example

Message ID

Timestamp

Version

Correlation ID

Request ID

Engine Origin

Destination

---

# Identity Section

Defines

Who

or

What

the message concerns.

Examples

Property

User

Engine

Organization

Simulation

Knowledge Object

---

# Intent Section

Defines

Why

the message exists.

Examples

Observe

Verify

Predict

Reason

Simulate

Explain

Plan

Approve

Reject

---

# Context Section

Carries active reasoning context.

Examples

Conversation Context

Property Context

Organization Context

Location Context

Historical Context

Legal Context

Financial Context

Execution Context

---

# Payload

Contains the actual working data.

Examples

Inspection Report

Satellite Image

Property Attributes

Financial Records

Sensor Readings

Text

Video

Image

---

# Evidence Section

Lists supporting evidence.

Each evidence item contains

Source

Authority

Timestamp

Verification Status

Confidence

Hash

---

# Confidence Section

Defines probabilistic certainty.

Example

```
Overall Confidence

0.93

Reasoning Confidence

0.91

Observation Confidence

0.97

Prediction Confidence

0.84
```

Confidence evolves throughout execution.

---

# Governance Section

Defines applicable policies.

Examples

Applicable Laws

Privacy Classification

Human Approval Required

Jurisdiction

Risk Level

Compliance Tags

---

# Provenance Section

Contains lineage references.

Fields include

Parent Message

Knowledge Node

Observation ID

Evidence Chain

Lineage Hash

---

# Budget Section

Defines execution limits.

Examples

Maximum Time

Maximum Tokens

Maximum Cost

Maximum Engine Depth

Maximum Recursion

Scheduler enforces these automatically.

---

# Metadata

Optional extensions.

Examples

Language

Currency

Measurement System

Locale

Region

Time Zone

Industry

---

# Digital Signature

Messages may be signed.

Supports

Integrity

Authenticity

Non-Repudiation

Zero Trust

---

# Validation Pipeline

Every ACMF message passes through

Schema Validation

↓

Identity Validation

↓

Governance Validation

↓

Trust Validation

↓

Budget Validation

↓

Kernel Acceptance

---

# Message States

Created

Validated

Queued

Running

Suspended

Completed

Rolled Back

Committed

Archived

---

# Suspend Support

Messages may enter

Suspend

without losing state.

Entire cognitive context remains preserved.

---

# Versioning

ACMF is versioned.

Example

```
ACMF

v1.0

↓

v1.1

↓

v2.0
```

Backward compatibility remains mandatory.

---

# Serialization

ACMF is independent of transport.

Possible representations

JSON

Protocol Buffers

Avro

FlatBuffers

Binary

CBOR

Internal Memory Objects

---

# Industry Independence

Healthcare

Property

Agriculture

Manufacturing

Finance

Education

all use identical ACMF envelopes.

Only payloads differ.

---

# Relationship to the Cognitive Bus

ACMF defines

the message.

The Cognitive Bus defines

transport.

Scheduler defines

execution.

Kernel defines

truth.

---

# Constitutional Compliance

Every ACMF message must satisfy

Law I

Reality

Law III

Provenance

Law VII

Explainability

Law XV

Governance

Law XVII

Human Authority

before Persistent State changes.

---

# Summary

The Austin Canonical Message Format is the universal language of cognition inside Austin.

Every engine speaks ACMF.

Every message carries not only data,

but identity,

intent,

context,

confidence,

evidence,

provenance,

governance,

and execution constraints.

It is the protocol that enables Austin to scale across industries while remaining one coherent Cognitive Operating System.