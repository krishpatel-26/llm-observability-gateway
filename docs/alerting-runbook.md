# LLM gateway alerting runbook

## Elevated error rate
1. Confirm the observation window and traffic volume.
2. Break down errors by model and error category.
3. Check whether failures are input validation, provider, timeout, or rate-limit related.
4. Compare latency buckets and p95 latency with the same window.
5. Apply a documented mitigation; do not silently drop telemetry.

## High latency
- Inspect p95 and bucket counts.
- Compare models and request sizes.
- Check provider degradation and retry amplification.
- Verify that retries have bounded attempts and timeouts.

## Privacy
Telemetry should not contain raw prompts or completions by default. Redaction is defense-in-depth, not permission to log sensitive content.
