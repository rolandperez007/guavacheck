from typing import Dict, Any

VALID_KEYS = {"dev-key-123": "dev_tenant"}


def api_key_validation_rule(context: Dict[str, Any]) -> Dict[str, Any]:
    headers = context.get("headers", {})
    api_key = headers.get("x-api-key")

    if not api_key:
        return {
            "score": 100,
            "critical": True,
            "block": True,
            "reason": "missing API key",
        }

    tenant = VALID_KEYS.get(api_key)

    if not tenant:
        return {
            "score": 100,
            "critical": True,
            "block": True,
            "reason": "invalid API key",
        }

    context["tenant"] = tenant

    return {"score": 0, "reason": "valid API key"}
