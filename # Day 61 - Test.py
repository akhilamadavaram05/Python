# Day 61 - Test
from day61_helper import seed_sample, load_data, total_expenses, balance

def test_budget():
    seed_sample()
    data = load_data()
    assert total_expenses(data) == 2600
    assert balance(data) == 2400
    print("✅ Budget calculations OK")
    print("Day 61 test ok")

test_budget()