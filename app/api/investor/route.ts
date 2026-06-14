import { MortgageAffordabilityEngine } from "@/lib/austin/ranking/MortgageAffordabilityEngine";

export async function POST(req: Request) {
  try {
    const body = await req.json();
    const properties = body?.properties || [];

    if (!Array.isArray(properties)) {
      return Response.json({ error: "Invalid properties payload" }, { status: 400 });
    }

    const enriched = properties.map((p: any) => {

      const mortgage = MortgageAffordabilityEngine.calculate({
        propertyPrice: p.price || 0,
        monthlyIncome: p.monthlyIncome
      });

      const aiScore = p.aiScore || {
        finalScore: 60,
        roiScore: 10,
        riskScore: 40,
        grade: "C"
      };

      const investmentScore =
        (aiScore.finalScore * 0.5) +
        (aiScore.roiScore * 0.3) -
        (aiScore.riskScore * 0.2);

      let decision = "HOLD";
      if (investmentScore >= 75) decision = "BUY";
      else if (investmentScore >= 55) decision = "WATCH";
      else decision = "AVOID";

      return {
        ...p,

        investment: {
          score: Math.round(investmentScore),
          decision
        },

        mortgage,

        summary: {
          price: p.price,
          location: p.location,
          grade: aiScore.grade
        }
      };
    });

    return Response.json({
      count: enriched.length,
      data: enriched
    });

  } catch (err: any) {
    return Response.json(
      { error: err.message },
      { status: 500 }
    );
  }
}
