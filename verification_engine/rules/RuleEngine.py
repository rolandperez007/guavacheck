"""
Enterprise Rule Engine
"""


class RuleEngine:
    def __init__(self):

        self.rules = []

    def add_rule(self, rule):

        self.rules.append(rule)

    async def execute(self, verification_data):

        results = []

        total_score = 0

        for rule in self.rules:
            result = await rule(verification_data)

            results.append(result)

            total_score += result.score

        return {"results": results, "score": total_score}
