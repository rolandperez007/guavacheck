export class ApiGateway {
  ensureDirectory(path: string) {
    const fs = require("fs");

    if (!fs.existsSync(path)) {
      fs.mkdirSync(path, { recursive: true });
    }
  }
}
