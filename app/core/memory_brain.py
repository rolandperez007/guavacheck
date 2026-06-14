from datetime import datetime
from app.memory.preference_engine import PreferenceEngine


class MemoryBrain:
    """
    Simple memory layer for Austin.
    Stores queries + extracts user behavior patterns.
    """

    def __init__(self):
        self.preference_engine = PreferenceEngine()

    def remember_query(self, user_id: str, query: str):
        """
        Store raw interaction in memory system.
        """
        self.preference_engine.log_interaction(user_id, query)

    def infer_preferences(self, user_id: str):
        """
        Extract behavioral patterns from stored memory.
        """
        return self.preference_engine.build_profile(user_id)
