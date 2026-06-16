# Day 51 - Test
from day51_helper import celsius_to_fahrenheit, fahrenheit_to_celsius, meters_to_feet, feet_to_meters

def test_temperature():
    assert celsius_to_fahrenheit(0) == 32
    assert fahrenheit_to_celsius(32) == 0
    assert celsius_to_fahrenheit(100) == 212
    print("✅ Temperature conversion OK")

def test_length():
    assert meters_to_feet(1) == 3.28084
    assert feet_to_meters(3.28084) == 1
    print("✅ Length conversion OK")
    print("Day 51 test ok")

test_temperature()
test_length()