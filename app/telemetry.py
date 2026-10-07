from collections import defaultdict
from dataclasses import dataclass, field
from threading import Lock

@dataclass
class Telemetry:
    total_requests: int = 0
    total_errors: int = 0
    latencies: list[float] = field(default_factory=list)
    by_model: dict[str, int] = field(default_factory=lambda: defaultdict(int))
    _lock: Lock = field(default_factory=Lock, repr=False)

    def record_success(self, model: str, latency_ms: float) -> None:
        with self._lock:
            self.total_requests += 1
            self.latencies.append(max(0.0, latency_ms))
            self.latencies = self.latencies[-1000:]
            self.by_model[model] += 1

    def record_error(self) -> None:
        with self._lock:
            self.total_errors += 1

    def snapshot(self) -> dict:
        with self._lock:
            values = sorted(self.latencies)
            if values:
                index = min(len(values) - 1, max(0, int((len(values) - 1) * 0.95)))
                p95 = values[index]
            else:
                p95 = 0.0
            total = self.total_requests
            errors = self.total_errors
            return {
                "requests": total,
                "errors": errors,
                "error_rate": round(errors / max(1, total + errors), 4),
                "p95_latency_ms": round(p95, 3),
                "by_model": dict(self.by_model),
            }

telemetry = Telemetry()
