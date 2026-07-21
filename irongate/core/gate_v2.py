from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class PolicyContext:

    request: Any = None

    body: Dict[str, Any] = field(
        default_factory=dict
    )

    path: str = ""

    headers: Dict[str, Any] = field(
        default_factory=dict
    )

    extra: Dict[str, Any] = field(
        default_factory=dict
    )


    def __init__(self, **kwargs):

        self.request = kwargs.pop(
            "request",
            None
        )

        self.body = kwargs.pop(
            "body",
            {}
        )

        self.path = kwargs.pop(
            "path",
            ""
        )

        self.headers = kwargs.pop(
            "headers",
            {}
        )

        self.extra = kwargs



@dataclass
class ScorePoint:

    rule: str

    score: int

    reason: Optional[str] = None

    critical: bool = False



class IronGateV2:

    """
    Stable policy engine (v2 clean contract)
    """

    def __init__(
        self,
        rules=None,
        score_threshold=100,
        warn_threshold=50,
    ):

        self.rules = rules or []

        self.score_threshold = score_threshold

        self.warn_threshold = warn_threshold



    def register_rule(
        self,
        rule,
        weight=1,
        critical=False,
    ):

        """
        Backwards compatible rule registration.
        """

        self.rules.append(
            {
                "rule": rule,
                "weight": weight,
                "critical": critical,
                "rule__name": getattr(
                    rule,
                    "__name__",
                    "unknown_rule",
                ),
            }
        )



    def evaluate(
        self,
        context: Dict[str, Any],
    ) -> Dict[str, Any]:

        score = 0

        reasons: List[str] = []

        rules_triggered = []


        for entry in self.rules:

            rule = entry["rule"]

            weight = entry.get(
                "weight",
                0,
            )

            critical = entry.get(
                "critical",
                False,
            )

            rule_name = entry.get(
                "rule__name",
                "unknown_rule",
            )


            try:

                result = rule(context)


            except Exception as e:

                result = str(e)



            if isinstance(
                result,
                bool,
            ):

                normalized = {

                    "allow": result,

                    "score": 0,

                    "reason": None,

                    "critical": False,

                }


            elif isinstance(
                result,
                str,
            ):

                normalized = {

                    "allow": False,

                    "score": weight,

                    "reason": result,

                    "critical": critical,

                }


            elif isinstance(
                result,
                dict,
            ):

                normalized = {

                    "allow":
                        bool(
                            result.get(
                                "allow",
                                True,
                            )
                        ),

                    "score":
                        int(
                            result.get(
                                "score",
                                0,
                            )
                        ),

                    "reason":
                        result.get(
                            "reason"
                        ),

                    "critical":
                        bool(
                            result.get(
                                "critical",
                                False,
                            )
                        ),

                }


            else:

                raise TypeError(
                    f"Invalid rule return type: {type(result)}"
                )



            rules_triggered.append(

                {
                    "rule": rule_name,
                    "weight": weight,
                    "critical": critical,
                }

            )



            if not normalized["allow"]:

                score += weight


                if normalized["reason"]:

                    reasons.append(
                        normalized["reason"]
                    )


                if normalized["critical"]:

                    return {

                        "allowed": False,

                        "score": 100,

                        "decision": "block",

                        "reason":
                            normalized["reason"]
                            or
                            "critical rule failed",

                        "reasons":
                            reasons,

                        "rules_triggered":
                            rules_triggered,

                        "final_action":
                            "block",

                    }


            else:

                score += normalized["score"]



        if score >= self.score_threshold:

            decision = "block"

        elif score >= self.warn_threshold:

            decision = "warn"

        else:

            decision = "allow"



        return {

            "allowed":
                decision != "block",

            "score":
                score,

            "decision":
                decision,

            "reasons":
                reasons,

            "reason":
                reasons[-1]
                if reasons
                else None,

            "rules_triggered":
                rules_triggered,

            "final_action":
                decision,

        }



__all__ = [
    "IronGateV2",
    "PolicyContext",
    "ScorePoint",
]