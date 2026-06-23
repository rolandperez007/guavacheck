import { PDFDocument, StandardFonts, rgb } from "pdf-lib";

export async function POST(req: Request) {
  try {
    const body = await req.json();
    const report = body?.report;

    if (!report) {
      return Response.json({ error: "Missing report" }, { status: 400 });
    }

    const pdf = await PDFDocument.create();
    const page = pdf.addPage([600, 800]);

    const font = await pdf.embedFont(StandardFonts.Helvetica);

    let y = 750;

    const draw = (text: string, size = 12) => {
      page.drawText(String(text ?? ""), {
        x: 50,
        y,
        size,
        font,
        color: rgb(0, 0, 0),
      });
      y -= 20;
    };

    // HEADER
    draw("AUSTIN REAL ESTATE REPORT", 16);
    y -= 10;

    // PROPERTY INFO
    draw(`Title: ${report?.project?.title}`);
    draw(`Location: ${report?.project?.location}`);
    draw(`Size: ${report?.project?.sqm} sqm`);
    draw(`Level: ${report?.project?.level}`);

    y -= 10;

    // FINANCIAL SUMMARY
    draw("FINANCIAL SUMMARY", 14);
    draw(`Total Cost: ${report?.summary?.totalCost}`);
    draw(`Monthly Mortgage: ${report?.summary?.monthlyPayment}`);
    draw(`ROI Score: ${report?.summary?.roiScore}`);

    y -= 10;

    // PHASES
    draw("PROJECT PHASES", 14);

    for (const p of report?.phases || []) {
      draw(`${p.name}: ${p.duration} weeks - ${p.cost}`);
    }

    y -= 10;

    // TIMELINE
    draw("TIMELINE", 14);

    for (const t of report?.timeline || []) {
      draw(`Week ${t.week}: ${t.activity}`);
    }

    y -= 10;

    // INSIGHTS
    draw("INSIGHTS", 14);

    for (const i of report?.insights || []) {
      draw(`- ${i}`);
    }

    const pdfBytes = await pdf.save();

    return new Response(pdfBytes, {
      headers: {
        "Content-Type": "application/pdf",
        "Content-Disposition": "attachment; filename=austin-report.pdf"
      }
    });

  } catch (err: any) {
    return Response.json(
      { error: err.message },
      { status: 500 }
    );
  }
}






