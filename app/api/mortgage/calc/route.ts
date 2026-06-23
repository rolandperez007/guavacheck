export async function GET() {
  return Response.json({
    ok: true,
    message: "mortgage calc working",
    sample: {
      principal: 1000000,
      rate: 6,
      termMonths: 24
    }
  });
}






