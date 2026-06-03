"use client";

import { useEffect, useState } from "react";
import { CommunityService } from "@/services/community/CommunityService";

export default function CommunityPage() {

  const [posts, setPosts] = useState<any[]>([]);

  useEffect(() => {

    CommunityService.getPosts()
      .then(setPosts);

  }, []);

  return (
    <div className="p-6">

      <h1>Community</h1>

      {posts.map(post => (

        <div key={post.id}>

          <h2>{post.title}</h2>

          <p>{post.excerpt}</p>

        </div>

      ))}

    </div>
  );
}