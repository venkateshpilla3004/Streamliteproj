import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client with API key from .env
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Model and temperature from env (with defaults)
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", "0.2"))

print("API KEY LOADED:", os.getenv("OPENAI_API_KEY"))


SYSTEM_PERSONAS = {
    "Default": "You are a helpful assistant.",
    "Tutor": "You explain concepts simply with examples.",
    "Therapist": "You respond empathetically with supportive advice.",
    "Coach": "You motivate and provide action steps."
}

def generate_response(persona, history, prompt):
    messages = [{"role": "system", "content": SYSTEM_PERSONAS.get(persona, "Default")}]
    messages.extend(history or [])
    messages.append({"role": "user", "content": prompt})

    completion = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=TEMPERATURE,
    )
    return completion.choices[0].message.content.strip()
