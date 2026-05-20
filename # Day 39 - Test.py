# Day 39 - Test
from day39 import add, subtract, multiply, divide

def test_ops():
    assert add(2, 3) == 5
    assert subtract(5, 2) == 3
    assert multiply(3, 4) == 12
    assert divide(10, 2) == 5.0
    print("✅ Op functions OK")

    # test divide by zero
    assert divide(5, 0) is None
    print("✅ Divide by zero OK")
    print("Day 39 test ok")

test_ops()