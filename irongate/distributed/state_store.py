import hashlib
import time
from collections import defaultdict, deque


class InMemoryStateStore:
    """
    v3.1 distributed-compatible state store.
    Later replaced by Redis without changing IronGate logic.
    """

    def __init__(self):
        # rate limiting
        self.rate_buckets = defaultdict(deque)

        # duplicate detection
        self.request_log = defaultdict(deque)

    # -------------------------
    # RATE LIMITING
    # -------------------------
    def increment_rate(self, key: str, window_sec: int = 60):
        now = time.time()
        bucket = self.rate_buckets[key]

        bucket.append(now)

        # remove old entries
        while bucket and now - bucket[0] > window_sec:
            bucket.popleft()

        return len(bucket)

    # -------------------------
    # DUPLICATE DETECTION
    # -------------------------
    def add_request(self, key: str, window_sec: int = 60):
        now = time.time()
        log = self.request_log[key]

        log.append(now)

        while log and now - log[0] > window_sec:
            log.popleft()

        return len(log)

    # -------------------------
    # FINGERPRINTING
    # -------------------------
    def fingerprint(self, payload: dict) -> str:
        raw = str(payload).encode()
        return hashlib.sha256(raw).hexdigest()


# GLOBAL STORE (swap to Redis later)
state_store = InMemoryStateStore()
