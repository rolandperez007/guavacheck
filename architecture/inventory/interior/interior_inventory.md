# Interior Intelligence Inventory

## Purpose

Inventory all existing interior-design intelligence, room specifications,
finishes, furniture, lighting, materials and related systems.

## Known Existing Components

- app/brains/design/interior.py
- app/vision/engines/interior_engine.py
- app/vision/api/furniture.py
- app/vision/models/furniture.py
- app/vision/repositories/furniture_repository.py
- app/vision/schemas/furniture.py
- app/vision/prompts/interior_prompt.py
- components/os/world/Lighting.tsx
- components/os/world/LightingEngine.ts
- components/world/Lighting.tsx
- backend/digital_twin/wall.py

## Building Room Schemas

Known examples include:

- BuildingBathroom.schema.json
- BuildingBedroom.schema.json

## Required Categories

- Room type
- Room dimensions
- Spatial requirements
- Finishes
- Flooring
- Walls
- Ceilings
- Doors
- Joinery
- Furniture
- Lighting
- Electrical
- Plumbing
- Fixtures
- Appliances
- Materials
- Style
- Quality tier

## Critical Principle

Interior intelligence must produce structured specifications that can
ultimately resolve into construction assemblies and measurable quantities.