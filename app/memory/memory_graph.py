from app.memory.preference_engine import PreferenceEngine


class MemoryGraph:

    def __init__(self):
        self.preference_engine = PreferenceEngine()

    def analyze(self, memory_records):

        return self.preference_engine.build_preferences(
            memory_records
        )