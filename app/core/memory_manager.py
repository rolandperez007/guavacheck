# app/core/memory_manager.py


class MemoryManager:
    def __init__(self):
        self.memory = {}

    def save(self, session_id, data):
        self.memory[session_id] = data

    def get(self, session_id):
        return self.memory.get(session_id)
