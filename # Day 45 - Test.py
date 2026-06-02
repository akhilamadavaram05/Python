# Day 45 - Test
from day45_helper import add, sub, mul, div

def test_calculator():
    assert add(2, 3) == 5
    assert sub(5, 2) == 3
    assert mul(4, 3) == 12
    assert div(8, 2) == 4
    assert div(5, 0) == "Error"
    print("✅ Calculator tests OK")
    print("Day 45 test ok")

test_calculator()