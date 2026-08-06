"""
Austin Session Context

Maintains active runtime context
for Austin's reasoning process.
"""


class SessionContext:


    def __init__(
        self,
        project=None,
        phase=None,
        domain=None,
    ):

        self.state = {

            "project": project,

            "phase": phase,

            "domain": domain,

            "last_action": None,

        }



    def update(
        self,
        key,
        value,
    ):

        self.state[key] = value



    def get(
        self,
        key,
        default=None,
    ):

        return self.state.get(
            key,
            default,
        )



    def remember_action(
        self,
        action,
    ):

        self.state["last_action"] = action



    def snapshot(
        self,
    ):

        return self.state.copy()