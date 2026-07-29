# Twin Studio API Specification

Version: 1.0

---

# Purpose

Provide secure APIs for managing Digital Twins.

---

# Core Endpoints

POST /twin

Create Twin

---

GET /twin/{id}

Retrieve Twin

---

PUT /twin/{id}

Update Twin

---

POST /twin/{id}/publish

Publish Twin

---

POST /twin/{id}/assets

Upload Asset

---

DELETE /twin/{id}/assets/{asset}

Delete Asset

---

POST /twin/{id}/annotations

Create Annotation

---

GET /twin/{id}/versions

Retrieve Versions

---

POST /twin/{id}/restore

Restore Version

---

# Supported Assets

GLB

GLTF

OBJ

FBX

Textures

HDRI

Materials

---

# Events

TwinCreated

TwinSaved

TwinPublished

AssetUploaded

AssetRemoved