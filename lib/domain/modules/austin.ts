import { DomainModule } from "../types";

export class AustinModule implements DomainModule {
  initialize() {
    console.log("Austin Ready");
  }

  destroy() {}

  handle(message: any) {
    console.log("Austin received", message);
  }
}
