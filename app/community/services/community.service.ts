import { supabase } from "@/lib/supabase";

export async function getCommunityPosts() {
  const { data, error } = await supabase
    .from("community_posts")
    .select("*")
    .eq("published", true)
    .order("featured", { ascending: false })
    .order("created_at", { ascending: false });

  if (error) throw error;

  return data ?? [];
}
