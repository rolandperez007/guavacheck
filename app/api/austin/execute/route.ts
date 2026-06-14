import { AustinEngine } from "@/lib/austin/AustinEngine";

export async function POST(req: Request) {
  const encoder = new TextEncoder();
  const stream = new TransformStream();
  const writer = stream.writable.getWriter();

  const engine = new AustinEngine();

  const body = await req.json();
  const input = body?.input;

  if (!input) {
    writer.write(encoder.encode("event: error\ndata: Missing input\n\n"));
    writer.close();
    return new Response(stream.readable);
  }

  // 🚀 STREAM EXECUTION
  (async () => {
    try {
      await engine.executeStream(input, async (event: any) => {
        writer.write(
          encoder.encode(`data: ${JSON.stringify(event)}\n\n`)
        );
      });

      writer.write(
        encoder.encode(`event: done\ndata: complete\n\n`)
      );

      writer.close();
    } catch (err: any) {
      writer.write(
        encoder.encode(`event: error\ndata: ${err.message}\n\n`)
      );
      writer.close();
    }
  })();

  return new Response(stream.readable, {
    headers: {
      "Content-Type": "text/event-stream",
      "Cache-Control": "no-cache",
      Connection: "keep-alive"
    }
  });
}