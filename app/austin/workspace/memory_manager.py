"""
Austin Memory Manager

Responsible for persistent memory.

Memory Layers

• Session

• Project

• Property

• User

• Institution

• Global

Supports

semantic search

vector retrieval

conversation history

knowledge graph

summaries
"""


class MemoryManager:

    def remember(self, key, value):

        return {
            "key": key,
            "value": value,
        }

    def recall(self, key):

        return {
            "key": key,
            "value": None,
        }