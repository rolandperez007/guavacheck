import { supabase } from "../../../../lib/supabase";

export async function POST(req: Request) {
  try {
    const formData = await req.formData();
    const file = formData.get("file") as File;

    if (!file) {
      return Response.json(
        { error: "No file uploaded" },
        { status: 400 }
      );
    }

    const fileName = `${Date.now()}-${file.name}`;

    const { data, error } = await supabase.storage
      .from("property-images")
      .upload(fileName, file);

    if (error) {
      return Response.json(
        { error: error.message },
        { status: 500 }
      );
    }

    const { data: publicUrl } = supabase.storage
      .from("property-images")
      .getPublicUrl(fileName);

    return Response.json({
      url: publicUrl.publicUrl,
    });
  } catch (err: any) {
    return Response.json(
      { error: err.message },
      { status: 500 }
    );
  }
}