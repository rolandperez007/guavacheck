# app/contracts/listing_schema.py

LISTING_SCHEMA = {
    "title": str,
    "description": str,
    "location": str,
    "price": int,
    "listing_type": str,  # rent | sale
    "user_id": str,
    "image_url": str | None,
    "status": str,  # draft | published
}
