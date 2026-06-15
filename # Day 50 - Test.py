# Day 50 - Test
from day50_helper import calculate_tip, validate_inputs

def test_calculate_tip():
    tip_amt, total, per = calculate_tip(100, 10, 2)
    assert tip_amt == 10
    assert total == 110
    assert per == 55
    print("✅ Tip calculation OK")

def test_validation():
    assert validate_inputs(100, 12, 2) is None
    assert validate_inputs(-10, 12, 2) == "Bill must be positive"
    assert validate_inputs(100, 20, 2) == "Tip should be 10, 12, or 15"
    assert validate_inputs(100, 12, 0) == "People must be positive"
    print("✅ Validation OK")
    print("Day 50 test ok")

test_calculate_tip()
test_validation()