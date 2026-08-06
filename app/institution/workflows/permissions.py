class InstitutionWorkflowPermissionService:
    """
    Controls workflow permissions.
    """

    def can_view(
        self,
        user,
        workflow,
    ) -> bool:
        return True

    def can_edit(
        self,
        user,
        workflow,
    ) -> bool:
        return True

    def can_execute(
        self,
        user,
        workflow,
    ) -> bool:
        return True

    def can_delete(
        self,
        user,
        workflow,
    ) -> bool:
        return True