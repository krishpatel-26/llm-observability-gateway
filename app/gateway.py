import time,uuid,logging
from .config import settings
from .models import ChatRequest,ChatResponse
log=logging.getLogger(__name__)
class Gateway:
    def chat(self,req:ChatRequest)->ChatResponse:
        chars=sum(len(m.content) for m in req.messages)
        if chars>settings.max_prompt_chars: raise ValueError('prompt exceeds configured limit')
        start=time.perf_counter(); out=f'[mock:{req.model}] {req.messages[-1].content.strip()}'
        rid=str(uuid.uuid4()); latency=(time.perf_counter()-start)*1000
        log.info('llm_request',extra={'request_id':rid,'provider':settings.llm_provider,'input_chars':chars,'latency_ms':latency})
        return ChatResponse(request_id=rid,output=out,latency_ms=latency,input_chars=chars,provider=settings.llm_provider)
