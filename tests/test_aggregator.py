import pytest
from typing import List, Dict, Generator
from aggregator import aggregate


@pytest.fixture
def data() -> [List[Dict[str, str]], None, None]:
    return [
        {"price": "10"},
        {"price": "20"},
        {"price": "30"},
    ]


def test_aggregate_avg(data: List[Dict[str, str]]) -> None:
    result = aggregate(data, "price", "avg")
    assert result == 20.0


def test_aggregate_min(data: List[Dict[str, str]]) -> None:
    result = aggregate(data, "price", "min")
    assert result == 10.0


def test_aggregate_max(data: List[Dict[str, str]]) -> None:
    result = aggregate(data, "price", "max")
    assert result == 30.0


def test_aggregate_invalid_op(data: List[Dict[str, str]]) -> None:
    with pytest.raises(ValueError):
        aggregate(data, "price", "median")


def test_aggregate_non_numeric() -> None:
    data: List[Dict[str, str]] = [{"brand": "apple"}, {"brand": "samsung"}]
    with pytest.raises(ValueError):
        aggregate(data, "brand", "avg")
