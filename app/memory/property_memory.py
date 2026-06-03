class PropertyMemory:

    def __init__(self):
        self.history = {}

    def save_view(
        self,
        user_id,
        property_id
    ):

        if user_id not in self.history:
            self.history[user_id] = []

        self.history[user_id].append(
            property_id
        )

    def get_recent_views(
        self,
        user_id
    ):
        return self.history.get(user_id, [])