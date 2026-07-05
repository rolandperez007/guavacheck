export enum ProjectRisk {

    LOW = "low",

    MEDIUM = "medium",

    HIGH = "high",

    CRITICAL = "critical"

}

export interface RiskAssessment {

    projectId: string;

    risk: ProjectRisk;

    score: number;

    reason: string[];

}