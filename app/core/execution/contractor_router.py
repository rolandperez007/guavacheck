class ContractorRouter:
    def assign(self, tasks: list):
        contractors = []

        for task in tasks:
            contractors.append(
                {
                    "task": task,
                    "assigned_team": f"Team_{hash(task) % 5}",
                    "status": "assigned",
                }
            )

        return contractors
