from irongate.core import IronGate

from irongate.rules import (
    block_empty_payload,
    allow_only_known_actions,
    block_suspicious_users,
)


def create_gate():

    gate = IronGate()

    gate.register_rule(
        block_empty_payload,
        weight=100,
        critical=True,
    )

    gate.register_rule(
        allow_only_known_actions,
        weight=100,
        critical=True,
    )

    gate.register_rule(
        block_suspicious_users,
        weight=100,
        critical=True,
    )

    return gate



def test_valid_job():

    gate = create_gate()

    result = gate.evaluate(
        {
            "user_id": "guava_user",
            "action": "run_job",
            "payload": {
                "task": "build_house_quote"
            },
        }
    )

    assert result["allowed"] is True



def test_empty_payload():

    gate = create_gate()

    result = gate.evaluate(
        {
            "user_id": "guava_user",
            "action": "run_job",
            "payload": {},
        }
    )

    assert result["allowed"] is False



def test_invalid_action():

    gate = create_gate()

    result = gate.evaluate(
        {
            "user_id": "guava_user",
            "action": "delete_database",
            "payload": {
                "danger": True
            },
        }
    )

    assert result["allowed"] is False



def test_banned_user():

    gate = create_gate()

    result = gate.evaluate(
        {
            "user_id": "test_spam_user",
            "action": "run_job",
            "payload": {
                "task": "hack_attempt"
            },
        }
    )

    assert result["allowed"] is False



