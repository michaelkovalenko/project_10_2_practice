import pytest

from src.TDD import calculate_tax


def test_calculated_tax():
    assert calculate_tax(20.0, 10.0, discount=10) == 19.8


def test_calculated_tax_type_error():
    with pytest.raises(TypeError) as exc_info:
        calculate_tax('20.0', '10.3')

    assert str(exc_info.value) == 'Неверный тип данных аргумента'


def test_calculated_price_error():
    with pytest.raises(ValueError) as exc_info:
        calculate_tax(-10.0, 10)

    assert str(exc_info.value) == 'Неверная цена'


def test_calculated_tax_error():
    with pytest.raises(ValueError) as exc_info:
        calculate_tax(50, -10)

    assert str(exc_info.value) == 'Неверный налоговый процент'


def test_calculated_round():
    assert calculate_tax(20.0, 10.0, discount=13.17, round_symbol = 3) == 19.103