# Canonical Interior Intelligence

## Purpose

Define the canonical interior intelligence layer connecting rooms, finishes,
materials, furniture, lighting and construction assemblies.

---

# Interior Intelligence Is Structured

Interior intelligence must not exist solely as prompts or rendering logic.

It must produce structured specifications.

---

# Interior Specification

A room specification may contain:

- room type
- dimensions
- spatial requirements
- finish specification
- flooring
- wall finish
- ceiling
- doors
- joinery
- furniture
- lighting
- electrical
- plumbing
- fixtures
- appliances
- materials
- style
- quality tier

---

# Interior Resolution

Room
→ Interior Profile
→ Finish Specification
→ Material Specification
→ Assembly

---

# Example

Master Bedroom

→ Flooring
→ Premium Porcelain Tile

→ Walls
→ Premium Paint System

→ Ceiling
→ Gypsum Ceiling Assembly

→ Lighting
→ Recessed LED Assembly

→ Joinery
→ Fitted Wardrobe Assembly

Each component may resolve into a measurable construction assembly.

---

# Interior Codes

Interior codes must be treated as canonical identifiers rather than arbitrary
strings embedded throughout application code.

An interior code should eventually identify a structured specification.

Example conceptual structure:

INTERIOR
  ROOM
    FINISH
      MATERIAL
        ASSEMBLY

---

# Interior Code Responsibilities

An interior code may identify:

- room specification
- finish specification
- material specification
- quality tier
- style family
- assembly mapping

---

# District Relationship

Districts may provide recommended interior profiles.

Example:

District
→ Luxury Interior Profile
→ Master Bedroom Profile
→ Premium Finish Set

The district should not duplicate every individual interior component.

---

# BOQ Relationship

Interior specifications resolve into measurable assemblies.

Interior
→ Assembly
→ Component
→ Quantity Rule
→ BOQ

This is the critical bridge between interior design and construction costing.

---

# Rendering Relationship

Rendering systems may consume interior specifications.

Rendering should not become the source of truth for construction quantities.

Correct:

Interior Specification
→ Rendering

and independently:

Interior Specification
→ Assembly
→ BOQ

---

# Source of Truth

The structured interior specification is authoritative.

Prompts, images and renders are representations of that specification.