from collections import defaultdict
from dataclasses import dataclass, field
from threading import Lock

LATENCY_BUCKETS_MS = (10, 25, 50, 100, 250, 500, 1000)

@dataclass
class Telemetry:
    total_requests: int = 0
    total_errors: int = 0
    latencies: list[float] = field(default_factory=list)
    by_model: dict[str, int] = field(default_factory=lambda: defaultdict(int))
    errors_by_type: dict[str, int] = field(default_factory=lambda: defaultdict(int))
    latency_buckets: dict[str, int] = field(default_factory=lambda: defaultdict(int))
    _lock: Lock = field(default_factory=Lock, repr=False)

    def record_success(self, model: str, latency_ms: float) -> None:
        latency = max(0.0, latency_ms)
        with self._lock:
            self.total_requests += 1
            self.latencies.append(latency)
            self.latencies = self.latencies[-1000:]
            self.by_model[model] += 1
            bucket = next((limit for limit in LATENCY_BUCKETS_MS if latency <= limit), "+Inf")
            self.latency_buckets[str(bucket)] += 1

    def record_error(self, error_type: str = "unknown") -> None:
        with self._lock:
            self.total_errors += 1
            self.errors_by_type[error_type] += 1

    def snapshot(self) -> dict:
        with self._lock:
            values = sorted(self.latencies)
            p95 = values[min(len(values) - 1, max(0, int((len(values) - 1) * .95)))] if values else 0.0
            return {
                "requests": self.total_requests,
                "errors": self.total_errors,
                "error_rate": round(self.total_errors / max(1, self.total_requests + self.total_errors), 4),
                "p95_latency_ms": round(p95, 3),
                "by_model": dict(self.by_model),
                "errors_by_type": dict(self.errors_by_type),
                "latency_buckets_ms": dict(self.latency_buckets),
            }

telemetry = Telemetry()
