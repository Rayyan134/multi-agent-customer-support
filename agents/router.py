import json
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class AgentRouter:
    def __init__(self):
        self.agents = ["product", "shipping"]

    def decide(self, message: str) -> str:
        """
        Uses LLM to decide which agent should handle the request.
        """

        prompt = f"""
You are a routing system for a customer support AI.

You must decide which agent should handle the user query.

Agents:
- product → handles product availability, pricing, features
- shipping → handles delivery times, shipping cost, logistics

Return ONLY one word:
product OR shipping OR fallback

User query:
{message}
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        decision = (response.choices[0].message.content or "").strip().lower()
        return decision