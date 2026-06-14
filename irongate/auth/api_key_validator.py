# irongate/auth/api_key_validator.py

VALID_KEYS = {"dev-key-123": "guava"}


def validate_api_key(key):
    if key in VALID_KEYS:
        return {"valid": True, "tenant": VALID_KEYS[key]}

    return {"valid": False, "reason": "invalid api key"}
