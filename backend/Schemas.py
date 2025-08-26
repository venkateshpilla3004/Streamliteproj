from typing import List, Literal, Optional
from pydantic import BaseModel

class Message(BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str

class ChatRequest(BaseModel):
    prompt: str
    persona: Literal["Default", "Tutor", "Therapist", "Coach"] = "Default"
    history: Optional[List[Message]] = []

class ChatResponse(BaseModel):
    answer: str
