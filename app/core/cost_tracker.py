class CostTracker:
    def __init__(self):
        self.usage = {}

    def add_cost(self, user_id: str, cost: float):
        if user_id not in self.usage:
            self.usage[user_id] = 0

        self.usage[user_id] += cost

    def get_usage(self, user_id: str):
        return self.usage.get(user_id, 0)

    def can_afford(self, user_id: str, limit=1.0):
        return self.get_usage(user_id) < limit
