import pytest
from calculator import summa, minus, multiplication, divide


def test_sum():
    assert summa(4, 5) == 9


def test_minus():
    assert minus(2, 0) == 2


def test_multiplication():
    assert multiplication(6, 3) == 18


def test_divide():
    assert divide(6, 2) == 3


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(100, 0)
