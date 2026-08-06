
# RFC-0016

# Austin Canonical Message Format (ACMF)

Status: Draft v1.0  
Category: Core Kernel Communication Specification  
System: Austin Cognitive Operating System  
Maintainer: Guava Networks Limited

---

# Abstract

Austin Canonical Message Format (ACMF) defines the standard communication structure between the Austin Kernel, intelligence engines, cognitive spaces, memory systems, and external integrations.

ACMF ensures that every cognitive interaction carries not only data, but also context, intent, governance requirements, provenance references, and confidence information.

Austin messages are not simple data packets.

They are governed cognitive envelopes.

---

# 1. Purpose

ACMF provides a universal communication contract for:

- engine communication
- cognitive state transitions
- memory operations
- governance validation
- external integrations
- audit processes

The format is independent of:

- programming language
- transport protocol
- model provider
- database technology

---

# 2. Core Principle

Every Austin message must answer:

Who created this?

What is being communicated?

Why does it exist?

What evidence supports it?

What authority governs it?

What action is requested?

---

# 3. Cognitive Envelope

All Austin communications use a Cognitive Envelope.

Structure:

Cognitive Envelope

{
Identity,
Intent,
Context,
Payload,
Provenance,
Confidence,
Governance,
Execution
}

---

# 4. Message Identity

Every message requires:


message_id

timestamp

source

destination

correlation_id

transaction_id

Purpose:

- traceability
- auditing
- distributed coordination

---

# 5. Intent Layer

The intent layer describes the purpose of communication.

Examples:

OBSERVE

ANALYZE

PREDICT

SIMULATE

REQUEST

PROPOSE_CHANGE

COMMIT

ROLLBACK

SUSPEND

Austin distinguishes between information exchange and cognitive action.

---

# 6. Context Layer

Context provides the information required for reasoning.

Includes:

user_context

system_state

active_cognitive_space

related_entities

environment_state

Context prevents isolated reasoning.

---

# 7. Payload Layer

Payload contains the actual information being transmitted.

Examples:

- property data
- analysis results
- generated designs
- valuation models
- engine outputs

Payload alone does not represent truth.

It requires governance metadata.

---

# 8. Provenance Layer

Every message may contain provenance references.

Example:

provenance:

{
observation_sources,
evidence_nodes,
reasoning_chain,
originating_events
}

This connects ACMF messages to the Provenance DAG.

---

# 9. Confidence Layer

Cognitive outputs must communicate uncertainty.

Example:

confidence:

{
score: 0.86,

factors:
[
    evidence_quality,
    source_reliability,
    model_accuracy
]


}


Confidence informs decisions.

It does not replace evidence.

---

# 10. Governance Layer

The governance layer defines permitted actions.

Example:

governance:

{
requires_consent: true,

requires_human_review: false,

authority_level: advisory

}

---

# 11. Execution Layer

The execution layer defines requested operations.

Examples:

execute_engine

update_memory

create_simulation

submit_commit_proposal

---

# 12. Cognitive Transaction Support

ACMF supports Austin transaction states:

## Commit

Validated cognitive change.

---

## Rollback

Rejected or invalid change.

---

## Suspend

Unresolved state awaiting additional information.

---

# 13. Example Cognitive Envelope

{
message_id:
"MSG-001",

intent:
"PROPOSE_CHANGE",

source:
"valuation_engine",

payload:
{
    property_value:
    500000
},

provenance:
{
    sources:
    [
        "market_data",
        "property_records"
    ]
},

confidence:
0.89,

governance:
{
    requires_review:
    true
}

}

---

# 14. Relationship With Austin Architecture

ACMF connects:

Intelligence Layer

↓

Cognitive Bus

↓

Coordination Layer

↓

Constitutional Layer

↓

State Layer

---

# 15. GuavaCheck Implementation

Within guavacheck, ACMF enables:

- property intelligence exchange
- valuation engine communication
- AI design generation
- investment analysis
- institutional integrations

Every intelligence operation becomes traceable.

---

# 16. Summary

Austin messages are not simple communication objects.

They are governed cognitive transactions.

ACMF provides the language through which Austin engines, memory systems, and external platforms communicate with accountability.

