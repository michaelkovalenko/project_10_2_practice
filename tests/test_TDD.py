import pytest

from src.TDD import calculate_tax


def test_calculated_tax():
    assert calculate_tax(20.0, 10) == 22.0


def test_calculated_price_error():
    with pytest.raises(ValueError) as exc_info:
        calculate_tax(-10.0, 10)

    assert str(exc_info.value) == 'Неверная цена'


def test_calculated_tax_error():
    with pytest.raises(ValueError) as exc_info:
        calculate_tax(50, -10)

    assert str(exc_info.value) == 'Неверный налоговый процент'
