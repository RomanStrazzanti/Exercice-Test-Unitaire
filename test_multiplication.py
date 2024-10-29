def func(n):
    return n * 2

def test_multiply():
    assert func(3) == 6
    assert func(0) == 0
    assert func(-2) == -4
    assert func(10) == 20