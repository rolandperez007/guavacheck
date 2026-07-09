"""
Evidence Collector

Aggregates evidence from every
verification subsystem.
"""


class EvidenceCollector:

    def collect(

        self,

        context,

    ) -> list:

        evidence = []

        for key, value in context.metadata.items():

            evidence.append({

                "source": key,

                "value": value,

            })

        return evidence
