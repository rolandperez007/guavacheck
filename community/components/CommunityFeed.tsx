import { posts } from "../data/mockPosts";
import PostCard from "./PostCard";

export default function CommunityFeed() {
  return (
    <section className="mt-8">

      {posts.map((post) => (

        <PostCard
          key={post.id}
          post={post}
        />

      ))}

    </section>
  );
}