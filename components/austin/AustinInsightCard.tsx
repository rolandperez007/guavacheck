export function AustinInsightCard({ insight }: any) {
  return (
    <div className="border-l-4 border-blue-500 bg-blue-50 p-3 rounded">
      <h4 className="font-semibold">Insight</h4>
      <p className="text-sm">{JSON.stringify(insight)}</p>
    </div>
  );
}