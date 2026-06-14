from dataclasses import dataclass


@dataclass
class ComplexityResult:
    score: float
    model: str


class ComplexityClassifier:
    @staticmethod
    def classify(query: str) -> ComplexityResult:
        q = query.lower()

        score = 0.0

        words = len(q.split())

        score += min(words / 100, 0.4)

        complex_terms = [
            "design",
            "generate",
            "analyze",
            "estimate",
            "architecture",
            "boq",
            "investment",
            "roi",
            "hospital",
            "contractor",
            "funding",
        ]

        score += sum(0.05 for term in complex_terms if term in q)

        score = min(score, 1.0)

        if score < 0.35:
            return ComplexityResult(score=score, model="haiku")

        if score < 0.75:
            return ComplexityResult(score=score, model="sonnet")

        return ComplexityResult(score=score, model="opus")
