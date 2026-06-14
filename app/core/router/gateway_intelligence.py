import hashlib
import time


class GatewayIntelligence:
    def __init__(self):
        self.cache = {}
        self.stats = {"fast": 0, "mid": 0, "heavy": 0}

    # -------------------------
    # 1. Complexity Scoring
    # -------------------------
    def score(self, prompt: str, context: dict = None) -> float:
        tokens = len(prompt.split())
        score = min(tokens / 300, 1.0)

        if context:
            if context.get("financial") or context.get("escrow"):
                score += 0.3

            if context.get("legal"):
                score += 0.3

            if context.get("multi_step"):
                score += 0.2

        return min(score, 1.0)

    # -------------------------
    # 2. Route Decision
    # -------------------------
    def route(self, score: float) -> str:
        if score < 0.3:
            return "fast"
        if score < 0.7:
            return "mid"
        return "heavy"

    # -------------------------
    # 3. Cache Key Generator
    # -------------------------
    def cache_key(self, prompt: str, route: str):
        raw = f"{route}:{prompt}"
        return hashlib.md5(raw.encode()).hexdigest()

    # -------------------------
    # 4. Check Cache
    # -------------------------
    def get_cached(self, key: str):
        item = self.cache.get(key)

        if not item:
            return None

        # expire after 10 min
        if time.time() - item["time"] > 600:
            return None

        return item["data"]

    # -------------------------
    # 5. Store Cache
    # -------------------------
    def set_cache(self, key: str, data: dict):
        self.cache[key] = {"data": data, "time": time.time()}

    # -------------------------
    # 6. Track usage
    # -------------------------
    def track(self, route: str):
        self.stats[route] += 1

    # -------------------------
    # 7. Full Decision Engine
    # -------------------------
    def decide(self, prompt: str, context: dict = None):
        score = self.score(prompt, context)
        route = self.route(score)
        key = self.cache_key(prompt, route)

        cached = self.get_cached(key)

        return {
            "score": score,
            "route": route,
            "cache_key": key,
            "cached": cached is not None,
        }
