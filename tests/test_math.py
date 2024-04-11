import pytest

products = [
    (2, 3, 6),
    (99, 1, 99),
    (0, 1, 0),
    (3, -4, -12),
    (-3, -3, 9),
    (2.5, 6.7, 16.75)
]


@pytest.mark.parametrize('a,b,product', products)
def test_multiplication(a, b, product):
    assert a*b == product


def test_one_plus_one():
    assert 1+1 == 1


def test_one_plus_two():
    a = 1
    b = 2
    c = 0
    assert a+b == c


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1/0

    assert 'division by zero' in str(e.value)
