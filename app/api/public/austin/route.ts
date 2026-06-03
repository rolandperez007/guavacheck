import { ApiKeyManager } from "@/lib/austin/security/ApiKeyManager";
import { AustinEngine } from "@/lib/austin/AustinEngine";
import { RevenueEngine } from "@/lib/austin/economy/RevenueEngine";

export async function POST(req: Request) {

  try {

    const body = await req.json();

    const input = body?.input;
    const apiKey = req.headers.get("x-api-key") || "public_demo";
    const plan = body?.plan || "free";

    if (!input) {
      return Response.json({ error: "Missing input" }, { status: 400 });
    }

    // 🧠 RUN AUSTIN ENGINE
    const engine = new AustinEngine();
    const result = await engine.execute(input);

    // 💰 CHARGE USAGE
    const billing = RevenueEngine.charge(apiKey, "full_analysis");

    return Response.json({
      success: true,
      billing,
      data: result,
      meta: {
        version: "1.0",
        plan,
        apiKey: apiKey.substring(0, 6) + "***"
      }
    });

  } catch (err: any) {

    return Response.json({
      success: false,
      error: err.message
    }, { status: 500 });

  }
}

