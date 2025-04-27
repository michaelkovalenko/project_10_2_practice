def calculate_tax(price: float, tax_rate: float) -> float:
    """вычисляет стоимость товара с учетом налога и возвращать результат"""
    if price <= 0:
        raise ValueError('Неверная цена')

    if tax_rate >= 100 or tax_rate < 0:
        raise ValueError('Неверный налоговый процент')

    tax = price * tax_rate / 100
    return price + tax
