"""
Austin Response Validator
"""

from __future__ import annotations


class RuntimeValidator:
    def validate(
        self,
        response,
    ):

        if "message" not in response:
            raise ValueError("Missing response message.")

        return response


validator = RuntimeValidator()
