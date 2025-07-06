import pytest
from sorter import sort_data


@pytest.fixture
def num_data():
    return [
        {"price": "10"},
        {"price": "30"},
        {"price": "20"},
    ]


@pytest.fixture
def str_data():
    return [
        {"brand": "apple"},
        {"brand": "samsung"},
        {"brand": "xiaomi"},
    ]


def test_sort_data_asc_numeric(num_data):
    sorted_data = sort_data(num_data, "price", "asc")
    prices = [float(row["price"]) for row in sorted_data]
    assert prices == [10.0, 20.0, 30.0]


def test_sort_data_desc_numeric(num_data):
    sorted_data = sort_data(num_data, "price", "desc")
    prices = [float(row["price"]) for row in sorted_data]
    assert prices == [30.0, 20.0, 10.0]


def test_sort_data_asc_string(str_data):
    sorted_data = sort_data(str_data, "brand", "asc")
    brands = [row["brand"] for row in sorted_data]
    assert brands == sorted(brands)


def test_sort_data_desc_string(str_data):
    sorted_data = sort_data(str_data, "brand", "desc")
    brands = [row["brand"] for row in sorted_data]
    assert brands == sorted(brands, reverse=True)
