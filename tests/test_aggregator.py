import pytest
from aggregator import aggregate


@pytest.fixture
def data():
    return [
        {"price": "10"},
        {"price": "20"},
        {"price": "30"},
    ]


def test_aggregate_avg(data):
    result = aggregate(data, "price", "avg")
    assert result == 20.0  # было: {"price avg": 20.0}


def test_aggregate_min(data):
    result = aggregate(data, "price", "min")
    assert result == 10.0  # было: {"price min": 10.0}


def test_aggregate_max(data):
    result = aggregate(data, "price", "max")
    assert result == 30.0  # было: {"price max": 30.0}


def test_aggregate_invalid_op(data):
    with pytest.raises(ValueError):
        aggregate(data, "price", "median")


def test_aggregate_non_numeric():
    data = [{"brand": "apple"}, {"brand": "samsung"}]
    with pytest.raises(ValueError):
        aggregate(data, "brand", "avg")
