"use client";

import { useEffect, useState } from "react";
import { CommunityService } from "@/lib/services/CommunityService";

export default function CommunityPage() {
  const [posts, setPosts] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadPosts() {
      try {
        const data = await CommunityService.getPosts();
        setPosts(data || []);
      } catch (err) {
        console.error("Failed to load posts:", err);
      } finally {
        setLoading(false);
      }
    }

    loadPosts();
  }, []);

  return (
    <main className="p-6">
      <h1 className="text-2xl font-bold mb-4">
        Community
      </h1>

      {loading ? (
        <p>Loading posts...</p>
      ) : (
        <div className="space-y-4">
          {posts.map((post, idx) => (
            <div key={idx} className="border rounded-lg p-4">
              <h2 className="font-semibold">
                {post.title || "Untitled"}
              </h2>
              <p>{post.content || post.body}</p>
            </div>
          ))}
        </div>
      )}
    </main>
  );
}









