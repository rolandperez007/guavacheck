from datetime import datetime


class ExecutionEngine:
    def create_project(self, pipeline_result):
        project_id = f"GVA-{int(datetime.utcnow().timestamp())}"

        return {
            "project_id": project_id,
            "status": "planning",
            "created_at": str(datetime.utcnow()),
            "asset_type": pipeline_result["project"]["asset_type"],
            "estimated_cost": pipeline_result["cost"]["estimated_cost"],
            "timeline_months": pipeline_result["timeline"]["total_months"],
        }

    def advance_stage(self, project, new_stage):
        project["status"] = new_stage

        return {"success": True, "project": project}

    def project_health(self, project):
        return {
            "project_id": project["project_id"],
            "status": project["status"],
            "health_score": 0.92,
            "risk_level": "low",
        }
