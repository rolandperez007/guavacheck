import Link from "next/link";

export default function NotFound() {
  return (
    <main className="container mx-auto py-20 text-center">
      <h1 className="text-6xl font-bold">Property Not Found</h1>

      <p className="mt-5 text-gray-600">
        This property may have been removed or is no longer available.
      </p>

      <Link
        href="/properties"
        className="mt-10 inline-block rounded-lg bg-emerald-600 px-6 py-3 text-white"
      >
        Browse Properties
      </Link>
    </main>
  );
}
