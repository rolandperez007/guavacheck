class TaskGenerator:
    def generate(self, project: dict):
        asset = project.get("project", {}).get("asset_type", "building")

        base_tasks = [
            f"Site preparation for {asset}",
            "Foundation work",
            "Structural framework",
            "Mechanical & Electrical installation",
            "Interior finishing",
            "Final inspection",
        ]

        return {"asset_type": asset, "tasks": base_tasks}
