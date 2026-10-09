import time
import uuid
import logging
from .config import settings
from .models import ChatRequest, ChatResponse
from .telemetry import telemetry

log = logging.getLogger(__name__)

class Gateway:
    def chat(self, req: ChatRequest) -> ChatResponse:
        if not req.messages:
            telemetry.record_error("empty_messages")
            raise ValueError("at least one message is required")
        chars = sum(len(m.content) for m in req.messages)
        if chars > settings.max_prompt_chars:
            telemetry.record_error("prompt_too_large")
            raise ValueError("prompt exceeds configured limit")

        start = time.perf_counter()
        out = f"[mock:{req.model}] {req.messages[-1].content.strip()}"
        rid = str(uuid.uuid4())
        latency = (time.perf_counter() - start) * 1000
        telemetry.record_success(req.model, latency)

        log.info("llm_request", extra={
            "request_id": rid, "provider": settings.llm_provider,
            "model": req.model, "input_chars": chars, "latency_ms": latency,
        })
        return ChatResponse(
            request_id=rid, output=out, latency_ms=latency,
            input_chars=chars, provider=settings.llm_provider,
        )
