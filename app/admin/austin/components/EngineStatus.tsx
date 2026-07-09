"use client";

import SectionTitle from "../widgets/SectionTitle";
import StatusBadge from "../widgets/StatusBadge";


const engines = [

  "Austin Engine",
  "Verification Engine",
  "Geo Engine",
  "World Engine",
  "Memory Engine",

];


export default function EngineStatus() {


  return (

    <section>

      <SectionTitle
        title="Engine Status"
        subtitle="Austin intelligence modules"
      />


      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">


        {engines.map((engine) => (

          <div
            key={engine}
            className="rounded-xl border bg-white p-5 shadow-sm"
          >

            <div className="flex items-center justify-between">

              <span className="font-semibold">
                {engine}
              </span>


              <StatusBadge
                status="active"
              />

            </div>


            <p className="mt-3 text-sm text-gray-500">
              Operational monitoring enabled.
            </p>


          </div>

        ))}


      </div>


    </section>

  );
}