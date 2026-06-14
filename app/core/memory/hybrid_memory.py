class HybridMemory:
    def __init__(self):
        self.memory = {}

    async def save(self, user_id, query):
        if user_id not in self.memory:
            self.memory[user_id] = []

        self.memory[user_id].append(query)

    async def recall(self, user_id):
        return self.memory.get(user_id, [])
