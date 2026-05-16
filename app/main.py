from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import os
from config import settings

app = FastAPI(title="Local AI Chat API", version="1.0.0")


class ChatRequest(BaseModel):
    message: str
    model: str = settings.DEFAULT_MODEL


class ChatResponse(BaseModel):
    reply: str
    model: str


@app.get("/health")
async def health():
    return {"status": "ok", "version": "1.0.0"}


@app.get("/models")
async def list_models():
    async with httpx.AsyncClient() as client:
        res = await client.get(f"{settings.OLLAMA_URL}/api/tags")
        return res.json()


@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    payload = {
        "model": req.model,
        "prompt": req.message,
        "stream": False
    }
    async with httpx.AsyncClient(timeout=120) as client:
        try:
            res = await client.post(
                f"{settings.OLLAMA_URL}/api/generate",
                json=payload
            )
            data = res.json()
            return ChatResponse(reply=data["response"], model=req.model)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
