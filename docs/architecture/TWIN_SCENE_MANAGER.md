# Twin Studio Scene Manager

Version: 1.0

---

# Purpose

The Scene Manager coordinates every digital twin within Twin Studio.

It is responsible for loading, rendering, updating and synchronising 3D scenes while remaining independent of business logic.

---

# Responsibilities

• Load property twins

• Manage scene hierarchy

• Coordinate cameras

• Lighting

• Materials

• Terrain

• Object visibility

• Level of Detail (LOD)

• Scene optimisation

• Event synchronisation

---

# Scene Structure

Twin Studio

↓

Scene

↓

Property

↓

Building

↓

Floor

↓

Room

↓

Component

↓

Asset

---

# Scene Objects

Land

Buildings

Roads

Furniture

Vegetation

Vehicles

Utilities

Annotations

Measurements

Inspection Points

Construction Equipment

---

# Engine Integration

Property Passport

↓

Twin Studio

↓

Construction Engine

↓

Commerce Engine

↓

Austin Intelligence

---

# Performance Goals

Lazy Loading

Object Caching

Frustum Culling

LOD Rendering

Texture Streaming

GPU Optimisation

Incremental Updates

---

# Events

SceneLoaded

SceneUpdated

AssetAdded

AssetRemoved

ObjectModified

TwinSaved

SceneClosed