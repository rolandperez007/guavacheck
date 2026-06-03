export function ROIBlock({ data }: any) {
  if (!data) return null;

  return (
    <div className="border rounded p-4 bg-green-50">
      <h3 className="font-bold text-green-700">
        ROI Analysis
      </h3>

      <div className="mt-2 text-sm space-y-1">
        <p>Recommended Type: {data.recommendedType}</p>
        <p>Floors: {data.floors}</p>
        <p>Land Size: {data.landSize} sqm</p>
        <p>Estimated Cost: ₦{data.estimatedCost?.toLocaleString()}</p>
        <p className="font-bold">
          ROI Score: {data.roiScore} / 100
        </p>
      </div>
    </div>
  );
}