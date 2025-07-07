import pytest
from typing import List, Dict
from aggregator import aggregate

'''
Аннотация к data() написана
Почти каждая функция принимает data() и возвращает None
В связи с этим код не захламлял, к ним аннотации не писал
'''


@pytest.fixture
def data() -> [List[Dict[str, str]], None, None]:
    return [
        {"price": "10"},
        {"price": "20"},
        {"price": "30"},
    ]


def test_aggregate_avg(data):
    result = aggregate(data, "price", "avg")
    assert result == 20.0


def test_aggregate_min(data):
    result = aggregate(data, "price", "min")
    assert result == 10.0


def test_aggregate_max(data):
    result = aggregate(data, "price", "max")
    assert result == 30.0


def test_aggregate_invalid_op(data):
    with pytest.raises(ValueError):
        aggregate(data, "price", "median")


def test_aggregate_non_numeric():
    data = [{"brand": "apple"}, {"brand": "samsung"}]
    with pytest.raises(ValueError):
        aggregate(data, "brand", "avg")
