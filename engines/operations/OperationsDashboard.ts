import { SystemHealth } from "./SystemHealthEngine";

export interface DashboardSummary {
  uptime: number;

  onlineUsers: number;

  activeProjects: number;

  activeEscrows: number;

  pendingVerifications: number;

  unresolvedAlerts: number;

  health: SystemHealth;
}

export class OperationsDashboard {
  static generate(summary: DashboardSummary): DashboardSummary {
    return summary;
  }
}
