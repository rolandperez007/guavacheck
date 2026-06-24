import type { AustinExecutionResult, AustinPlan } from "./types/austin.types";

export class Executor {
  async run(plan: AustinPlan, emit?: Function): Promise<AustinExecutionResult> {

    const results: AustinExecutionResult = {
      stepsCompleted: [],
      tables: [],
      insights: [],
      raw: []
    };

    for (const step of plan.steps) {

      emit?.({ stage: "step", step });

      const output = {
        step,
        status: "completed"
      };

      results.raw.push(output);
      results.stepsCompleted.push(step);

      emit?.({ stage: "step_done", step, output });
    }

    return results;
  }
}