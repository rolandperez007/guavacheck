def jwt_validation_rule(context):
    headers = context.get("headers", {})
    auth = headers.get("authorization") or headers.get("Authorization")

    if not auth:
        return "missing JWT token"

    try:
        token = auth.replace("Bearer ", "")
        jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return True

    except Exception:
        return "invalid JWT"
