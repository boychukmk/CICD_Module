import pytest
from main import read_file
@pytest.mark.parametrize("productName, result",
                         (
        ["Apple", 3],
        ["Banana", 10]
))
def test_product_price_change(productName, result):
    assert read_file("items1.txt", productName) == result
def test_prices(file_fixture):
    assert read_file(file_fixture, "Apple") == 3