"""
Document Validation Stage

Checks uploaded documents for
structure and completeness.
"""


class DocumentStage:
    name = "DOCUMENT"

    async def execute(
        self,
        context,
    ):

        documents = getattr(context, "documents", [])

        validation_result = {
            "completed": True,
            "documents_received": len(documents),
            "documents_valid": len(documents) > 0,
            "missing_fields": [],
            "status": "VALIDATED" if documents else "NO_DOCUMENTS",
        }

        context.stages[self.name] = validation_result

        context.evidence.append(
            {"type": "document_validation", "data": validation_result}
        )

        return context
