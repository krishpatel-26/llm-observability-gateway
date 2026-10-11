from app.redaction import redact_sensitive_text

def test_redacts_key_value_secrets():
    assert "supersecret" not in redact_sensitive_text("api_key=supersecret")

def test_redacts_token_like_values():
    assert "sk-" not in redact_sensitive_text("token sk-abcdefghijklmnop")

def test_preserves_non_sensitive_context():
    assert redact_sensitive_text("model=demo latency_ms=12") == "model=demo latency_ms=12"
