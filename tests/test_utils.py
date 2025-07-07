import pytest
from utils import filter_data
from typing import List, Dict

'''
Аннотация к sample_data() написана
Каждая функция принимает data() и возвращает None
В связи с этим код не захламлял, к ним аннотации не писал
'''


@pytest.fixture
def sample_data() -> List[Dict[str, str]]:
    return [
        {"price": "100", "brand": "apple"},
        {"price": "200", "brand": "samsung"},
        {"price": "300", "brand": "xiaomi"},
    ]


def test_filter_greater_than(sample_data):
    result = filter_data(sample_data, "price>150")
    assert len(result) == 2
    assert result[0]["price"] == "200"


def test_filter_less_than(sample_data):
    result = filter_data(sample_data, "price<250")
    assert len(result) == 2
    assert result[0]["price"] == "100"


def test_filter_equal(sample_data):
    result = filter_data(sample_data, "price=200")
    assert len(result) == 1
    assert result[0]["brand"] == "samsung"


def test_filter_text_match(sample_data):
    result = filter_data(sample_data, "brand=xiaomi")
    assert len(result) == 1
    assert result[0]["price"] == "300"


def test_filter_invalid_column(sample_data):
    with pytest.raises(KeyError):
        filter_data(sample_data, "nonexistent=500")
