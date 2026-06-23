import { IngestionPipeline } from "@/lib/austin/ingestion/IngestionPipeline";
import { MarketForecastEngine } from "@/lib/austin/prediction/MarketForecastEngine";
import { AustinAgent } from "@/lib/austin/agent/AustinAgent";

export async function POST(req: Request) {

  const body = await req.json();
  const user = body?.user;
  const action = body?.action;

  if (!user) {
    return Response.json({ error: "Missing user" }, { status: 400 });
  }

  switch (action) {

    case "dashboard":

      return Response.json({
        feed: IngestionPipeline.getAll().slice(-20),
        insights: "Live global property intelligence feed"
      });

    case "analyze":

      const result = await AustinAgent.analyzeDeal(body);

      return Response.json(result);

    case "forecast":

      return Response.json(
        MarketForecastEngine.predict(body.property)
      );

    default:

      return Response.json({
        error: "Unknown action"
      }, { status: 400 });
  }
}






