export default function Dashboard() {
  return (
    <div className="grid gap-4">
      <h1 className="text-2xl font-bold">Dashboard</h1>

      <div className="grid grid-cols-3 gap-4">
        <div className="p-4 border rounded">Listings</div>
        <div className="p-4 border rounded">Analytics</div>
        <div className="p-4 border rounded">AI Insights</div>
      </div>
    </div>
  );
}
