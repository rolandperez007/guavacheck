import { supabase } from "../../../../lib/supabase";

export async function POST(req: Request) {
  try {
    const body = await req.json();

    const { id, title, location, price, status, image_url } = body;

    if (!id) {
      return Response.json({ error: "ID required" }, { status: 400 });
    }

    const { data, error } = await supabase
      .from("properties")
      .update({
        title,
        location,
        price: price && !isNaN(Number(price)) ? Number(price) : 0,
        status,
        image_url: image_url || null,
      })
      .eq("id", id)
      .select();

    if (error) {
      return Response.json({ error: error.message }, { status: 500 });
    }

    return Response.json(data);
  } catch (err) {
    return Response.json({ error: "Update failed" }, { status: 500 });
  }
}






