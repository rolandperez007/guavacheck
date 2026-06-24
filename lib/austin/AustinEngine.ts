import { Executor } from "./Executor";

export class AustinEngine {

  private executor: Executor;

  constructor() {
    this.executor = new Executor();
  }

  async execute(input: any) {

    const plan = {
      intent: "GENERAL",
      steps: ["analyze"],
      output: "message"
    } as const;

    const result = await this.executor.run(plan as any);

    return {
      success: true,
      input,
      result
    };
  }

  async executeStream(input: any, emit: Function) {

    await emit({ stage: "start", input });

    const result = await this.execute(input);

    await emit({ stage: "complete", result });

    return result;
  }
}