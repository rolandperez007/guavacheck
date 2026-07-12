export interface AustinStatus {
  platform: string;
  status: string;
  austin: boolean;
  message: string;
}

export interface QueueSummary {
  total: number;
  pending: number;
  running: number;
  completed: number;
  failed: number;
}

export interface AustinEvent {
  event_id: string;
  timestamp: string;
  correlation_id: string;
  event_type: string;
  source_service: string;
  engine: string;
  severity: string;
  category: string;
  message: string;
  metadata: Record<string, unknown>;
}