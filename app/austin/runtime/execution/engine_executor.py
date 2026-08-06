"""
Austin Engine Executor

Executes a selected engine and
returns a standardized result.
"""


class EngineExecutor:

    def execute(
        self,
        engine,
        request,
    ):

        if engine is None:

            return {
                "success": False,
                "error": "No engine selected",
            }

        if not hasattr(engine, "execute"):

            return {
                "success": False,
                "error": "Engine has no execute() method",
            }

        result = engine.execute(request)

        return {
            "success": True,
            "engine": engine.__class__.__name__,
            "result": result,
        }