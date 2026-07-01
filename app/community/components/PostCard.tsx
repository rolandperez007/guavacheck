import { CommunityPost } from "../types/community";

interface Props {
  post: CommunityPost;
}

export default function PostCard({ post }: Props) {
  return (
    <article className="rounded-3xl border bg-white p-6 shadow-sm">

      <div className="flex justify-between">

        <div>

          <h3 className="font-semibold">
            {post.author}
          </h3>

          <p className="text-sm text-gray-500">
            {post.role}
          </p>

        </div>

        <span className="rounded-full bg-green-50 px-3 py-1 text-sm">

          {post.category}

        </span>

      </div>

      <h2 className="mt-5 text-2xl font-bold">

        {post.title}

      </h2>

      <p className="mt-3 text-gray-600">

        {post.excerpt}

      </p>

      <div className="mt-6 flex gap-6 text-sm text-gray-500">

        <span>👍 {post.likes}</span>

        <span>💬 {post.replies}</span>

        <span>{post.time}</span>

      </div>

    </article>
  );
}