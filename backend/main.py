from fastapi import FastAPI
from Schemas import ChatRequest, ChatResponse

app = FastAPI()

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    # Simple dummy response for now
    return ChatResponse(answer=f"You said: {request.prompt}")
@app.get("/")
def root():
    return {"message": "FastAPI server is running!"}
