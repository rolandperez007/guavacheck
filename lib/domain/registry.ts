import { DomainModule } from "./types";

class Registry {
  private modules: DomainModule[] = [];

  register(module: DomainModule) {
    this.modules.push(module);
  }

  broadcast(message: any) {
    this.modules.forEach((module) => {
      module.handle(message);
    });
  }
}

export const registry = new Registry();
