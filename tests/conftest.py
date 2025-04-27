import pytest

@pytest.fixture
def prises_float_list():
    return [10.0, 30.0, 50.0]


@pytest.fixture
def negative_float_list():
    return [-10.0, -20.0]


@pytest.fixture
def negative_float():
    return -10.0
