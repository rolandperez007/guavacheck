/**
 * guavacheck Property Service
 * Temporary implementation
 */

export const propertyService = {
  async createProperty(data: unknown) {
    return {
      success: true,
      data,
    };
  },

  async updateProperty(id: string, data: unknown) {
    return {
      success: true,
      id,
      data,
    };
  },

  async deleteProperty(id: string) {
    return {
      success: true,
      id,
    };
  },

  async getPropertyById(id: string) {
    return {
      success: true,
      id,
    };
  },

  async listProperties() {
    return [];
  },
};