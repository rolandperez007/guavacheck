import { RevenueEngine } from "@/lib/austin/economy/RevenueEngine";
import { IngestionPipeline } from "@/lib/austin/ingestion/IngestionPipeline";
import { MarketForecastEngine } from "@/lib/austin/prediction/MarketForecastEngine";

export async function GET() {

  return Response.json({
    revenue: RevenueEngine.calculateRevenue(),
    ingestion: {
      total: IngestionPipeline.getAll().length
    },
    predictions: {
      total: MarketForecastEngine["history"]?.length || 0
    },
    system: {
      status: "healthy",
      ai: "online",
      forecast: "active"
    }
  });
}
