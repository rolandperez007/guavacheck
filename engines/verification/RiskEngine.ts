export enum RiskLevel {

    LOW = "low",

    MEDIUM = "medium",

    HIGH = "high",

    CRITICAL = "critical"

}

export interface RiskProfile {

    entityId: string;

    score: number;

    level: RiskLevel;

    reasons: string[];

}