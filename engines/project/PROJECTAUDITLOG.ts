export interface AuditLog {
  id: string;

  projectId: string;

  action: string;

  performedBy: string;

  timestamp: Date;

  details?: Record<string, unknown>;
}
