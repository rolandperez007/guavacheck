class AustinMemory:

    def __init__(self):
        self.memory = {}

    def save(self, user_id, event):

        if user_id not in self.memory:
            self.memory[user_id] = []

        # prevent duplicates
        if self.memory[user_id]:
            last = self.memory[user_id][-1]
            if last.get("query") == event.get("query"):
                return

        self.memory[user_id].append(event)

    def get_history(self, user_id):
        return self.memory.get(user_id, [])
    