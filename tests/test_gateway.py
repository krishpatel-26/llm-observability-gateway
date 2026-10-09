from app.gateway import Gateway
from app.models import ChatRequest, Message
from app.telemetry import telemetry

def test_chat_captures_metadata():
    r = Gateway().chat(ChatRequest(model="mock", messages=[Message(role="user", content="hello")]))
    assert r.request_id and r.input_chars == 5 and r.provider
    metrics = telemetry.snapshot()
    assert metrics["requests"] >= 1
    assert metrics["by_model"]["mock"] >= 1

def test_prompt_limit_records_error():
    from app.config import settings
    before = telemetry.snapshot()["errors"]
    try:
        Gateway().chat(ChatRequest(model="mock", messages=[Message(role="user", content="x" * (settings.max_prompt_chars + 1))]))
    except ValueError:
        pass
    metrics = telemetry.snapshot()
    assert metrics["errors"] == before + 1
    assert metrics["errors_by_type"]["prompt_too_large"] >= 1

def test_empty_messages_are_classified():
    before = telemetry.snapshot()["errors_by_type"].get("empty_messages", 0)
    try:
        Gateway().chat(ChatRequest(model="mock", messages=[]))
    except ValueError:
        pass
    assert telemetry.snapshot()["errors_by_type"]["empty_messages"] == before + 1
