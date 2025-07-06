import pytest
from utils import parse_condition


def test_parse_equal():
    column, operator, value = parse_condition("price=200")
    assert column == "price"
    assert operator == "=="
    assert value == "200"


def test_parse_greater():
    column, operator, value = parse_condition("rating>4")
    assert column == "rating"
    assert operator == ">"
    assert value == "4"


def test_parse_less():
    _, operator, _ = parse_condition("price<500")
    assert operator == "<"


def test_parse_invalid_format():
    with pytest.raises(ValueError):
        parse_condition("price500")  # некорректный формат
