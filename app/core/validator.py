# app/core/validator.py


def validate_listing(data: dict):
    required_fields = ["title", "location", "price", "listing_type", "user_id"]

    missing = [f for f in required_fields if not data.get(f)]

    if missing:
        return {"valid": False, "missing": missing}

    return {"valid": True, "data": data}
