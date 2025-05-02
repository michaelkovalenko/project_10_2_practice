from typing import Union


def calculate_tax(price: Union[float, int], tax_rate: Union[float, int], *, discount: Union[float, int]=0, round_symbol=2) -> Union[float, int]:
    """вычисляет стоимость товара с учетом налога и возвращать результат"""

    if not isinstance(price, (float, int)) or not isinstance(tax_rate, (float, int)) or not isinstance(discount, (float, int)):
        raise TypeError('Неверный тип данных аргумента')

    if price <= 0:
        raise ValueError('Неверная цена')

    if tax_rate >= 100 or tax_rate < 0:
        raise ValueError('Неверный налоговый процент')

    tax = price * tax_rate / 100
    return round((price + tax) * (1 - discount / 100), round_symbol)
