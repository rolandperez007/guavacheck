import { supabase } from "@/lib/supabase";

export class CommunityService {

  static async getPosts() {

    const { data, error } = await supabase
      .from("community_posts")
      .select("*")
      .order("created_at", { ascending: false });

    if (error) throw error;

    return data;
  }

  static async getPost(slug: string) {

    const { data, error } = await supabase
      .from("community_posts")
      .select("*")
      .eq("slug", slug)
      .single();

    if (error) throw error;

    return data;
  }

  static async createPost(post: any) {

    const { data, error } = await supabase
      .from("community_posts")
      .insert(post)
      .select()
      .single();

    if (error) throw error;

    return data;
  }

  static async addComment(comment: any) {

    return supabase
      .from("community_comments")
      .insert(comment);
  }

  static async likePost(postId: string, userId: string) {

    return supabase
      .from("community_likes")
      .insert({
        post_id: postId,
        user_id: userId
      });
  }
}
