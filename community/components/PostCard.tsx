import type { FC } from "react";

type Props = {
  post: any;
};

const PostCard: FC<Props> = ({ post }) => {
  return (
    <article className="rounded-3xl border bg-white p-6 mb-6 shadow-sm hover:shadow-md transition">

      <div className="flex items-center justify-between">

        <div>

          <h3 className="font-semibold">{post.author}</h3>

          <p className="text-sm text-gray-500">

            {post.role}

          </p>

        </div>

        <span className="text-xs rounded-full bg-green-50 px-3 py-1">

          {post.category}

        </span>

      </div>

      <h2 className="text-2xl font-semibold mt-5">

        {post.title}

      </h2>

      <p className="text-gray-600 mt-3">

        {post.excerpt}

      </p>

      <div className="flex gap-6 mt-6 text-sm text-gray-500">

        <span>👍 {post.likes}</span>

        <span>💬 {post.replies}</span>

        <span>{post.time}</span>

      </div>

    </article>
  );
};

export default PostCard;