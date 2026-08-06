import os

# =========================
# CONFIG
# =========================
JWT_SECRET = os.getenv("IRON_GATE_JWT_SECRET", "dev_secret_change_me")
JWT_ALGORITHM = "HS256"


# =========================
# JWT VALIDATION RULE
# =========================
def jwt_validation_rule(context: dict):
    """
    Simple placeholder JWT validation rule for v3.2
    Replace later with real JWT verification.
    """

    headers = context.get("headers", {})

    auth = headers.get("authorization")

    if not auth:
        return "missing auth token"

    if not auth.startswith("Bearer "):
        return "invalid auth format"

    token = auth.replace("Bearer ", "")

    if token == "dev-token":
        return True

    return "invalid token"
