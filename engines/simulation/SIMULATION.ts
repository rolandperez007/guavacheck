export interface Simulation {
  id: string;

  name: string;

  description: string;

  category: string;

  difficulty: "easy" | "medium" | "hard" | "critical";

  expectedOutcome: string;

  createdAt: Date;
}
