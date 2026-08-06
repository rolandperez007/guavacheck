class WorkflowAssignmentService:
    """
    Assign workflows to institution entities.
    """

    def assign_to_department(
        self,
        workflow_id,
        department_id,
    ):
        return {
            "workflow_id": workflow_id,
            "department_id": department_id,
        }

    def assign_to_team(
        self,
        workflow_id,
        team_id,
    ):
        return {
            "workflow_id": workflow_id,
            "team_id": team_id,
        }

    def assign_to_role(
        self,
        workflow_id,
        role_id,
    ):
        return {
            "workflow_id": workflow_id,
            "role_id": role_id,
        }