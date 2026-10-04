from pydantic import BaseModel,Field
class Message(BaseModel):
    role:str=Field(pattern='^(system|user|assistant)$')
    content:str=Field(min_length=1)
class ChatRequest(BaseModel):
    model:str=Field(min_length=1,max_length=100)
    messages:list[Message]=Field(min_length=1)
class ChatResponse(BaseModel):
    request_id:str
    output:str
    latency_ms:float
    input_chars:int
    provider:str
