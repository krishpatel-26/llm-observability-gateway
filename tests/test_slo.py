import pytest
from app.slo import evaluate_error_budget

def test_empty_window_is_not_treated_as_error():
    result = evaluate_error_budget(0, 0, 0.01)
    assert result.error_rate == 0.0
    assert result.within_error_budget

def test_error_budget_detects_breach():
    result = evaluate_error_budget(100, 3, 0.02)
    assert result.error_rate == 0.03
    assert not result.within_error_budget

def test_rejects_impossible_counts():
    with pytest.raises(ValueError):
        evaluate_error_budget(2, 3, 0.1)
