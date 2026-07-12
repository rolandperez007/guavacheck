"use client";

export default function PropertyError({
  error,
  reset,
}: {
  error: Error;
  reset: () => void;
}) {
  return (
    <main className="container mx-auto py-20 text-center">

      <h1 className="text-5xl font-bold text-red-600">
        Unable to load property
      </h1>

      <p className="mt-4 text-gray-600">
        {error.message}
      </p>

      <button
        onClick={reset}
        className="mt-8 rounded-lg bg-emerald-600 px-6 py-3 text-white"
      >
        Reload
      </button>

    </main>
  );
}