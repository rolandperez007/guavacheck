"use client";

import { AustinTable } from "./AustinTable";
import { AustinInsightCard } from "./AustinInsightCard";
import { ROIBlock } from "./ROIBlock";
import { RecommendationCard } from "./RecommendationCard";

export function AustinRenderer({ data }: any) {
  if (!data?.ui) return null;

  const ui = data.ui;
  const downloadPDF = async () => {
  try {
    const res = await fetch("/api/austin/report/pdf", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ report: data?.report }),
    });

    const blob = await res.blob();
    const url = window.URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = url;
    a.download = "austin-construction-report.pdf";
    a.click();

    window.URL.revokeObjectURL(url);
  } catch (err) {
    console.error("PDF download failed:", err);
  }
};
  switch (ui.type) {

    // 📊 BOQ TABLE VIEW
    case "boq_table":
      return (
        <div className="space-y-4">
          {ui.tables?.map((t: any, i: number) => (
            <AustinTable key={i} table={t} />
          ))}

          <div style={{ marginTop: 20 }}>
            <button
              onClick={downloadPDF}
              style={{
                padding: "10px 16px",
                background: "#111",
                color: "#fff",
                borderRadius: 8,
                border: "none",
                cursor: "pointer",
              }}
           >
              Download Construction Report (PDF)
          </button>
        </div>
      </div>
   
    );

    // 💡 INSIGHTS VIEW
    case "insight":
      return (
        <div className="space-y-3">
          {ui.insights?.map((i: any, idx: number) => (
            <AustinInsightCard key={idx} insight={i} />
          ))}

          <div style={{ marginTop: 20 }}>
            <button
              onClick={downloadPDF}
              style={{
                padding: "10px 16px",
                background: "#111",
                color: "#fff",
                borderRadius: 8,
                border: "none",
                cursor: "pointer",
              }}
            >
              Download Construction Report (PDF)
            </button>
          </div>
        </div>
      );
    // 📈 ROI VIEW
    case "roi":
      return (
        <ROIBlock data={ui.data} />
      );

    // 🏠 RECOMMENDATION VIEW
    case "recommendation":
      return (
        <RecommendationCard data={ui.data} />
      );

    // 🔁 MIXED DASHBOARD VIEW
       case "dashboard":
         return (
           <div className="space-y-6">
             {ui.tables?.map((t: any, i: number) => (
               <AustinTable key={i} table={t} />
          ))}

          {ui.insights?.map((i: any, idx: number) => (
            <AustinInsightCard key={idx} insight={i} />
          ))}

          <div style={{ marginTop: 20 }}>
            <button
              onClick={downloadPDF}
              style={{
                padding: "10px 16px",
                background: "#111",
                color: "#fff",
                borderRadius: 8,
                border: "none",
                cursor: "pointer",
              }}
            >
              Download Construction Report (PDF)
            </button>
          </div>
        </div>
      )
          default:
            return (
              <pre className="text-xs bg-gray-100 p-2 rounded">
                {JSON.stringify(ui, null, 2)}
              </pre>
            );
        }
      }


