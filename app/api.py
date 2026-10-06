from fastapi import FastAPI, HTTPException
from .models import ChatRequest, ChatResponse
from .gateway import Gateway
from .telemetry import telemetry

app = FastAPI(title="LLM Observability Gateway", version="1.1.0")
gateway = Gateway()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/v1/metrics")
def metrics():
    return telemetry.snapshot()

@app.post("/v1/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    try:
        return gateway.chat(req)
    except ValueError as e:
        raise HTTPException(status_code=413, detail=str(e))
