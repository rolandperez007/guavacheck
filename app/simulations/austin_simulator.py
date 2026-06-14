import time
from app.core.ui.ui_event_stream import UIEventStream


class AustinSimulator:
    def __init__(self):
        self.ui = UIEventStream()

    def run(self, query: str):
        # 1. USER INPUT RECEIVED
        self.ui.thinking(f"Analyzing: {query}")

        time.sleep(1)

        # 2. SIMULATED MARKET ANALYSIS
        self.ui.thinking("Scanning market conditions...")

        time.sleep(1)

        # 3. BUILDING GENERATION STARTS
        self.ui.milestone({"phase": "foundation", "status": "building"})

        time.sleep(1)

        self.ui.milestone({"phase": "structure", "status": "building"})

        time.sleep(1)

        self.ui.milestone({"phase": "roofing", "status": "building"})

        # 4. COMPLETION STATE
        self.ui.thinking("Simulation complete.")
