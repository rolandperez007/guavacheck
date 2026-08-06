"""
Registry Stage

Queries official government registries
through the Registry Aggregator.
"""

from verification_engine.government.RegistryAggregator import (
    RegistryAggregator,
)


class RegistryStage:
    name = "REGISTRY"

    def __init__(self):

        self.registry = RegistryAggregator()

    async def execute(
        self,
        context,
    ):

        property_data = getattr(context, "property_data", {})

        registry_result = await self.registry.verify(property_data)

        context.stages[self.name] = {
            "completed": True,
            "registry": registry_result,
            "status": "SUCCESS",
        }

        context.evidence.append(
            {"type": "registry_verification", "data": registry_result}
        )

        return context
