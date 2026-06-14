class MilestoneManager:
    def split(self, amount: float):
        return {
            "milestones": [
                {"stage": 1, "amount": amount * 0.4},
                {"stage": 2, "amount": amount * 0.4},
                {"stage": 3, "amount": amount * 0.2},
            ]
        }
