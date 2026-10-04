from fastapi import FastAPI,HTTPException
from .models import ChatRequest,ChatResponse
from .gateway import Gateway
app=FastAPI(title='LLM Observability Gateway',version='1.0.0'); gateway=Gateway()
@app.get('/health')
def health(): return {'status':'ok'}
@app.post('/v1/chat',response_model=ChatResponse)
def chat(req:ChatRequest):
    try:return gateway.chat(req)
    except ValueError as e:raise HTTPException(status_code=413,detail=str(e))
