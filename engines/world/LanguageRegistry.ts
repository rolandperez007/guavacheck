export class LanguageRegistry {
  private static registry = new Map<string, string[]>();

  static register(country: string, languages: string[]) {
    this.registry.set(country, languages);
  }

  static byCountry(country: string) {
    return this.registry.get(country) ?? [];
  }
}
