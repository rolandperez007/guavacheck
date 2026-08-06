class InstitutionWorkflowEvents:
    """
    Institution workflow event publisher.
    """

    def workflow_created(
        self,
        workflow_id,
    ):
        return {
            "event": "institution.workflow.created",
            "workflow_id": workflow_id,
        }

    def workflow_completed(
        self,
        workflow_id,
    ):
        return {
            "event": "institution.workflow.completed",
            "workflow_id": workflow_id,
        }