import pytest

products = [
    (2,3,6),
    (99,1,99),
    (0,1,0),
    (3,-4,-12),
    (-3,-3,9),
    (2.5,6.7,16.75)
]

@pytest.mark.parametrize('a,b,product', products)
def test_multiplication(a,b, product):
    assert a*b==product