export class CommunityEngine {
  static generatePost(property: any) {
    return {
      title: property.title ?? "Property Update",
      content: "Auto-generated listing post",
      createdAt: new Date(),
    };
  }
}
