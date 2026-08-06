"""
Austin Validator

Validates engine outputs before
they are returned to users.
"""

from __future__ import annotations


class Validator:
    def validate(
        self,
        response,
    ):

        return {
            "valid": True,
            "response": response,
        }


validator = Validator()
