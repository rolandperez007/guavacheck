import { supabase } from "../../../../lib/supabase";

export async function POST(req: Request) {
  try {
    const { id } = await req.json();

    if (!id) {
      return Response.json(
        { error: "Property ID required" },
        { status: 400 }
      );
    }

    const { error } = await supabase
      .from("properties")
      .delete()
      .eq("id", id);

    if (error) {
      return Response.json(
        { error: error.message },
        { status: 500 }
      );
    }

    return Response.json({ success: true });
  } catch (err: any) {
    return Response.json(
      { error: "Delete failed" },
      { status: 500 }
    );
  }
}