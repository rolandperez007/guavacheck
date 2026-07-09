interface StatusBadgeProps {

  status:
    | "online"
    | "offline"
    | "active"
    | "idle"
    | "error"
    | "unknown"
    | "degraded"
    | "checking";

}


export default function StatusBadge({
  status,
}: StatusBadgeProps) {


  return (

    <span
      className="
        rounded-full
        px-3
        py-1
        text-xs
        font-semibold
        uppercase
      "
    >

      {status}

    </span>

  );
}