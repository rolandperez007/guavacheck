# Simple smoke tests for IronGate components
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from types import SimpleNamespace

from irongate.normalizer import normalize_request
from irongate.rule import (
    austin_low_risk_rule,
    automation_header_rule,
    duplicate_request_rule,
    payload_size_limit_rule,
    rate_limit_rule,
    spam_pattern_rule,
)


def make_request(path="/", method="POST", headers=None):
    headers = headers or {}
    url = SimpleNamespace(path=path)
    req = SimpleNamespace(url=url, headers=headers, method=method)
    return req


def test_normalizer():
    req = make_request(
        path="/austin/execute", headers={"user-agent": "python-requests/2.31"}
    )
    body = {"query": "build house quote", "user_id": "guava_user"}
    ctx = normalize_request(req, body)
    assert ctx["action"] == "run_job"
    assert ctx["user_id"] == "guava_user"
    assert "build house" in ctx["query"]


def test_rules_and_scoring():
    ctx = {
        "payload": {"text": "Buy now for free"},
        "headers": {"user-agent": "curl/7.68.0"},
    }
    r1 = spam_pattern_rule(ctx)
    assert isinstance(r1, str) and "spam pattern" in r1
    r2 = automation_header_rule(ctx)
    assert isinstance(r2, str) and "automation" in r2


def test_austin_low_risk():
    ctx = {
        "query": "Please provide a quote to build house",
        "payload": {"query": "Please provide a quote to build house"},
    }
    r = austin_low_risk_rule(ctx)
    assert isinstance(r, (bool, str))


def test_payload_size_limit():
    # Small payload
    ctx = {"payload": {"query": "test"}, "user_id": "user1"}
    r1 = payload_size_limit_rule(ctx, max_bytes=1000)
    assert r1 is True

    # Large payload
    ctx = {"payload": {"data": "x" * 2000}, "user_id": "user1"}
    r2 = payload_size_limit_rule(ctx, max_bytes=1000)
    assert isinstance(r2, str) and "payload too large" in r2


def test_rate_limit():
    ctx = {"user_id": "user_rl"}

    # First few requests should pass
    r1 = rate_limit_rule(ctx, max_requests_per_minute=5)
    assert r1 is True
    r2 = rate_limit_rule(ctx, max_requests_per_minute=5)
    assert r1 is True

    # Fill up to limit
    for _ in range(3):
        rate_limit_rule(ctx, max_requests_per_minute=5)

    # Next request should trigger rate limit
    r_final = rate_limit_rule(ctx, max_requests_per_minute=5)
    assert isinstance(r_final, str) and "rate limit" in r_final


def test_duplicate_request():
    ctx = {
        "user_id": "user_dup",
        "query": "build house",
        "payload": {"query": "build house"},
    }

    # First request
    r1 = duplicate_request_rule(ctx, window_seconds=60)
    assert r1 is True

    # Second request
    r2 = duplicate_request_rule(ctx, window_seconds=60)
    assert r2 is True

    # Third request
    r3 = duplicate_request_rule(ctx, window_seconds=60)
    assert r3 is True

    # Fourth identical request should trigger (3 or more duplicates)
    r4 = duplicate_request_rule(ctx, window_seconds=60)
    assert isinstance(r4, str) and "duplicate request" in r4


if __name__ == "__main__":
    test_normalizer()
    print("✓ test_normalizer passed")
    test_rules_and_scoring()
    print("✓ test_rules_and_scoring passed")
    test_austin_low_risk()
    print("✓ test_austin_low_risk passed")
    test_payload_size_limit()
    print("✓ test_payload_size_limit passed")
    test_rate_limit()
    print("✓ test_rate_limit passed")
    test_duplicate_request()
    print("✓ test_duplicate_request passed")
    print("✅ All irongate checks passed")
