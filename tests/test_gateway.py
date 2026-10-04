from app.gateway import Gateway
from app.models import ChatRequest,Message
def test_chat_captures_metadata():
    r=Gateway().chat(ChatRequest(model='mock',messages=[Message(role='user',content='hello')]))
    assert r.request_id and r.input_chars==5 and r.provider
