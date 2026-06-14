from app.core.events.event_bus import EventBus


class UIEventStream:
    def __init__(self):
        self.bus = EventBus()

    # -----------------------------
    # AUSTIN THINKING STATE
    # -----------------------------
    def thinking(self, message: str):
        return self.bus.emit(
            "ui.austin.thinking",
            {"message": message, "state": "thinking", "animation": "pulse"},
        )

    # -----------------------------
    # ESCROW UPDATE STATE
    # -----------------------------
    def escrow_update(self, escrow):
        return self.bus.emit(
            "ui.escrow.update",
            {
                "escrow_id": escrow.get("escrow_id"),
                "amount": escrow.get("amount"),
                "status": escrow.get("status"),
                "progress": escrow.get("current_phase", 0),
            },
        )

    # -----------------------------
    # MILESTONE UPDATE
    # -----------------------------
    def milestone(self, milestone):
        return self.bus.emit(
            "ui.milestone.update",
            {
                "phase": milestone.get("phase"),
                "status": milestone.get("status"),
                "animation": "slide",
            },
        )
