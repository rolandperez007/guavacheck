import { SimulationMetrics } from "./SIMULATIONMETRICS";

export interface SimulationReport {

    generatedAt: Date;

    metrics: SimulationMetrics;

    summary: string;

}