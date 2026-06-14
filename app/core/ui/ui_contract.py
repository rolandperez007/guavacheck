class UIEventTypes:
    AUSTIN_THINKING = "austin.thinking"
    EXECUTION_STEP = "execution.step"
    ESCROW_UPDATE = "escrow.update"
    MILESTONE_UPDATE = "milestone.update"


def ui_event(event_type: str, data: dict):
    return {"type": event_type, "data": data}
