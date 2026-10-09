# Gateway Latency Buckets

The telemetry snapshot now includes `latency_buckets_ms` with upper-bound buckets at 10, 25, 50, 100, 250, 500, and 1,000 milliseconds, plus a `+Inf` overflow bucket.

Each successful request is assigned to exactly one bucket. This provides a compact latency distribution alongside p95 latency without retaining unbounded samples. The existing rolling latency window remains capped at 1,000 observations.

These in-process metrics reset on process restart; production deployments should export them to a durable metrics backend.
