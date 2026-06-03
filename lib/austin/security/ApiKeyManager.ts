export class ApiKeyManager {

  static keys: Record<string, any> = {
    "public_demo": {
      plan: "free",
      active: true
    }
  };

  static generateKey(name: string) {
    const key = "ak_" + Math.random().toString(36).substring(2, 15);

    this.keys[key] = {
      name,
      plan: "pro",
      active: true,
      created: new Date()
    };

    return key;
  }

  static validate(key: string) {
    return this.keys[key] || null;
  }

  static revoke(key: string) {
    if (this.keys[key]) {
      this.keys[key].active = false;
    }
    return true;
  }
}
