import os

import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load the local API.env file
load_dotenv("API.env")

# First read the local environment variable
api_key = os.getenv("GEMINI_API_KEY")

# If deployed on Streamlit Cloud, try Streamlit Secrets
if not api_key:
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except (FileNotFoundError, KeyError):
        api_key = None

client = genai.Client(api_key=api_key) if api_key else None


def get_ai_recommendation(prompt):
    """Send a prompt to Gemini and return its response."""

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

        except Exception:
            continue

    return None