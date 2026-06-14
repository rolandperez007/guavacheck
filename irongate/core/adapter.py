from typing import Any


def normalize_rule_output(result: Any):
    """
    Converts ANY future rule format into gate_v2-safe format.
    This prevents ALL future patching of core engine.
    """

    # ✔ already valid
    if isinstance(result, bool):
        return result

    if isinstance(result, str):
        return result

    # ✔ AI / scoring system (future-proof)
    if hasattr(result, "allow"):
        return result.allow

    # ✔ dict-based legacy AI systems
    if isinstance(result, dict):
        if result.get("block") is True:
            return result.get("reason", "blocked")
        return True

    # ❌ fallback safety
    return "invalid_rule_output"
