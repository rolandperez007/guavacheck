interface MetricCardProps {

  title: string;

  value: string | number;

  description?: string;

  status?:
    | "good"
    | "warning"
    | "danger"
    | "neutral";
}


export default function MetricCard({
  title,
  value,
  description,
  status = "neutral",
}: MetricCardProps) {


  return (
    <div className="rounded-xl border bg-white p-5 shadow-sm">

      <div className="text-sm text-gray-500">
        {title}
      </div>


      <div className="mt-2 text-3xl font-bold">
        {value}
      </div>


      {description && (
        <div className="mt-2 text-sm text-gray-500">
          {description}
        </div>
      )}


      <div className="mt-3 text-xs uppercase">
        {status}
      </div>

    </div>
  );
}