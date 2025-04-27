import pytest

from src.main import calculate_taxes


def test_calculate_taxes_tax_rate_error(prises_float_list, negative_float):
    with pytest.raises(ValueError) as exc_info:
        calculate_taxes(prises_float_list, negative_float)

    assert str(exc_info.value) == 'Неверный налоговый процент'


def test_calculate_taxes_price_error(negative_float_list):
    with pytest.raises(ValueError) as exc_info:
        calculate_taxes(negative_float_list, 10)

    assert str(exc_info.value) == 'Неверная цена'


@pytest.mark.parametrize("price, tax_rate, taxed_price", [
    ([1000.0, 2000.0], 10.0, [1100.0, 2200.0]),
    ([2000.0, 3000.0], 20.0, [2400.0, 3600.0])
])
def test_calculate_taxes(price, tax_rate, taxed_price):
    assert calculate_taxes(price, tax_rate) == taxed_price
