from app.core.operations import add, subtract, multiply, divide, is_prime, square_root


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(7, 2) == 3.5


def test_is_prime():
    assert is_prime(7) is True
    assert is_prime(8) is False


def test_square_root():
    assert square_root(16) == 4.0
