# Latency bucket interpretation

Latency buckets help operators understand tail behavior rather than relying only on averages.

- Median latency describes a typical request.
- p95 latency approximates the boundary for the slowest 5% of requests.
- Bucket counts show distribution across configured thresholds.
- Compare like-for-like windows and segment by model/provider when volume permits.

Do not infer provider causality from correlation alone. Low-volume windows can produce unstable percentiles; show sample size alongside summaries.
