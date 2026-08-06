export interface Alert {
  id: string;

  severity: "info" | "warning" | "critical";

  message: string;

  createdAt: Date;
}

export class AlertEngine {
  private static alerts: Alert[] = [];

  static push(alert: Alert): void {
    this.alerts.push(alert);
  }

  static active(): Alert[] {
    return this.alerts;
  }
}
