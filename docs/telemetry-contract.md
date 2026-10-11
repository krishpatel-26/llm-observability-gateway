# Telemetry contract

A request observation should record only operational fields needed for debugging and SLOs.

Recommended fields:
- timestamp and request correlation ID
- model/provider identifier
- duration in milliseconds
- outcome and normalized error category
- input/output token counts when available
- retry count and timeout indicator

Avoid raw prompt/completion content, credentials, and direct personal identifiers. Keep metric labels bounded; do not use request IDs or user IDs as metric labels because they create unbounded cardinality. Redact sensitive strings before writing logs.
