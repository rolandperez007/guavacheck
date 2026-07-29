# Event Contracts

Version: 1.0

---

# Standard Event Structure

{
    event_id,
    event_name,
    timestamp,
    engine,
    correlation_id,
    property_id,
    passport_id,
    twin_id,
    actor,
    payload
}

---

# Example

PropertyCreated

Payload

{
    property_id,
    owner_id,
    listing_type,
    location,
    created_at
}

---

TwinCreated

Payload

{
    twin_id,
    property_id,
    version,
    model_url
}

---

OwnershipTransferred

Payload

{
    previous_owner,
    new_owner,
    transfer_date,
    agreement_id,
    certificate_id
}

---

ConstructionCompleted

Payload

{
    property_id,
    contractor,
    completion_date,
    inspection_report
}

---

# Event Processing Rules

Events are immutable.

Events are append-only.

Events must never be edited.

Consumers acknowledge successful processing.

Retries must be idempotent.

Failed events enter the Dead Letter Queue.

---

# Event Versioning

Every event supports version numbers.

Example

PropertyCreated.v1

PropertyCreated.v2

Consumers must remain backwards compatible whenever possible.