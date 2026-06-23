import { ToolRegistry } from "./ToolRegistry";
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

      let output: any = null;

      switch (step) {
        case "calculate_total_cost":
          output = await ToolRegistry.tools.boq.calculateTotalCost();
          break;

        case "generate_boq_table":
          output = await ToolRegistry.tools.boq.generateTable(output);
          results.tables.push(output);
          break;

        case "generate_valuation_report":
          output = await ToolRegistry.tools.valuation.generateReport(output);
          results.insights.push(output);
          break;

        default:
          output = { step, status: "unknown_step" };
      }

      results.raw.push(output);
      results.stepsCompleted.push(step);

      emit?.({ stage: "step_done", step, output });
    }

    return results;
  }
}
