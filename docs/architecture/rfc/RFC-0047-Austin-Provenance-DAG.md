# RFC-0047

# Austin Provenance DAG

**Status:** Draft v1.0  
**Category:** Core Knowledge Architecture  
**System:** Austin Cognitive Operating System  
**Maintainer:** Guava Networks Limited

---

# Abstract

The Austin Provenance Directed Acyclic Graph (Provenance DAG) records the complete lineage of every fact, conclusion, recommendation, prediction, simulation, and cognitive decision produced by Austin.

While the Event Ledger answers:

> **"What happened?"**

and the Knowledge Graph answers:

> **"What is true?"**

the Provenance DAG answers:

> **"Why is it true?"**

Every validated piece of knowledge must possess an explainable ancestry.

Knowledge without provenance is constitutionally invalid.

---

# 1. Purpose

The Provenance DAG provides:

- knowledge lineage
- evidence tracking
- explainability
- reproducibility
- governance transparency
- auditability
- trust

---

# 2. Core Principle

Every knowledge object must be traceable back to its originating observations.

```
Observation

↓

Evidence

↓

Reasoning

↓

Knowledge
``` id="prov-core"

Austin never creates orphan knowledge.

---

# 3. Relationship to Tri-Part Memory

Austin's permanent memory consists of:

```
Event Ledger

↓

Knowledge Graph

↓

Provenance DAG
``` id="tripart"

The Provenance DAG links the other two together.

---

# 4. Why a DAG?

Austin uses a Directed Acyclic Graph because:

- knowledge has ancestry
- ancestry never loops
- multiple observations may support one conclusion
- one observation may influence many conclusions

Cycles are prohibited.

---

# 5. Provenance Nodes

Nodes may represent:

- observations
- evidence
- reasoning steps
- governance decisions
- simulations
- predictions
- knowledge objects

Each receives a unique identifier.

---

# 6. Provenance Edges

Edges describe dependency.

Examples:

```
supports

derived_from

validated_by

approved_by

generated_from

contradicted_by
``` id="edges"

Relationships preserve reasoning history.

---

# 7. Knowledge Lineage

Example:

```
Satellite Image

↓

Survey Report

↓

Ownership Registry

↓

Austin Verification

↓

Property Passport
``` id="lineage"

Every step remains permanently visible.

---

# 8. Evidence Accumulation

Knowledge may depend upon multiple observations.

```
Observation A

Observation B

Observation C

↓

Validated Knowledge
``` id="evidence"

Austin records every contributing source.

---

# 9. Contradictions

Conflicting evidence creates branching.

```
Registry

↓

Owner A

Survey

↓

Owner B
``` id="contradiction"

Governance determines which branch becomes authoritative.

History remains preserved.

---

# 10. Simulation Provenance

Predictions include their own lineage.

Example:

```
Current Building

↓

Simulation

↓

Predicted Value
``` id="simulation"

Synthetic knowledge never loses its ancestry.

---

# 11. Explainability

Austin answers:

```
Why?

↓

Evidence

↓

Reasoning

↓

Decision
``` id="explain"

Every recommendation becomes fully reconstructable.

---

# 12. Human Contributions

Human reviewers become provenance nodes.

Example:

```
Engineer

↓

Inspection

↓

Approval

↓

Knowledge
``` id="human"

Institutional trust becomes part of cognitive memory.

---

# 13. GuavaCheck Example

Construction Cost Estimate:

```
BOQ

↓

Material Prices

↓

Market Index

↓

Currency Engine

↓

Construction Estimate
``` id="guava"

Every estimate remains explainable.

---

# 14. Institutional Benefits

Banks may verify:

- valuation origin
- ownership evidence
- inspection history
- approval chain

Insurance companies verify:

- inspection lineage
- maintenance records
- structural history

Every institution reasons from transparent provenance.

---

# 15. Relationship With Other RFCs

Depends on:

- RFC-0024 Knowledge Requires Provenance
- RFC-0042 Knowledge Evolution
- RFC-0045 Event Ledger
- RFC-0046 Knowledge Graph

Supports:

- Explainability
- Audit
- Simulation
- Prediction
- Institutional Trust

---

# 16. Architectural Importance

Most AI systems explain outputs poorly.

Austin records every reasoning dependency.

Nothing enters long-term knowledge without a visible ancestry.

The Provenance DAG transforms explainability from documentation into architecture.

---

# 17. Summary

The Provenance DAG preserves Austin's intellectual ancestry.

Every fact.

Every recommendation.

Every prediction.

Every simulation.

Every conclusion.

Austin always knows why it believes what it believes.