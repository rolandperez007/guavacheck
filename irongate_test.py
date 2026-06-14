from irongate.core import IronGate
from irongate.rule import (
    block_empty_payload,
    allow_only_known_actions,
    block_suspicious_users,
)

# setup gate
gate = IronGate()
gate.register_rule(block_empty_payload, weight=100, critical=True)
gate.register_rule(allow_only_known_actions, weight=100, critical=True)
gate.register_rule(block_suspicious_users, weight=100, critical=True)


def test_case(name, context):
    result = gate.evaluate(context)
    print(
        f"{name}: {'APPROVED' if result.get('allowed') else 'BLOCKED'} (score={result.get('score')}, decision={result.get('decision')})"
    )


# 1. VALID REQUEST
test_case(
    "Valid Job",
    {
        "user_id": "guava_user",
        "action": "run_job",
        "payload": {"task": "build_house_quote"},
    },
)

# 2. EMPTY PAYLOAD (should fail)
test_case(
    "Empty Payload", {"user_id": "guava_user", "action": "run_job", "payload": {}}
)

# 3. INVALID ACTION (should fail)
test_case(
    "Invalid Action",
    {"user_id": "guava_user", "action": "delete_database", "payload": {"danger": True}},
)

# 4. BANNED USER TEST
test_case(
    "Banned User",
    {
        "user_id": "test_spam_user",
        "action": "run_job",
        "payload": {"task": "hack_attempt"},
    },
)
