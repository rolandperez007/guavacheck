class UserProfile:

    def __init__(
        self,
        user_id,
        preferred_locations=None,
        property_types=None,
        budget_min=None,
        budget_max=None
    ):
        self.user_id = user_id

        self.preferred_locations = preferred_locations or []
        self.property_types = property_types or []

        self.budget_min = budget_min
        self.budget_max = budget_max

        self.saved_properties = []
        self.viewed_properties = []

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "preferred_locations": self.preferred_locations,
            "property_types": self.property_types,
            "budget_min": self.budget_min,
            "budget_max": self.budget_max,
            "saved_properties": self.saved_properties,
            "viewed_properties": self.viewed_properties
        }