class SchedulerService:
    """
    Schedules workflow executions.
    """

    def schedule(
        self,
        workflow,
        when,
    ):
        return {
            "workflow": workflow,
            "scheduled_for": when,
        }