import { NextResponse } from "next/server";

// TEMP SAFE MOCK (prevents build failure)
// Replace later with your real AI engine safely
async function rankProperties(properties: any[]) {
  return properties.map((p) => ({
    id: p.id,
    investmentScore: Math.floor(Math.random() * 100),
    constructionEstimate: null,
    distressedScore: Math.floor(Math.random() * 100),
    grade: "B",
    meta: {
      model: "mock-v1",
    },
  }));
}

export async function GET() {
  try {
    // 1. Mock properties (replace with DB later)
    const properties = [
      {
        id: "1",
        title: "Sample Property A",
        location: "Lagos",
        price: 5000000,
        status: "active",
      },
      {
        id: "2",
        title: "Sample Property B",
        location: "Abuja",
        price: 12000000,
        status: "draft",
      },
    ];

    // 2. Rank properties safely
    const ranked = await rankProperties(properties);

    // 3. Merge ranking + properties
    const enriched = properties.map((p) => {
      const score = ranked?.find?.((r: any) => r.id === p.id);

      return {
        ...p,
        aiScore: score || null,
      };
    });

    // 4. Return response
    return NextResponse.json({
      success: true,
      count: enriched.length,
      data: enriched,
    });
  } catch (error: any) {
    return NextResponse.json(
      {
        success: false,
        error: error?.message || "AI feed failed",
      },
      { status: 500 }
    );
  }
}






