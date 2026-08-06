export default function LoadingProperties() {
  return (
    <main className="container mx-auto py-16">
      <div className="animate-pulse space-y-6">
        <div className="h-10 w-72 rounded bg-gray-200" />

        <div className="h-5 w-full rounded bg-gray-200" />

        <div className="h-5 w-5/6 rounded bg-gray-200" />

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-10">
          {Array.from({ length: 6 }).map((_, index) => (
            <div key={index} className="rounded-xl border p-4 space-y-4">
              <div className="h-52 rounded bg-gray-200" />

              <div className="h-6 rounded bg-gray-200" />

              <div className="h-4 rounded bg-gray-200" />
            </div>
          ))}
        </div>
      </div>
    </main>
  );
}
