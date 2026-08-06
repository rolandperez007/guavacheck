export interface Incident {
  id: string;

  severity: "low" | "medium" | "high" | "critical";

  description: string;

  reportedAt: Date;
}
