"use client";

import { useRouter } from "next/navigation";

export default function RecoveryActions() {
  const router = useRouter();

  return (
    <div className="flex flex-wrap justify-center gap-3 mt-6">
      <button onClick={() => router.push("/")} className="px-4 py-2 bg-green-600 rounded">
        🏠 Home
      </button>

      <button onClick={() => router.push("/properties")} className="px-4 py-2 bg-blue-600 rounded">
        🏡 Properties
      </button>

      <button onClick={() => router.push("/dashboard")} className="px-4 py-2 bg-purple-600 rounded">
        📊 Dashboard
      </button>
    </div>
  );
}
