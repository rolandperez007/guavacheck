import Link from "next/link";

export default function PropertyNotFound() {
  return (
    <main className="container mx-auto py-20 text-center">

      <h1 className="text-6xl font-bold">
        404
      </h1>

      <p className="mt-4 text-gray-600">
        We couldn't find the property you're looking for.
      </p>

      <Link
        href="/properties"
        className="mt-8 inline-block rounded-lg bg-emerald-600 px-6 py-3 text-white"
      >
        Back to Properties
      </Link>

    </main>
  );
}