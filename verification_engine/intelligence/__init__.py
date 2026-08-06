"""
Verification Intelligence Engine

Responsible for transforming raw verification
results into explainable AI decisions.

Components

- Evidence Collector
- Confidence Engine
- Conflict Resolver
- Explanation Generator
- Reasoning Engine
"""

from .ConfidenceEngine import ConfidenceEngine
from .ConflictResolver import ConflictResolver
from .EvidenceCollector import EvidenceCollector
from .ExplanationGenerator import ExplanationGenerator
from .ReasoningEngine import ReasoningEngine

__all__ = [
    "ConfidenceEngine",
    "ConflictResolver",
    "EvidenceCollector",
    "ExplanationGenerator",
    "ReasoningEngine",
]
