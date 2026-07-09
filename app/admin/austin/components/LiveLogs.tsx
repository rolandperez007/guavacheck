"use client";

import SectionTitle from "../widgets/SectionTitle";


const logs = [

  "Austin Engine initialized",
  "Global Parser v3 loaded",
  "Verification Engine heartbeat received",
  "WebSocket stream connected",
  "Memory Engine cache synchronized",

];


export default function LiveLogs() {


  return (

    <section>

      <SectionTitle
        title="Live Logs"
        subtitle="Real-time Austin engineering events"
      />


      <div
        className="
          rounded-xl
          border
          bg-black
          p-5
          font-mono
          text-sm
        "
      >

        {logs.map((log, index) => (

          <div
            key={index}
            className="mb-2"
          >

            <span>
              [{new Date().toLocaleTimeString()}]
            </span>

            {" "}

            {log}

          </div>

        ))}


      </div>


    </section>

  );
}