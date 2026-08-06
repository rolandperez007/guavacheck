from .aggregator import MetricsAggregator
from .collector import MetricsCollector
from .insights import WorkflowInsights
from .report_generator import WorkflowReportGenerator


class AnalyticsManager:
    """
    Coordinates workflow analytics.
    """

    def __init__(self):

        self.collector = MetricsCollector()
        self.aggregator = MetricsAggregator()
        self.reporter = WorkflowReportGenerator()
        self.insights = WorkflowInsights()

    def analyze(self):

        metrics = self.aggregator.aggregate(
            self.collector.all(),
        )

        return {
            "metrics": metrics,
            "report": self.reporter.generate(
                metrics,
            ),
            "insights": self.insights.generate(
                metrics,
            ),
        }