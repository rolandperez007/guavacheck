from app.simulation.models import Simulation


class DashboardAnalytics:
    """
    Executive dashboard metrics.
    """

    def summary(self):
        return {
            "total_simulations": 0,
            "completed": 0,
            "failed": 0,
            "running": 0,
            "success_rate": 0.0,
        }

    def latest(
        self,
        limit: int = 10,
    ):
        return []