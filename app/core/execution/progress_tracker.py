class ProgressTracker:
    def track(self, tasks: list):
        total = len(tasks)
        completed = 0  # simulation baseline

        return {
            "total_tasks": total,
            "completed": completed,
            "progress_percent": (completed / total) * 100,
        }
