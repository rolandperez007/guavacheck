# District Intelligence Inventory

## Purpose

Inventory all district, zone, urban, neighbourhood, planning and
location intelligence.

## Required Categories

- District identity
- Geography
- Planning
- Zoning
- Land use
- Density
- Height
- Setbacks
- Plot constraints
- Infrastructure
- Flood risk
- Wind exposure
- Seismic exposure
- Market positioning
- Architectural character
- Interior character
- Construction standards
- Finish standards
- Material preferences
- Security expectations
- Landscape expectations
- Cost tier

## Known Existing Components

- lib/world/districts.ts
- tests/test_district_loader.py
- world/construction/geography/flood_zones.json
- world/construction/geography/seismic_zones.json
- world/construction/geography/wind_zones.json

## Critical Principle

Districts must be represented primarily as structured data and profiles,
not bespoke application code.

## Future Flow

Location
→ District Profile
→ Applicable Rules
→ Building Constraints
→ Architectural Profile
→ Interior Profile
→ Construction Assemblies
→ BOQ