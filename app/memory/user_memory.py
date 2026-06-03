class UserMemory:

    def __init__(self):
        self.users = {}

    def save_preference(
        self,
        user_id,
        key,
        value
    ):
        if user_id not in self.users:
            self.users[user_id] = {}

        self.users[user_id][key] = value

    def get_preferences(
        self,
        user_id
    ):
        return self.users.get(user_id, {})