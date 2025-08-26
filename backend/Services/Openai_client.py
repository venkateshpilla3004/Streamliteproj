import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("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"))
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", "0.2"))

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
