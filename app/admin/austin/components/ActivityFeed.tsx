const activities = [

  "Austin started.",

  "Verification Engine online.",

  "Geo Engine synchronized.",

  "Redis cache connected.",

  "Memory initialized.",

  "Background workers healthy."

];

export default function ActivityFeed() {

  return (

    <div className="rounded-xl border border-slate-800 bg-[#0d1a28] p-5">

      <h2 className="mb-5 text-lg font-bold">
        Activity
      </h2>

      <div className="space-y-3">

        {activities.map((item, index) => (

          <div
            key={index}
            className="rounded-lg bg-[#101d2d] p-3"
          >

            <p className="text-sm text-slate-300">

              {item}

            </p>

          </div>

        ))}

      </div>

    </div>

  );

}