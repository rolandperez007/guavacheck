import json
from urllib.request import Request, urlopen


def post(payload):
    data = json.dumps(payload).encode()
    req = Request(
        "http://127.0.0.1:8000/irongate/evaluate",
        data=data,
        headers={"Content-Type": "application/json"},
    )
    resp = urlopen(req, timeout=10)
    body = resp.read().decode()
    return resp.getcode(), body


if __name__ == "__main__":
    import uuid

    unique = str(uuid.uuid4())[:8]
    warn_payload = {"payload": {"query": f"free money click here buy now {unique}"}}
    block_payload = {
        "payload": {"query": f"free money click here buy now {unique}"},
        "user_id": "test_spam_user",
    }

    tests = [
        (warn_payload, "warn example (unique nested payload)"),
        (block_payload, "block example (nested payload + banned user)"),
    ]

    for payload, desc in tests:
        try:
            status, body = post(payload)
            print("---", desc)
            print("status:", status)
            print("body:", body)
        except Exception as e:
            print("---", desc)
            print("error:", type(e), e)
