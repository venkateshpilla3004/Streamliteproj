from fastapi import FastAPI, HTTPException
from Schemas import ChatRequest, ChatResponse
from Services.Openai_client import generate_response

app = FastAPI()

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        answer = generate_response(
            persona=request.persona,
            history=request.history,
            prompt=request.prompt
        )
        return ChatResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
def root():
    return {"message": "FastAPI server is running!"}
