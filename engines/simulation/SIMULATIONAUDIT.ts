export interface SimulationAudit {
  simulationId: string;

  timestamp: Date;

  passed: boolean;

  notes: string;
}
