import { PropertyService } from "@/services/austin/PropertyService";
import { PropertyRankingEngine } from "@/lib/austin/ranking/PropertyRankingEngine";

export async function GET() {
  try {
    // 1. Get raw properties
    const properties = await PropertyService.search();

    // 2. Rank using AI engine
    const ranked = PropertyRankingEngine.rank(properties);

    // 3. Merge ranking + property data
    const enriched = properties.map((p: any) => {
      const score = ranked.find(r => r.id === p.id);

      return {
        ...p,
        aiScore: score
      };
    });

    // 4. Sort by intelligence score
    enriched.sort(
      (a: any, b: any) =>
        (b.aiScore?.finalScore || 0) - (a.aiScore?.finalScore || 0)
    );

    return Response.json({
      success: true,
      count: enriched.length,
      data: enriched
    });

  } catch (err: any) {
    return Response.json(
      { success: false, error: err.message },
      { status: 500 }
    );
  }
}