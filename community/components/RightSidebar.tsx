export default function RightSidebar() {
  return (
    <aside className="space-y-6">

      <div className="rounded-3xl border p-6">

        <h3 className="font-semibold">

          Community Statistics

        </h3>

        <div className="mt-4 space-y-2 text-gray-600">

          <p>Members: 12,840</p>

          <p>Today's Posts: 216</p>

          <p>Verified Experts: 94</p>

        </div>

      </div>

      <div className="rounded-3xl border p-6">

        <h3 className="font-semibold">

          Popular Categories

        </h3>

        <div className="mt-4 space-y-2">

          <p>Architecture</p>

          <p>Construction</p>

          <p>Finance</p>

          <p>Materials</p>

          <p>Interior Design</p>

        </div>

      </div>

    </aside>
  );
}