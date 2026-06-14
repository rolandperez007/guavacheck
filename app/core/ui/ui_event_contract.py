class UIEventContract:
    @staticmethod
    def austin_thinking(message: str, state: str = "thinking"):
        return {
            "event": "austin.thinking",
            "payload": {"state": state, "message": message},
        }

    @staticmethod
    def execution_update(step: str, progress: float):
        return {
            "event": "execution.update",
            "payload": {"step": step, "progress": progress},
        }

    @staticmethod
    def escrow_release(amount: float, phase: str):
        return {
            "event": "escrow.release",
            "payload": {"amount": amount, "phase": phase},
        }
