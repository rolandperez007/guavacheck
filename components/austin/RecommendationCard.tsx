export function RecommendationCard({ data }: any) {
  if (!data) return null;

  return (
    <div className="border rounded p-4 bg-blue-50">
      <h3 className="font-bold text-blue-700">
        Property Recommendation
      </h3>

      <div className="mt-2 text-sm space-y-1">
        <p>Type: {data.type}</p>
        <p>Location Fit: {data.locationFit}</p>
        <p>Budget Range: ₦{data.budget}</p>
        <p>Reason: {data.reason}</p>
      </div>
    </div>
  );
}


