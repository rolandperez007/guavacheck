def compute_risk(ai_context: dict):
    score = 0

    reputation = ai_context["reputation"]

    # 🧠 TRUST LAYER (very important)
    if reputation >= 80:
        score -= 20  # trusted users are less suspicious
    elif reputation <= 30:
        score += 30  # low trust increases risk

    # ❌ no auth
    if not ai_context["has_auth"]:
        score += 50

    # 🚨 traffic spike
    if ai_context["request_rate_per_min"] > 20:
        score += 35
    elif ai_context["request_rate_per_min"] > 10:
        score += 15

    # sensitive endpoint
    if "admin" in ai_context["endpoint"]:
        score += 20

    return max(0, min(score, 100))
