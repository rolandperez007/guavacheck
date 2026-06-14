class ConversationMemory:
    def __init__(self):
        self.store = {}

    def add_message(self, session_id, role, content):
        if session_id not in self.store:
            self.store[session_id] = []

        self.store[session_id].append({"role": role, "content": content})

    def get_context(self, session_id):
        return self.store.get(session_id, [])[-20:]
