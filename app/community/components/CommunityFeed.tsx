"use client";

import PostCard from "./PostCard";
import { useCommunity } from "../hooks/useCommunity";

export default function CommunityFeed() {
  const { posts, loading, error } = useCommunity();

  if (loading) {
    return (
      <div className="text-gray-500 p-6">
        Loading Community Square...
      </div>
    );
  }

  if (error) {
    return (
      <div className="text-red-500 p-6">
        {error}
      </div>
    );
  }

  if (!posts.length) {
    return (
      <div className="text-gray-500 p-6">
        No discussions yet. Be the first to post.
      </div>
    );
  }

  return (
    <section className="space-y-6">
      {posts.map((post) => (
        <PostCard key={post.id} post={post} />
      ))}
    </section>
  );
}