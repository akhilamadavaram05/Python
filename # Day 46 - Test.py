# Day 46 - Test
import random

def test_random_range():
    # Check that random numbers are in expected range
    for _ in range(100):
        n = random.randint(1, 100)
        assert 1 <= n <= 100
    print("✅ Random range OK")
    print("Day 46 test ok")

test_random_range()