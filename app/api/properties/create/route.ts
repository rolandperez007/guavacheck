import { supabase } from "@/lib/supabase";

export async function POST(req: Request) {
  try {
    const body = await req.json();

    const {
      title,
      location,
      price,
      status,
      user_id,
    } = body;

    // 🔒 strict validation
    if (!title || !location) {
      return Response.json(
        { error: "title and location are required" },
        { status: 400 }
      );
    }

    const { data, error } = await supabase
      .from("properties")
      .insert([
        {
          title,
          location,
          price: price ? Number(price) : null,
          status: status || "draft",
          user_id: user_id || null,
        },
      ])
      .select();

    if (error) {
      return Response.json(
        { error: error.message },
        { status: 500 }
      );
    }

    return Response.json(data);
  } catch (err) {
    return Response.json(
      { error: "Invalid request" },
      { status: 400 }
    );
  }
}



