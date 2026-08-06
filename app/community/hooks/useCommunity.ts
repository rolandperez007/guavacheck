"use client";

import { useEffect, useState } from "react";
import { getCommunityPosts } from "../services/community.service";

export function useCommunity() {
  const [posts, setPosts] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function load() {
      try {
        setLoading(true);
        const data = await getCommunityPosts();
        setPosts(data);
      } catch (err: any) {
        setError(err.message || "Failed to load posts");
      } finally {
        setLoading(false);
      }
    }

    load();
  }, []);

  return { posts, loading, error };
}
