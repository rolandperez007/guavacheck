from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")


class AustinGPT:
    def explain(self, query: str, analysis: dict):
        prompt = f"""
You are Austin AI, a real estate investment assistant.

User Query:
{query}

Analysis Result:
{analysis}

Give a short, clear, human explanation of the investment decision.
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a real estate AI assistant."},
                {"role": "user", "content": prompt},
            ],
        )

        return response.choices[0].message.content
