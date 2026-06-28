import { propertyService } from "../../../../services/propertyService";

export async function POST(req: Request) {
  try {
    const { id } = await req.json();

    if (!id) {
      return Response.json(
        { success: false, error: "Property ID required" },
        { status: 400 }
      );
    }

    const result = await propertyService.deleteProperty(id);

    if (!result.success) {
      return Response.json(result, { status: 500 });
    }

    return Response.json(result);
  } catch {
    return Response.json(
      { success: false, error: "Delete failed" },
      { status: 500 }
    );
  }
}