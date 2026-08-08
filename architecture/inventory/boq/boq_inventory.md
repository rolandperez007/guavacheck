# BOQ Intelligence Inventory

## Purpose

Canonical inventory of all existing Bill of Quantities, quantity takeoff,
construction costing, estimation, and BOQ-generation capabilities in guavacheck.

## Existing Discovery Targets

- BOQ
- Bill of Quantities
- Quantity Takeoff
- Quantity Calculation
- Material Quantity
- Construction Cost
- Cost Estimate
- Estimate
- Pricing
- BOQ Service
- BOQ Tool
- BOQ Planner
- BOQ Intent Classification

## Known Existing Components

- lib/austin/services/BOQService.ts
- services/austin/BOQService.ts
- lib/austin/IntentClassifier.ts
- lib/austin/Planner.ts
- lib/austin/ToolRegistry.ts
- app/core/execution/job_engine.py
- ConstructionPricingModel.ts

## Classification

Every discovered implementation must be classified as:

1. Canonical candidate
2. Supporting implementation
3. Duplicate
4. Legacy
5. Documentation only
6. Test
7. Unknown

## Required Future Capabilities

- Project quantities
- Element quantities
- Material quantities
- Labour quantities
- Waste factors
- Assemblies
- BOQ line items
- Unit rates
- Regional pricing
- Currency conversion
- Cost summaries
- Editable BOQ
- BOQ versioning
- Audit trail
- Confidence/provenance

## Important Rule

No new BOQ implementation should be created until this inventory has
been reviewed and a canonical implementation path has been selected.