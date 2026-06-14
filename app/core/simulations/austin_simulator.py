import time
from app.core.ui.ui_event_stream import UIEventStream

print("🔥 AUSTIN SIMULATOR MODULE LOADED")


class AustinSimulator:
    def __init__(self):
        print("⚙️ INIT OK")

        self.ui = UIEventStream()

    def run(self, query: str):
        print("🧠 AI STARTING SIMULATION:", query)

        # 1. ANALYSIS PHASE
        self.ui.thinking(f"Analyzing project: {query}")
        time.sleep(1)

        # 2. MARKET SCAN
        self.ui.thinking("Scanning market conditions...")
        time.sleep(1)

        # 3. FOUNDATION
        self.ui.milestone({"phase": "foundation", "status": "building"})
        self.ui.thinking("Foundation completed")
        time.sleep(1)

        # 4. STRUCTURE
        self.ui.milestone({"phase": "structure", "status": "building"})
        self.ui.thinking("Structure rising")
        time.sleep(1)

        # 5. ROOFING
        self.ui.milestone({"phase": "roofing", "status": "building"})
        self.ui.thinking("Roofing in progress")
        time.sleep(1)

        # 6. COMPLETION
        self.ui.thinking("Finalizing project...")
        time.sleep(1)

        self.ui.thinking("Simulation complete")
