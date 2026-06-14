class ProjectSchema:
    @staticmethod
    def create():
        return {
            "project_type": None,
            "category": None,
            "location": None,
            "country": None,
            "land": {"size": None, "unit": None},
            "design": {},
            "construction": {},
            "finance": {},
            "timeline": {},
            "operations": {},
            "metadata": {"version": "v1"},
        }
