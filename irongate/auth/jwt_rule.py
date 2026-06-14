from irongate.auth.jwt_validator import validate_jwt


def jwt_validation_rule(context):
    token = context.get("jwt")

    if not token:
        return "missing jwt"

    result = validate_jwt(token)

    if not result["valid"]:
        return result["reason"]

    context["jwt_payload"] = result["payload"]
    if context["path"] in ["/health", "/ready", "/status", "/docs", "/openapi.json"]:
        return True
    if os.getenv("DEV_MODE") == "true":
        return True
