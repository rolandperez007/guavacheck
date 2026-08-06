class InstitutionWorkflowExecutionService:
    """
    Executes institution-owned workflows.
    """

    def start(
        self,
        workflow_id,
    ):
        return {
            "workflow_id": workflow_id,
            "status": "started",
        }

    def stop(
        self,
        execution_id,
    ):
        return {
            "execution_id": execution_id,
            "status": "stopped",
        }