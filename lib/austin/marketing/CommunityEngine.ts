import { createClient } from "@supabase/supabase-js";

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
);

export class CommunityEngine {

  // 💬 Create post
  static async createPost(data: {
    user_id: string;
    message: string;
    type?: "general" | "investment" | "question";
  }) {

    const { data: post, error } = await supabase
      .from("community_posts")
      .insert([data])
      .select()
      .single();

    return { post, error };
  }

  // 📥 Get feed
  static async getFeed() {

    const { data, error } = await supabase
      .from("community_posts")
      .select("*")
      .order("created_at", { ascending: false });

    return { data, error };
  }

  // 👍 Like post
  static async likePost(post_id: string, user_id: string) {

    const { data, error } = await supabase
      .from("post_likes")
      .insert([{ post_id, user_id }]);

    return { data, error };
  }

  // 💬 Comment system
  static async comment(post_id: string, user_id: string, comment: string) {

    const { data, error } = await supabase
      .from("post_comments")
      .insert([{ post_id, user_id, comment }]);

    return { data, error };
  }
}
