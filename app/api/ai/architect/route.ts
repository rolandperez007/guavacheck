import { generateArchitectAdvice } from "@/lib/aiArchitect";

export async function POST(req: Request) {
  try {
    const body = await req.json();

    const result = generateArchitectAdvice({
      location: body.location,
      price: Number(body.price),
      landSize: Number(body.landSize),
    });

    return Response.json(result);
  } catch (err) {
    return Response.json({ error: "AI Architect failed" }, { status: 500 });
  }
}
