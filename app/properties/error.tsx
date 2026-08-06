"use client";

export default function Error({ error, reset }: { error: Error; reset: () => void }) {
  return (
    <main className="container mx-auto py-20 text-center">
      <h1 className="text-4xl font-bold text-red-600">Something went wrong</h1>

      <p className="mt-5 text-gray-600">{error.message}</p>

      <button onClick={reset} className="mt-8 rounded-lg bg-emerald-600 px-6 py-3 text-white">
        Try Again
      </button>
    </main>
  );
}
