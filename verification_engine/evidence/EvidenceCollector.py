"""
Evidence Collector

Collects every piece of evidence
used during verification.
"""

from verification_engine.evidence.EvidenceModels import Evidence


class EvidenceCollector:
    def __init__(self):

        self.items = []

    def add(self, evidence: Evidence):

        self.items.append(evidence)

    def all(self):

        return self.items

    def clear(self):

        self.items.clear()
