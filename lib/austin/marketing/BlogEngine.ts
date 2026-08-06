import { createClient } from "@supabase/supabase-js";

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
);

export class BlogEngine {
  // 📰 Create blog post
  static async createPost(data: {
    title: string;
    content: string;
    author_id?: string;
    tags?: string[];
  }) {
    const { data: post, error } = await supabase
      .from("blog_posts")
      .insert([data])
      .select()
      .single();

    return { post, error };
  }

  // 📚 Fetch all posts
  static async getPosts() {
    const { data, error } = await supabase
      .from("blog_posts")
      .select("*")
      .order("created_at", { ascending: false });

    return { data, error };
  }

  // 🔍 Get single post
  static async getPost(id: string) {
    const { data, error } = await supabase.from("blog_posts").select("*").eq("id", id).single();

    return { data, error };
  }

  // 🤖 AI draft helper (hook for later GPT integration)
  static generateDraftPrompt(topic: string) {
    return `
    Write a professional real estate insight article about: ${topic}

    Focus on:
    - Investment value
    - Market trends
    - Global relevance
    - Practical buyer advice
    `;
  }
}
