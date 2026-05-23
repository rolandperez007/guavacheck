import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

function sanitizePrompt(input) {
  return input
    .replace(/api[_-]?key/gi, "[REDACTED]")
    .replace(/\b\d{12,}\b/g, "[REDACTED]");
}

export async function POST(req) {
  try {
    const body = await req.json();

    if (!body.prompt) {
      return Response.json(
        { error: "Prompt is required" },
        { status: 400 }
      );
    }

    const cleanPrompt = sanitizePrompt(body.prompt);

    const completion = await client.chat.completions.create({
      model: "gpt-4.1-mini",
      messages: [
        {
          role: "system",
          content:
            "You are Guava AI, a secure real estate intelligence assistant.",
        },
        {
          role: "user",
          content: cleanPrompt,
        },
      ],
    });

    return Response.json({
      success: true,
      response: completion.choices[0].message.content,
    });
  } catch (error) {
    console.error(error);

    return Response.json(
      { error: "AI request failed" },
      { status: 500 }
    );
  }
}