import asyncio
from app.core.realtime.websocket_manager import ws_manager


class EventBus:
    def __init__(self):
        # Local event listeners (sync callbacks)
        self.listeners = {}

        # Shared websocket manager (UI layer bridge)
        self.ws = ws_manager

    # -----------------------------
    # SUBSCRIBE
    # -----------------------------
    def subscribe(self, event_name, callback):
        if event_name not in self.listeners:
            self.listeners[event_name] = []

        self.listeners[event_name].append(callback)

    # -----------------------------
    # EMIT EVENT
    # -----------------------------
    def emit(self, event_name, payload=None):
        result = {"event": event_name, "payload": payload}

        # -----------------------------
        # REALTIME UI BRIDGE (SAFE)
        # -----------------------------
        try:
            loop = asyncio.get_event_loop()

            if loop.is_running():
                asyncio.create_task(self.ws.broadcast(result))
            else:
                loop.run_until_complete(self.ws.broadcast(result))

        except Exception:
            # Never crash core logic because UI layer failed
            pass

        # -----------------------------
        # LOCAL SUBSCRIBERS
        # -----------------------------
        for callback in self.listeners.get(event_name, []):
            try:
                callback(payload)
            except Exception:
                pass

        return result
