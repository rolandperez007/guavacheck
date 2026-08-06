export class AuthEngine {
  static users: any[] = [];

  static register(user: any) {
    const newUser = {
      id: Math.random().toString(36).substring(2),
      email: user.email,
      role: user.role || "investor",
      plan: "free",
      createdAt: new Date(),
    };

    this.users.push(newUser);

    return newUser;
  }

  static login(email: string) {
    const user = this.users.find((u) => u.email === email);

    if (!user) {
      return { error: "user_not_found" };
    }

    return {
      success: true,
      user,
    };
  }

  static getUser(id: string) {
    return this.users.find((u) => u.id === id);
  }

  static assignRole(id: string, role: string) {
    const user = this.getUser(id);

    if (!user) return { error: "not_found" };

    user.role = role;

    return user;
  }
}
