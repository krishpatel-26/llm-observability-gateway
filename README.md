# LLM Observability Gateway

Provider-neutral LLM gateway with request validation, telemetry capture, structured logging, and a deterministic local provider.

## Architecture

`client -> validation -> provider -> telemetry -> response`

The gateway exposes `GET /v1/metrics` with request count, error count/rate, rolling p95 latency, and per-model traffic. The latency window is bounded to the latest 1,000 successful requests.

## Run

`pip install -r requirements.txt`

`uvicorn app.api:app --reload`

- POST `/v1/chat` with a model and message list
- GET `/v1/metrics` for gateway telemetry
- GET `/health` for liveness
