class PassportWorkflowEvents:
    """
    Publishes passport workflow events.
    """

    def verification_started(
        self,
        passport_id,
    ):
        return {
            "event": "passport.verification.started",
            "passport_id": passport_id,
        }

    def ownership_changed(
        self,
        passport_id,
    ):
        return {
            "event": "passport.ownership.changed",
            "passport_id": passport_id,
        }