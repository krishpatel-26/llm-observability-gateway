from dataclasses import dataclass

@dataclass(frozen=True)
class SLOStatus:
    total: int
    errors: int
    error_rate: float
    within_error_budget: bool

def evaluate_error_budget(total: int, errors: int, max_error_rate: float) -> SLOStatus:
    if total < 0 or errors < 0:
        raise ValueError("total and errors must be non-negative")
    if errors > total:
        raise ValueError("errors cannot exceed total observations")
    if not 0.0 <= max_error_rate <= 1.0:
        raise ValueError("max_error_rate must be between 0 and 1")
    rate = errors / total if total else 0.0
    return SLOStatus(total, errors, rate, rate <= max_error_rate)
