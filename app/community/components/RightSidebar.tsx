export default function RightSidebar() {
  return (
    <div className="space-y-6">
      <section className="rounded-3xl border bg-white p-6 shadow-sm">
        <h2 className="font-semibold">Community</h2>

        <div className="mt-4 space-y-2 text-gray-600">
          <p>Members: 12,842</p>
          <p>Verified Experts: 96</p>
          <p>Posts Today: 214</p>
        </div>
      </section>

      <section className="rounded-3xl border bg-white p-6 shadow-sm">
        <h2 className="font-semibold">Popular Topics</h2>

        <div className="mt-4 space-y-2">
          <p>Architecture</p>
          <p>Construction</p>
          <p>Finance</p>
          <p>Interior Design</p>
        </div>
      </section>
    </div>
  );
}
