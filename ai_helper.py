import os

from dotenv import load_dotenv
from google import genai
from google.genai.errors import ServerError

load_dotenv("API.env")

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None


def get_ai_recommendation(prompt):
    """Return an AI recommendation, or None if Gemini is unavailable."""

    if client is None:
        return None

    models_to_try = [
        "gemini-3.1-flash-lite",
        "gemini-3.5-flash"
    ]

    for model_name in models_to_try:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt
            )
            return response.text

        except ServerError:
            continue

        except Exception:
            return None

    return None