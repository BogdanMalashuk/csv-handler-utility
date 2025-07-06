import pytest
from utils import parse_condition


def test_parse_equal():
    col, op, val = parse_condition("price=200")
    assert col == "price"
    assert op == "=="
    assert val == "200"


def test_parse_greater():
    col, op, val = parse_condition("rating>4")
    assert col == "rating"
    assert op == ">"
    assert val == "4"


def test_parse_less():
    col, op, val = parse_condition("price<500")
    assert op == "<"


def test_parse_invalid_format():
    with pytest.raises(ValueError):
        parse_condition("price500")  # некорректный формат
