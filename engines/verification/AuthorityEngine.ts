export interface Authority {
  id: string;

  name: string;

  country: string;

  category: string;

  trusted: boolean;

  endpoint?: string;
}

export class AuthorityEngine {
  private static authorities = new Map<string, Authority>();

  static register(authority: Authority): void {
    this.authorities.set(
      authority.id,

      authority,
    );
  }

  static find(id: string): Authority | undefined {
    return this.authorities.get(id);
  }

  static all(): Authority[] {
    return [...this.authorities.values()];
  }
}
