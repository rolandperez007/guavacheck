import { IntentClassifier } from "./IntentClassifier";
import { Planner } from "./Planner";
import { Executor } from "./Executor";
import type {
  AustinIntent,
  AustinPlan,
  AustinExecutionResult,
  AustinReport
} from "./types/austin.types";

export class AustinEngine {
  private classifier = new IntentClassifier();
  private planner = new Planner();
  private executor = new Executor();

  async execute(input: string): Promise<{
    intent: AustinIntent;
    plan: AustinPlan;
    result: AustinExecutionResult;
    ui: any;
  }> {
    const intent = await this.classifier.parse(input);
    const plan = await this.planner.create(intent);
    const result = await this.executor.run(plan);

    return this.format(intent, plan, result);
  }

  async executeStream(input: string, emit: Function) {
    emit({ stage: "intent" });

    const intent = await this.classifier.parse(input);
    emit({ stage: "intent_done", intent });

    const plan = await this.planner.create(intent);
    emit({ stage: "plan", plan });

    const result = await this.executor.run(plan, emit);
    emit({ stage: "result", result });

    return this.format(intent, plan, result);
  }

  private format(
    intent: AustinIntent,
    plan: AustinPlan,
    result: AustinExecutionResult
  ) {
    return {
      intent,
      plan,
      result,
      ui: {
        type: plan.output,
        tables: result.tables,
        insights: result.insights,
        raw: result.raw
      }
    };
  }
}
