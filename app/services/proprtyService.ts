import { supabase } from "../lib/supabase/client";

export const propertyService = {
  async deleteProperty(id: string) {
    const { error } = await supabase
      .from("properties")
      .delete()
      .eq("id", id);

    if (error) {
      return {
        success: false,
        error: error.message,
      };
    }

    return { success: true };
  },
};