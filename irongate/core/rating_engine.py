from dataclasses import dataclass


@dataclass
class AIStatus:
    name: str
    rating: float
    grade: str
    status: str
    launch_ready: bool


def build_ai_status(name: str, score: int) -> AIStatus:
    """
    Converts IronGate score into a dashboard-friendly AI rating.
    """

    rating = max(0.0, min(10.0, 10.0 - (score / 10.0)))

    if rating >= 9:
        grade = "A+"
        status = "Production Ready"
        launch_ready = True

    elif rating >= 8:
        grade = "A"
        status = "Near Production"
        launch_ready = True

    elif rating >= 7:
        grade = "B"
        status = "Beta"
        launch_ready = False

    elif rating >= 5:
        grade = "C"
        status = "Development"
        launch_ready = False

    else:
        grade = "D"
        status = "Experimental"
        launch_ready = False

    return AIStatus(
        name=name,
        rating=round(rating, 2),
        grade=grade,
        status=status,
        launch_ready=launch_ready,
    )
